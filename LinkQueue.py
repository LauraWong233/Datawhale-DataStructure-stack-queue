#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 18:02:37 2019

@author: laura
"""

class Node(object):
	def __init__(self,val):
		super(Node, self).__init__()
		self.data = val
		self.next = None
class LinkQueue(object):
	def __init__(self):
		super(LinkQueue, self).__init__()
		self.top = None
	def is_empty(self):
		if self.top == None:
			return True;
		else:
			False
	def get_head(self):
		if self.top == None:
			return False;
		else:
			return self.top.data
	def head(self):
	#删除操作
		if self.top == None:
			return False;
		else:
			self.top = self.top.next
	def entry(self,val):
		if self.top == None:
			self.top = Node(val)
		else:
			node = Node(val)
			cur  = self.top
			while cur.next!=None:
				cur = cur.next
			cur.next = node
	def traverse(self):
		if self.top == None:
			return False
		else:
			cur = self.top
			while cur!=None:
				print(cur.data,end =' ')
				cur = cur.next
	def initqueue(self,l):
		if l==[]:
			self.top = None
		else:
			for i in range(0,len(l)):
				self.entry(l[i])


if __name__ == '__main__':
	test = LinkQueue()
	test.is_empty()
	test.initqueue([1,2,3])
	test.traverse()
	test.entry(4)
	test.traverse()
	test.head()
	test.get_head()
	test.traverse()
		
		