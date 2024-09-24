import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config.build_config import BuildConfig
from util.log_util import LogUtil


# 需要添加附件：测试报告
# 需要增加发送日志

class Send_Message():
    def set_content(self):
        subject = "Python自动化测试报告"
        msg = MIMEMultipart()
        msg["Subject"] = Header(subject, charset="utf-8").encode()
        content = MIMEText("<html><h1>最新自动化测试报告，请查看附件！</h1></html>","html","utf-8")
        msg.attach(content)
        return msg

    def send_mail_by_netease(self, msg):
        self.msg = msg
        # 账号信息以及授权码
        user = BuildConfig.NETEASE_MAIL_USER
        auth_passwd = BuildConfig.NETEASE_MAIL_AUTH_PASSWORD
        host = BuildConfig.NETEASE_SMTP_HOST
        from_user = BuildConfig.NETEASE_FROM_USER
        to_users = BuildConfig.NETEASE_TO_USERS
        # 发送邮件
        smtp = smtplib.SMTP(host)
        smtp.connect()
        smtp.login(user, auth_passwd)
        smtp.sendmail(from_user,to_users,self.msg.as_string())
        # 关闭邮件服务器的连接
        smtp.close()

    def send_mail_by_aliyun(self,msg):
        """
        用阿里邮箱发送文件
        :param msg: 文件内容
        :return: 无返回，如果报错写入日志
        """
        self.msg = msg
        user = BuildConfig.ALIYUN_MAIL_USER
        auth_passwd =BuildConfig.ALIYUN_MAIL_AUTH_PASSWORD
        host = BuildConfig.ALIYUN_SMTP_HOST
        port = BuildConfig.ALIYUN_SMTP_PORT
        try:
            smtp = smtplib.SMTP_SSL(host, port)
            smtp.login(user, auth_passwd)
            from_user = BuildConfig.ALIYUN_SMTP_FROM_USER
            to_users =BuildConfig.ALIYUN_SMTP_TO_USER
            smtp.sendmail(from_user, to_users, self.msg.as_string())
        except Exception as e:
            LogUtil.error(e)
        finally:
            smtp.close()



if __name__ == "__main__":
    send_mail = Send_Message()
    content = send_mail.set_content()
    send_mail.send_mail_by_aliyun(content)