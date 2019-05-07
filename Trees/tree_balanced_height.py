from node import Node

def is_height_balanced_tree(root):
	if root is None:
		# leaf node is height balanced by definition
		return True

	left_height = get_height(root.left)
	right_height = get_height(root.right)

	if (abs(left_height - right_height) > 1):
		return False
		
	return True

def get_height(root):
	if root is None:
		return -1
	
	left_height = get_height(root.left)
	right_height = get_height(root.right)

	return 1 + max(left_height, right_height)

def main():
	n1, n2, n3, n4, n5, n6, n7, n8, n9 = Node(), Node(), Node(), Node(), Node(), Node(), Node(), Node(), Node()
	n1.left = n2
	n1.right = n3
	n2.left = n4
	n2.right = n5
	n5.right = n6
	n6.right = n7
	n1.right = n3
	n3.right = n8
	n8.right = n9

	print(is_height_balanced_tree(n1))
main()
