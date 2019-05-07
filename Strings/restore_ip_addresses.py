# Given a string containing only digits, 
# restore it by returning all possible 
# valid IP address combinations.

# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]

def restore_ip_address(ip):
	return restore_ip_address_helper(ip, 0, "", [])

def restore_ip_address_helper(remaining_str, dots, out_str, out_list):
	if len(remaining_str) > 12 or len(remaining_str) < 1:
		return None

	if dots == 3 and len(remaining_str) > 3:
		return None

	if (dots == 3) and len(remaining_str) <= 3 and int(remaining_str) <= 255 and int(remaining_str) >= 0:
		if len(remaining_str) > 1 and int(remaining_str[0]) == 0:
			return
		out_list.append(out_str+remaining_str)
		return
	
	i, j, curr_num = 0, 0, ""
	while i < len(remaining_str):
			while(j<3):
				curr_num = remaining_str[i:j+1]
				if len(curr_num) <= 3 and int(curr_num) <= 255:
					if int(curr_num[0]) == 0 and len(curr_num) != 1:
						j += 1
						continue
					restore_ip_address_helper(remaining_str[i+j+1:], dots+1, out_str + curr_num + '.', out_list)
				j+=1
			i+=1

	return out_list
			
def main():
	print(restore_ip_address("10101010"))

main()
