from selenium.webdriver.common.by import By


class PageElements:
    """首页"""
    # 菜单滑动区域
    menu_scroll_area_class = (By.CLASS_NAME, "android.widget.HorizontalScrollView")
    # 菜单选项
    menu_scroll_option_xpath = (By.XPATH, "//android.widget.HorizontalScrollView//*[contains(@text,'{}')]")
