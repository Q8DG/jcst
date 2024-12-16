# xss-labs通关记录
[@长安城第一美](undefined/arnie-rytcr)

<font style="color:rgb(51, 51, 51);">在线靶场：</font>[<font style="color:rgb(51, 51, 51);">XSS平台|CTF欢迎来到XSS挑战|XSS之旅|XSS测试 (ctf8.com)</font>](http://test.ctf8.com/)

<font style="color:rgb(51, 51, 51);">下载地址：</font>[<font style="color:rgb(51, 51, 51);">https://github.com/do0dl3/xss-labs</font>](https://github.com/do0dl3/xss-labs)

<font style="color:rgb(51, 51, 51);">我是下载在虚拟机下用小皮启动，这样也方便看源码学习，建议是下载，因为这个在线我做的几次里面有时候会页面丢失</font>

<font style="color:rgb(51, 51, 51);">本文主要讲通关方法，至于对应方法绕过对应的函数的介绍就不多赘述了，感兴趣的可以打开源码就可以了解对应函数的作用</font>

# <font style="color:rgb(51, 51, 51);">level1</font>
<font style="color:rgb(51, 51, 51);">在URL发现有参数可以提交</font>

 http://192.168.12.139/xss-labs-master/level1.php?name=test

<font style="color:rgb(51, 51, 51);">payload</font>

```javascript
 http://192.168.12.139/xss-labs-master/level1.php?name=<script>alert('document.cookie')</script>
```

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728473771474-350d3fab-c9a4-4a4e-bfd2-a03df0597e8c.png)

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728473911115-cffdbca9-8070-4c35-af0d-b40f13d96159.png)

**本关小结**： JS弹窗函数<font style="color:#fe2c24;">alert()</font>

# <font style="color:rgb(51, 51, 51);">level2</font>
<font style="color:rgb(51, 51, 51);">先随便输入值，查看代码，发现要闭合闭合value参数</font>

<font style="color:rgb(51, 51, 51);">payload</font>

```javascript
"><script>alert('document.cookie')</script>
```

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728474037002-e199ecd5-bd95-4187-9996-3b087cd49058.png)

**本关小结：闭合****<font style="color:rgb(51, 51, 51);">value</font>****绕过   **

# <font style="color:rgb(51, 51, 51);">level3</font>
<font style="color:rgb(51, 51, 51);">我们先随便输入，然后尝试闭合value</font>

```javascript
"><script>alert('document.cookie')</script>
```

<font style="color:rgb(51, 51, 51);">单引号双引号和><被转义</font>

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728474063989-9e8967e0-e110-4478-97a9-a515a1f565cc.png)

**<font style="color:rgb(51, 51, 51);">onfocus事件绕过</font>**

<font style="color:rgb(51, 51, 51);">onfocus可以绕过html实体化（即<>号的过滤）</font>

 onfocus事件在元素获得焦点时触发，最常与 <input>、<select> 和 <a> 标签一起使用，以上面图片的html标签<input>为例，<input>标签是有输入框的，简单来说，onfocus事件就是当输入框被点击的时候，就会触发myFunction()函数，然后我们再配合javascript伪协议来执行javascript代码

<font style="color:rgb(51, 51, 51);">payload</font>

```javascript
 ' onfocus=javascript:alert() '
```

<font style="color:rgb(51, 51, 51);">将payload去搜索然后再点击一下输入框就可以了</font>

**本关小结**<font style="color:rgb(51, 51, 51);"> ：</font><font style="color:#fe2c24;">onfocus</font><font style="color:rgb(51, 51, 51);">可以绕过html实体化（即<>号的过滤）  </font>

# <font style="color:rgb(51, 51, 51);">level4</font>
<font style="color:rgb(51, 51, 51);">我们先用</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">' onfocus=javascript:alert() '</font>`<font style="color:rgb(51, 51, 51);">看发现是双引号</font>

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728474074759-c1808408-be8d-481a-ba88-22e791c8cea2.png)

<font style="color:rgb(51, 51, 51);">用上一关的方法变双引号就OK</font>

```javascript
 " onfocus=javascript:alert() "
```

