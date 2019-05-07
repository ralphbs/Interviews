def permutations(s):
	permutations_helper(s, "")


def permutations_helper(s, prefix=""):
	if (len(s)) == 0:
		print(prefix)
		return
	for i,_ in enumerate(s):
		permutations_helper(s[:i]+s[i+1:], prefix+s[i])

def main():
	permutations("yara")

main()
