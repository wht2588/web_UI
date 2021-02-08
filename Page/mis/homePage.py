from Base.base import Base
from Page.mis.pageElements import PageElements
import logging, allure


class MisHomePage(Base):

    def __init__(self):
        super().__init__("mis")
        logging.info("后台管理 首页")

    @allure.step("首页点击信息管理")
    def click_info_manage(self):
        """点击信息管理"""
        logging.info("点击信息管理")
        self.click_ele(PageElements.home_info_manage_link_text)

    @allure.step("首页点击内容审核")
    def click_content_audit(self):
        """点击内容审核"""
        # 点击信息管理
        self.click_info_manage()
        logging.info("点击内容审核")
        # 点击内容审核
        self.click_ele(PageElements.home_content_audit_link_text)
