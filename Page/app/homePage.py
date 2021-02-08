from Base.base import Base

from Page.app.pageElements import PageElements


class AppHomePage(Base):

    def __init__(self):
        super().__init__("app")

    def choice_menu_option(self, name):
        """
        选择菜单
        :param name: 菜单名字
        :return:
        """
        self.app_area_choice_menu_option(PageElements.menu_scroll_area_class,
                                         (PageElements.menu_scroll_option_xpath[0],
                                          PageElements.menu_scroll_option_xpath[1].format(name))
                                         )
