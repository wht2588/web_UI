from Base.page import Page
from Base.data import Data
import pytest,logging


def mp_login_data():
    # 空列表
    mp_login_list = []
    # 读数据
    login_data = Data.get_json_data("publish_article_audit.json").get("mp_login")
    # 追加数据到列表
    mp_login_list.append((login_data.get("phone"), login_data.get("code"), login_data.get("exp")))

    return mp_login_list


@pytest.mark.run(order=1)
class TestMpLogin:

    @pytest.mark.parametrize("phone,code,exp", mp_login_data())
    def test_login(self, phone, code, exp):
        """自媒体登陆"""
        logging.info("自媒体登录输入数据，phone:{} - code:{} - exp:{}".format(phone,code,exp))
        # 登录
        Page.get_mp_login().login(phone, code)
        # 断言
        assert Page.get_mp_home().page_exits_text(exp)
