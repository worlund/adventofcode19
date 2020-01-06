import sys

def find_input(intcode, output):
	for i in range(100):
		for j in range(100):
			res = run_program(intcode[:], i, j)[0]
			if res == output:
				return i, j
	print("no answer")


def run_program(intcode, noun, verb):
	intcode[1] = noun
	intcode[2] = verb
	for i in range(0, len(intcode), 4):
		opcode = intcode[i]
		pos1 = intcode[i+1]
		pos2 = intcode[i+2]
		pos3 = intcode[i+3]
		if opcode == 1:
			intcode[pos3] = intcode[pos1] + intcode[pos2]
		elif opcode == 2:
			intcode[pos3] = intcode[pos1] * intcode[pos2]
		elif opcode == 99:
			break
		else:
			print("uknown code", opcode)
			break
	return intcode

intcode = list(map(int, "".join(sys.stdin.readlines()).strip().split(",")))

##PART 1
res = run_program(intcode[:], 12, 2)[0]
print("Results for noun = 12 and verb = 2: ",res)

##PART 2
output = 19690720
n, v = find_input(intcode[:], output)
print(100*n+v)