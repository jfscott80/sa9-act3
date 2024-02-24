'''
create a stack class that implements a stack ADT using a Python 
list to store the stack elements with index 0 as the 
bottom of the stack



'''






class Stack:
	# constructor
	def __init__(self):
		self.elements = []
		
	# make printing stack readable
	def __str__(self):
		if self.size() > 0:
			result = '| '
			for i in self.elements:
				result += str(i) + ' | '
			return result
		else:
			return 'None'

	# find size of stack
	def size(self):
		return len(self.elements)

	# add to stack
	def push(self, data):
		self.elements.append(data)

	# remove from stack
	def pop(self):
		if self.size() > 0:
			temp = self.elements[-1]
			self.elements.pop()
			return temp
		else:
			return None
	# look at top of stack
	def peek(self):
		if self.size() > 0:
			temp = self.elements[self.size() -1]
			return f'{temp}'
		else:
			return None
