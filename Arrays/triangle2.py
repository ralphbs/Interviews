def get_min_path(lsts):
	first = lsts[-2]
	second = lsts[-1]
	print('first: ', first)
	print('second: ', second)
	for i in range(len(lsts)-3, -1, -1):
		tmp_arr = [] 
		for j in range(len(first)):
			tmp_arr.append(first[j] + min(second[j], second[j+1]))
		second = tmp_arr
		first = lsts[i]
		print('first: ', first)
		print('second: ', second)

	return first[0] + min(second[0], second[1])

print(get_min_path([[2], [300,100], [5,7,6], [8,9,10,11]]))
