# 1. 什么是爬虫

## 1.1 HTTP 协议

HTTP 协议：HyperText Transfer Protocol（超文本传输协议），发布和接受HTML页面的方法。服务器端口号为80端口。

HTTPS协议：是 HTTP协议加密版本，在HTTP下加入了SSL层，服务器端口是443端口。



## 1.2 URL 

URL 是 Uniform Resource Locator， 同意资源定位符。一个URL由以下几个部分组成：

- scheme: //host:port/path/?query-string=xxx#anchor
- scheme: 访问的协议，http, https, ftp 等
- host: 主机名，域名， 如 www.baidu.com 
- port: 端口号。 80， 443 等
- path: 查找路径，如：sz.58.com/chuzu  （后面的chuzu就是path）
- query-string: 查询字符，比如: www.baidu.com/s?wd=python, （后面的wd=python就是查询字符）
- anchor: 锚点，前端用来做页面定位的。现在一些后端用来分离项目，也用锚点来做导航。



## 1.3  Crawler 定义

​	网络爬虫（英语：web crawler），也叫网络蜘蛛（spider），是一种用来自动浏览万维网的网络机器人。其目的一般为编纂网络索引。
网络搜索引擎等站点通过爬虫软件更新自身的网站内容或其对其他网站的索引。网络爬虫可以将自己所访问的页面保存下来，以便搜索引擎事后生成索引供用户搜索。

​	爬虫访问网站的过程会消耗目标系统资源。不少网络系统并不默许爬虫工作。因此在访问大量页面时，爬虫需要考虑到规划、负载，还需要讲“礼貌”。 不愿意被爬虫访问、被爬虫主人知晓的公开站点可以使用robots.txt文件之类的方法避免访问。这个文件可以要求机器人只对网站的一部分进行索引，或完全不作处理。

​	互联网上的页面极多，即使是最大的爬虫系统也无法做出完整的索引。因此在公元2000年之前的万维网出现初期，搜索引擎经常找不到多少相关结果。现在的搜索引擎在这方面已经进步很多，能够即刻给出高素质结果。
爬虫还可以验证超链接和HTML代码，用于网络抓取.



## 1.4 Chrome 等搜索引擎工作

- 首先，网络爬虫持续抓取网站内容，将其存储在搜索引擎的数据库中。
- 紧接着，索引程序对数据库中的网页进行整理，创建倒排索引。
- 最后，当用户输入查询关键词时，搜索程序会在索引中查找相关内容，并通过排序算法（例如Pagerank）将最相关的结果展现给用户。

​	网络爬虫是用于自动获取互联网上公开数据的工具。搜索引擎和网站之间形成了一种默契——robots.txt协议。网站通过这个文件指明哪些内容可以被爬虫抓取，哪些不可以；同时，搜索引擎在访问网站时会通过User-Agent标识自己的身份（如Googlebot、Baiduspider），以此保持双方的和平共处和互利共赢。



## 1.5 爬虫Crawler的职责

 **抓取页面（Fetching）**:
	网络爬虫会按照一定的规则和算法，访问网站上的页面并下载页面内容。这个过程需要考虑页面的深度、频率、并发请求数量等因素，以确保高效地获取数据。

**解析页面（Parsing）：** 
	爬虫需要解析下载的页面内容，提取其中的文本、链接、图像等信息。通过解析页面，爬虫可以识别页面结构、内容特征以及与其他页面的关联。

**处理链接（Link Handling）**：
	时会提取页面中的链接，然后根据一定的策略处理这些链接。这包括去重、筛选、调度等操作，以确保爬虫系统能够高效地覆盖目标网站的内容。

**存储数据（Storing）**：
	爬虫需要将抓取到的数据进行存储，通常存储在数据库或索引中。这样可以为后续的数据处理、索引建立和搜索提供支持。

**遵守规则（Respect Robots.txt）：**
	爬虫需要遵守网站所有者制定的规则，比如robots.txt文件中定义的爬取限制。爬虫需要尊重网站的爬取策略，以避免对目标网站造成不必要的干扰。





# 2. Crawler 工作原理

## 2.1 基本流程

现代的网络爬虫工作流程大致可以分为以下几个步骤：

1. **识别入口点**：确定需要抓取数据的API入口点。这些入口点是爬虫开始抓取数据的起点，通常是一些返回JSON数据的URL。
2. **构造请求**：根据API文档或通过分析网络请求，构造出正确的HTTP/HTTPS请求。这包括正确的请求方法（GET、POST等）、请求头、以及必要的参数。
3. **发送请求**：爬虫对API入口点发起请求，等待服务器响应。对于需要认证的API，可能还需要处理登录和会话管理。
4. **解析响应**：服务器返回JSON或其他格式的数据。爬虫需要解析这些数据，提取有价值的信息。
5. **数据处理**：将提取出的数据进行清洗、转换和存储。数据可以存储在数据库、文件或其他存储系统中。
6. **遍历与递归**：从返回的数据中提取出新的URL或API入口点，重复上述过程，直至抓取到所需的全部数据。



## 2.2 关键技术点

1. **HTTP/HTTPS协议**

2. **请求库**

   - **Requests**：Python的Requests库是处理HTTP请求的同步库，简单易用，适合初学者。
   - **Aiohttp**：Aiohttp是一个支持异步请求的库，可以在处理大量并发连接时提高效率。
   - **HTTPX**：HTTPX支持同步和异步请求，是一个现代化的网络请求库，提供了丰富的功能。

3. **解析库**

   - **Parsel**：Parsel基于lxml，专为HTML/XML解析设计，简化了数据提取的流程。

   >可以基于css选择器，也可以基于xpath，是从Scrapy框架中的解析库做了二次封装得来的，
   >
   > lxml = 高性能的 XML / HTML 解析与处理工具（支持 XPath、XSLT）可以把字符串、文件、网页内容解析成一棵“文档树”。

