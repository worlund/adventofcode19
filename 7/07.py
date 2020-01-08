import sys
from itertools import permutations

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

def test_amplifiers(intcode):
	settings = list(permutations(range(0,5)))
	amp_input = 0
	largest_output = -1
	res = 0
	for config in settings:
		A = run_program(intcode[:], 0, [config[0], amp_input])
		B = run_program(intcode[:], 0, [config[1], A[4]])
		C = run_program(intcode[:], 0, [config[2], B[4]])
		D = run_program(intcode[:], 0, [config[3], C[4]])
		E = run_program(intcode[:], 0, [config[4], D[4]])
		if E[4] > largest_output:
			largest_output = E[4]
			res = config

	print("max signal settings:",largest_output, res)

def run_feedbackloop(intcode):
	settings = list(permutations(range(5, 10)))
	max_output = 0
	for config in settings:
		A = [config[0], 0]
		B = [config[1]]
		C = [config[2]]
		D = [config[3]]
		E = [config[4]]
		inputs = [A, B, C, D, E]
		active = [1, 1, 1, 1, 1]
		amp_states = [
			("INPUT", intcode[:], 0),
			("INPUT", intcode[:], 0),
			("INPUT", intcode[:], 0),
			("INPUT", intcode[:], 0),
			("INPUT", intcode[:], 0)]

		while sum(active) > 0:
			amp_id = 0
			for amp in amp_states:
				if amp[0] != "HALT":
					code = amp[1]
					pc = amp[2]
					amp_inputs = inputs[amp_id]
					print("RUNNING AMP: ", amp_id, " Settings: ", inputs[amp_id], amp_states[amp_id][0])
					state = run_program(code, pc, inputs[amp_id])
					print("RESULTS = ", state[0], state[2], state[3])
					amp_states[amp_id] = state
					#print("STATE\n", state)
					inputs[amp_id] = state[3]
					if state[0] == "HALT":
						active[amp_id] = 0
					elif state[0] == "OUTPUT": #add output to next amps input
						print("adding output:", state[4], " from amp:" ,amp_id, " to", (amp_id+1)%5)
						inputs[(amp_id+1)%5].append(state[4])
						if amp_id == len(amp_states)-1:
							if state[4] > max_output:
								max_output = state[4]
				amp_id+=1

		print("max output: ", max_output)

	 	
intcode = list(map(int, "".join(sys.stdin.readlines()).strip().split(",")))
inputs = [3, 0]
run_program(intcode[:], 0, inputs)
test_amplifiers(intcode)
run_feedbackloop(intcode)