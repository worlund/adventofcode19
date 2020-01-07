import sys
import math

def point(x, y):
	return (x,y)

def line(x1, y1, x2, y2):
	return ((x1, y1), (x2, y2))

def wire_path_to_lines(wire, center):
	lines = []
	current_pos = center
	totalsteps = 0
	for path in wire:
		direction = path[0]
		steps = int(path[1:])
		if direction == 'R':
			lines.append((line(current_pos[0], current_pos[1], current_pos[0]+steps, current_pos[1]), totalsteps))
			current_pos = point(current_pos[0]+steps, current_pos[1])
		elif direction == 'L':
			lines.append((line(current_pos[0], current_pos[1], current_pos[0]-steps, current_pos[1]), totalsteps))
			current_pos = point(current_pos[0]-steps, current_pos[1])
		elif direction == 'U':
			lines.append((line(current_pos[0], current_pos[1], current_pos[0], current_pos[1]+steps), totalsteps))
			current_pos = point(current_pos[0], current_pos[1]+steps)
		elif direction == 'D':
			lines.append((line(current_pos[0], current_pos[1], current_pos[0], current_pos[1]-steps), totalsteps))
			current_pos = point(current_pos[0], current_pos[1]-steps)
		totalsteps += steps
	return lines

def between(v, n, m):
	if v < n and v >m:
		return True
	elif v > n and v < m:
		return True
	else:
		return False

def crossing(l1, l2):
	l1steps = 0
	l2steps = 0
	if l1[0][0] == l1[1][0] and l2[0][1] == l2[1][1]:
		if between(l1[0][0], l2[0][0], l2[1][0]) and between(l2[0][1], l1[0][1], l1[1][1]):
			#print("found intersection for l1 {} and l2 {}: {}".format(l1, l2, (l1[0][0], l2[0][1])))
			l1steps = abs(l2[0][1]-l1[0][1])
			l2steps = abs(l1[0][0]-l2[0][0])
			return ((l1[0][0], l2[0][1]), l1steps, l2steps)
	elif l1[0][1] == l1[1][1] and l2[0][0] == l2[1][0]:
		if between(l2[0][0], l1[0][0], l1[1][0]) and between(l1[0][1], l2[0][1], l2[1][1]):
			#print("found intersection for l1 {} and l2 {}: {}".format(l1, l2, (l2[0][0], l1[0][1])))
			l1steps = abs(l1[0][0]-l2[0][0])
			l2steps = abs(l2[0][1]-l1[0][1])
			return ((l2[0][0], l1[0][1]), l1steps, l2steps)
	return (0, -1, -1)

def find_intersections(wire1, wire2):
	intersections = []
	for (l1, w1) in wire1:
		for (l2, w2) in wire2:
			(intersect, l1steps, l2steps) = crossing(l1, l2)
			if intersect != 0:
				print("intersect:",intersect, "w1:",w1+l1steps,"w2:", w2+l2steps)
				intersections.append((intersect, w1+l1steps, w2+l2steps))
	return intersections

def shortest_taxicab_dist(points, target):
	shortest = 99999999999999999
	for (p, _, _) in points:
		dist = 0
		for i in range(len(p)):
			dist+=abs(target[i]-p[i])
		if dist > 0:
				shortest = min(dist, shortest)
		#print(p, dist)
	return shortest

def shortest_steps_dist(points):
	shortest = 999999999999999999
	for (_, w1steps, w2steps) in points:
		shortest = min(shortest, w1steps+w2steps)
	return shortest


##START HERE
startpos = point(0,0)

#[(line, steps)]
wire1 = sys.stdin.readline().strip().split(",")
wire2 = sys.stdin.readline().strip().split(",")

wire1 = wire_path_to_lines(wire1, startpos)
wire2 = wire_path_to_lines(wire2, startpos)

intersections = find_intersections(wire1, wire2)
print("shortest X: ", shortest_taxicab_dist(intersections, startpos))
print("shortest steps: ", shortest_steps_dist(intersections))
