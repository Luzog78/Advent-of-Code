with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-15.txt') as f:
	input = f.read()

map, sequence = input.strip().split('\n\n')

map = [list(l) for l in map.split('\n')]
sequence = list(sequence.replace('\n', ''))

w, h = len(map[0]), len(map)
x, y = 0, 0

for i in range(h):
	for j in range(w):
		if map[i][j] == '@':
			x, y = j, i
			break

def up(x: int, y: int, nw: str = '@') -> bool:
	y -= 1
	c = map[y][x]
	if c == '#' or (c == 'O' and not up(x, y, c)):
		return False
	map[y][x] = nw
	map[y + 1][x] = '.'
	return True

def down(x: int, y: int, nw: str = '@') -> bool:
	y += 1
	c = map[y][x]
	if c == '#' or (c == 'O' and not down(x, y, c)):
		return False
	map[y][x] = nw
	map[y - 1][x] = '.'
	return True

def left(x: int, y: int, nw: str = '@') -> bool:
	x -= 1
	c = map[y][x]
	if c == '#' or (c == 'O' and not left(x, y, c)):
		return False
	map[y][x] = nw
	map[y][x + 1] = '.'
	return True

def right(x: int, y: int, nw: str = '@') -> bool:
	x += 1
	c = map[y][x]
	if c == '#' or (c == 'O' and not right(x, y, c)):
		return False
	map[y][x] = nw
	map[y][x - 1] = '.'
	return True

for s in sequence:
	if s == '^':
		if up(x, y):
			y -= 1
	elif s == 'v':
		if down(x, y):
			y += 1
	elif s == '<':
		if left(x, y):
			x -= 1
	elif s == '>':
		if right(x, y):
			x += 1

gps_sum = 0

for i in range(h):
	for j in range(w):
		if map[i][j] == 'O':
			gps_sum += 100 * i + j

print(gps_sum)
