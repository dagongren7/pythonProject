import smtplib
from email.mime.text import MIMEText
from email.header import Header

#发送邮箱服务器
smtpserver ='smtp.sina.cn'
#发送邮箱用户/密码
user ='18614924844@sina.cn'
password ='1234567890'
#发送邮箱
sender = '18614924844@sina.cn'
#接收邮箱
receiver = '359407130@qq.com'
#发送邮箱主题
subject = 'Python email test'
#编写HTML类型的邮件正文
msg = MIMEText("正文内容")
msg['Subject'] = 'subject_test'
msg['From'] = sender
msg['To'] = receiver
#连接发送邮件
smtp =smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()