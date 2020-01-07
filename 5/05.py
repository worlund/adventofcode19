import sys

def immidiate_mode(instruction, param):
	mode = 0
	if (instruction%(100*pow(10, param)))//(10*pow(10,param)) == 1:
		mode = 1
	return mode

def mode_val(intcode, instruction, v, p):
	if immidiate_mode(instruction, p):
		return v
	else:
		return intcode[v] 

def mode_mult(intcode, v1, v2):
	result = 1

	return result

def run_program(intcode, val):
	i = 0
	while i < len(intcode):
		instruction = intcode[i]
		#print("instruction:",instruction)
		opcode = instruction % 100
		if opcode == 1:
			v1 = intcode[i+1]
			v2 = intcode[i+2]
			v3 = intcode[i+3]

			val1 = mode_val(intcode, instruction, v1, 1)
			val2 = mode_val(intcode, instruction, v2, 2)
			#print("param modes", immidiate_mode(instruction, 1), immidiate_mode(instruction, 2))
			intcode[v3] = val1 + val2
			i += 4
		elif opcode == 2:
			v1 = intcode[i+1]
			v2 = intcode[i+2]
			v3 = intcode[i+3]

			val1 = mode_val(intcode, instruction, v1, 1)
			val2 = mode_val(intcode, instruction, v2, 2)
			#print("param modes", immidiate_mode(instruction, 1), immidiate_mode(instruction, 2))
			intcode[v3] = val1 * val2
			i += 4
		elif opcode == 3:
			v1 = intcode[i+1]
			intcode[v1] = val
			i += 2
		elif opcode == 4:
			v1 = intcode[i+1]
			print(mode_val(intcode, instruction, v1, 1))
			i += 2
		elif opcode == 5:
			val1 = mode_val(intcode, instruction, intcode[i+1], 1)
			val2 = mode_val(intcode, instruction, intcode[i+2], 2)
			if val1 > 0:
				i = val2
			else:
				i += 3
		elif opcode == 6:
			val1 = mode_val(intcode, instruction, intcode[i+1], 1)
			val2 = mode_val(intcode, instruction, intcode[i+2], 2)
			if val1 == 0:
				i = val2
			else:
				i += 3
		elif opcode == 7:
			val1 = mode_val(intcode, instruction, intcode[i+1], 1)
			val2 = mode_val(intcode, instruction, intcode[i+2], 2)
			storepos = intcode[i+3]
			if val1 < val2:
				intcode[storepos] = 1
			else:
				intcode[storepos] = 0
			i += 4
		elif opcode == 8:
			val1 = mode_val(intcode, instruction, intcode[i+1], 1)
			val2 = mode_val(intcode, instruction, intcode[i+2], 2)
			storepos = intcode[i+3]
			if val1 == val2:
				intcode[storepos] = 1
			else:
				intcode[storepos] = 0
			i += 4
		elif opcode == 99:
			break
		else:
			print("uknown code", opcode)
			break
	return intcode

intcode = list(map(int, "".join(sys.stdin.readlines()).strip().split(",")))

inpt = 5
run_program(intcode[:], inpt)