# 整理的 BurpSuite插件汇总共计30+ 

TsojanScan([GitHub - Tsojan/TsojanScan: An integrated BurpSuite vulnerability detection plug-in.](https://github.com/Tsojan/TsojanScan))：一个集成的BurpSuite漏洞探测插件，它会以最少的数据包请求来准确检测各漏洞存在与否，你只需要这一个足矣。 - JsRouteScan([GitHub - F6JO/JsRouteScan: Burpsuite - Js Route Scan 正则匹配获取响应中的路由进行被动探测与递归目录探测的burp插件](https://github.com/F6JO/JsRouteScan))：正则匹配获取响应中的路由进行探测或递归目录探测的burp插件。 

BurpAPIFinder([GitHub - shuanx/BurpAPIFinder: 攻防演练过程中，我们通常会用浏览器访问一些资产，但很多未授权/敏感信息/越权隐匿在已访问接口过html、JS文件等，该插件能让我们发现未授权/敏感信息/越权/登陆接口等。](https://github.com/shuanx/BurpAPIFinder/))：攻防演练过程中，我们通常会用浏览器访问一些资产，但很多未授权/敏感信息/越权隐匿在已访问接口过html、JS文件等，该插件能让我们发现未授权/敏感信息/越权/登陆接口等。 

BurpShiroPassiveScan([GitHub - pmiaowu/BurpShiroPassiveScan: 一款基于BurpSuite的被动式shiro检测插件](https://github.com/pmiaowu/BurpShiroPassiveScan))：一款基于BurpSuite的被动式shiro检测插件。 

turbo-intruder([GitHub - PortSwigger/turbo-intruder: Turbo Intruder is a Burp Suite extension for sending large numbers of HTTP requests and analyzing the results.](https://github.com/PortSwigger/turbo-intruder))：Turbo  Intruder 是一个 Burp Suite 扩展插件， 用于发送大量 HTTP 请求并分析结果，它旨在处理那些需要异常速度、持续时间或复杂性的攻击来补充 Burp  Intruder，可以发现条件竞争和短信轰炸等漏洞。  

captcha-killer-modified([GitHub - f0ng/captcha-killer-modified: captcha-killer的修改版，支持关键词识别base64编码的图片，添加免费ocr库，用于验证码爆破，适配新版Burpsuite](https://github.com/f0ng/captcha-killer-modified))：一款适用于Burp的验证码识别插件。 

HackBar([GitHub - d3vilbug/HackBar: HackBar plugin for Burpsuite](https://github.com/d3vilbug/HackBar))：HackBar是burp插件，支持很多便携功能，SQL注入payload、XSS payload、常见LFI漏洞、web shell payload和反弹shell payload。 

Autorize([GitHub - Quitten/Autorize: Automatic authorization enforcement detection extension for burp suite written in Jython developed by Barak Tawily in order to ease application security people work and allow them perform an automatic authorization tests](https://github.com/Quitten/Autorize))：越权检测 burp插件。 

HaE([GitHub - gh0stkey/HaE: HaE - Highlighter and Extractor, Empower ethical hacker for efficient operations.](https://github.com/gh0stkey/HaE))：HaE是一个基于BurpSuite Java插件API开发的辅助型框架式插件，旨在实现对HTTP消息的高亮标记和信息提取。该插件通过自定义正则表达式匹配响应报文或请求报文，并对匹配成功的报文进行标记和提取。 

jsEncrypter([GitHub - c0ny1/jsEncrypter: 一个用于前端加密Fuzz的Burp Suite插件](https://github.com/c0ny1/jsEncrypter))：本插件使用phantomjs启动前端加密函数对数据进行加密，方便对加密数据输入点进行fuzz，比如可以使用于前端加密传输爆破等场景。 

Wsdler([GitHub - NetSPI/Wsdler: WSDL Parser extension for Burp](https://github.com/NetSPI/Wsdler))：Wsdler 可以解析 WSDL 请求，以便使用 repeater 和 scanner 对 WSDL 请求进行测试。 

domain_hunter_pro([GitHub - bit4woo/domain_hunter_pro: domain_hunter的高级版本，SRC挖洞、HW打点之必备！自动化资产收集；快速Title获取；外部工具联动；等等](https://github.com/bit4woo/domain_hunter_pro))：这款插件很好的补充了BURP的域名收集问题，让你的BURP更加强大，更加系统的收集项目内的域名和子域名扩大域名资产，增加攻击面。 

J2EEScan([GitHub - ilmila/J2EEScan: J2EEScan is a plugin for Burp Suite Proxy. The goal of this plugin is to improve the test coverage during web application penetration tests on J2EE applications.](https://github.com/ilmila/J2EEScan))：J2EEScan 是一个扫描器增强插件，可以通过该插件扫描 J2EE 漏洞，如 weblogic、struts2 、 jboss 等漏洞。 

Struts2Burp([GitHub - x1a0t/Struts2Burp](https://github.com/x1a0t/Struts2Burp))：一款检测Struts2 RCE漏洞的burp被动扫描插件，仅检测url后缀为.do以及.action的数据包。 

software-vulnerability-scanner([GitHub - PortSwigger/software-vulnerability-scanner: Vulnerability scanner based on vulners.com search API](https://github.com/PortSwigger/software-vulnerability-scanner))：Software Vulnerability Scanner 是一个扫描器增强插件，它会检查网站的一些软件版本信息，然后通过 [http://vulners.com](http://vulners.com/) 上的漏洞数据库来查询相应的 CVE 编号，找到的结果会显示在漏洞面板上，不用我们自己手动去查找某个版本的 CVE 。 

BurpJSLinkFinder([GitHub - InitRoot/BurpJSLinkFinder: Burp Extension for a passive scanning JS files for endpoint links.](https://github.com/InitRoot/BurpJSLinkFinder))：插件很好的兼容进了BURP里面，随着你的点击自动进行收集JS里面的路径。 - jython-standalone(https://repo1.maven.org/maven2/org/python/jython-standalone/2.7.3/jython-standalone-2.7.3.jar)：Jython是一个将Python语言与Java虚拟机集成的工具，burp中安装python编写插件。 

FastjsonScan([GitHub - Maskhe/FastjsonScan: 一个简单的Fastjson反序列化检测burp插件](https://github.com/Maskhe/FastjsonScan))：被动扫描fastjson漏洞。 - BurpFastJsonScan([GitHub - pmiaowu/BurpFastJsonScan: 一款基于BurpSuite的被动式FastJson检测插件](https://github.com/pmiaowu/BurpFastJsonScan))：一款基于BurpSuite的被动式FastJson检测插件。 

log4j2burpscanner([GitHub - f0ng/log4j2burpscanner: CVE-2021-44228 Log4j2 BurpSuite Scanner,Customize ceye.io api or other apis,including internal networks](https://github.com/f0ng/log4j2burpscanner))：被动发现log4j2 RCE漏洞。 chunked-coding-converter([GitHub - c0ny1/chunked-coding-converter: Burp suite 分块传输辅助插件](https://github.com/c0ny1/chunked-coding-converter))：分块传输绕WAF插件。 

CaA([GitHub - gh0stkey/CaA: CaA - Collector and Analyzer, Insight into information, exploring with intelligence in a thousand ways.](https://github.com/gh0stkey/CaA))：CaA是一个基于BurpSuite Java插件API开发的流量收集和分析插件。它的主要作用就是收集HTTP协议报文中的参数、路径、文件、参数值等信息，并统计出现的频次，为使用者积累真正具有实战意义的Fuzzing字典。除此之外，CaA还提供了独立的Fuzzing功能，可以根据用户输入的字典，以不同的请求方式交叉遍历请求，从而帮助用户发现隐藏的参数、路径、文件，以便于进一步发现安全漏洞。 

APIKit([GitHub - API-Security/APIKit: APIKit：Discovery, Scan and Audit APIs Toolkit All In One.](https://github.com/API-Security/APIKit))：APIKit可以主动/被动扫描发现应用泄露的API文档，并将API文档解析成BurpSuite中的数据包用于API安全测试。 

ssrf-king([GitHub - ethicalhackingplayground/ssrf-king: SSRF plugin for burp Automates SSRF Detection in all of the Request](https://github.com/ethicalhackingplayground/ssrf-king))：burp插件自动化检测ssrf漏洞。 

npscrack([GitHub - weishen250/npscrack: 蓝队利器、溯源反制、NPS 漏洞利用、NPS exp、NPS poc、Burp插件、一键利用](https://github.com/weishen250/npscrack))：蓝队利器、溯源反制、NPS 漏洞利用、NPS exp、NPS poc、Burp插件、一键利用。 

burpFakeIP([GitHub - TheKingOfDuck/burpFakeIP: 服务端配置错误情况下用于伪造ip地址进行测试的Burp Suite插件](https://github.com/TheKingOfDuck/burpFakeIP))：伪造请求IP插件。 

BurpSuite_403Bypasser([GitHub - sting8k/BurpSuite_403Bypasser: Burpsuite Extension to bypass 403 restricted directory](https://github.com/sting8k/BurpSuite_403Bypasser))：绕过 403 受限目录的 burpsuite 扩展。 

gatherBurp([GitHub - kN6jq/gatherBurp: 一款burp插件,请看简介](https://github.com/kN6jq/gatherBurp))：一款综合的burp插件。 

xia_Liao([GitHub - smxiazi/xia_Liao: xia Liao（瞎料）burp插件 用于Windows在线进程/杀软识别 与 web渗透注册时，快速生成需要的资料用来填写，资料包含：姓名、手机号、身份证、统一社会信用代码、组织机构代码、银行卡，以及各类web语言的hello world输出和生成弱口令字典等。](https://github.com/smxiazi/xia_Liao))：xia Liao（瞎料）burp插件 用于Windows在线进程/杀软识别 与 web渗透注册时，快速生成需要的资料用来填写，资料包含：姓名、手机号、身份证、统一社会信用代码、组织机构代码、银行卡，以及各类web语言的hello world输出和生成弱口令字典等。 

OneScan([GitHub - vaycore/OneScan: OneScan是递归目录扫描的BurpSuite插件](https://github.com/vaycore/OneScan))：OneScan是递归目录扫描的BurpSuite插件。 

BurpFingerPrint([GitHub - shuanx/BurpFingerPrint: BurpSuite插件集成Ehole指纹库并进行常见OA弱口令爆破插件](https://github.com/shuanx/BurpFingerPrint))：攻击过程中，我们通常会用浏览器访问一些资产，该BurpSuite插件实现被动指纹识别+网站提取链接+OA爆破，可帮助我们发现更多资产。 - reflector([GitHub - elkokc/reflector: Burp plugin able to find reflected XSS on page in real-time while browsing on site](https://github.com/elkokc/reflector))：BurpSuite反射XSS插件。

