from Base.base import Base
from Page.mis.pageElements import PageElements
import datetime, time, logging, allure

"""获取当前日期"""


# print("日志:{}".format(datetime.datetime.now()))
# print("日志:{}".format(datetime.datetime.now().year))
# print("日志:{}".format(datetime.datetime.now().day))


class MisAuditPage(Base):

    def __init__(self):
        super().__init__("mis")
        logging.info("审核文章页面")

    @allure.step("查询文章操作")
    def query_article(self, title):
        """
        查询文章
        :param title: 文章名字
        :return:
        """
        logging.info("输入搜索文章标题:{}".format(title))
        # 输入搜索文章标题
        self.send_ele(PageElements.audit_search_article_css, title)
        logging.info("选择结束日期")
        # 点击结束日期选择按钮
        self.click_ele(PageElements.audit_search_over_date_btn_css)
        time.sleep(1)
        # 选择结束日期
        self.click_ele((PageElements.audit_search_date_over_day_xpath[0],
                        PageElements.audit_search_date_over_day_xpath[1].format(datetime.datetime.now().day + 1)))
        # 点击确定
        self.click_ele(PageElements.audit_search_date_over_day_acc_btn_class)
        logging.info("执行查询操作")
        # 点击查询
        self.click_ele(PageElements.audit_query_article_btn_class)

    @allure.step("审核文章操作")
    def audit_article_pass(self):
        """审核通过文章"""
        time.sleep(1)
        logging.info("点击文章通过按钮")
        # 点击通过
        self.click_ele(PageElements.audit_pass_article_btn_xpath)
        logging.info("点击文章通过弹窗确定按钮")
        # 点击确定
        self.click_ele(PageElements.audit_pass_article_alert_acc_btn_class)
