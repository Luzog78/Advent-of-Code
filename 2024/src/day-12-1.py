with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-12.txt') as f:
	input = f.read()

map = [['#', *list(l), '#'] for l in input.strip().split('\n')]
w, h = len(map[0]), len(map)

map = [['#'] * w] + map + [['#'] * w]
h += 2

regions: list[tuple[int, int]] = [] # (area, perimeter)

def analyse(x: int, y: int) -> tuple[int, int]:
	global map
	a, p = 1, 0
	v = map[y][x]
	map[y][x] = ' '

	def nxt(_x, _y):
		nonlocal a, p
		_v = map[_y][_x]
		if _v == v:
			_a, _p = analyse(_x, _y)
			a += _a
			p += _p
		elif _v != ' ':
			p += 1

	nxt(x + 1, y)
	nxt(x - 1, y)
	nxt(x, y + 1)
	nxt(x, y - 1)
	return a, p

for y in range(1, h - 1):
	for x in range(1, w - 1):
		if map[y][x] == '#':
			continue
		regions.append(analyse(x, y))
		map = [['#' if c == ' ' else c for c in l] for l in map]

print(sum(a * p for a, p in regions))
