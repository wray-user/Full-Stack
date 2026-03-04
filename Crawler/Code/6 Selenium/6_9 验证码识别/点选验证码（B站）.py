# -*- coding: utf-8 -*-
# @Time    : 2026/1/31 上午10:23
# @Author  : hjx
# @File    : 点选验证码（B站）.py

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from chaojiying_Python.chaojiying import Chaojiying_Client

opt = Options()
opt.debugger_address = "127.0.0.1:8888"
service = Service(r"W:\Chrome\chromedriver-win64\chromedriver-win64\chromedriver.exe")

def login(url, username, password):
    browser = webdriver.Chrome(service=service, options=opt)
    browser.get(url)

    # 点击登录
    login_element = (By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[1]/ul[2]/li[1]/li/div[1]/div/span')
    WebDriverWait(browser, 4).until(EC.visibility_of_element_located(login_element))
    browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[1]/ul[2]/li[1]/li/div[1]/div/span').click()

    # 确认弹框加载
    pw_element = (By.XPATH, '/html/body/div[3]/div/div[4]/div[1]/div[1]')
    WebDriverWait(browser, 6).until(EC.visibility_of_element_located(pw_element))

    # 输入用户名
    time.sleep(2)
    browser.find_element(By.XPATH, '//input[@placeholder="请输入账号"]').send_keys(username)

    # 输入密码
    time.sleep(2)
    browser.find_element(By.XPATH, '//input[@placeholder="请输入密码"]').send_keys(password)

    # 点击登录
    time.sleep(1)
    browser.find_element(By.XPATH, '/html/body/div[3]/div/div[4]/div[2]/div[2]/div[2]').click()

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


    # 点击确认
    browser.find_element(By.XPATH, '//div[@class="geetest_commit_tip"]').click()




if __name__ == '__main__':
    url = "https://www.bilibili.com/"
    username = "usename"
    password = "<PASSWORD>"

    login(url, username, password)