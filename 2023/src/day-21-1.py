with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-21.txt') as f:
	input = f.read()

garden = input.split('\n')

h, w = len(garden), len(garden[0])

steps_left = 64

for y in range(h):
	for x in range(w):
		if garden[y][x] == 'S':
			start = (x, y)
			break

possibilities = set([start])

for _ in range(steps_left):
	poss = list(possibilities)
	possibilities = set()
	for p in poss:
		x, y = p
		if 0 <= x + 1 < w and garden[y][x + 1] != '#':
			possibilities.add((x + 1, y))
		if 0 <= x - 1 < w and garden[y][x - 1] != '#':
			possibilities.add((x - 1, y))
		if 0 <= y + 1 < h and garden[y + 1][x] != '#':
			possibilities.add((x, y + 1))
		if 0 <= y - 1 < h and garden[y - 1][x] != '#':
			possibilities.add((x, y - 1))

print(len(possibilities))
