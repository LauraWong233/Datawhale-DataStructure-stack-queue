class Solution:
	def factorial(self,n):
		if n==0 or n==1:
			return 1
		if n<0:
			print('输入不合法')
			return 0;
		return n*self.factorial(n-1)

