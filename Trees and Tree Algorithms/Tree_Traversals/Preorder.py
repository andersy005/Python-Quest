def preorder(tree):
	"""Function uses a tree as a data Structure"""
	if tree:
		print(tree.getRootVal())
		preorder(tree.getLeftChild())
		preorder(tree.getRightChild())


