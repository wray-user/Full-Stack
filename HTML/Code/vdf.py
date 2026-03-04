import requests
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# 创建保存图片的文件夹
if not os.path.exists('cat_image'):
    os.makedirs('cat_image')

# 初始化浏览器，最大化反爬绕过
options = webdriver.ChromeOptions()
# 核心反爬绕过配置
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument(
    '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
# 禁用图片加载（可选，加快页面加载）
# options.add_argument('--blink-settings=imagesEnabled=false')

service = Service("W:\Chrome\chromedriver-win64\chromedriver-win64\chromedriver.exe")
browser = webdriver.Chrome(service=service, options=options)
# 彻底清除webdriver标识
browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

# 访问页面
target_Url = 'https://pixabay.com/images/search/cat/'
browser.get(target_Url)

# 模拟真人深度交互，触发完整内容加载
time.sleep(3)
# 随机点击页面空白处
ActionChains(browser).move_by_offset(300, 400).click().perform()
# 分多次滚动，触发懒加载（关键）
for _ in range(5):
    browser.execute_script("window.scrollBy(0, 500)")
    time.sleep(1)

# 等待图片容器完全加载
WebDriverWait(browser, 20).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, 'cell--UMz-x'))
)

# 获取所有图片容器
img_containers = browser.find_elements(By.CLASS_NAME, 'cell--UMz-x')
print(f"总共找到 {len(img_containers)} 个.cell--UMz-x 容器\n")

success_count = 0  # 成功下载计数
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Referer': 'https://pixabay.com/'  # 必须加referer，否则图片请求会被拒绝
}

for idx, container in enumerate(img_containers):
    try:
        # 1. 定位容器内的img标签（核心：直接从img提取地址）
        img_tags = container.find_elements(By.TAG_NAME, 'img')
        if not img_tags:
            print(f"第 {idx + 1} 个容器：无img标签（跳过）")
            continue

        img_tag = img_tags[0]  # 取第一个img标签
        # 2. 优先从srcset提取高清地址（格式："地址1 1x, 地址2 2x, 地址3 4x"）
        srcset = img_tag.get_attribute('srcset')
        img_url = None

        if srcset and srcset.strip():
            # 拆分srcset，取分辨率最高的地址（最后一个）
            src_list = [item.strip().split(' ')[0] for item in srcset.split(',') if item.strip()]
            if src_list:
                img_url = src_list[-1]  # 最后一个是最高清的
        else:
            # 没有srcset则取src属性
            img_url = img_tag.get_attribute('src')

        # 3. 验证图片地址有效性
        if not img_url or not img_url.startswith('https'):
            print(f"第 {idx + 1} 个容器：无有效图片地址（跳过）")
            continue

        # 4. 下载图片（必须加referer请求头）
        print(f"第 {idx + 1} 个容器：开始下载 {img_url[:60]}...")
        response = requests.get(
            img_url,
            headers=headers,
            timeout=20,
            stream=True
        )

        if response.status_code == 200:
            # 保存图片
            img_name = f"cat_{success_count + 1}.jpg"
            with open(f'cat_image/{img_name}', 'wb') as f:
                for chunk in response.iter_content(chunk_size=2048):
                    if chunk:
                        f.write(chunk)
            success_count += 1
            print(f"✅ 第 {success_count} 张图片下载完成：{img_name}")
        else:
            print(f"❌ 第 {idx + 1} 个容器：图片请求失败（状态码：{response.status_code}）")

    except Exception as e:
        print(f"❌ 第 {idx + 1} 个容器：处理异常 - {str(e)[:60]}...")

    # 控制爬取频率，避免被封
    time.sleep(1.5)
    # 只下载10张，避免过多请求
    # if success_count >= 10:
    #     break

# 最终统计
print(f"\n===== 爬取完成 =====\n总容器数：{len(img_containers)}\n成功下载：{success_count} 张图片")
browser.quit()