import smtplib
from email.mime.text import MIMEText
from email.header import Header

#发送邮箱服务器
smtpserver ='smtp.163.com'
#发送邮箱用户/密码
user ='13023294697@163.com'
password ='chen184550'
#发送邮箱
sender = '13023294697@163.com'
#接收邮箱
receiver = '810483775@qq.com'
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