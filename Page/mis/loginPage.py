from Base.base import Base
from Page.mis.pageElements import PageElements
import logging, allure


class MisLoginPage(Base):

    def __init__(self):
        super().__init__("mis")
        logging.info("后台管理登录页面")

    @allure.step("后台管理登录")
    def login(self, username, password):
        """
        登录
        :param username: 用户名
        :param password: 密码
        :return:
        """
        logging.info("输入用户名:{}".format(username))
        # 用户名
        self.send_ele(PageElements.login_username_name, username)
        logging.info("输入密码:{}".format(password))
        # 密码
        self.send_ele(PageElements.login_password_name, password)
        # js删除登录按钮属性
        js = 'document.getElementById("inp1").removeAttribute("disabled")'
        self.driver.execute_script(js)
        logging.info("点击登录按钮")
        # 登录
        self.click_ele(PageElements.login_btn_id)
