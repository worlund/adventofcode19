import sys

pixels = sys.stdin.readline().strip()

x = 25
y = 6
layers = int(len(pixels)/(x*y))

fewest = (999, 0 ,0)

final_image = [[2]*x for i in range(y)]

layer = 0
while layer < layers:
	zeros = 0
	ones = 0
	twos = 0
	i = 0
	for i in range(y):
		for j in range(x):
			p = int(pixels[j+x*i+x*y*layer])

			if final_image[i][j] == 2:
				final_image[i][j] = p

			if p == 0:
				zeros += 1
			elif p == 1:
				ones += 1
			elif p == 2:
				twos += 1

	if zeros < fewest[0]:
		fewest = (zeros, ones, twos)
	layer+=1

print("part1:",fewest[1]*fewest[2],"\n")

##PRINT FINAL IMAGE
print("part2:")
for i in range(y):
	for j in range(x):
		if(final_image[i][j] == 1):
			print(final_image[i][j], end='')
		else:
			print(' ',end='')
	print()

