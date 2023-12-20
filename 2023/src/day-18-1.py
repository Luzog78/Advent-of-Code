import sys
sys.setrecursionlimit(2147483647)

with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-18.txt') as f:
	input = f.read()

input = input.split('\n')

moves = [(l.split(' ')[0], int(l.split(' ')[1]), l.split(' ')[2][2:-1]) for l in input]

pos = [0, 0]

positions = [tuple(pos)]

for dir, dist, color in moves:
	step = None
	if dir == 'U':
		step = [0, 1]
	elif dir == 'D':
		step = [0, -1]
	elif dir == 'L':
		step = [-1, 0]
	elif dir == 'R':
		step = [1, 0]
	for i in range(dist):
		pos[0] += step[0]
		pos[1] += step[1]
		positions.append(tuple(pos))

minx, miny = min(positions, key=lambda p: p[0])[0] - 1, min(positions, key=lambda p: p[1])[1] - 1
maxx, maxy = max(positions, key=lambda p: p[0])[0] + 1, max(positions, key=lambda p: p[1])[1] + 1

tab = [[1 if (x, y) in positions else 0 for x in range(minx, maxx + 1)] for y in range(miny, maxy + 1)]

# ############################################################################ #
# Note: It is verry efficient but segfaults on large inputs.
# def repend(pos):
# 	if pos[0] < 0 or pos[1] < 0 or pos[0] >= len(tab[0]) or pos[1] >= len(tab):
# 		return
	
# 	if tab[pos[1]][pos[0]] != 0:
# 		return
	
# 	tab[pos[1]][pos[0]] = -1

# 	repend((pos[0] - 1, pos[1] - 1))
# 	repend((pos[0] - 1, pos[1] + 1))
# 	repend((pos[0] - 1, pos[1]))
# 	repend((pos[0] + 1, pos[1] - 1))
# 	repend((pos[0] + 1, pos[1] + 1))
# 	repend((pos[0] + 1, pos[1]))
# 	repend((pos[0], pos[1] - 1))
# 	repend((pos[0], pos[1] + 1))
# ############################################################################ #

tab[0][0] = -1

changes = True

while changes:
	changes = False

	for y in range(len(tab)):
		for x in range(len(tab[0])):
			if tab[y][x] == 0 \
				and (x == 0 or y == 0 or x == len(tab[0]) - 1 or y == len(tab) - 1 \
					or tab[y - 1][x - 1] == -1 or tab[y - 1][x + 1] == -1 or tab[y - 1][x] == -1 \
					or tab[y + 1][x - 1] == -1 or tab[y + 1][x + 1] == -1 or tab[y + 1][x] == -1 \
					or tab[y][x - 1] == -1 or tab[y][x + 1] == -1):
				tab[y][x] = -1
				changes = True

	for y in range(len(tab) - 1, -1, -1):
		for x in range(len(tab[0]) - 1, -1, -1):
			if tab[y][x] == 0 \
				and (x == 0 or y == 0 or x == len(tab[0]) - 1 or y == len(tab) - 1 \
					or tab[y - 1][x - 1] == -1 or tab[y - 1][x + 1] == -1 or tab[y - 1][x] == -1 \
					or tab[y + 1][x - 1] == -1 or tab[y + 1][x + 1] == -1 or tab[y + 1][x] == -1 \
					or tab[y][x - 1] == -1 or tab[y][x + 1] == -1):
				tab[y][x] = -1
				changes = True

#for l in tab:
#	print(''.join(['#' if c == 1 else '.' if c == -1 else ' ' for c in l]))

print(sum(l.count(0) + l.count(1) for l in tab))
