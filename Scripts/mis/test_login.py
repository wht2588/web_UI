from Base.page import Page
from Base.data import Data
import pytest, logging


def mis_login_data():
    # 空列表
    mis_login_list = []
    # 读数据
    login_data = Data.get_json_data("publish_article_audit.json").get("mis_login")
    # 追加数据
    mis_login_list.append((login_data.get("name"),
                           login_data.get("passwd"),
                           login_data.get("exp")))

    return mis_login_list


@pytest.mark.run(order=101)
class TestMisLogin:
    @pytest.mark.parametrize("name,passwd,exp", mis_login_data())
    def test_login(self, name, passwd, exp):
        """后台登录"""
        logging.info('后台登录: name:{} - passwd:{} - exp:{}'.format(name, passwd, exp))
        # 登录
        Page.get_mis_login().login(name, passwd)
        # 断言
        assert Page.get_mis_login().page_exits_text(exp)
