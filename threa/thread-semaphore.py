#!/usr/bin/env python
#_*_coding:utf-8_*_

import threading
import time

def run(n):
	global num
	semaphore.acquire()
	time.sleep(2)
	num +=1
	print(num)
	print("run the thread: %s\n" %n)
	semaphore.release()
	
	
if __name__ == '__main__':
	num= 0
	semaphore  = threading.BoundedSemaphore(5) #最多允许5个线程同时运行
	for i in range(20):
		t = threading.Thread(target=run,args=(i,))
		t.start()
	
while threading.active_count() != 1:
	pass# print threading.active_count()
else:
	print('----all threads done---')
	print(num)	