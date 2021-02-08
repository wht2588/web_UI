from Base.page import Page


# 登录
Page.get_mis_login().login("testid", "testpwd123")

# 进入内容审核页面
Page.get_mis_home().click_content_audit()


# 查询文章
Page.get_mis_audit().query_article("000000ddd11111111111111111111")
# 审核文章
# Page.get_mis_audit().audit_article_pass()


import time
time.sleep(2)
# 审核通过
Page.get_mis_audit().page_exits_text("审核通过")

