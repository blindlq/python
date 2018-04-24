#!/usr/bin/env python
#_*_coding:utf-8_*_

import socket

HOST = '192.168.10.10'
PORT=50007
ADDR = (HOST,PORT)

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)      #定义socket类型，网络通信，TCP
s.connect(ADDR)       #要连接的IP与端口

while True:
	cmd=input("Please input cmd:")       #与人交互，输入命令
	s.sendall((cmd).encode())      #把命令发送给对端
	data=s.recv(1024).decode()     #把接收的数据定义为变量
	print(data)         #输出变量


s.close()   #关闭连接	  