**本关小结**<font style="color:rgb(51, 51, 51);"> ：</font><font style="color:#fe2c24;">onfocus</font><font style="color:rgb(51, 51, 51);">可以绕过html实体化（即<>号的过滤）  </font>

# <font style="color:rgb(51, 51, 51);">level5</font>
<font style="color:rgb(51, 51, 51);">源码</font>

<font style="color:rgb(51, 51, 51);">过滤了js的标签还有onfocus事件，有小写字母转化函数</font>

<font style="color:rgb(51, 51, 51);">用新的方法</font>**<font style="color:rgb(51, 51, 51);">a href标签法</font>**

<font style="color:rgb(51, 51, 51);">href属性的意思是 当标签</font><font style="color:rgb(167, 167, 167);"><a></font><font style="color:rgb(51, 51, 51);">被点击的时候，就会触发执行转跳，上面是转跳到一个网站，我们还可以触发执行一段js代码</font>

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728474096835-9cc7aaf5-1ff6-4df9-b15d-d926c364244e.png)

```javascript
 "> <a href=javascript:alert()>我要cookie</a> <"
```

**本关小结**：可以<font style="color:#fe2c24;">插入标签</font>（如<a>标签的href属性）达到js执行的效果，前提是闭合号<"">没失效  

# <font style="color:rgb(51, 51, 51);">level6</font>
<font style="color:rgb(51, 51, 51);">先随便输入带大小写，发现没有过滤大小写，所以我们使用大小写法绕过str_replace()函数，同时闭合value，下面3种都可以</font>

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728474105637-7e55f91b-ec6a-4711-8f82-43e94f0a4c47.png)

```javascript
"> <sCript>alert()</sCript> <"
 " Onfocus=javascript:alert() "
 "> <a hRef=javascript:alert()>x</a> <"
```

**本关小结**：大小写法绕过<font style="color:#fe2c24;">str_replace()</font>函数   

# <font style="color:rgb(51, 51, 51);">level7</font>
<font style="color:rgb(51, 51, 51);">先丢测试字</font>

```javascript
" OnFocus <sCriPt> <a hReF=javascript:alert()>
 变成了
 " focus <> <a =java:alert()>
```

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728474121111-7dc37720-9c72-4110-ac78-10956919f30c.png)

<font style="color:rgb(51, 51, 51);">双写绕过</font>

```javascript
"> <a hrehreff=javasscriptcript:alert()>x</a> <"
```

**本关小结**：双拼写绕过删除函数   

# <font style="color:rgb(51, 51, 51);">level8</font>
<font style="color:rgb(51, 51, 51);">先丢入测试代码测试</font>

```javascript
" sRc DaTa OnFocus <sCriPt> <a hReF=javascript:alert()>
```

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728474294369-fb7b85db-043c-48f9-b264-2c72386a55ed.png)

<font style="color:rgb(51, 51, 51);"> input标签添加了html实体转化函数还把双引号也给实体化了， 添加了小写转化函数，还有过滤掉了src、data、onfocus、href、script、"（双引号）  </font>

**<font style="color:rgb(51, 51, 51);">解决办法</font>**

<font style="color:rgb(51, 51, 51);">能利用href的隐藏属性自动Unicode解码，我们可以插入一段js伪协议</font>

```javascript
javascript:alert()
```

<font style="color:rgb(51, 51, 51);">利用在线工具进行Unicode编码后得到</font>[在线Unicode编码解码](https://www.matools.com/code-convert-unicode)

```javascript
&#106;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;&#58;&#97;&#108;&#101;&#114;&#116;&#40;&#41;
```

<font style="color:rgb(51, 51, 51);">点击友情链接</font>

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728474484684-3f734f04-7779-4f5c-b0cb-e939d6a48f4d.png)

 本关小结： href属性<font style="color:#fe2c24;">自动解析Unicode编码</font>

# <font style="color:rgb(51, 51, 51);">level9</font>
老样子先丢测试代码

```javascript
" sRc DaTa OnFocus <sCriPt> <a hReF=javascript:alert()> &#106;
```

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728474870848-95bb1bdd-1e59-4c39-8043-e9e95fa61f65.png)

看一下源码

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728474882118-f78ee642-bd80-492f-bc5d-dcd878f43bb6.png)

