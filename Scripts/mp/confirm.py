from Base.page import Page

# 登录
Page.get_mp_login().login("13911111111", "246810")
# 进入发表文章
Page.get_mp_home().click_publish_article()

# 发布文章
Page.get_publish_article().publish_article("嘻嘻哈哈1", "哈哈哈哈啊", "设计")
