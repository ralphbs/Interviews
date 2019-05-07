class Matcher:

	def __init__(self, s):
		self.s = s

	def is_matching(self):
		stack = []
		lookup = {
			'(': ')',
			'[': ']',
			'{': '}',
		}
		for c in self.s:
			if c in lookup:
				stack.append(c)
				continue
			if not stack or lookup[stack.pop()] != c:
				return False

		return not stack		


print(matcher.is_matching())

