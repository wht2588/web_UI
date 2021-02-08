from appium import webdriver as app
from selenium import webdriver as web


class Driver:
    # app端
    __app_driver = None
    # 自媒体
    __mp_driver = None
    # 后台
    __mis_driver = None

    @classmethod
    def get_app_driver(cls):
        """声明app驱动"""
        if cls.__app_driver is None:  # 如果为None说明没有赋值
            # 声明driver
            desired_caps = {
                'platformName': 'Android',  # 平台
                'platformVersion': '5.1',  # 平台所属版本
                'deviceName': '192.168.56.101:5555',  # 设备名字 随便写
                'appPackage': 'com.itcast.toutiaoApp',  # app包名
                'appActivity': '.MainActivity',  # app启动名
                'noReset': True  # 不重置app，保留app原本在手机状态
            }

            # 声明驱动对象 创建session 打开启动参数中指定的app
            cls.__app_driver = app.Remote('http://localhost:4723/wd/hub', desired_caps)

        return cls.__app_driver

    @classmethod
    def quit_app_driver(cls):
        """退出app驱动"""
        if cls.__app_driver:
            # 退出
            cls.__app_driver.quit()
            # 置为None
            cls.__app_driver = None

    @classmethod
    def get_mp_driver(cls):
        """声明自媒体驱动"""
        if cls.__mp_driver is None:
            # chrome浏览器
            cls.__mp_driver = web.Chrome()
            # 最大化
            cls.__mp_driver.maximize_window()
            # 访问自媒体首页
            cls.__mp_driver.get("http://ttmp.research.itcast.cn/")
        return cls.__mp_driver

    @classmethod
    def quit_mp_driver(cls):
        """退出自媒体driver"""
        if cls.__mp_driver:
            # 退出
            cls.__mp_driver.quit()
            # 置为None
            cls.__mp_driver = None

    @classmethod
    def get_mis_driver(cls):
        """声明自媒体驱动"""
        if cls.__mis_driver is None:
            # chrome浏览器
            cls.__mis_driver = web.Chrome()
            # 最大化
            cls.__mis_driver.maximize_window()
            # 访问自媒体首页
            cls.__mis_driver.get("http://ttmis.research.itcast.cn/")
        return cls.__mis_driver

    @classmethod
    def quit_mis_driver(cls):
        """退出自媒体driver"""
        if cls.__mis_driver:
            # 退出
            cls.__mis_driver.quit()
            # 置为None
            cls.__mis_driver = None