4. **浏览器自动化测试工具**

   - **Playwright**：Playwright是一个由Microsoft开发的现代化浏览器自动化库。它支持所有主流浏览器和多种语言，特别适合高效率的自动化测试和爬虫开发。
   - **Selenium**：Selenium是一个浏览器自动化工具，可以模拟用户操作浏览器。它支持多种编程语言和浏览器，适合处理JavaScript渲染的页面。

   >优先推荐Playwright，因为现在Python的异步编程很流行，那基于异步的爬虫代码也很多，Playwright它也是支持异步调用， 并且微软开源的，更新迭代速度还行，这也是我推荐的。

   



# 3. 常用的抓包工具

在进行网络爬虫开发时，抓包是一个非常重要的步骤。它可以帮助我们了解客户端和服务器之间的通信过程，包括请求的发送和响应的接收。这对于分析和模拟网络请求尤其关键。本教程将介绍几种常用的抓包工具，包括Chrome的开发者工具、Charles和Fiddler。

- Chrome抓包Web应用

- Charles和Fiddler既可以抓包APP也可以抓包Web

  

## 3.1 Chrome的开发者工具

Chrome浏览器内置的开发者工具是最直接便捷的抓包方式之一，特别适合前后端分离的网站分析。[微博帖子评论爬取教程](https://blog.csdn.net/weixin_43252709/article/details/135431751)

1. 打开Chrome浏览器，访问目标网站。
2. 按`F12`或右键点击页面，选择“检查”打开开发者工具。
3. 切换到“Network”（网络）标签页。此时可能需要刷新页面以捕获所有网络请求。
4. 浏览网络请求列表，点击任一请求查看详细信息，包括请求头、响应头、响应体等。
5. 可以通过过滤器筛选特定类型的请求，例如XHR（Ajax请求）。
6. 使用Chrome开发者工具的优点在于无需安装额外软件，操作简单，适合快速查看和分析HTTP/HTTPS请求。

检查网页源代码：查看静态网页的源代码，里面包含网页框架和数据内容。

Elements：可以邦族我们分析网页结构，获取数据。但是 Elements 下最终呈现的网页数据，有时候网页数据是通过 ajax 请求得到到，因此 Element 下的数据有可能在网页中并未出现，需要抓包分析。

Network：查看整个网页发送的所有网络请求，一般我们想要去查看某个请求的信息，都可以在这个里面去看。 



##  3.2 使用Charles



Charles是一款广受欢迎的跨平台抓包工具，它可以作为代理服务器运行，监控和修改进出电脑的所有HTTP和HTTPS请求。[charles安装入门使用示例](https://zhuanlan.zhihu.com/p/140942687)

1. 下载并安装Charles。
2. 启动Charles，它会自动开始捕获网络请求。
3. 配置浏览器或设备使用Charles为代理服务器。这通常涉及到设置代理服务器地址为127.0.0.1（本机地址），端口为Charles显示的端口（默认8888）。
4. 访问目标网站或应用，Charles会显示通过它的所有请求和响应。
5. 双击任一请求或响应以查看详细内容。

Charles强大之处在于它能够修改请求或响应，实现更深入的测试和分析。



## 3.3  使用Fiddler

Fiddler同样是一款功能强大的网络请求分析工具，它也可以捕获计算机上的HTTP/HTTPS请求。[Fiddler安装入门使用示例](https://blog.csdn.net/FourAu/article/details/136479512)

1. 下载并安装Fiddler。
2. 启动Fiddler，它默认开始捕获网络请求。
3. 在“Web Sessions”窗口中，可以看到通过Fiddler的所有HTTP/HTTPS请求和响应。
4. 点击任一条目查看详细的请求和响应信息。

Fiddler提供了广泛的自定义选项，包括断点设置、请求编辑、性能测试等高级功能。





# 4. 常见的请求库

## 4.1 常见的请求方法

在 http 协议中，定义了8中请求方法，常见的是 get 和 post 请求。

- get 请求：一般情况下，只从服务器获取数据，并捕获对服务器资源产生任何影响的时候会使用 get 请求。
- post 请求：向服务器发送数据（登录），上传文件等，会对服务器资源产生影响的时候会使用post 请求。

打开网页，F12 -> Nextwork -> Headers -> 查看相应的请求方式：

<img src="assets/image-20251231094731440.png" alt="image-20251231094731440" style="zoom: 67%;" />



## 4.2 请求头参数

在 http 协议中，向服务器发送一个请求，数据分为三部分： 第一个是把数据放在 url 中，第二个是把数据放在 body 中(post 请求中) ，第三个是把数据放在 head 中。经常用到的一些请求头参数：

- User-Agent：浏览器名称。可用于伪装爬虫。
- Referer：表明当前这个请求是从哪个 url 过来的。
- Cookie：http协议是无状态的。同一个人发送了两次请求，服务器没有能力知道这两个请求是否来自同一个人。因此用 cookie 来做标识。一般如果想要做登陆后才能访问的网站，那么就需要发送 cookie 信息了。

打开网页，F12 -> Nextwork -> Headers -> 最下面 -> User-Agent:  

![image-20251231100408686](assets/image-20251231100408686.png)

打开网页，F12 -> Nextwork -> Headers -> Request Headers -> Cookie: 

![image-20251231095706783](assets/image-20251231095706783.png)







## 4.3 状态相应码（Response Code)

- 200: 正常

- 301：永久重定向。比如访问 www.jingdong.com 时会重定向到 www.jd.com 

- 302：临时重定向。比如在访问一个需要登录的页面时，但此时没有登陆，就会重定向的登录界面。

- 400：请求的 url 在服务器上招不到。请求 url 错误

- 403：服务器拒绝访问，权限不够，或者是被反爬。

- 500：服务器内部错误。可能是服务器内部 bug，或者宕机。

  



## 4.4 请求库

在Python中，进行网络请求的库主要分为同步和异步两大类。

**同步请求库：**

`urllib`: Python的标准库之一，提供了一系列用于操作URL的功能。

`requests`: 第三方库，提供了更加方便的API来发送HTTP请求，是最受欢迎的HTTP客户端之一。模拟历览器发送请求。

步骤：

1. 指定 url 
2. 发送请求 -- get 方法会返回一个相应对象。
3. 获得相应对象 response.text 返回的是一个字符串数据
4. 存储到本地。

**Requests-get :** 

```python 
import requests
# 1. 指定 url 
keyword = input('请输入需要查询的关键字： ')
url = f'https://www.sogou.com/web?query={keyword}'

User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
headers = {'User-Agent': User_Agent}

# 2. 网络请求，获得参数
response = requests.get(url=url, headers=headers)
print(response.text)

# 3.保存网页
with open(keyword + '.html', 'w', encoding='utf-8') as f:
    f.write(response.text)
    print(f'已下载..{keyword}')
```



**Requests-post：**

异步加载（Ajax请求），与 Ajax相关的文件 -> Fetch/XHR -> 找到需要的数据包（点击 Preview）-> Payload(text:cat)

<img src="assets/image-20251231143236067.png" alt="image-20251231143236067" style="zoom:67%;" />

<img src="assets/image-20251231143425502.png" alt="image-20251231143425502" style="zoom:67%;" />

利用post 请求，基于搜狗翻译实现文本翻译：

```python 
import requests
import pprint   # 用于打印 json 格式规范化

keyword = input('请输入需要翻译的关键字： ')
query_url = 'https://fanyi.sogou.com/reventondc/suggV3'   # 从 Headers 处拿到网址
User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'

data = {             # Payload 处拿取，
    'from': 'auto',
    'to': 'zh-CHS',
    'client': 'web',
    'text': keyword,
    'uuid': 'c1c030ce-17e5-407f-9ca6-57c491874069',
    'pid': 'sogou-dict-vr',
    'addSugg': 'on'
    }

response = requests.post(query_url, data=data, headers={'User-Agent': User_Agent})

result = response.json()['sugg'][0]['v']    # 存放翻译结果
pprint.pprint(result)
```







**异步请求库：**

- `aiohttp`: 支持异步请求的库，使用`asyncio`进行网络通信，适合处理高并发需求。
- `httpx`: 是一个全功能的HTTP客户端，支持HTTP/1.1和HTTP/2，并且同时支持同步和异步接口。



## 4.1 优缺点及适用场景

**`urllib`:**

- **优点**: 标准库，不需要额外安装。
- **缺点**: API相对繁琐。
- **适用场景**: 简单的应用，或不想引入外部依赖时。

**`requests`:**

- **优点**: API简单易用，社区支持强大。
- **缺点**: 不支持异步。
- **适用场景**: 大多数HTTP请求场景，尤其是对性能要求不是非常高的同步程序。

**`aiohttp`:**

- **优点**: 支持异步，适合高并发场景。
- **缺点**: API相对复杂。
- **适用场景**: 需要处理大量并发连接的应用。

**`httpx`:**

- **优点**: 同时支持同步和异步API，支持HTTP/2。
- **缺点**: 相对较新，社区支持和稳定性正在增强中。
- **适用场景**: 需要同时使用同步和异步请求，或需要HTTP/2支持的应用。



## 4.2  Requests和httpx的使用

headers、cookies、auth、proxy这几种是我们日常爬虫过程中，经常需要使用的，下面分别基于request和httpx来展示如何使用：

**Requests**:

- Headers、cookies、认证、SSL证书验证

```py
import requests

url = 'https://httpbin.org/get'
headers = {'User-Agent': 'My App'}
cookies = {'session_id': '12345'}
auth = ('user', 'passwd')   # 认证 
verify = '/path/to/certfile'   # SSL证书
response = requests.get(url, headers=headers, auth=auth, verify=verify)
```



**httpx**:

- Headers、cookies、认证、SSL证书验证

```py
import httpx

url = 'https://httpbin.org/get'
headers = {'User-Agent': 'My App'}
cookies = {'session_id': '12345'}
auth = ('user', 'passwd')   # 认证 
verify = '/path/to/certfile'   # SSL证书
response = httpx.get(url, headers=headers, auth=auth, verify=verify)
```



httpx和request的用法大差不差，是的没错。

httpx 的设计灵感来源于 requests，因此两者在用法上有很多相似之处。这是因为 httpx 的开发者希望提供一个类似于 requests 的简洁、易用的接口，同时又能够支持更多的功能和特性，比如对异步请求的支持以及对 HTTP/2 的原生支持。因此，如果您熟悉 requests 的用法，那么学习和使用 httpx 会变得非常容易和顺畅。





# 5. 爬虫静态网页数据提取

本篇的内容html内容解析会用两个库来完成，一个是`BeautifulSoup` 另一个是我比较喜欢用的`parsel`. 大多数新入门朋友可能学习爬虫的时候，都是从BeautifulSoup这个库开始的。



## 5.1 什么是静态网页

静态网页是指内容固定不变的网页，它的内容是直接写在 HTML 文件中的，不会因为用户的请求或者其他因素而改变。静态网页的内容通常由 HTML、CSS 和 JavaScript 组成，服务器只需要将这些文件发送给浏览器，浏览器就可以直接解析并显示网页内容。



## 5.2 静态网页工作原理

当用户在浏览器中输入一个静态网页的 URL 时，浏览器会向服务器发送一个 HTTP 请求，请求获取该 URL 对应的 HTML 文件。服务器接收到请求后，会在服务器上查找对应的 HTML 文件，并将其内容发送给浏览器。浏览器接收到 HTML 文件后，会解析其中的 HTML、CSS 和 JavaScript 代码，并根据这些代码渲染出网页内容。

![image-20251230181718205](assets/image-20251230181718205.png)



## 5.3 实战 BBS论坛网站的股票

今天我要爬取的是一个BBS论坛网站的股票讨论部分，目标站点地址：https://www.ptt.cc/bbs/Stock/index.html 需要采集前N页的信息，具体采集内容如下：

<img src="assets/100000004.BtVt63l4.png" alt="img.png" style="zoom:50%;" />

**1、如何获取前N页中的最新分页Number？**

需求中说的是前N页帖子，那么我们是不是要从最新的帖子往前推N页就可以了，理论上我们只需要找出它最新的分页Number就可以了。 我们打开 `https://www.ptt.cc/bbs/Stock/index.html` 并点击`上一页` 按钮，从页面URL `https://www.ptt.cc/bbs/Stock/index9600.html` 可以得出 9600可能是分页Number

<img src="assets/image-20251230183103908.png" alt="image-20251230183103908" style="zoom: 50%;" />

我们再点一次`上一页` 按钮，可以发现URL变为了：`https://www.ptt.cc/bbs/Stock/index9600.html`, 那么我们可以初步断定，这个网站的分页模式就是从高到低递减了。
我们如何知道9600这个分页数字？
静态网页一般找这个数字都不难，Chrome浏览器，F12，选中上一页按钮，从html文档中的elements就能看见这个按钮是一个a标签，其中的href属性放着点击该按钮之后要跳转的URL地址。

<img src="assets/image-20251230183246720.png" alt="image-20251230183246720" style="zoom: 50%;" />

所以我们只需要使用解析库把这个数字解析出来就可以了.



**2、html结构分析**

同样F12进入控制台，鼠标选择其中一个帖子，查看右边Chrome调试工具的Eelements，可以看到每一个帖子的一块区域所对应的html代码都是由一个`div calss='r-ent'`包裹的. 这种结构化的网页是我们最喜欢看见的，有规律可循，所以下一步就是按需提取信息了。

![image-20251230183530160](assets/image-20251230183530160.png)

下面我贴出一个帖子的html代码，然后分别基于两个解析库`BeautifulSoup`、`parsel`提取我们想要的信息

```html
<div class="r-ent">
    <div class="nrec"><span class="hl f3">11</span></div>
    <div class="title">

        <a href="/bbs/Stock/M.1711544298.A.9F8.html">[新聞] 童子賢：用稅收補貼電費非長久之計 應共</a>

    </div>
    <div class="meta">
        <div class="author">addy7533967</div>
        <div class="article-menu">

            <div class="trigger">⋯</div>
            <div class="dropdown">
                <div class="item"><a href="/bbs/Stock/search?q=thread%3A%5B%E6%96%B0%E8%81%9E%5D+%E7%AB%A5%E5%AD%90%E8%B3%A2%EF%BC%9A%E7%94%A8%E7%A8%85%E6%94%B6%E8%A3%9C%E8%B2%BC%E9%9B%BB%E8%B2%BB%E9%9D%9E%E9%95%B7%E4%B9%85%E4%B9%8B%E8%A8%88+%E6%87%89%E5%85%B1">搜尋同標題文章</a></div>

                <div class="item"><a href="/bbs/Stock/search?q=author%3Aaddy7533967">搜尋看板內 addy7533967 的文章</a></div>

            </div>

        </div>
        <div class="date"> 3/27</div>
        <div class="mark"></div>
    </div>
</div>
```





流程图：

![image-20251230184508847](assets/image-20251230184508847.png) 

















# 6. Selenium

## 6.1 基本概念及安装

复杂的动态网页解决方案： 

1. 直接抓包分析调用接口，然后通过代码请求这个接口（ JS 逆向）。
   - 优点：可以直接请求到数据，不需要做一些解析工作，代码量少，性能高。
   - 缺点：分析接口比较复杂，特别是一些通过 js 混淆的接口，需要 JS逆向功底。
2. 使用 Selenium + chromedriver 模拟浏览器行为获取数据。
   - 优点：浏览器能请求到的数据，使用 selenium 也能请求到，爬虫更稳定，且适用于所有类型的动态渲染网页。
   - 缺点：代码量多，性能低容易被反爬。



**Selenium 简介**
Selenium 相当于是一个机器人。可以模拟人类在浏览器上的一些行为，自动处理浏览器上的一些行为，比如点击、填充数据、删除cookie等。

chromedriver 是一个驱动 Chrome浏览器的驱动程序，针对不同的浏览器有不同的 driver.



**Selenium + chromedriver	**

1.  安装 Selenium： 在命令行输入 pip install selenium
2. 安装 chromedriver：
   - 先下载 chromedriver.exe，注意版本要和 Chrome 浏览器对应。
   - http://chromedriver.storage.googleapis.com/index.html
   - 将安装文件 Python 解释器安装目录



- Selenium 相关资料： https://selenium-python.readthedocs.io/



初始化 selenium 浏览器：

```py 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

target_url = 'https://pixabay.com/images/search/cat/'

service = Service(executable_path="W:\Chrome\chromedriver-win64\chromedriver-win64\chromedriver.exe")
browser = webdriver.Chrome(service=service)
browser.get(url=target_url)
```



## 6.2 浏览器基本操作

- 打开浏览器
- 设置窗口大小
- 设置打开浏览器位置
- 关闭浏览器
- 前进
- 后退
- 刷新
- 获取网页代码

```py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

target_url = 'https://www.baidu.com'
jb_url = 'https://www.jingdong.com'

service = Service(executable_path="W:\Chrome\chromedriver-win64\chromedriver-win64\chromedriver.exe")
opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')   # 添加参数，隐藏 selenium 浏览器的某些痕迹。
browser = webdriver.Chrome(service=service, options=opt)   # 实例化浏览器对象
# browser.maximize_window()   # 全屏显示
# browser.set_window_size(1910, 1080)   # 设置窗口打开大小
# browser.set_window_position(1000, 10)   # 设置窗口打开位置
browser.get(url=target_url)

time.sleep(1)   # 延迟 1 s
browser.get(jb_url)   # 先打开百度，再打开京东

time.sleep(1)
browser.back()   # 回退

time.sleep(1)
browser.forward()  # 向前

time.sleep(1)
browser.refresh()   # 刷新页面

time.sleep(1)
page_text = browser.page_source  # 获取当面页面代码
print(page_text)

browser.close()  # 关闭当前标签
browser.quit()  # 关闭整个浏览器

```



## 6.3 定位页面元素

 查找元素： 

1. 根据ID。
2. 根据 class。
3. 根据标签名
4. 根据 CSS 选择器。 
5. 根据 name。 
6. 根据 XPath 
7. 根据文本链接。

```py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


element = browser.find_element(By.XPATH, )   # XPATH, CSS 等方法查找
element.click()  # 点击

search_element = browser.find_element(By.ID, 'search_input')
search_element.send_keys('python')  # 在搜索框中输入 
```





## 6.4 设置元素等待和加载策略

**页面加载策略**一共分为三种： 

- `normal`（默认）：完整的加载。把 get 地址的页面以及所有静态资源都下载完成（如 css, 图片，js 等）
- `eager`：等待初始 HTML 文档完全加载和解析，并放弃样式表、图像和子框架加载。
- `none`：仅等待初始页面下载。从现象来看就是打开浏览器输入地址后就不管了。

```py
opt.page_load_strategy = 'eager'   # 设置加载策略方式

start = time.time()
browser.get(url)
end = time.time()
print(end - start)
```



**设置 webdriver等待**： 

很多页面都使用 ajax 技术，页面元素不是同时被加载出来的，为了防止定位这些尚在加载的元素报错，可以设置元素等来增加脚本的稳定性。 webdriver 中的等待分为 显示等待 和 隐式等待。

- 隐式等待：也是指定一个超时时间，如果超出这个时间指定元素还没有被加载出来，就会抛出 NoSuchElementException 异常。除了抛出的异常不同外，还有一点，隐式等待是全局性的，即运行过程中，如果元素可以定位到，它不会影响代码运行，但如果定位不到，则它会以轮询的方式不断地访问元素直到元素被找到，若超过指定时间，则抛出异常。

  `implicitly_wait()`

- 显示等待：设置一个超时时间，每隔一段时间就会检测一次该元素是否存在，如果存在，则执行后续内容，如果超过最大时间（超时时间）则抛出超时异常（TimeoutException）。显示等待需要使用 WebDriverWait，同时配合 untile 或 not until.

  ```py
  from selenium.webdriver.support.ui import WebDriverWait   # 等待
  from selenium.webdriver.support import expected_conditions as EC  # 判断条件
  
  try:
  	elelment = WebDriverWait(driver, 10).until(
  		EC.presence_of_element_located((By.ID, "myDynamicElement"))
  	)
  finally:
  	driver.quit()
  ```

> 当遇到 点击被拦截的问题时：（点击按钮被一些东西覆盖了）
> 使用代码滑动页面：
>
> ```py
> from selenium.webdriver.common.action_chains import ActionChains
> # 通过ActionChains滚动到元素位置
> ActionChains(browser).move_to_element(next_page).perform()  # 移动鼠标到元素上，自动滚动
> ```





## 6.5 切换窗口

在当我们点击页面按钮时，他一般会打开一个新的标签页，但实际上代码并没有切换到最新页面中，这时你如果要定位新页面的标签就会发现定位不到，这时就需要将实际窗口切换到最新打开的那个窗口。

我们先获取当前各个窗口的句柄，这些信息的保存顺序是按时间来的，最新打开的窗口放在数组的末尾，这时我们就可以定位到最新打开的那个窗口了。

```py
browser.switch_to.window(browser.window_handles[-1])  # 使用 clik()点击到新的窗口需要切换
```

```py
browser.switch_to.new_window('tab')   # 直接切换焦点到新窗口就不用切换
browser.get('https://jd.com')   
```



## 6.6 切换表单 frame

很多页面也会用到 `frame/iframe` 表单嵌套，对于这种内嵌的页面 selenium 是无法直接定位的，需要使用 `switch_to.frame()`  方法将当前操作的对象切换到 `frame/iframe` 内嵌的页面。

switch_to.frame() 默认可以用的 id 或 name 属性值直接定位，但如果 iframe 没有 id 或 name，这时就需要使用 xpath 进行定位。

遇到 `<iframe> ` 列嵌表单, 拿不到元素,需要切换到表单中,再定位： 

```py
iframe = browser.find_element(By.XPATH, '//*[@id="anony-reg-new"]/div/div[1]/iframe')
browser.switch_to.frame(iframe)
```



## 6.7 动作链

用 selenium 做爬虫，有时候会遇到需要模拟鼠标和键盘操作才能进行的情况，单击、双击、点击鼠标右键、拖拽、滚动等等。而 selenium 给我们提供了一个处理这类事件 —— ActionChains()

常用方法： 

- `move_to_element`： 将鼠标移动到指定 element, 参数为标签
- `move_by_offset(xoffset, yoffset)`：将鼠标移动到与当前是鼠标位置的偏移处，参数为 X轴 Y轴上移动的距离，（距离单位为像素）
- `click()`：点击一个标签
- `scroll_to_element(iframe)`：鼠标滚动到某个元素
- `scroll_by_amount(0, delta_y)`：鼠标滚轮安装偏移量滚动
- `perform()`：执行所有存储的操作，因为行为链是一系列的动作，上边的命令不会写一个执行一个，执行要通过 perform() 命令全部执行。
- `context_clikc(element)`：右键点击一个标签
- `click_and_hold(element)`：点击且不松开鼠标
- `double_click(element)`：双击
- `drag_and_drop(source,target)`：按住源元素上的鼠标左键，然后移动到目标元素并释放鼠标按钮。
- `drag_and_drop_by_offset(source, xoffset, yffset)`：按住源元素上的鼠标左键，然后移动到目标偏移并释放鼠标按钮
- `release(on_element=None)`：在元素上释放按住的鼠标按钮
- `key_down(value,element=None)`：按下某个键盘上的键
- `key_up(value,element=None)`：松开某个键。

```py
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')   # 隐藏浏览器痕迹
opt.add_experimental_option('excludeSwitches', ['enable-automation'])  # 隐藏自动化浏览器控制标识
opt.add_experimental_option('detach', True)   # 防止浏览器自动退出
service = Service(executable_path="W:\Chrome\chromedriver-win64\chromedriver-win64\chromedriver.exe")
browser = webdriver.Chrome(service=service, options=opt)

url = 'https://www.12306.cn/index/'
browser.implicitly_wait(4)  # 隐式等待
browser.maximize_window()
# temp_url = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc'
browser.get(url)

# 把鼠标悬停到 车票 上
ticket_element = browser.find_element(By.XPATH, '//*[@id="J-chepiao"]/a')
ActionChains(browser).move_to_element(ticket_element).perform()

# 点击单程，进入下一个页面
one_way = browser.find_element(By.XPATH, '//*[@id="megamenu-3"]/div[1]/ul/li[1]/a')
ActionChains(browser).click(one_way).perform()

# 输入出发地
from_station = browser.find_element(By.XPATH, '//*[@id="fromStationText"]')
ActionChains(browser)\
    .click(from_station)\
    .pause(1)\
    .send_keys('西安')\
    .pause(1) \
    .send_keys(Keys.ARROW_DOWN)\
    .pause(1)\
    .send_keys(Keys.ENTER)\
    .perform()   # \ 表示 连续接着写。 send_keys 模拟键盘按键，Keys 都能有代表

# 输入目的地
time.sleep(1)
to_station = browser.find_element(By.XPATH, '//*[@id="toStationText"]')
ActionChains(browser)\
    .click(to_station)\
    .pause(1)\
    .send_keys('北京')\
    .pause(1) \
    .send_keys(Keys.ARROW_DOWN, Keys.ARROW_DOWN)\
    .pause(1)\
    .send_keys(Keys.ENTER)\
    .perform()

# 出发时间
date_element = browser.find_element(By.XPATH, '//*[@id="train_date"]')
ActionChains(browser)\
    .click(date_element)\
    .send_keys(Keys.RIGHT)\
    .send_keys(Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE)\
    .send_keys('2026-01-30')\
    .send_keys(Keys.ENTER)\
    .perform()

# 选择 高铁
browser.find_element(By.XPATH, '//*[@value="G"]').click()

# 发车时间 select 对象
start_time_element = browser.find_element(By.XPATH, '//*[@id="cc_start_time"]')
Select(start_time_element).select_by_visible_text("12:00--18:00")

# 查询
browser.find_element(By.XPATH, '//*[@id="query_ticket"]').click()

```



## 6.8 防止检测

### 6.8.1 使用 stealth.min.js 文件

stealth.min.js 文件来源于 puppeteer, 有开发者给 puppeteer 写了一套插件，叫做 puppeteer-extra。其中，及有一个插件叫做 puppeteer-extra-plugin-stealth 专门用来让 puppeteer 隐藏模拟浏览器的指纹特征。 



python 开发者就需要把其中的隐藏特征的脚本提取出来，做成一个 js 文件。然后让 Selenium 或者 Pyppeteer 在打开任意网页之前，先运行一下这个 js 文件里面的内容。 puppeteer-extra-plugin-stealth 的作者还写了另外一个工具，叫做 extract-stealth-evasions。这个东西就是用来生成 stealth.min.js 文件的。



下载地址： https://github.com/requireCool/stealth.min.js 

执行代码： （隐藏浏览器特征）

```py
with open("W:\Chrome\chromedriver-win64\chromedriver-win64\stealth.min.js") as f:
    js = f.read()
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
                        {"source": js})
```



### 6.8.2 使用 debugging 模式

让 selenium 连接实现配置好的浏览器



引用场景： 

爬取需要登陆才能获取的内容，比如扫码登录、手机验证码登录等。通过这种方式绕过短期无法解决的验证码识别； 

也可以通过这种方式绕过一些无法自动完成的复杂操作，然后自动再执行后面的爬虫工作。



**步骤1：**

找到 Chrome 浏览器的安装路径： `C:\Program Files\Google\Chrome\Application`

在命令提示符输入下面命令创建配置一个浏览器： `chrome.exe --remote-debugging-port='端口' --user-data-dir="安装路径"`

``` linux
chrome.exe --remote-debugging-port=8888 --user-data-dir="W:\Chrome\chromedriver-win64\chromedriver-win64"
```

快捷方式设置参数： 

​	在 chrome 的快捷方式上右击，选择属性，快捷方式的目标栏加空格加上命令： （先复制一个快捷方式，重命名 t1）

​	`"C:\Program Files\Google\Chrome\Application\chrome.exe"  --remote-debugging-port=8888 --user-data-dir="W:\Chrome\chromedriver-win64\chromedriver-win64" `



加入调配模式： 

```py
opt = Options()
opt.debugger_address = '127.0.0.1:8888'  # Selenium 的Chrome 调试模式配置
```



**如何使用： **

1. 手工打开浏览器
2. 用 Selenium 链接浏览器。 





### 6.8.3 使用 undertected_chromedriver

undetected_chromedriver 是 Python 爱好者基于 selenium ，专门开发用来可以防止浏览器特征被识别的库，目前能规避大多数检测，并且可以根据浏览器版本自动下载驱动。 

但是目前版本更新较慢，随着 Chrome 浏览器的不断更新，各种兼容新问题不断涌入。



**使用方法： **

先安装库：`pip install undetected_chromedriver`





##  6.9 验证码识别

### 6.9.1 图片识别

**超级鹰：**

1. 地址： https://www.chaojiying.com/

2. 进入开发文档： <img src="assets/image-20260130141928666.png" alt="image-20260130141928666" style="zoom: 50%;" />

3.  文档解压缩后放入项目中。 

4. 软件ID：<img src="assets/image-20260130144307947.png" alt="image-20260130144307947" style="zoom:50%;" />

5. 生成一个 json 文件，存放 用户名，密码，软件ID：

   ```py
   {
     "username" : "55252624",
     "password" : "WYwy132639@",
     "soft_id"  : "977480"
   }
   
       with open("password.json", 'r') as f:
           info = json.loads(f.read())   # 以json 格式读取
       password = info['password']
       username = info['username']
       soft_id = info['soft_id']
   ```

6. 查看识别类型：  <img src="assets/image-20260130145407339.png" alt="image-20260130145407339" style="zoom:50%;" />

**登录步骤：**

1. 输入用户名和密码
2. 截取图片验证码
3. 等待打码平台识别
4. 输入验证码
5. 点击登录





### 6.9.2 滑块验证码

模拟登录豆瓣： 使用 debugging 模式（比较严格）

登录步骤： 

1. 输入用户名和密码； 
2. 截取滑块背景图片和滑块图片；
3. 计算滑块和缺口之间的距离； 
4. 按照合理速度拖动滑块过验证。 



`pyautogui`：可以控制电脑上的鼠标和键盘，绕过自动化检测； 

根据指定坐标进行点击。 

```py
def press_button(pic_addr):
    loc = pyautogui.locateOnScreen(pic_addr, confidence=0.6)  # 置信度为 0.6, 求的坐标
    p = pyautogui.center(loc)   # 移动到按钮中间
    pyautogui.moveTo(p)
    pyautogui.leftClick()

# 点击登录
pic_addr = 'slid_img/douban_login.png'   # 存入需要点击的地址图片
press_button(pic_addr)
```



获取滑块图片，利用 `screenshot_as_png` 进行截图。

```py
# 进入验证码 iframe
WebDriverWait(browser, 4).until(EC.visibility_of_element_located((By.ID, 'tcaptcha_iframe_dy')))
slid_iframe = browser.find_element(By.ID, 'tcaptcha_iframe_dy')
browser.switch_to.frame(slid_iframe)

# 获取滑块背景图片  
background_element = browser.find_element(By.ID, 'slideBg')
background_location = background_element.location
print(background_location)
bg_img = background_element.screenshot_as_png   # 此处注意不要缩放页面
filename = int(time.time())
# 获取图片
with open(f'slid_img/{filename}_background.png', 'wb') as f:
    f.write(bg_img)
    print("已下载滑块图片")
 
# 获取小滑块图片 （因为是 CSS 加载，Xpath可能会变化）
slid_element1 = browser.find_element(By.XPATH, '//*[@id="tcOperation"]/div[8]')
slid_element2 = browser.find_element(By.XPATH, '//*[@id="tcOperation"]/div[9]')
s1 = slid_element1.size
s2 = slid_element2.size
if s1['width'] > 100 and s1['height'] < 20:
slid_element = slid_element2
else:
slid_element = slid_element1
slid_location = slid_element.location
print(slid_location)
slid_img = slid_element.screenshot_as_png
# 获取图片
with open(f'slid_img/{filename}_slid.png', 'wb') as f:
f.write(slid_img)
print("已下载滑块图片") 
```





计算滑块和缺口距离： OpenCV 模块匹配（`cv2.matchTemplate`）

应用模板匹配就像在源图像上从左到右，从上到下滑动模板，在每一个位置都计算一个指标表明这个位置处两个图像块之间匹配程度的高低。

OpenCV 官网链接： https://docs.opencv.org/3.4/de/da9/tutorial_template_matching.html

`opencv-python`, `opencv-contrib-python`

计算距离 distance: 

```python
class CalculateDistance:
    # 获取需要滑动的地址
    # 将验证码背景大图和需要滑动的小图进行处理，先在大图中找到相似的小图位置，再获取对应的像素偏移量

    def __init__(self, background_path, slide_path, offset_px, offset_py, diaplay):
        '''

        :param background_path: 验证码背景大图地址
        :param slide_path: 需要滑块图片地址
        :param offset_px: 小图距离在大图上的左边边距（像素偏移量）
        :param offset_py: 小图距离在大图上的顶部边距（像素偏移量）
        :param diaplay:
        '''

        # 读取图片
        self.background_img = cv2.imread(background_path)
        self.offset_px = offset_px
        self.offset_py = offset_py
        self.slide_img = cv2.imread(slide_path, cv2.IMREAD_UNCHANGED)
        # 计算 x轴 缩放隐私，以 50px 为基准
        scale_x = 50 / self.slide_img.shape[1]
        # 使用最近邻插值法缩放，得到缩放后 50x50 的图片
        self.slide_scale_img = cv2.resize(self.slide_img, (0, 0), fx=scale_x, fy=scale_x)
        self.background_cut_img = None
        self.display = diaplay

    def get_distance(self):
        # 将小图转换为灰色
        slid_grey_img = cv2.cvtColor(self.slide_scale_img, cv2.COLOR_BGR2GRAY)
        # 使用 canny 算子，提出图片边缘特征
        # 特征值可以调试： 100， 200， 细节特征比较明显，数值增大后特征较为粗略
        slide_edge_img = cv2.Canny(slid_grey_img, 100, 250)
        # self.cv_show('canny', slide_edge_img)
        # 将背景图转换为灰色
        background_grey_img = cv2.cvtColor(self.background_cut_img, cv2.COLOR_BGR2GRAY)
        # 使用 canny 算子，提取图片边缘特征
        background_edge_img = cv2.Canny(background_grey_img, 100, 300)
        # self.cv_show('bg_canny', background_edge_img)
        # 取小图的高和宽
        h, w = slide_edge_img.shape

        # 将滑块图与背景进行模板匹配，找到缺口对应的位置
        result = cv2.matchTemplate(slide_edge_img, background_edge_img, cv2.TM_CCOEFF)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        # 获取缺口左上角位置
        top_left = (max_loc[0], max_loc[1])
        # 右下角位置
        bottom_right = (max_loc[0] + w, max_loc[1] + h)

        # 在切割后背景图片中画出需要移动的终点位置
        # rectangle（图片源数据，左上角，右下角，颜色，画笔厚度）
        # if self.display:
        #     print(top_left)
        #     print(bottom_right)
        #     after_img = cv2.rectangle(self.background_cut_img, top_left, bottom_right, (0, 0, 255), 0)
            # 画图
            # self.cv_show('after', after_img)
        # 计算移动距离
        slide_distance = top_left[0] + w + 10
        return slide_distance

    # 对背景图片进行剪切
    def cut_background(self):
        # 切割图片的上下边框
        height = self.slide_scale_img.shape[0]
        # 将背景图中上下多余部分以及滑块图片部分去除. 如：background_img[y1:y2, x1:]
        self.background_cut_img = self.background_img[self.offset_py - 10: self.offset_py + height + 10,
                                  self.offset_px + height + 10:]

    def cv_show(self, name, img):
        cv2.imshow(name, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def run(self):
        self.cut_background()
        return self.get_distance()
```

将拖动轨迹模拟人工操作： 

```python
def handle_distance(distance):
    # 将直线距离转为缓慢的轨迹
    import random
    slow_distance = []
    while sum(slow_distance) <= distance:
        slow_distance.append(random.randint(-2, 15))

    if sum(slow_distance) != distance:
        slow_distance.append(distance - sum(slow_distance))
    return slow_distance

def drag_slide(tracks, slide_addr):
    # 拖动滑块
    loc = pyautogui.locateOnScreen(slide_addr, confidence=0.6)
    p1 = pyautogui.center(loc)
    pyautogui.moveTo(p1)
    pyautogui.mouseDown()
    for track in tracks:
        pyautogui.move(track, uniform(-2, 2), duration=0.15)
    pyautogui.mouseUp()
```



### 6.9.3 处理点选验证码（B站）

利用 debugging 模式 ： 



点选验证码利用超级鹰： 

```python 
# 获取图片
WebDriverWait(browser, 4).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="geetest_panel_next"]')))
pic_element = browser.find_element(By.XPATH, '//div[@class="geetest_panel_next"]')
img = pic_element.screenshot_as_png

# 点击验证码
chaojiying = Chaojiying_Client("55252624", "WYwy132639@", "977480")
locs = chaojiying.PostPic(img, 9004)['pic_str']
print(locs)

locs = locs.split('|')
width = pic_element.size['width']
height = pic_element.size['height']
for loc in locs:
    x_ref = int(loc.split(',')[0])
    y_ref = int(loc.split(',')[1])
    x = x_ref - width // 2 + 10
    y = y_ref - height // 2 + 30

    ActionChains(browser).move_to_element_with_offset(pic_element, x, y).click().perform()
```







# 7 反反爬

**什么是反反爬**

爬虫：采用任何技术手段，用别人开发好的程序， 批量获取对方数据，都是爬虫。

反爬：用任何计算手段，阻止别人批量获取自己的数据。

反反爬： 使用任何技术手段，绕过对方的反爬策略。



**常见的反爬手段：**

- 检测 user_agent
- ip 访问频率的限制
- 必须登录（账号访问频率 + ip）最有效的方式，需要维护多个账号。账号管理比爬虫本身更加重要。
- 动态网页，js 逻辑加密和混淆，加大分析难度。
- 机器学习，分析爬虫行为。



## 7.1 user_agent

python 库 ： `fake-useragent`用于存储 user_agent 池

 ```py
 from fake_useragent import UserAgent
 
 ua = UserAgent() 
 user_agent = ua.random
 
 headers = {'User_Agent': user_agent}
 ```



## 7.2 ip 代理

在 `快代理` 购买私密代理； 



## 7.3 使用 cookie 

**获取 cookie: **

1. 登录账号（手动或者模拟登录）
2. 获取 cookie，下载到本地。 
3. 加载到浏览器中，刷新



手动获取： 

手动登录后打开 Network：<img src="assets/image-20260131141225915.png" alt="image-20260131141225915" style="zoom: 50%;" />

复制：

```py
headers = {
	'Cookie': "", 
	'User-Agent': " "
}
```





自动获取，使用 selenium 自动登录后： 

```py
douban.cookies = browser.get_cookies()
douban_cookies_json = json.dumps(douban_cookies)

with open(f'Cookies/douban_cookies.json', 'w', encoding='utf-8') as f:
    f.write(douban_cookies_json)
    print('已存储 cookies')
    
```

拿取： 

```py
browser.get(url)

with open(f'Cookies/douban_cookies.json', 'r', encoding='utf-8') as f:
    cookies = json.loads(f.read)
    print('已读取 cookies')
    
for cookie in cookies: 
    cookie_dic = {
        "domain": ".douban.com", 
        'name': cookie.get('name'),
        'value': cookie.get('value'),
        "expires": "", 
        'path': '/', 
        'httpOnly': False,
        'HostOnly': False, 
        'Secure': False
    }
    print(f'正在添加Cookie---{cookie_dic}')
    bowser.add_cookie(cookie_dict)
    
browse.refresh() 
```



## 7.4 机器人验证

![image-20260203114028090](assets/image-20260203114028090.png)

```py
# 等待页面加载+处理可能的验证（如果出现验证，手动过一下，或者加打码平台）
try:
    WebDriverWait(browser, 15).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'cell--UMz-x'))
    )
except:
    print("出现人机验证，请手动完成验证后按回车键继续...")
    input()  # 暂停，让你手动过验证
```





# 8 图像化界面 PyQT5

图形化界面相关库：Tkinter，wxPython, PyQT5 



## 8.1 安装

安装清华镜像源：https://pypi.tuna.tsinghua.edu.cn/simple

新建一个项目，下载 pyqt5 和 pyqt5-tools 两个软件包。 

添加图形化界面工具到 Pycharm 中。<img src="assets/image-20260131174718645.png" alt="image-20260131174718645" style="zoom: 50%;" />

添加工具： 将显示页面转化为 py 文件。 <img src="assets/image-20260131175228260.png" alt="image-20260131175228260" style="zoom:67%;" />



`m PyQt5.uic.pyuic $FileName$ -o $FileNameWithoutExtension$.py`



创建可视化 UI： 工具 -> 外部工具 -> QT_designer 

生成可编辑 python 文件： 右击新建的 .ui 文件 -> 外部工具 -> pyuic



控件窗口： <img src="assets/image-20260131224502608.png" alt="image-20260131224502608" style="zoom:67%;" />

创建应用：`QApplication`

窗口 ：

- `QWidget`：通用小窗口，用户名、密码等。
- `QMainWindow`：做复杂窗口，例如 Pycharm 窗口
- `QDialog`：确认、取消等。

设置窗口大小：resize

设置窗体位置： move



添加控件：

- 创建标签： QLabel()
- 创建按钮：QPushButton()

































































































































































































































































































































































