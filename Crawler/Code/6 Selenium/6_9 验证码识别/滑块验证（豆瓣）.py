# -*- coding: utf-8 -*-
# @Time    : 2026/1/30 下午3:34
# @Author  : hjx
# @File    : slid_img（豆瓣）.py

import time
import cv2
import requests
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint
from random import uniform
from OpenCV.CalculateDistance import CalculateDistance

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
def press_button(pic_addr):
    loc = pyautogui.locateOnScreen(pic_addr)   # , confidence=0.6
    p = pyautogui.center(loc)   # 移动到按钮中间
    pyautogui.moveTo(p)
    pyautogui.leftClick()


def login(url, nsername, password):
    serivce = Service(r"W:\Chrome\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    opt = Options()
    opt.debugger_address = "127.0.0.1:8888"
    browser = webdriver.Chrome(service=serivce, options=opt)
    browser.get(url)

    # 点击密码登录
    # 进入到 iframe
    iframe = browser.find_element(By.XPATH, '//*[@id="anony-reg-new"]/div/div[1]/iframe')
    browser.switch_to.frame(iframe)
    browser.find_element(By.XPATH, '/html/body/div[1]/div[1]/ul[1]/li[2]').click()
    browser.implicitly_wait(4)  # 隐式等待
    time.sleep(uniform(1, 4))

    # 输入用户名和密码
    browser.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
    time.sleep(uniform(1, 4))
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    time.sleep(uniform(1, 4))

    # 点击登录
    pic_addr = 'slid_img/douban_login.png'
    press_button(pic_addr)

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

    '''
        # 从style属性提取背景图URL
    bg_style_text = background_element.get_attribute('style')
    # 用字符串分割精准提取
    bg_url = bg_style_text.split('background-image: url("')[1].split('");')[0]  # 先分要后面，后分要前面
    # 获取图片
    filename = int(time.time())
    with open(f'slid_img/{filename}_background.png', 'wb') as f:
        f.write(requests.get(bg_url).content)
        print("已下载背景图片")
    '''

    # 获取小滑块图片
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


    # 背景图片地址和滑块图片的地址
    bg_addr = f'slid_img/{filename}_background.png'
    sd_addr = f'slid_img/{filename}_slid.png'
    print(sd_addr)

    # 计算滑块和背景图片之间 x轴距离
    offset_x = slid_location['x'] - background_location['x']
    offset_y = slid_location['y'] - background_location['y']

    slide_offset = CalculateDistance(bg_addr, sd_addr, offset_x, offset_y, 0)
    slide_distance = slide_offset.run() + 40
    print(slide_distance)

    # 计算滑块轨迹
    tracks = handle_distance(slide_distance)

    # 拖动滑块
    slid_img_addr = 'slid_img/douban_slid.png'
    drag_slide(tracks, slid_img_addr)




if __name__ == '__main__':
    url = "https://www.douban.com/"
    username = "19102712955"
    password = "WYwy132639@"
    login(url, username, password)


