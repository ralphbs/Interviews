from node import Node

def compute_symmetric_tree(root):
	if root is None:
		return

	compute_symmetric_tree(root.left)
	compute_symmetric_tree(root.right)

	temp = root.left
	root.left = root.right
	root.right = temp



def print_in_order(root):
	if root is None:
		return
	print_in_order(root.left)
	print(root.val, '->')
	print_in_order(root.right)

def main():
	na, nb, nc, nd, ne = Node('a'), Node('b'), Node('c'), Node('d'), Node('e')
	na.left = nb
	nb.right = nd
	na.right = nb
	nb.left = nd

	print_in_order(na)
	print('--------------')
	compute_symmetric_tree(na)
	print_in_order(na)

main()
