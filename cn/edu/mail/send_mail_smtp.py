# -*- coding:utf-8 -*- 
# Author: Henry

from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
from email.mime.text import MIMEText

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# 构造纯文本邮件
# msg = MIMEText('hello, the mail send by python...', 'plain', 'utf-8')
# 构造HTML邮件
# msg = MIMEText('<html><body><h1>Hello</h1>' +
#     '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
#     '</body></html>', 'html', 'utf-8')
msg = MIMEMultipart('alternative')
# 添加邮件正文
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))
# 添加附件就是加上一个MIMEBase
with open('test.bmp', 'rb') as f:
    # 设置附件的MIME和文件名，这里是bmp类型
    mime = MIMEBase('image', 'bmp', filename='test.bmp')
    mime.add_header('Content-Disposition', 'attachment', filename='test.bmp')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime) # Base64编码
    msg.attach(mime)
# 输入Emial地址和口令
from_addr = input('From: ')
password = input('Password: ')
# 输入收件人地址

to_addr = input('To: ')
# 输入SMTP服务器地址
smtp_server = input('SMTP server: ')

msg['From'] = _format_addr('Python初学者 <%s>' % from_addr)
msg['To'] = _format_addr('My Best Friends <%s>' % to_addr)
msg['Subject'] = Header('测试用例……', 'utf-8').encode()

# server = smtplib.SMTP(smtp_server, 25)
# Gmail 如何发送安全SMTP
server = smtplib.SMTP(smtp_server, 587)
server.starttls()

server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
