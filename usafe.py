#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen
import socket
import uuid
import myAES
import datetime
cutime = datetime.datetime.now()

# mailto_list = ['610566353@qq.com']  # 收件人(列表)
mail_to = 'xxx@gmail.com'
mail_host = "smtp.163.com"            # 使用的邮箱的smtp服务器地址，这里是163的smtp地址
mail_user = "xxx"  # 用户名
mail_pass = "xxx"  # 密码
mail_postfix = "163.com"  # 邮箱的后缀，网易就是163.com


def send_mail(nick, to_list,sub,content):
    me = "myaigo" + "<" + mail_user + "@" + mail_postfix + ">"
    msg = MIMEText(content,_subtype='plain')
    msg['Subject'] = sub
    msg['From'] = me
    # msg['To'] = ";".join(to_list)  # 将收件人列表以‘；’分隔
    msg['To'] = nick + "<" + mail_to + ">"
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)  # 连接服务器
        server.login(mail_user,mail_pass)  # 登录操作
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception as e:
        print(str(e))
        return False


def get_mac_address():  # 获取Mac地址
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0,11,2)])


def get_pub_ip():
    year = cutime.year
    html = urlopen(r'http://%s.ip138.com/ic.asp' % year)
    x = BeautifulSoup(html.read(),'html5lib')
    result0 = x.center.get_text()
    # y = str(x.center)
    # result0 = y[y.index('[')+1:y.index(']')]

    url = "http://www.baidu.com/s?"
    wd = {'wd': 'ip138'}
    wd = urllib.parse.urlencode(wd)
    fullurl = url + wd
    bdhtml = urlopen(fullurl)
    request = BeautifulSoup(bdhtml.read(),'html5lib')
    resdiv = request.find(name='div',attrs={"class":"c-span21 c-span-last op-ip-detail"})
    result1 = resdiv.find('td').get_text().strip()
    content = "['http://%s.ip138.com/ic.asp' % year] " + result0 \
              + "\n[More Reliable: baidu search 'ip138'] " + result1
    return content


if __name__ == '__main__':
    hostname = socket.gethostname()  # 获取主机名
    ip = socket.gethostbyname(hostname)  # 获取IP
    mac_add = get_mac_address()
    pub_ip = get_pub_ip()

    message = 'Hostname: %s\nIntranet IP: %s\nMAC Address: %s\nInternet IP:\n%s'\
              % (hostname, ip, mac_add, pub_ip)
    key = myAES.keyGenerater(16)
    mode = myAES.AES.MODE_CFB
    en_message = myAES.AESencrypt(key, mode, message)
    print(en_message)
    de_message = myAES.AESdecrypt(key, mode, en_message)
    print(de_message)

    if send_mail(key, mail_to, 'new state%s' % cutime,  # mailto_list
                 "See here>>\n%s" % en_message):  # 邮件主题和邮件内容
        # 最好写点中文，如果随便写，可能会被网易当做垃圾邮件退信
        print("done!")
    else:
        print("failed!")
