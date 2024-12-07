with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-06.txt') as f:
	input = f.read()

'''
Cell:

0bxx: type (0: empty, 1: wall, 2: guard)
0bxx: facing (0: ^, 1: >, 2: v, 3: <)
0bxxxx: visited facing

0bxxxx_xxxx: visited << 4 | facing << 2 | type
'''

map = [[(0b0000_0010 if c == '^' else 0b0000_0001 if c == '#' else 0)
			for c in s] for s in input.strip().split('\n')]
w, h = len(map[0]), len(map)

def start_pos():
	for y in range(h):
		for x in range(w):
			if map[y][x] & 2:
				return x, y
	return -1, -1

px, py = start_pos()
facing = 0  # 0: ^, 1: >, 2: v, 3: <

def simulation(map, px, py, facing) -> bool:
	while True:
		curr_visited = map[py][px] >> 4
		if curr_visited & (1 << facing):
			return True
		map[py][px] = (curr_visited | (1 << facing)) << 4 | facing << 2 | 2
		nx, ny = px, py
		match facing:
			case 0:
				ny -= 1
			case 1:
				nx += 1
			case 2:
				ny += 1
			case 3:
				nx -= 1
		if nx < 0 or nx >= w or ny < 0 or ny >= h:
			return False
		if map[ny][nx] & 1:
			facing += 1
			facing %= 4
		else:
			px, py = nx, ny

map_copy = [l.copy() for l in map]

simulation(map_copy, px, py, facing)

visited = []
y = 0
while y < h:
	x = 0
	while x < w:
		if map_copy[y][x] & 2 and not (x == px and y == py):
			visited.append((x, y))
		x += 1
	y += 1

loops = []

for x, y in visited:
	map_copy = [l.copy() for l in map]
	map_copy[y][x] = 1
	if simulation(map_copy, px, py, facing):
		loops.append((x, y))

print(len(loops))
