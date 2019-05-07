def partial_multiplication(arr, digit):
	sum = 0
	multiple_10 = 1
	for idx in reversed(range(0, len(arr))):
		val = arr[idx]
		sum += digit*val*multiple_10 
		multiple_10 *= 10
	return sum

# O(nm) solution where n and m are lengths of 
# arrays num1 and num2 respectively
def multiply_arrays(num1, num2):
	sum = 0
	multiple_10 = 1
	for idx in reversed(range(0, len(num2))):
		val = num2[idx]
		sum += partial_multiplication(num1, val)*multiple_10
		multiple_10 *= 10
	return sum


def main():
	print multiply_arrays([-123], [-9])

main()