<font style="color:rgb(51, 51, 51);"> 当false等于false的时候(就是传入的值没有http://)就会执行if，为了防止false===false，我们需要向传入的值里面添加</font><font style="color:#fe2c24;">http://并用注释符注释掉否则会执行不了无法弹窗</font><font style="color:rgb(51, 51, 51);">，让函数strpos返回一个数字，构造payload  </font>

```javascript
&#106;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;&#58;&#97;&#108;&#101;&#114;&#116;&#40;&#41;/* http:// */
```

**本关小结**<font style="color:rgb(51, 51, 51);">：</font><font style="color:#fe2c24;">插入指定内容</font><font style="color:rgb(51, 51, 51);">（本关是http://）绕过检测，再将指定内容用注释符注释掉即可   </font>

# <font style="color:rgb(51, 51, 51);">level10</font>
![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728474976887-bc31c35e-901e-4459-bfe1-b05ad18dd67d.png)

进来什么也没有？？？

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728475045181-8086d768-b6c5-4521-9f45-8e826f71ff99.png)

**<font style="color:rgb(51, 51, 51);"> </font>**<font style="color:rgb(51, 51, 51);">这里可以看到，Get传参的值，只插入了h2标签里头，那下面的input标签下的东西，还隐藏掉了  </font>

**<font style="color:rgb(51, 51, 51);">输入框被隐藏了，需要添加type="text"，构造payload</font>**

```javascript
?t_sort=" onfocus=javascript:alert() type="text
```

```javascript
http://192.168.12.139/xss-labs-master/level10.php

http://192.168.12.139/xss-labs-master/level10.php?t_sort=" onfocus=javascript:alert() type="text
```

**<font style="color:rgb(51, 51, 51);">本关小结</font>**<font style="color:rgb(51, 51, 51);">：根据源码猜解传参的参数名，隐藏的input标签可以插入type="text"显示 </font>

# <font style="color:rgb(51, 51, 51);">level11</font>
![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728475293200-5500d5f7-299a-471c-bc39-9da17aa649ca.png)

<font style="color:rgb(167, 167, 167);"><input></font><font style="color:rgb(51, 51, 51);">标签有四个值，都做了隐藏处理，不难看出，第四个名为t_ref的</font><font style="color:rgb(167, 167, 167);"><input></font><font style="color:rgb(51, 51, 51);">标签是http头referer的参数（就是由啥地址转跳到这里的，http头的referer会记录有）</font>

<font style="color:rgb(51, 51, 51);">referer头，用burpsuite抓包一下，添加http头</font>

```javascript
Referer: " sRc DaTa OnFocus <sCriPt> <a hReF=javascript:alert()> &#106;
```

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728475520889-c166fa9b-282d-4b9a-8904-46b5ab17ea0e.png)

<font style="color:rgb(51, 51, 51);">再看一下代码</font>

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728475582765-e33dd735-60a7-4a4a-bbee-7183be324008.png)

<font style="color:rgb(51, 51, 51);">对比发现，把大于小于号><给删掉了，但是我们还能用onfocus，构造一个http头</font>

```javascript
Referer: " onfocus=javascript:alert() type="text
```

<font style="color:rgb(51, 51, 51);">重新抓包修改再点击输入框就OK了</font>

**本关小结**<font style="color:rgb(51, 51, 51);">：考虑一下http头传值，本关是referer，但接下来也有可能是其他头，如Cookie等  </font>

# <font style="color:rgb(51, 51, 51);">level12</font>
直接看源码

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728473670729-8ec93579-222d-45b0-9e14-283d96f84575.png)

<font style="color:rgb(51, 51, 51);">这肯定是User-Agent头了，再用burpsuite抓包一下，将User-Agent头修改为我们的测试代码</font>

```javascript
" sRc DaTa OnFocus <sCriPt> <a hReF=javascript:alert()> &#106;
```

<font style="color:rgb(51, 51, 51);">再看一下源码</font>

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728473670735-f5dbe7c4-84e3-4539-856c-13b5821c7a54.png)

<font style="color:rgb(51, 51, 51);">跟上题一样，抓包构造UA头，替换User-Agent的内容</font>

