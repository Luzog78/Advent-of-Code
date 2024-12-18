with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-15.txt') as f:
	input = f.read()

raw_map, sequence = input.strip().split('\n\n')

map = ''
for c in raw_map:
	if c == '@':
		map += '@.'
	elif c == 'O':
		map += '[]'
	elif c == '#':
		map += '##'
	elif c == '.':
		map += '..'
	else:
		map += c

map = [list(l) for l in map.split('\n')]
sequence = list(sequence.replace('\n', ''))

w, h = len(map[0]), len(map)
x, y = 0, 0

for i in range(h):
	for j in range(w):
		if map[i][j] == '@':
			x, y = j, i
			break

def up(m: list[tuple[int, int, str]], x: int, y: int, nw: str = '@') -> bool:
	y -= 1
	c = map[y][x]
	if nw == '[':
		cc = map[y][x + 1]
		if cc == '#' or (cc == '[' and not up(m, x + 1, y, cc)):
			return False
	if c == '#' or (c == '[' and not up(m, x, y, c)) or (c == ']' and not up(m, x - 1, y, '[')):
		return False
	if nw == '[':
		m.append((y, x + 1, map[y][x + 1]))
		m.append((y + 1, x + 1, map[y + 1][x + 1]))
		map[y][x + 1] = ']'
		map[y + 1][x + 1] = '.'
	m.append((y, x, map[y][x]))
	m.append((y + 1, x, map[y + 1][x]))
	map[y][x] = nw
	map[y + 1][x] = '.'
	return True

def down(m: list[tuple[int, int, str]], x: int, y: int, nw: str = '@') -> bool:
	y += 1
	c = map[y][x]
	if nw == '[':
		cc = map[y][x + 1]
		if cc == '#' or (cc == '[' and not down(m, x + 1, y, cc)):
			return False
	if c == '#' or (c == '[' and not down(m, x, y, c)) or (c == ']' and not down(m, x - 1, y, '[')):
		return False
	if nw == '[':
		m.append((y, x + 1, map[y][x + 1]))
		m.append((y - 1, x + 1, map[y - 1][x + 1]))
		map[y][x + 1] = ']'
		map[y - 1][x + 1] = '.'
	m.append((y, x, map[y][x]))
	m.append((y - 1, x, map[y - 1][x]))
	map[y][x] = nw
	map[y - 1][x] = '.'
	return True

def left(m: list[tuple[int, int, str]], x: int, y: int, nw: str = '@') -> bool:
	x -= 1
	c = map[y][x]
	if c == '#' or (c == ']' and not left(m, x - 1, y, '[')):
		return False
	if nw == '[':
		m.append((y, x + 1, map[y][x + 1]))
		m.append((y, x + 2, map[y][x + 2]))
		map[y][x + 1] = ']'
		map[y][x + 2] = '.'
	else:
		m.append((y, x + 1, map[y][x + 1]))
		map[y][x + 1] = '.'
	m.append((y, x, map[y][x]))
	map[y][x] = nw
	return True

def right(m: list[tuple[int, int, str]], x: int, y: int, nw: str = '@') -> bool:
	x += 1
	c = map[y][x]
	if c == '#' or (c == '[' and not right(m, x + 1, y, ']')):
		return False
	if nw == ']':
		m.append((y, x - 1, map[y][x - 1]))
		m.append((y, x - 2, map[y][x - 2]))
		map[y][x - 1] = '['
		map[y][x - 2] = '.'
	else:
		m.append((y, x - 1, map[y][x - 1]))
		map[y][x - 1] = '.'
	m.append((y, x, map[y][x]))
	map[y][x] = nw
	return True

def rollback(m: list[tuple[int, int, str]]):
	for y, x, c in m[::-1]:
		map[y][x] = c

for _, s in enumerate(sequence):
	modified: list[tuple[int, int, str]] = []
	if s == '^':
		if up(modified, x, y):
			y -= 1
		else:
			rollback(modified)
	elif s == 'v':
		if down(modified, x, y):
			y += 1
		else:
			rollback(modified)
	elif s == '<':
		if left(modified, x, y):
			x -= 1
		else:
			rollback(modified)
	elif s == '>':
		if right(modified, x, y):
			x += 1
		else:
			rollback(modified)

gps_sum = 0

for i in range(h):
	for j in range(w):
		if map[i][j] == '[':
			gps_sum += 100 * i + j

print(gps_sum)
