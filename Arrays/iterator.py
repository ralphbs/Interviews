# Given an array of arrays, implement an iterator class to allow the client to traverse and remove elements in the array list in place. This iterator should provide three public class member functions:

# boolean hasNext()
#    return true if there is another element in the whole structure
# int next()
#    return the value of the next element in the structure
# void remove()
#    remove the last element returned by the iterator.
#    I.e., remove the element that the previous call to next() returned.
#    This method can be called only once per call to next(), otherwise an exception will be thrown.

# Example Input:
# [[], [1,2,3]]

# iterator = new Iterator(input)
# iterator.next() -> returns 1
# iterator.remove() -> removes 1
# print input [[], [2,3]]
# iterator.hasNext() -> true
# iterator.next() -> 2
# iterator.remove() -> removes 2
# iterator.remove() -> throws exception

class Iterator:
	def __init__(self, input):
		self.input = input
		self.outer_array_curr = 0
		self.inner_array_curr = -1

	def next(self):
		if self.outer_array_curr >= len(self.input):
			print("Nothing to iterate over anymore.")
			return None

		# if inner array is empty, keep moving until you find next available spot
		sub_input_len = len(self.input[self.outer_array_curr])
		if (sub_input_len == 0):
			next_non_empty_idx = self.find_next_non_empty_idx()
			# This means it did not find anything
			if next_non_empty_idx is None:
				return None
			# Reset inner_array_curr to 0
			self.inner_array_curr = 0
			return self.input[next_non_empty_idx][self.inner_array_curr]

		# if current idx is the last element in an internal array
		if (self.inner_array_curr == sub_input_len - 1):
			self.outer_array_curr += 1
			# Have we reached the end?
			if (self.outer_array_curr == len(self.input) - 1):
				return None
			next_non_empty_idx = self.find_next_non_empty_idx()
			if next_non_empty_idx is None:
				return None
			# Reset inner_array_curr to 0
			self.inner_array_curr = 0
			return self.input[next_non_empty_idx][self.inner_array_curr]
		
		# if current idx is the last array in the main array
		if (self.outer_array_curr == sub_input_len - 1):
			# if current idx is the last element in the array
			if (self.inner_array_curr == sub_input_len - 1):
				return None

		self.inner_array_curr += 1
		return self.input[self.outer_array_curr][self.inner_array_curr]
		

	def find_next_non_empty_idx(self):
		return_idx = None
		sub_input_len = len(self.input[self.outer_array_curr])
		while(sub_input_len == 0 and self.outer_array_curr < len(self.input) - 1):
			self.outer_array_curr += 1
			# Reached the last array
			if (self.outer_array_curr == len(self.input) - 1):
				break
			return_idx = self.outer_array_curr
			sub_input_len = len(self.input[self.outer_array_curr])
		
		# Reached the last array
		if self.outer_array_curr > len(self.input)-1:
			return None		

		return return_idx


def main():
	iterator = Iterator([[], [2,3], [], [], [4], [], [5, 6]])
	print(iterator.input)
	print(iterator.next())
	print(iterator.next())
	print(iterator.next())
	print(iterator.next())
	print(iterator.next())
	print(iterator.next())
	print(iterator.next())

main()



# Normal case: If I am in the beginning or middle of an array, just keep outer_curr_array as is and increment inner_curr_array by 1
# Edge cases:
#	* If an array is empty, keep searching until you find a non-empty array (reset inner_array_curr to 0, the outer_array_curr is the new index you found) or you have reached the end of the main list where you return None
#	* If I am on the last element of an array, keep searching for a non-empty array or the end of the main list (indices same as above)
