import sys
sys.setrecursionlimit(2147483647)

with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-10.txt') as f:
	input = f.read()

# [ [ (north, south, east, west), ... ], ... ]
pipes = [[(c in "|LJS", c in "|7FS", c in "-LFS", c in "-J7S") for c in l] for l in input.split('\n')]

distances = [[-1 for x in range(len(pipes[0]))] for y in range(len(pipes))]

pos = [(x, y) for x in range(len(pipes[0])) for y in range(len(pipes)) if pipes[y][x] == (True, True, True, True)][0]

def backtrack(pos, dist):
	if pos[0] < 0 or pos[1] < 0 or pos[0] >= len(pipes[0]) or pos[1] >= len(pipes):
		return

	if distances[pos[1]][pos[0]] != -1:
		if distances[pos[1]][pos[0]] > dist:
			distances[pos[1]][pos[0]] = dist
		else:
			return

	distances[pos[1]][pos[0]] = dist
	
	if pipes[pos[1]][pos[0]][0] and pipes[pos[1] - 1][pos[0]][1]:
		backtrack((pos[0], pos[1] - 1), dist + 1)
	if pipes[pos[1]][pos[0]][1] and pipes[pos[1] + 1][pos[0]][0]:
		backtrack((pos[0], pos[1] + 1), dist + 1)
	if pipes[pos[1]][pos[0]][2] and pipes[pos[1]][pos[0] + 1][3]:
		backtrack((pos[0] + 1, pos[1]), dist + 1)
	if pipes[pos[1]][pos[0]][3] and pipes[pos[1]][pos[0] - 1][2]:
		backtrack((pos[0] - 1, pos[1]), dist + 1)

backtrack(pos, 0)

distances = [[0 if d < 0 else d for d in l] for l in distances]

print(max([max(l) for l in distances]))
