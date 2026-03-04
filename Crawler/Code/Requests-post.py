# -*- coding: utf-8 -*-
# @Time    : 2025/12/31 下午2:37
# @Author  : hjx
# @File    : Requests-post.py

import requests
import pprint   # 用于打印 json 格式规范化

keyword = input('请输入需要翻译的关键字： ')
query_url = 'https://fanyi.sogou.com/reventondc/suggV3'   # 从 Headers 处拿到网址
User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
headers = {'User-Agent': User_Agent}
data = {             # Payload 处拿取，post 请求才有
    'from': 'auto',
    'to': 'zh-CHS',
    'client': 'web',
    'text': keyword,
    'uuid': 'c1c030ce-17e5-407f-9ca6-57c491874069',
    'pid': 'sogou-dict-vr',
    'addSugg': 'on'
    }

response = requests.post(query_url, data=data, headers=headers)

result = response.json()['sugg'][0]['v']    # 存放翻译结果
pprint.pprint(result)