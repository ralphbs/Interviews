from node import Node

def print_all_path_to_leaves(root):
	def print_all_path_to_leaves_helper(root, stack):
		if not root:
			return
		
		stack.append(root)
		print_all_path_to_leaves_helper(root.left, stack)
		print_all_path_to_leaves_helper(root.right, stack)

		if not root.left and not root.right:
			print_stack(stack)
		stack.pop()

	return print_all_path_to_leaves_helper(root, [])

def print_stack(s):
	i = 0
	while i < len(s) - 1:
		print(s[i].val,'->')
		i+=1
	print(s[i].val)

def main():
	nA = Node('A')
	nB = Node('B')
	nC = Node('C')
	nD = Node('D')
	nE = Node('E')

	nA.left = nB
	nB.left = nC
	nB.right = nD
	nA.right = nE

	print_all_path_to_leaves(nA)

main()
