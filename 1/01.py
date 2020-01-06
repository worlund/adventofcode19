import sys

def fuel(m):
	return m//3-2

def totalfuel(m):
	total = 0
	while(fuel(m) > 0):
		total += fuel(m)
		m = fuel(m)
	return total

c = list(map(int, sys.stdin.readlines()))

total = 0
for m in c:
	total += fuel(m)
print(total)

totalf = 0
for m in c:
	totalf += totalfuel(m)
print(totalf)