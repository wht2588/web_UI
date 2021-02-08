from Base.page import Page
import pytest, time, logging
from Base.data import Data


def audit_data():
    # 空列表
    audit_list = []
    # 读数据
    audit_article_data = Data.get_json_data("publish_article_audit.json").get("mis_audit")
    # 追加数据
    audit_list.append((audit_article_data.get("article"),
                       audit_article_data.get("exp")))
    return audit_list


@pytest.mark.run(order=102)
class TestAudit:

    def setup_class(self):
        """进入审核文章页面"""
        Page.get_mis_home().click_content_audit()

    @pytest.mark.parametrize("article,exp", audit_data())
    def test_audit_article(self, article, exp):
        """审核文章"""
        logging.info("审核文章: article:{} - exp:{}".format(article, exp))
        # 查询
        Page.get_mis_audit().query_article(article)
        # 审核
        Page.get_mis_audit().audit_article_pass()
        # 断言
        assert Page.get_mis_audit().page_exits_text(exp)
