from Base.base import Base
from Page.mp.pageElements import PageElements
import logging, allure


class MpPublishArticlePage(Base):

    def __init__(self):
        super().__init__("mp")
        logging.info("自媒体发布文章页面")

    @allure.step("发布文章操作")
    def publish_article(self, title, content, channel):
        """
        发布文章
        :param title: 标题
        :param content: 内容
        :param channel: 渠道名字
        :return:
        """
        logging.info("输入文章标题:{}".format(title))
        # 输入标题
        self.send_ele(PageElements.publish_article_title_css, title)
        logging.info("输入文章内容:{}".format(content))
        # 切换frame
        self.driver.switch_to.frame(PageElements.publish_article_frame_id)
        # 内容
        self.send_ele(PageElements.publish_article_content_id, content)
        # 切换回默认页面
        self.driver.switch_to.default_content()
        logging.info("选择封面")
        # 选择封面
        self.click_ele(PageElements.publish_article_fm_xpath)
        logging.info("选择渠道")
        # 选择渠道
        self.select_option(PageElements.publish_article_channel_btn_css,
                           PageElements.publish_article_channel_all_list_css,
                           channel)
        logging.info("点击发表文章")
        # 发表
        self.click_ele(PageElements.publish_article_submit_btn_xpath)
