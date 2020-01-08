import sys
import queue
from timeit import default_timer as timer

def bfs(orbits, root):
	q = queue.Queue()
	q.put(root)
	visited = {}
	visited[root] = 0
	paths = {}
	total = 0
	while not q.empty():
		v = q.get()
		for o in orbits:
			if o[0] == v and o[1] not in visited:
				q.put(o[1])
				visited[o[1]] = visited[o[0]]+1
				paths[o[1]] = v
				total+=visited[o[1]]
	return total, paths, visited

def dist(node1, node2, paths):
	curr = node1
	n1steps = 0
	n2steps = 0
	while paths[curr] != "COM":
		n1steps+=1
		tmp = node2
		curr = paths[curr]
		found = False
		n2steps = 0
		while paths[tmp] != "COM":
			n2steps += 1
			if curr == paths[tmp]:
				found = True
				break
			tmp = paths[tmp]
		if found:
			break
	return n1steps+n2steps-2

def dist_better(node1, node2, paths, weights):
	curr = node1
	target = node2
	targetPath = set()
	dist = 0

	#get whole path for target node
	while paths[target] != "COM":
		targetPath.add(paths[target])
		target = paths[target]

	#find first occurence of intersection in target path for start node
	while paths[curr] != "COM":
		if paths[curr] in targetPath:
			dist = weights[node1] + weights[node2] - 2*weights[paths[curr]] - 2
			break
		curr = paths[curr]
	return dist

orbits = [x.strip().split(")") for x in sys.stdin.readlines()]

root = "COM"
n1 = "YOU"
n2 = "SAN"

res, paths, weights = bfs(orbits, root)
print("total orbits: ",res)
res1 = dist("YOU", "SAN", paths)
print("orbits between {} and {}: {}".format(n1, n2, res1))
res2 = dist_better(n1,n2,paths, weights)
print("orbits between {} and {}: {}".format(n1, n2, res2))
