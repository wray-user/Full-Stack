# -*- coding: utf-8 -*-
# @Time    : 2026/1/24 下午10:56
# @Author  : hjx
# @File    : 猫咪图片爬取.py


import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from fake_useragent import UserAgent
import json

# ua = UserAgent()
# user_agent = ua.random
#
# headers = {'User_Agent': user_agent}

# 初始化浏览器，模拟真实访问
options = webdriver.ChromeOptions()
# 1. 隐藏自动化标识
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
# 2. 随机UA（避免固定UA）
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36')
# 3. 模拟真人窗口（避免无头模式被检测）
options.add_argument('--window-size=1920,1080')
options.add_argument('--start-maximized')

# 创建带重试的session，避免单次超时失败
session = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
           'Referrer-Policy': 'strict-origin-when-cross-origin',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
           }
service = Service("W:\Chrome\chromedriver-win64\chromedriver-win64\chromedriver.exe")
browser = webdriver.Chrome(service=service, options=options)
# 彻底清除webdriver标识
browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

target_Url = 'https://pixabay.com/images/search/cat/'
browser.get(target_Url)
time.sleep(2)

# 等待页面加载+处理可能的验证（如果出现验证，手动过一下，或者加打码平台）
try:
    WebDriverWait(browser, 5).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'cell--UMz-x'))
    )
except:
    print("出现人机验证，请手动完成验证后按回车键继续...")
    input()  # 暂停，让你手动过验证

imgs = browser.find_elements(By.CLASS_NAME, 'cell--UMz-x')
print(f"总共找到 {len(imgs)} 个.cell--UMz-x 容器\n")
i = 1

for img in imgs:
    # time.sleep(3)
    time.sleep(1)
    # 方式A：使用Selenium内置方法（推荐，稳定）
    browser.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", img)
    img_element = img.find_element(By.TAG_NAME, 'img')
    src = img_element.get_attribute('src')

    print(f"第{i}张地址：{src}")
    if 'https://cdn.pixabay.com/photo' not in src:
        print(f"未加地址{src}图片")
        continue
    else:
        time.sleep(1)
        response = session.get(
                src,
                headers=headers,
                timeout=8,  # 超时时间8秒，避免卡死
                verify=False  # 忽略SSL验证，解决握手超时
            )
        print(response.status_code)
        with open(f'cat_image/{i}.jpg', 'wb') as f:
            f.write(response.content)
            print(f"已保存第{i}张照片")
        i += 1








