import smtplib


from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import  Config
import  configparser
import  sys

configall = configparser.ConfigParser()
configall.read("../config.ini")

class Mailer(object):

    def __init__(self):
        self.subject = configall['mail']['subject']
        self.mail_user = configall['mail']['user']
        self.mail_pass = configall['mail']['passwd']
        self.mail_host = configall['mail']['host']
        self.mail_port = configall['mail']['port']
        self.html_data = configall['mail']['html_data']

    def send_mail(self,mail_user,mail_to,messages):

        # for msg in messages:
        for msg in messages:
            _time, sql, dbname, exetime = msg
            self.html_data += "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (_time, sql, dbname, exetime)
        self.html_data = "Hi All:<br>5分钟执行sql!<br><br><table border='1' style='background-color:#CCCCCC'>" + self.html_data + "</table>"
        msg = MIMEText(self.html_data, _subtype="html", _charset="utf-8")
        msg["Subject"] = self.subject
        msg["From"] = self.mail_user
        msg["To"] = ";".join([mail_to])

        try:
            s = smtplib.SMTP_SSL("%s:%s" %(self.mail_host,self.mail_port), timeout=30)  # 连接smtp邮件服务器,端口默认是25
            s.login(self.mail_user, self.mail_pass)  # 登陆服务器
            ss = s.sendmail(self.mail_user,mail_to, msg.as_string())  # 发送邮件 s.close()
            #print(ss)
            return True
        except Exception as e:
            print(e)
            return False







