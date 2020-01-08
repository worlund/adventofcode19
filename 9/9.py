import sys
from itertools import permutations

def mode(instruction, param):
	mode = 0
	if param < len(str(instruction)):
		mode = int(instruction[param])
	return mode

def mode_val(intcode, instruction, v, p):
	if immidiate_mode(instruction, p):
		return v
	else:
		return intcode[v] 

def run_program(intcode, start_pos, inputs):
	i = start_pos
	output = 0
	while i < len(intcode):
		instruction = intcode[i]
		#print("running instruction:",instruction)
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
			if len(inputs) > 0:
				intcode[v1] = inputs[0]
				inputs = inputs[1:]
			else:
				return ("INPUT", intcode, i, [])
			i += 2
		elif opcode == 4:
			v1 = intcode[i+1]
			output = mode_val(intcode, instruction, v1, 1)
			i += 2
			return ("OUTPUT", intcode, i, inputs, output)
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
			return ("HALT", intcode, i, inputs, output)
		else:
			print("uknown code", opcode)
			break
	return output

	 	
intcode = list(map(int, "".join(sys.stdin.readlines()).strip().split(",")))
inputs = [3, 0]
run_program(intcode[:], 0, inputs)
