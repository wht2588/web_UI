from selenium.webdriver.common.by import By


class PageElements:
    """登录"""
    # 用户名
    login_username_name = (By.NAME, "username")
    # 密码
    login_password_name = (By.NAME, "password")
    # 登录
    login_btn_id = (By.ID, "inp1")

    """首页"""
    # 信息管理
    home_info_manage_link_text = (By.LINK_TEXT, "信息管理")
    # 内容审核
    home_content_audit_link_text = (By.LINK_TEXT, "内容审核")

    """审核"""
    # 搜索文章输入框
    audit_search_article_css = (By.CSS_SELECTOR, 'input[placeholder="请输入: 文章名称"]')
    # 结束日期框按钮
    audit_search_over_date_btn_css = (By.CSS_SELECTOR, 'input[placeholder="选择结束时间"]')
    # 选择结束时间
    audit_search_date_over_day_xpath = (By.XPATH, "//td[contains(@class,'available')]//span[contains(text(),'{}')]")
    # 点击确定按钮
    audit_search_date_over_day_acc_btn_class = (By.CLASS_NAME, "is-plain")
    # 点击查询
    audit_query_article_btn_class = (By.CLASS_NAME, "find")
    # 点击通过
    audit_pass_article_btn_xpath = (By.XPATH, "//button/span[text()='通过']")
    # 点击确认弹窗确定
    audit_pass_article_alert_acc_btn_class = (By.CLASS_NAME, 'el-button--primary')
