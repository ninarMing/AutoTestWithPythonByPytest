#-*-coding:utf-8-*-


class BuildConfig:
    # 是否需要日志
    DEBUG = True
    LOGGING_PATH = "..\\log\\"
    LOGGING_CONFIG = "..\\config\\logging_config.yaml"
    LOG_IMAGE_PATH = "..\\log\\image_log\\"
    # 待测试地址
    TESTED_URL = "https://xxx/login.html"
    ALREADY_LOGGED_URL = "https://xxx/desk.html"
    # 阿里云邮箱配置：
    ALIYUN_MAIL_USER = "xxx@inlinke.com"
    # 授权密码
    ALIYUN_MAIL_AUTH_PASSWORD = "MDMkg0zQ9W0zTAtO00"
    ALIYUN_SMTP_HOST="smtp.qiye.aliyun.com"
    ALIYUN_SMTP_PORT=465
    ALIYUN_SMTP_FROM_USER ="xxx@inlinke.com"
    ALIYUN_SMTP_TO_USER =["xxxx@inlinke.com", "xxx@126.com"]
    # 网易126邮箱配置：
    NETEASE_MAIL_USER = "xxxx@126.com"
    NETEASE_MAIL_AUTH_PASSWORD ="NZSTSTEXESRYEHGZ00"
    NETEASE_SMTP_HOST="smtp.126.com"
    NETEASE_FROM_USER = "XXX@126.com"
    NETEASE_TO_USERS=["XXXXX@qq.com","XXXX@126.com"]
