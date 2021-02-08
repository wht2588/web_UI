from selenium.webdriver.common.by import By


class PageElements:
    """登录"""
    # 手机号
    login_phone_css = (By.CSS_SELECTOR, 'input[placeholder="请输入手机号"]')
    # 验证码
    login_code_css = (By.CSS_SELECTOR, 'input[placeholder="验证码"]')
    # 登录按钮
    login_btn_class = (By.CLASS_NAME, "el-button--primary")

    """首页"""
    # 内容管理
    home_content_manage_xpath = (By.XPATH, "//div[@class='el-submenu__title']/span[text()='内容管理']")
    # 发表文章
    home_publish_article_xpath = (By.XPATH, "//li[@class='el-menu-item' and contains(text(),'发布文章')]")

    """发表文章"""
    # 文章标题
    publish_article_title_css = (By.CSS_SELECTOR, 'input[placeholder="文章名称"]')
    # frame
    publish_article_frame_id = "publishTinymce_ifr"
    # 文章内容
    publish_article_content_id = (By.ID, "tinymce")
    # 封面
    publish_article_fm_xpath = (By.XPATH, "//span[@class='el-radio__label' and contains(text(),'无图')]")
    # 选择频道按钮
    publish_article_channel_btn_css = (By.CSS_SELECTOR, 'input[placeholder="请选择"]')
    # 所有渠道
    publish_article_channel_all_list_css = (By.CSS_SELECTOR, "ul.el-select-dropdown__list li.el-select-dropdown__item span")
    # 选择具体频道
    publish_article_channel_option_xpath = (By.XPATH, "//li[@class='el-select-dropdown__item']/span[text()='css']")
    # 发表按钮
    publish_article_submit_btn_xpath = (By.XPATH, "//button[contains(@class,'el-button--primary')]/span[text()='发表']")
