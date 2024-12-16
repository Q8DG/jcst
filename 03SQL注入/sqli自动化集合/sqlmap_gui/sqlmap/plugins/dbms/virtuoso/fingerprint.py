#!/usr/bin/env python

"""
Copyright (c) 2006-2023 sqlmap developers (https://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

from lib.core.common import Backend
from lib.core.common import Format
from lib.core.data import conf
from lib.core.data import kb
from lib.core.data import logger
from lib.core.enums import DBMS
from lib.core.session import setDbms
from lib.core.settings import VIRTUOSO_ALIASES
from lib.request import inject
from plugins.generic.fingerprint import Fingerprint as GenericFingerprint

class Fingerprint(GenericFingerprint):
    def __init__(self):
        GenericFingerprint.__init__(self, DBMS.VIRTUOSO)

    def getFingerprint(self):
        value = ""
        wsOsFp = Format.getOs("web server", kb.headersFp)

        if wsOsFp:
            value += "%s\n" % wsOsFp

        if kb.data.banner:
            dbmsOsFp = Format.getOs("back-end DBMS", kb.bannerFp)

            if dbmsOsFp:
                value += "%s\n" % dbmsOsFp

        value += "back-end DBMS: "

        if not conf.extensiveFp:
            value += DBMS.VIRTUOSO
            return value

        actVer = Format.getDbms()
        blank = " " * 15
        value += "活动指纹: %s" % actVer

        if kb.bannerFp:
            banVer = kb.bannerFp.get("dbmsVersion")

            if banVer:
                banVer = Format.getDbms([banVer])
                value += "\n%s 横幅解析指纹: %s" % (blank, banVer)

        htmlErrorFp = Format.getErrorParsedDBMSes()

        if htmlErrorFp:
            value += "\n%s html错误消息指纹: %s" % (blank, htmlErrorFp)

        return value

    def checkDbms(self):
        if not conf.extensiveFp and Backend.isDbmsWithin(VIRTUOSO_ALIASES):
            setDbms(DBMS.VIRTUOSO)
            return True

        infoMsg = "测试 %s" % DBMS.VIRTUOSO
        logger.info(infoMsg)

        result = inject.checkBooleanExpression("GET_KEYWORD(NULL,NULL) IS NULL")

        if result:
            infoMsg = "确认 %s" % DBMS.VIRTUOSO
            logger.info(infoMsg)

            result = inject.checkBooleanExpression("RDF_NOW_IMPL() IS NOT NULL")

            if not result:
                warnMsg = "后端DBMS不是 %s" % DBMS.VIRTUOSO
                logger.warning(warnMsg)

                return False

            setDbms(DBMS.VIRTUOSO)

            return True
        else:
            warnMsg = "后端DBMS不是 %s" % DBMS.VIRTUOSO
            logger.warning(warnMsg)

            return False
