#!usr/bin/env python

# coding:utf8

import sys

reload(sys)
sys.setdefaultencoding('utf8')

import MySQLdb
import MySQLdb.cursors

import types



db = MySQLdb.connect(host='127.0.0.1',user='homestead',passwd='secret',db='douban',port=3306,charset='utf8',cursorclass = MySQLdb.cursors.DictCursor)
db.autocommit(True)
cursor = db.cursor()


fr = open('douban_movie_clean.txt','r')

# # Creat
# count = 0
# for line in fr:
	# count += 1
	# print count
	# if count ==1:
		# continue
		
	# line = line.strip().split('^')
	# # if line[-3] == '':
		# # print count
		# # break
	# cursor.execute("insert into movie(title,url,rate,length,description) values(%s,%s,%s,%s,%s)",[line[1],line[2],line[4],line[-3],line[-1]])

	
# # Update
# cursor.execute("update movie set title=%s,length=%s where id=1",['zhangcheng',999])


# # Read
# cursor.execute("select * from movie")
# movie = cursor.fetchall()
# print movie[0]['title']

# Drop
cursor.execute("delete from movie where id=1")	
	
	
	
fr.close()
cursor.close()
db.close()




