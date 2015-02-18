

class Node(object):
	def __init__(self, data):
		self.data = data
		self.count = 0
		self.next = None

class linkedList(object):
	def __init__(self, head=None):
		self.head = head

	def insert(self, node):
		if not self.head:
			self.head = node
		else:
			node.next = self.head
			self.head = node

	def search(self, Node):
		if self.head == None:
			return -1
		temp = self.head
		while(temp.data != Node.data):
			if temp.next == None:
				return -1
			temp = temp.next
		temp.count = temp.count + 1

