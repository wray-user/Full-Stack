# -*- coding: utf-8 -*-
# @Time    : 2025/12/31 上午10:17
# @Author  : hjx
# @File    : Requests-get.py

import requests

# 1. 指定 url
# 'https://www.sogou.com/web?query=%E5%91%A8%E6%9D%B0%E4%BC%A6'

# keyword = '周杰伦'
# url = 'https://www.sogou.com/web?query=周杰伦'

keyword = input('请输入需要查询的关键字： ')
url = f'https://www.sogou.com/web?query={keyword}'
# url = 'https://www.sogou.com/web?query={}'.format(keyword)   # 和上面一样，f 就是format 的缩写。

User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'

headers = {'User-Agent': User_Agent}

# 2. 网络请求，获得参数
response = requests.get(url=url, headers=headers)
print(response.text)
# print(response.request.headers)
# print(response.url)

# 3.保存网页
with open(keyword + '.html', 'w', encoding='utf-8') as f:
    f.write(response.text)
    print(f'已下载..{keyword}')