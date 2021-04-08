import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.header import Header


def send_mail(mail_subject, mail_content, to_add='mmmt123321@126.com', from_name='telankesi_', from_add='mmmt123321@126.com', from_pwd='mt61519ZZmail'):
    # 连接邮箱服务器
    con = smtplib.SMTP_SSL('smtp.126.com', 465)
    # 登录邮箱
    con.login(from_add, from_pwd)
    # 创建邮件对象
    msg = MIMEMultipart()
    # 设置邮件主题
    subject = Header(mail_subject, 'utf-8').encode()
    msg['Subject'] = subject
    # 设置邮件发送者
    msg['From'] = '{0} <{1}>'.format(from_name, from_add)
    # 设置邮件接受者
    msg['To'] = to_add
    # 添加文字内容
    text = MIMEText(mail_content, 'plain', 'utf-8')
    msg.attach(text)
    # 添加附件
    with open('./电子保单20200925.zip', 'rb') as f:
        file_1 = f.read()
        file_1 = MIMEApplication(file_1)
        file_1.add_header('Content-Disposition', 'attachment', filename='电子保单20200925.zip')
        msg.attach(file_1)

    with open('./截至20200925承保信息.xlsx', 'rb') as f:
        file_2 = f.read()
        file_2 = MIMEApplication(file_2)
        file_2.add_header('Content-Disposition', 'attachment', filename='截至20200925承保信息.xlsx')
        msg.attach(file_2)

    # 发送邮件
    con.sendmail(from_add, to_add, msg.as_string())
    con.quit()


if __name__ == "__main__":
    
    mail_subject = 'test'  # 邮件主题
    mail_content = 'mail content'  # 邮件内容
    send_mail(mail_subject, mail_content)
