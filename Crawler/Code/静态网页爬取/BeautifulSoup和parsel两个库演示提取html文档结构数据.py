# -*- coding: utf-8 -*-
# @Time    : 2025/12/30 下午6:58
# @Author  : hjx
# @File    : BeautifulSoup和parsel两个库演示提取html文档结构数据.py.py


from bs4 import BeautifulSoup
from parsel import Selector


# 帖子保存容器
class NoteContent:
    def __init__(self, title: str = "", author: str = "", publish_date: str = "", detail_link: str = ""):
        self.title = title
        self.author = author
        self.publish_date = publish_date
        self.detail_link = detail_link      # 文章的详情页链接（URL 地址）

    def __str__(self):
        return f"""
        Title: {self.title}
        User: {self.author}
        Publish Date: {self.publish_date}
        Detail Link: {self.detail_link}
        """




def parse_html_use_bs(html_content:str):
    """
    使用 BeautifulSoup 提取帖子标题、作者、发布日期， 基于 css 选择器提取
    :param html_content: htlm 源码内容
    :return:
    """

    # 初始化一个帖子保存容器
    note_content = NoteContent()

    # 初始化 bs 查询对象
    soup = BeautifulSoup(html_content, 'lxml')
    '''
    作用是把爬取到的 HTML 文本（html_content）转换成一个可操作的、结构化的对象（soup），方便后续提取数据。
    lxml 是 BeautifulSoup 依赖的 “解析器”，负责把原始的 HTML 字符串解析成 BeautifulSoup 能识别的树形结构（DOM 树）。
    BeautifulSoup 支持多种解析器（比如 html.parser、lxml、html5lib），lxml 是最常用的一种，优势是：
    '''

    # 提取标题并去掉左右除换行空格字符
    note_content.title = soup.select("div.r-ret div.title a")[0].text.strip()
    '''
    soup.select() 方法 —— 它专门支持 CSS 选择器语法，通过标签层级、标签名、class 属性（此处省略了 .，实际是通过 class 筛选）来定位元素.
    按 “父元素 → 子 / 后代元素” 的顺序逐层筛选，
    .r-ret：这是 CSS 选择器中匹配 class 属性的规则
    空格：表示 “后代元素”（即当前元素下的任意层级子元素，不是必须直接子元素）；
    .text：提取该 <a> 标签内的文本内容（即标题文字）；
    .strip()：去除文本首尾的空格、换行符、制表符等无效字符，得到纯净的标题。
    '''

    # 提取作者
    note_content.author = soup.select("div.r-ret div.meta div.author")[0].text.strip()

    # 提取发布日期
    note_content.publish_date = soup.select("div.r-ret div.meta div.date")[0].text.strip()

    # 提取帖子连接
    note_content.detail_link = soup.select("div.r-ret div.title a")[0]["href"]

    print("BeautifulSoup" + "*" * 30)
    print(note_content)
    print("BeautifulSoup" + "*" * 30)



def parse_html_use_parse(html_content:str):
    '''
    使用 parsel 提取帖子标题、作者、发布日期，基于 xpath 选择器提取
    :param html_content:  html 源码
    :return:
    '''

    # 初始化一个帖子保存容器
    note_content = NoteContent()

    # 使用 parsel 创建选择器对象
    selector = Selector(text=html_content)

    # 使用 XPath 提取标题并去除左右空格
    note_content.title = selector.xpath(
        "//div[@class='r-ent']/div[@class='title']/a/text()").extract_first().strip()
    '''
    // 全局查找标识，表示 “从 HTML 文档的任意位置开始查找”（不限制起始层级，非仅根节点下），是 XPath 常用的起始匹配符。
    [@class='r-ent']：XPath 中匹配属性的固定语法（@ + 属性名 = ' 属性值 '），表示筛选出 class="r-ent" 的 <div> 标签；
    .extract_first() 是 Scrapy Selector 的专属方法（lxml 中对应 xpath()[0]，若需兼容可使用），功能是：
        提取列表中的第一个有效匹配结果（对应第一个 <a> 标签的文本）；
        容错性强：如果 XPath 未匹配到任何结果（列表为空），不会抛出 IndexError 异常，而是返回 None，避免程序崩溃；
    对比：若写成 selector.xpath("xxx")[0].extract()，当无匹配结果时会报错，.extract_first() 更安全。
    '''

    # 使用 xpath 提取作者
    note_content.author = selector.xpath(
        "//div[@class='r-ent']/div[@class='meta']/div[@class='author']/text()").extract_first().strip()

    # 使用XPath提取发布日期
    note_content.publish_date = selector.xpath(
        "//div[@class='r-ent']/div[@class='meta']/div[@class='date']/text()").extract_first().strip()

    # 使用XPath提取帖子链接
    note_content.detail_link = selector.xpath(
        "//div[@class='r-ent']/div[@class='title']/a/@href").extract_first()

    print("parsel" + "*" * 30)
    print(note_content)
    print("parsel" + "*" * 30)