```javascript
" onfocus=javascript:alert() type="text
```

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728475907697-319403dc-a9e2-4b36-ab8e-36e28fd903be.png)

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728475920388-6fe41e48-00b8-4307-8583-a3c007d92739.png)

<font style="color:rgb(51, 51, 51);">再点输入框就OK了</font>

**本关小结**<font style="color:rgb(51, 51, 51);">：跟上题一样，本题为 User-Agent头</font>

# <font style="color:rgb(51, 51, 51);">level13</font>
![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728473671258-07f4e68d-06bf-4077-a1ea-65e2d6296ef7.png)

<font style="color:rgb(51, 51, 51);">名字是t_cook，考虑到是cookie头，我们先看一下这个网页的cookie，F12打开</font>

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728473671281-5213e48c-9d43-4a95-8ee0-5ee75de684b3.png)

<font style="color:rgb(51, 51, 51);">果然是，cookie名为user，我们直接在这里改一下就好，onfocus用腻了，换成onclick，用法也差不多，改为</font>

```javascript
" onclick=alert() type="text 
```

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728473671277-20fcad75-a744-4ba5-b70d-2cf4623ae70e.png)

<font style="color:rgb(51, 51, 51);">再刷新一下就多出来来框框了</font>

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728476048657-fff210d4-4ed3-4530-9352-af5d51996056.png)

<font style="color:rgb(51, 51, 51);">再点一下框框就过了</font>

**本关小结**<font style="color:rgb(51, 51, 51);">：http头的 cookie 传参  </font>

# level14
![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728476160434-2a37c34c-64c2-4139-bc12-86e02fa6a897.png)

这是一个坏掉的页面

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728476175837-b267a3a3-8ec3-46bd-80c3-df2104bb911e.png)

查看源码

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728476138540-13790c36-7cc2-48d2-9477-68673781a6cc.png)

这题本来是利用转跳到的网站，在那网站去上传一个，属性里面含有xss代码的图片，以达到弹窗的效果，由于网站挂了，这里就不能演示

# <font style="color:rgb(51, 51, 51);">level 15 </font>
![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728476379249-56cecc2c-3c93-42e8-b68b-37feba51cd62.png)

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728473671277-9bbebd25-f226-47fe-bb00-9eec439af420.png)

<font style="color:rgb(51, 51, 51);">ng-include指令就是文件包涵的意思，用来包涵外部的html文件，如果包涵的内容是地址，需要加引号</font>

<font style="color:rgb(51, 51, 51);">我们先试试看包涵第一关，构建payload</font>

```javascript
?src='/level1.php'
```

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728473671296-a480387f-e185-420f-b6ff-6ef695659b58.png)

<font style="color:rgb(51, 51, 51);">所以可以随便包涵之前的一关并对其传参，以达到弹窗的效果，先测试一下过滤了啥，构造payload</font>

```javascript
?src=" ' sRc DaTa OnFocus <sCriPt> <a hReF=javascript:alert()> &#106;
```

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728473671725-6215b495-00fc-40c8-b1eb-3bfb1b19e82b.png)

<font style="color:rgb(51, 51, 51);">对比发现，这里有个html实体化函数在，没有删掉东西，所以不影响我们接下来的操作，我们可以包涵第一关并让第一关弹窗（注意，这里不能包涵那些直接弹窗的东西如</font><font style="color:rgb(167, 167, 167);"><script></font><font style="color:rgb(51, 51, 51);">，但是可以包涵那些标签的东西比如</font><font style="color:rgb(167, 167, 167);"><a></font><font style="color:rgb(51, 51, 51);">、</font><font style="color:rgb(167, 167, 167);"><input></font><font style="color:rgb(51, 51, 51);">、</font><font style="color:rgb(167, 167, 167);"><img></font><font style="color:rgb(51, 51, 51);">、</font><font style="color:rgb(167, 167, 167);"><p></font><font style="color:rgb(51, 51, 51);">标签等等，这些标签是能需要我们手动点击弹窗的），这里我们使用img标签，可参考</font>[<font style="color:rgb(51, 51, 51);">XSS常见的触发标签</font>](https://blog.csdn.net/LYJ20010728/article/details/116462782)<font style="color:rgb(51, 51, 51);">，构造payload</font>

```javascript
?src='/level1.php?name=<img src=1 onmouseover=alert()>'
```

<font style="color:rgb(51, 51, 51);">当鼠标移动到图片的时候就触发了弹窗</font>

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728476718295-1f5259fd-b475-4d1a-84b5-0930437b057b.png)

