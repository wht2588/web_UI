from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from Base.driver import Driver
import time, logging


class Base:

    def __init__(self, tag):
        if tag == "app":
            self.driver = Driver.get_app_driver()
        if tag == "mp":
            self.driver = Driver.get_mp_driver()
        if tag == "mis":
            self.driver = Driver.get_mis_driver()

    def search_ele(self, loc, timeout=5, poll=1.0):
        """
        定位单个元素
        :param loc: 元组 (类型,属性值) demo:(By.ID,"id属性值")......
        :param timeout: 超时时间
        :param poll: 搜索间隔
        :return: 定位对象
        """
        logging.info("操作元素:{}".format(loc))
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    def search_eles(self, loc, timeout=5, poll=1.0):
        """
        定位一组元素
        :param loc: 元组 (类型,属性值) demo:(By.ID,"id属性值")......
        :param timeout: 超时时间
        :param poll: 搜索间隔
        :return: 定位对象列表
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))

    def click_ele(self, loc, timeout=5, poll=1.0):
        """
        点击元素
        :param loc: 元组 (类型,属性值) demo:(By.ID,"id属性值")......
        :param timeout: 超时时间
        :param poll: 搜索间隔
        :return:
        """
        logging.info('执行点击操作')
        self.search_ele(loc, timeout, poll).click()

    def send_ele(self, loc, text, timeout=5, poll=1.0):
        """
        输入文本
        :param loc: 元组 (类型,属性值) demo:(By.ID,"id属性值")......
        :param text:
        :param timeout: 超时时间
        :param poll: 搜索间隔
        :return:
        """

        logging.info("输入数据:{}".format(text))
        # 定位
        input_value = self.search_ele(loc, timeout, poll)
        # 清空
        input_value.clear()
        # 输入
        input_value.send_keys(text)

    def page_exits_text(self, text, tag="web"):
        """
        判断页面包含某个文本
        :param text: 查找文本
        :param tag: 标识
        :return:
        """
        logging.info("判断页面包含文本:{}".format(text))
        # 定义变量
        text_path = None

        if tag == "web":
            text_path = (By.XPATH, "//*[contains(text(),'{}')]".format(text))
        if tag == "app":
            text_path = (By.XPATH, "//*[contains(@text,'{}')]".format(text))
        try:
            # 定位
            self.search_ele(text_path)
            logging.info("页面存在元素:{}".format(text))
            return True
        except TimeoutException:
            logging.info("页面不存在元素:{}".format(text))
            return False

    def select_option(self, ele1, ele2, text):
        """
        下拉框选择 -web
        :param text: 渠道名字
        :param ele1: 下拉框选择按钮 (类型,属性值)
        :param ele2: 下拉框展开选项所有元素定位方法 (类型,属性值)
        :return:
        """
        # 点击下拉框按钮
        self.click_ele(ele1)
        # 选择下拉框内选项
        channel_list = self.search_eles(ele2)
        # 找到元素标识
        is_element = False
        # 遍历
        for i in channel_list:
            # 判断
            if i.text == text:
                i.click()
                # 置为True
                is_element = True
                # 跳出
                break
            # 鼠标移动到当前元素 执行键盘向下键
            ActionChains(self.driver).move_to_element(i).send_keys(Keys.DOWN)
            time.sleep(1)
        # 判断is_element
        if not is_element:
            # 抛出没有找到元素异常
            NoSuchElementException("下拉框中文本:{} 没有找到".format(text))

    def app_area_choice_menu_option(self, area_ele, area_option):
        """
        app区间水平滑动查找文本
        :param area_ele: 滑动区域定位方式 (类型,属性值)
        :param area_option: 滑动区域内文本定位方式 (类型,属性值)
        :return:
        """
        # 定位滑动区域
        area = self.search_ele(area_ele)
        # 取左上角坐标x area.location = {"x":x,"y":y}
        x = area.location.get("x")
        # 取左上角坐标y
        y = area.location.get("y")
        # 取宽 area.size={"width":x, "height":y}
        width = area.size.get("width")
        # 取高
        height = area.size.get("height")

        while True:
            # 取滑动前元素结构
            prev_page = self.driver.page_source
            try:
                # 定位元素
                self.click_ele(area_option)
                break
            except TimeoutException:
                # 滑动 起点: x+width*0.8, y+height*0.5 终点：x+width*0.2, y+height*0.5
                self.driver.swipe(x + width * 0.8, y + height * 0.5, x + width * 0.2, y + height * 0.5, 1500)
                # 取页面元素结构 和 滑动之前对比
                if self.driver.page_source == prev_page:  # 滑动到页面底端
                    raise NoSuchElementException("滑动区域菜单:{} 没有找到".format(area_option))
