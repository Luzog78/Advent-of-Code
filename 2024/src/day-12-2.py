with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-12.txt') as f:
	input = f.read()

map = [['#', *list(l), '#'] for l in input.strip().split('\n')]
w, h = len(map[0]), len(map)

map = [['#'] * w] + map + [['#'] * w]
h += 2

regions: list[tuple[int, int]] = [] # (area, number of sides)

def analyse(x: int, y: int) -> tuple[int, dict[int, tuple[int, int]]]: # (area, sides(x, y, orientation))
	global map
	a, p = 1, []
	v = map[y][x]
	map[y][x] = ' '

	def nxt(_x, _y, orientation):
		nonlocal a, p
		_v = map[_y][_x]
		if _v == v:
			_a, _p = analyse(_x, _y)
			a += _a
			p += _p
		elif _v != ' ':
			p.append((_x, _y, orientation))

	nxt(x + 1, y, 1)
	nxt(x - 1, y, 2)
	nxt(x, y + 1, 3)
	nxt(x, y - 1, 4)
	return a, p

def calc_sides(sides: list[tuple[int, int, int]]) -> int:
	d: dict[int, list[tuple[int, int]]] = {1: [], 2: [], 3: [], 4: []}
	for x, y, o in sides:
		d[o].append((x, y))

	def horz(l: list[tuple[int, int]]) -> int:
		sides = 0
		ys = {y for _, y in l}
		for y in ys:
			xs = sorted([x for x, _ in l if _ == y])
			sides += 1
			if len(xs) == 1:
				continue
			for i in range(1, len(xs)):
				if xs[i] - xs[i - 1] > 1:
					sides += 1
		return sides

	def vert(l: list[tuple[int, int]]) -> int:
		sides = 0
		xs = {x for x, _ in l}
		for x in xs:
			ys = sorted([y for _, y in l if _ == x])
			sides += 1
			if len(ys) == 1:
				continue
			for i in range(1, len(ys)):
				if ys[i] - ys[i - 1] > 1:
					sides += 1
		return sides

	return vert(d[1]) + vert(d[2]) + horz(d[3]) + horz(d[4])

for y in range(1, h - 1):
	for x in range(1, w - 1):
		if map[y][x] == '#':
			continue
		a, sides = analyse(x, y)
		s = calc_sides(sides)
		regions.append((a, s))
		map = [['#' if c == ' ' else c for c in l] for l in map]

print(sum(a * p for a, p in regions))
