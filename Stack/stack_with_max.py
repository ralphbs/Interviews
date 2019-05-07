class Stack:
	def __init__(self, elements = []):
		self.elements = elements

	def pop(self):
		if self.elements:
			return self.elements.pop()
		raise Exception('You cannot call max on an empty stack!')	

	def push(self, elem):
		if len(self.elements) == 0:
			self.elements.append(elem)
			return
		new_max = max(self.elements[-1].max, elem.val)
		self.elements.append(StackNode(elem.val, new_max))

	def max(self):
		if self.elements:
			return self.elements[-1].max
		raise Exception('You cannot call max on an empty stack!')	
			
	def pretty_print(self):
		for elem in self.elements:
			print('[Max: ', elem.max, ']', '[Elem: ', elem.val, ']', '--->')


class StackNode:
	def __init__(self, val, max):
		self.val = val
		self.max = max

s = Stack()
s1 = StackNode(1,1)
s2 = StackNode(2,2)
s3 = StackNode(4,4)
s4 = StackNode(3,3)

print('Pushing s1')
s.push(s1)
print('Pushing s2')
s.push(s2)
print('Pushing s3')
s.push(s3)
print('Pushing s4')
s.push(s4)
s.pretty_print()
print(s.max())
print('Popping')
s.pop()
print(s.max())
print('Popping')
s.pop()
print(s.max())
s.pretty_print()
print('Popping')
s.pop()
s.pretty_print()
print(s.max())
