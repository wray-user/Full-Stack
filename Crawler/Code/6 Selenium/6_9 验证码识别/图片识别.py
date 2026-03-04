# -*- coding: utf-8 -*-
# @Time    : 2026/1/30 下午2:36
# @Author  : hjx
# @File    : 图片识别.py

import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from chaojiying_Python.chaojiying import Chaojiying_Client

service = Service(r"W:\Chrome\chromedriver-win64\chromedriver-win64\chromedriver.exe")

def login(url, username, password, soft_id):

    browser = webdriver.Chrome(service=service)
    browser.get(url)

    # 输入用户名
    time.sleep(1)
    browser.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys(username)

    # 输入密码
    time.sleep(1)
    browser.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys(password)

    # 获取验证码图片
    img = browser.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png  # screenshot_as_png 截图
    chaojiying = Chaojiying_Client(username=username, password=password, soft_id=soft_id)
    code = chaojiying.PostPic(img, 1902)['pic_str']
    print(code)

    # 输入验证码
    time.sleep(1)
    browser.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(code)

    # 点击登录
    browser.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()

    time.sleep(100)


if __name__ == '__main__':
    url = "https://www.chaojiying.com/user/login/"
    with open('./chaojiying_Python/password.json', 'r', encoding='utf-8') as f:
        info = json.loads(f.read())  # 以json 格式读取
    password = info['password']
    username = info['username']
    soft_id = info['soft_id']
    login(url, username, password, soft_id)