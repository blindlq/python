#!/usr/bin/env python
#_*_coding:utf-8_*_

import threading
import time

def addNum():
	global num#在每个线程中都获取这个全局变量
	print('--get num:',num )
	time.sleep(1)
	num  -=1 #对此公共变量进行-1操作
	
	
num = 100 #设定一个共享变量
thread_list = []
for i in range(100):
	t = threading.Thread(target=addNum)
	t.start()
	thread_list.append(t)

for t in thread_list:
		t.join()

print('final num:', num )		