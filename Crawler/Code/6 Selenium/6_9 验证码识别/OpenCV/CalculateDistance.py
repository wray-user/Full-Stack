import numpy
import cv2

class CalculateDistance:
    # 获取需要滑动的地址
    # 将验证码背景大图和需要滑动的小图进行处理，先在大图中找到相似的小图位置，再获取对应的像素偏移量

    def __init__(self, background_path, slide_path, offset_px, offset_py, diaplay):
        '''

        :param background_path: 验证码背景大图地址
        :param slide_path: 需要滑块图片地址
        :param offset_px: 小图距离在大图上的左边边距（像素偏移量）
        :param offset_py: 小图距离在大图上的顶部边距（像素偏移量）
        :param diaplay:
        '''

        # 读取图片
        self.background_img = cv2.imread(background_path)
        self.offset_px = offset_px
        self.offset_py = offset_py
        self.slide_img = cv2.imread(slide_path, cv2.IMREAD_UNCHANGED)
        # 计算 x轴 缩放隐私，以 50px 为基准
        scale_x = 50 / self.slide_img.shape[1]
        # 使用最近邻插值法缩放，得到缩放后 50x50 的图片
        self.slide_scale_img = cv2.resize(self.slide_img, (0, 0), fx=scale_x, fy=scale_x)
        self.background_cut_img = None
        self.display = diaplay

    def get_distance(self):
        # 将小图转换为灰色
        slid_grey_img = cv2.cvtColor(self.slide_scale_img, cv2.COLOR_BGR2GRAY)
        # 使用 canny 算子，提出图片边缘特征
        # 特征值可以调试： 100， 200， 细节特征比较明显，数值增大后特征较为粗略
        slide_edge_img = cv2.Canny(slid_grey_img, 100, 250)
        # self.cv_show('canny', slide_edge_img)
        # 将背景图转换为灰色
        background_grey_img = cv2.cvtColor(self.background_cut_img, cv2.COLOR_BGR2GRAY)
        # 使用 canny 算子，提取图片边缘特征
        background_edge_img = cv2.Canny(background_grey_img, 100, 300)
        # self.cv_show('bg_canny', background_edge_img)
        # 取小图的高和宽
        h, w = slide_edge_img.shape

        # 将滑块图与背景进行模板匹配，找到缺口对应的位置
        result = cv2.matchTemplate(slide_edge_img, background_edge_img, cv2.TM_CCOEFF)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        # 获取缺口左上角位置
        top_left = (max_loc[0], max_loc[1])
        # 右下角位置
        bottom_right = (max_loc[0] + w, max_loc[1] + h)

        # 在切割后背景图片中画出需要移动的终点位置
        # rectangle（图片源数据，左上角，右下角，颜色，画笔厚度）
        # if self.display:
        #     print(top_left)
        #     print(bottom_right)
        #     after_img = cv2.rectangle(self.background_cut_img, top_left, bottom_right, (0, 0, 255), 0)
            # 画图
            # self.cv_show('after', after_img)
        # 计算移动距离
        slide_distance = top_left[0] + w + 10
        return slide_distance

    # 对背景图片进行剪切
    def cut_background(self):
        # 切割图片的上下边框
        height = self.slide_scale_img.shape[0]
        # 将背景图中上下多余部分以及滑块图片部分去除. 如：background_img[y1:y2, x1:]
        self.background_cut_img = self.background_img[self.offset_py - 10: self.offset_py + height + 10,
                                  self.offset_px + height + 10:]

    def cv_show(self, name, img):
        cv2.imshow(name, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def run(self):
        self.cut_background()
        return self.get_distance()
