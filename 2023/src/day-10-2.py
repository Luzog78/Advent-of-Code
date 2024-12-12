import sys
sys.setrecursionlimit(2147483647)

with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-10.txt') as f:
	input = f.read()

input = input.split('\n')

# [ [ (north, south, east, west), ... ], ... ]
pipes = [[(c in "|LJS", c in "|7FS", c in "-LFS", c in "-J7S") for c in l] for l in input]

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

distances = [[0 if d < 0 else 1 for d in l] for l in distances]

inside = []

for y in range(len(distances)):
	is_inside = False
	for x in range(len(distances[0])):
		if distances[y][x] == 1:
			if input[y][x] in "|LJ":
				is_inside = not is_inside
		elif is_inside:
			inside.append((x, y))


print(len(inside))

# Tried 762: too high
# Tried 758: too high

