def preorder(self):
	"""method of the tree data structure itself"""
	print(self.key)
	if self.leftChild:
		self.leftChild.preorder()
	if self.rightChild:
		self.rightChild.preorder()