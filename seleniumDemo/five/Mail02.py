from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib, datetime

def SendMailAttach():
    #发送邮箱服务器
    smtpserver = 'smtp.sina.cn'
    #发送邮箱用户/密码
    user = '18614924844@sina.cn'
    password = '1234567890'
    #发送邮箱
    sender = '18614924844@sina.cn'
    #接收邮箱
    receiver = '18614924844@sina.cn'
    msg = MIMEMultipart()
    att = MIMEText(open('D:\\test\\testTemplate.html', 'rb').read(), 'base64', 'gb2312')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="testTemplate.html"'
    msg.attach(att)

    msg['From'] = sender
    msg['To'] = receiver
    msg['subject'] = Header('测试结果(' + str(datetime.date.today()) + ')','utf8')

    body = "Python test mail"
    msg.attach(MIMEText(body, 'plain'))

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user,password)
    smtp.sendmail(msg['from'], msg['to'],msg.as_string())
    smtp.quit()

SendMailAttach()