from Base.page import Page
from Base.data import Data
import pytest, logging


def publish_article_data():
    # 空列表
    article_list = []
    # 读数据
    article_data = Data.get_json_data("publish_article_audit.json").get("mp_publish_article")
    # 追加数据
    article_list.append((article_data.get("title"),
                         article_data.get("content"),
                         article_data.get("channel"),
                         article_data.get("exp")))
    return article_list


@pytest.mark.run(order=2)
class TestPublishArticle:

    def setup_class(self):
        # 点击发表文章
        Page.get_mp_home().click_publish_article()

    @pytest.mark.parametrize("title,content,channel,exp", publish_article_data())
    def test_publish_article(self, title, content, channel, exp):
        """测试发布表文章"""
        logging.info("发布文章: title:{} - content:{} - channel:{} - exp:{}".format(title,content,channel,exp))
        # 发表文章
        Page.get_mp_publish_article().publish_article(title, content, channel)
        # 断言
        assert Page.get_mp_publish_article().page_exits_text(exp)
