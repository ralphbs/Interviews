def print_list(indices, nums):
	for i in indices:
		print nums[i]


def permutation(prefix, nums):
	if len(prefix) == len(nums):
		print [nums[i] for i in prefix]
		return

	for i in range(len(nums)):
		if i in prefix: 
			continue

		prefix.append(i)
		permutation(prefix, nums)
		prefix.remove(i)

def main():
	permutation([], [3,4,5])

main()