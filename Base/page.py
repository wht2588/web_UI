from Page.mp.loginPage import MpLoginPage
from Page.mp.homePage import MpHomePage
from Page.mp.publishArticlePage import MpPublishArticlePage
from Page.mis.loginPage import MisLoginPage
from Page.mis.homePage import MisHomePage
from Page.mis.auditPage import MisAuditPage
from Page.app.homePage import AppHomePage


class Page:

    @classmethod
    def get_mp_login(cls):
        """返回自媒体登录"""
        return MpLoginPage()

    @classmethod
    def get_mp_home(cls):
        """返回自媒体首页"""
        return MpHomePage()

    @classmethod
    def get_mp_publish_article(cls):
        """自媒体返回发表文章"""
        return MpPublishArticlePage()

    @classmethod
    def get_mis_login(cls):
        """返回后台登录"""
        return MisLoginPage()

    @classmethod
    def get_mis_home(cls):
        """返回后台首页"""
        return MisHomePage()

    @classmethod
    def get_mis_audit(cls):
        """返回后台审核文章页面"""
        return MisAuditPage()

    @classmethod
    def get_app_home(cls):
        """返回App首页"""
        return AppHomePage()
