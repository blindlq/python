#!/usr/bin/env python
#_*_coding:utf-8_*_


import xml.etree.ElementTree as ET

tree = ET.parse("xmltest.xml")
root = tree.getroot()
print(root.tag)

#遍历xml文档
for child in root:
	print(child.tag,child.attrib)
	for i in child:
		print(i.tag,i.text)
		

#只遍历	year 节点
for node in root.iter('year'):
	print(node.tag,node.text)