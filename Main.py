# -*- coding: UTF-8 -*-

import login_get_cookies
import follow_and_apply
import threading
import time


def update_cookies():
    global cookies_addr  #设置全局变量
    while True:
        print 'start update cookies'
        time.sleep(1800)
        cookies_addr = login_get_cookies.login_get_cookies(user_name, password)  # 输入用户名及密码，返回cookie文本地址



user_name = 'user_name'
password = 'password'

cookies_addr = login_get_cookies.login_get_cookies(user_name, password)  # 输入用户名及密码，返回cookie文本地址，先运行一次

t2 = threading.Thread(target=follow_and_apply.follow_and_apply,args=(cookies_addr,))  #输入cookies文本地址作为参数
t2.daemon = True  #设置线程属性，使主里程退出时一同退出
t2.start()
t1 = threading.Thread(target=update_cookies())  #构造线程对象，使get_cookies作为线程同时运行
t1.daemon = True  #设置线程属性，使主里程退出时一同退出
t1.start()

time.sleep(86400)
