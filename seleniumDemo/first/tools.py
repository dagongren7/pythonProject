from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib, datetime


def sendmail_kong(title):
    #发送邮箱服务器
    smtpserver = 'smtp.sina.cn'
    #发送邮箱用户/密码
    user = '18614924844@sina.cn'
    password = '1234567890'
    #发送邮箱
    sender = '18614924844@sina.cn'
    #接收邮箱
    receiver = '359407130@qq.com'
    #发送邮箱主题
    subject = '邮件发送测试'
    #编写HTML类型的邮件正文
    msg = MIMEText("正文内容hehe")
    msg['Subject'] = title
    msg['From'] = sender
    msg['To'] = receiver

    #连接发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())

    smtp.quit()
    #--------------------------------------
def SendMailAttach(filename):
    #发送邮箱服务器
    smtpserver = 'smtp.sina.cn'
    #发送邮箱用户/密码
    user = '18614924844@sina.cn'
    password = '1234567890'
    #发送邮箱
    sender = '18614924844@sina.cn'
    #接收邮箱
    receiver = '359407130@qq.com'
    msg = MIMEMultipart()
    att = MIMEText(open(filename, 'rb').read(), 'base64', 'gb2312')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename=report.html'
    msg.attach(att)

    msg['From'] = sender
    msg['To'] = receiver
    msg['subject'] = Header('冒烟测试结果 (' + str(datetime.date.today()) + ')','gb2312')

    body = "Python test mail"
    msg.attach(MIMEText(body, 'plain'))

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user,password)
    smtp.sendmail(msg['from'], msg['to'],msg.as_string())
    smtp.quit()