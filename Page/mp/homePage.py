from Base.base import Base
from Page.mp.pageElements import PageElements
import logging,allure


class MpHomePage(Base):

    def __init__(self):
        super().__init__("mp")
        logging.info("自媒体首页")

    @allure.step("首页点击内容管理")
    def click_content_manage(self):
        """点击内容管理"""
        logging.info("自媒体首页 点击内容管理")
        self.click_ele(PageElements.home_content_manage_xpath)

    @allure.step("首页点击发表文章")
    def click_publish_article(self):
        """发表文章"""
        # 点击内容管理
        self.click_content_manage()
        logging.info("自媒体首页 点击发表文章")
        # 点击发表文章
        self.click_ele(PageElements.home_publish_article_xpath)
