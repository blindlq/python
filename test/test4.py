#!/usr/bin/env python
#_*_coding:utf-8_*_

class A:
	def __init__(self):
		self.n = 'A'
		
class B(A):
	 pass

class C(A):
	def __init__(self):
		self.n = 'C'
		
class D(B,C):
	pass
	
obj = D()

print(obj.n)	