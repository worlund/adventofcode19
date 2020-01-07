import sys

def check_password(number):
	prev = -1
	pair = 0
	ascending = True
	cons = 0

	for ch in number:
		d = int(ch)
		if d >= prev:
			if d == prev:
				cons+=1
			else:
				if cons == 1:
					pair+=1
				cons=0
			prev = d
		else:
			ascending = False
			break

	#handle last pair
	if cons == 1:
		pair+=1

	if ascending and pair >= 1:
		return True

	return False

def check_range(start, end):
	passwords = 0

	for i in range(start, end+1):
		number = str(i)
		if check_password(number):
			passwords += 1

	return passwords
	

start = 382345
end = 843167
print(check_range(start, end))

#print(check_password("1111144"))
