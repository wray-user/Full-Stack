# -*- coding: utf-8 -*-
# @Time    : 2025/12/31 下午2:49
# @Author  : hjx
# @File    : 案例-筛选豆瓣电影.py

import requests
import pprint

''' https://m.douban.com/rexxar/api/v2/subject/recent_hot/movie?
  start=0&limit=20&category=%E5%86%B7%E9%97%A8%E4%BD%B3%E7%89%87&type=%E6%AC%A7%E7%BE% '''

url = 'https://m.douban.com/rexxar/api/v2/subject/recent_hot/movie'
parameters = {              # 用于get 请求，在 Payload 处拿取
    'start': '0',
    'limit': '20',
    'category': '热门',
    'type': '全部',
}

User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
headers = {'User-Agent': User_Agent,
           'Referer': 'https://movie.douban.com/explore',    # 注明来源， 来源合法
           }

response = requests.get(url=url, headers=headers, params=parameters).json()['items']

# 提取评分和 title
for info in response:
    rate = info['rating']['value']
    title = info['title']
    if float(rate) >= 8:
        print(title, rate)


