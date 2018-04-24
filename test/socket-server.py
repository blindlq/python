#!/usr/bin/env python
#_*_coding:utf-8_*_



import socket   #socket模块
import commands   #执行系统命令模块

HOST = '192.168.10.10'
PORT = 50007
BUFSIZ = 1024
ADDR = (HOST,PORT)

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM) #定义socket类型，网络通信，TCP
s.bind(ADDR)		#套接字绑定的IP与端口
s.listen(5)         #开始TCP监听,监听1个请求

while True:
	print("watting for connection....")
	conn,addr=s.accept()   #接受TCP连接，并返回新的套接字与IP地址
	print ' ...conected from:', addr
	
	while True:
		data=conn.recv(1024)    #把接收的数据实例化
		cmd_status,cmd_result=commands.getstatusoutput(data)   #commands.getstatusoutput执行系统命令（即shell命令），返回两个结果，第一个是状态，成功则为0，第二个是执行成功或失败的输出信息
		if len(cmd_result.strip()) ==0:   #如果输出结果长度为0，则告诉客户端完成。此用法针对于创建文件或目录，创建成功不会有输出信息
			conn.sendall('Done.')
		else:
			conn.sendall(cmd_result)   #否则就把结果发给对端（即客户端）
	
conn.close()


# import SocketServer
# import commands

# HOST = '192.168.10.10'
# PORT = 50007

# ADDR = (HOST,PORT)

# class MyTCPHandler(SocketServer.BaseRequestHandler):
	# def handle(self):
		# print("get conection from: %s", self.client_address)
		# while True:
			# self.data = self.request.recv(4096)
			# print(self.data)
			# cmd_status,cmd_result=commands.getstatusoutput(self.data)
			# if len(cmd_result.strip()) ==0:   #如果输出结果长度为0，则告诉客户端完成。此用法针对于创建文件或目录，创建成功不会有输出信息
				# self.data = 'Done.'
				# self.request.sendall(self.data)
			# else:
				# self.data = cmd_result    #否则就把结果发给对端（即客户端）
				# self.request.sendall(self.data)
			
			
# if __name__ == "__main__":			
	# server = SocketServer.TCPServer(ADDR, MyTCPHandler)
	
	# server.serve_forever()
			