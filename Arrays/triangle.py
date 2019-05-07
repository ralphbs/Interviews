def get_min_path(lsts):
	if not lsts:
		return 0
	val = 0
	i = 0
	min_sum = 999999999999 
	while(i<len(lsts)):
		j = 0
		while(j<len(lsts[i])):
			val = lsts[i][j] + min(lsts[i+1][j]+get_min_path(lsts[i+2:]), lsts[i+1][j+1] + get_min_path(lsts[i+2:]))
			if val<min_sum:
				min_sum = val
			j+=1
		i+=1
	print('batata', lsts[0][0])
	return val


input = [[2], [3,4], [6,5,7], [4,1,8,3]]
# input2 = [[3], [6,4], [5,2,7], [9,1,8,6]] 
print(get_min_path(input))
#  print('------------------')
# print(get_min_path(input2))