<font style="color:rgb(51, 51, 51);">当然也能用p标签，可以构造payload</font>

```javascript
?src='/level1.php?name=<p onmousedown=alert()>我是长安城第一美</p>'
```

**<font style="color:rgb(51, 51, 51);">本关小结</font>**<font style="color:rgb(51, 51, 51);">：ng-include文件包涵，可以无视html实体化</font>

# <font style="color:rgb(51, 51, 51);">level 16</font>
 test插入到了center标签中，所以这里就不用闭合了，老规矩，先测试一波关键字  ![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728473671745-b1e164e4-986f-4b34-ae70-94171029bf32.png)

```javascript
?keyword=" ' sRc DaTa OnFocus OnmOuseOver OnMouseDoWn P <sCriPt> <a hReF=javascript:alert()> &#106; 
```

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728476804899-00ae4e84-10b8-4936-a88e-2200048bbe25.png)

 对比发现，这里先是将字母小写化了，再把script替换成空格，最后将空格给实体化，想尝试一下p标签<p οnmοusedοwn=alert()>abc</p>，谁知道也将/给替换成了空格，无奈，只好看一下后端源码  

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728476814580-e487e96d-4d60-4172-98bd-29176ac04fca.png)

<font style="color:rgb(51, 51, 51);">空格可以用回车来代替绕过，回车的url编码是%0a，再配合上不用/的</font><font style="color:rgb(167, 167, 167);"><img></font><font style="color:rgb(51, 51, 51);">、</font><font style="color:rgb(167, 167, 167);"><details></font><font style="color:rgb(51, 51, 51);">、</font><font style="color:rgb(167, 167, 167);"><svg></font><font style="color:rgb(51, 51, 51);">等标签，更多标签可参考</font>[<font style="color:rgb(51, 51, 51);">XSS常见的触发标签</font>](https://blog.csdn.net/LYJ20010728/article/details/116462782)

<font style="color:rgb(51, 51, 51);">随便选个标签，将空格替换成回车的url编码，构造payload</font>

<font style="color:rgb(51, 51, 51);">直接在 URL 后加上 payload 即可</font>

```javascript
?keyword=<svg%0Aonload=alert(1)>
```

**<font style="color:rgb(51, 51, 51);">本关小结</font>**<font style="color:rgb(51, 51, 51);">：回车代替空格绕过检测</font>

# <font style="color:rgb(51, 51, 51);">level 17</font>
![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728473671982-09dc158b-c40f-4d7e-9466-4412e82253ac.png)

<font style="color:rgb(51, 51, 51);">先测测关键字</font>

```javascript
?arg01=" ' sRc DaTa OnFocus OnmOuseOver OnMouseDoWn P <sCriPt> <a hReF=javascript:alert()>; &arg02=" ' sRc DaTa OnFocus OnmOuseOver OnMouseDoWn P <sCriPt> <a hReF=javascript:alert()>;
```

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728473671996-772e8a00-cd21-4e78-a903-a88affffc479.png)

<font style="color:rgb(51, 51, 51);">对比发现，虽然加了该死的html转义，但是这里不需要闭合符号，传入的参数都出现在了embed标签上，打开后缀名为swf的文件（FLASH插件的文件，现在很多浏览器都不支持FLASH插件了）</font>

<font style="color:rgb(51, 51, 51);">所以，这题的解法很简单，首先得用一个支持flash插件的浏览器打开本关（打开后会有个图片出来的，不支持flash插件浏览器就没有），如果不想下载的话，自己去后端改一下也行，将后端第十七关的代码（level17.php）指向的swf文件改为index.png</font>

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728473671994-5262178e-395e-4e27-9e75-2d1d4b87b1c1.png)

