class Node(object):
	def __init__(self,val):
		self.data = val
		self.next = None
class LinkStack(object):
	def __init__(self):
		self.top = None
		self.size = 0
	def is_empty(self):
		if self.top == None:
			print('stack is empty')
			return True
		else:
			print('stack is not empty')
			return False
	def get_size(self):
		print('the size of stack is %d' %self.size)
	def top(self):
		if self.top is True:
			print('stack is empty')
			return False
		else:
			return self.top.data
	def pop(self):
		if self.top is True:
			print('stack is empty')
			return False
		else:
			self.size-=1
			self.top = self.top.next
	def push(self,val):
		node = Node(val)        
		if self.top == None:
			self.top = node
		else:
			self.size+=1
			node.next = self.top
			self.top = node
	def initstack(self,l):#初始化
		if l == []:
			self.top = None
		else:
			for i in range(0,len(l)):
				self.push(l[i])
	def traverse(self):
		if self.top == None:
			print('stack is empty')
			return False
		else:
			cur = self.top
			for i in range(0,self.size+1):
				print(cur.data,end = ' ')
				cur = cur.next


if __name__=='__main__':
	test = LinkStack()
	test.initstack([1,2,3])
	test.is_empty()
	test.get_size()
	test.traverse()
	test.push(0)
	test.push(-1)
	test.pop()
	test.traverse()
	test.get_size()
