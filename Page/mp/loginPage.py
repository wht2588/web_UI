from Base.base import Base
from Page.mp.pageElements import PageElements
import logging
import allure


class MpLoginPage(Base):

    def __init__(self):
        super().__init__("mp")
        logging.info("自媒体登录页面")

    @allure.step("自媒体登陆")
    def login(self, phone, code):
        """
        登录
        :param phone: 手机号
        :param code: 验证码
        :return:
        """
        logging.info("输入手机号")
        # 输入手机号
        self.send_ele(PageElements.login_phone_css, phone)
        logging.info("输入验证码")
        # 输入验证码
        self.send_ele(PageElements.login_code_css, code)
        logging.info("点击登录按钮")
        # 点击登录
        self.click_ele(PageElements.login_btn_class)