<font style="color:rgb(51, 51, 51);">改为：</font>

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728473672297-833be590-66a4-405b-95c8-a67b077ae1be.png)

<font style="color:rgb(51, 51, 51);"> 这样我们再去打开第十七关的网站  </font>

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728476962872-3b6663b1-4f97-4701-bd92-25b5c4577400.png)

<font style="color:rgb(51, 51, 51);"></font>

<font style="color:rgb(51, 51, 51);">就有个embed标签的区域在啦，其实用不用swf文件都一样的，主要是区域，接着我们构造payload</font>

```javascript
?arg02= onclick=alert()
```

 点击一下区域就弹窗成功了   

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728476989979-1d35d21e-7d74-468c-a9ba-0d43c777b47a.png)

**本关小结**：要有 flash 的插件

本关有点抽象，我并没有复现成功

# <font style="color:rgb(51, 51, 51);">level 18</font>
![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728477078874-e87fb7db-f7a4-49c5-9a18-2fcfa088cb7d.png)

<font style="color:rgb(51, 51, 51);">这次不改后端代码了，换个支持flash插件的浏览器，Cent Browser。</font>

<font style="color:rgb(51, 51, 51);">看源码</font>

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728477065975-ec525a6d-e1f7-4b76-9aa9-fad5e2e4e263.png)

<font style="color:rgb(51, 51, 51);"> 源码跟上关差别不大，就是换了个swf文件，我们直接测试一波过滤了啥，构建payload  </font>

```javascript
?arg02=" ' sRc DaTa OnFocus OnmOuseOver OnMouseDoWn P <sCriPt> <a hReF=javascript:alert()>;
```

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728477114594-28fd8c79-9a3f-48a8-a95f-f66df31f1613.png)

<font style="color:rgb(51, 51, 51);">也是只搞了个html实体化函数，也没过滤啥，感觉跟上关一样，用事件触发属性即可（如onmouse系列、onfocus、onclick等）直接上payload</font>

```javascript
?arg02= onmousedown=alert()
```

 再点一下embed标签区域  

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728477149096-8a48116c-ae58-47f8-bfcc-b7f548fb82b1.png)

  **本关小结**：  与上一关类似

# <font style="color:rgb(51, 51, 51);">level 19</font>
![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728477196190-25ab0387-b687-4040-8abc-9b8e209fe7b8.png)

<font style="color:rgb(51, 51, 51);">网页源码差不多，也就是只有swf文件不同的差别，直接上payload</font>

```javascript
?arg02= onmouseup=alert()
```

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728477210221-82fa2a70-4d00-4be9-9474-73e270fe4adc.png)

这关用到的是Flash Xss注入，可参考

[Level 19 Flash XSS](https://blog.csdn.net/u014029795/article/details/103213877)<font style="color:rgb(51, 51, 51);">与</font>[Flash XSS 漏洞详解](https://blog.csdn.net/weixin_30702413/article/details/99326627)

<font style="color:rgb(51, 51, 51);">还有实体化函数在无法闭合，那就利用其他的，其实就是往Flash里面插入一段js代码，然后手动执行嘛，构造payload </font>

```javascript
?arg01=version&arg02=<a href="javascript:alert()">here</a>
```

 至于为啥arg01得传version，那就得去swf反编译才能知道了  

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728477288938-2eebaeaa-10ca-4ca2-864c-0b6ba9b6165c.png)

**本关小结**：Flash xss了解一下就行，现在许多浏览器都用不上flash插件了 ，打 4399 倒是得用这个插件哈哈哈

# <font style="color:rgb(51, 51, 51);">level 20</font>
![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728477391621-ea59b8fb-3493-4278-b84d-27433e9c2f0e.png)

 这关也是有双引号，不想反编译，直接参考大佬的文章  

[Level 20 Flash XSS](https://blog.csdn.net/u014029795/article/details/103217680)

 直接构建payload  

```javascript
?arg01=id&arg02=xss\"))}catch(e){alert(1)}//%26width=123%26height=123
```

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728477445662-fab3a30f-3bea-4148-9277-042bcfaf26eb.png)

本关小结：很难，难遇到

从 17 关开始用到 flash 插件，现在浏览器基本已经不用了，所以说这后面几关了解了解

