import time
import undetected_chromedriver as uc

# 方法1：最推荐（明确指定显示窗口）
browser = uc.Chrome(headless=False)          # 或 headful=False（部分版本支持）

# 方法2：使用 ChromeOptions（更清晰，兼容性好）
options = uc.ChromeOptions()
options.headless = False               # 旧写法（部分版本还能用）
# 或
# options.add_argument("--headless")   # 有这个参数 = 无头
# options.add_argument("--headless=new")  # 新的无头模式（Chrome 109+）

options = uc.ChromeOptions()
options.headless = False
options.add_argument("--start-maximized")      # 启动时最大化（可选）
options.add_argument("--disable-infobars")     # 去掉“Chrome正被自动化测试软件控制”提示（可选）
browser = uc.Chrome(options=options)


browser.get('https://www.taobao.com')
time.sleep(100)