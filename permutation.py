#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 16:40:55 2019

@author: laura
"""
class solution:
	def next_sequence(self,l):
		j=len(l)-1
		while l[j]<l[j-1]:
			j-=1
		temp1 = l[j-1]#这是第一个违反递增规则的数字
		ind = [] #寻找temp1数字后面序列内比他大的最小的那个数字及其位置
		for i in range(j,len(l)):
			if l[i]<temp1:
				continue
			else:
				ind.append(i)
		ind2 = list(l[k] for k in ind)#把后面大于它的数字都取出来
		temp2 = min(ind2)
		loc = ind2.index(min(ind2))#寻找大于的里面最小的数字和位置
		l[loc+j] = temp1#将二者进行交换
		l[j-1] = temp2        
        #把temp1位置后面的数据进行sort
		a = l[j:]
		a.sort()
		aa = l[:j]
		aa.extend(a)
		return aa
	def permutation(self,l):
		l = list(set(l))#防止输入进来的数据有重复
		temp0 = sorted(l)
		print(temp0,'\n')
		l.sort(reverse=True)
		reverse = l       
		while temp0!=reverse:
		    temp0=self.next_sequence(temp0)
		    print(temp0,'\n')
        

if __name__=='__main__':
    test = solution()
    test.permutation([1,2,3,5,6,3])       

