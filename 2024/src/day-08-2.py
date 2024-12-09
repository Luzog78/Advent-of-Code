with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-08.txt') as f:
	input = f.read()

map = [list(s) for s in input.strip().split('\n')]

w, h = len(map[0]), len(map)

antennas: dict[str, list[tuple[int, int]]] = {}

for y in range(h):
	for x in range(w):
		c = map[y][x]
		if c != '.':
			if c not in antennas:
				antennas[c] = [(x, y)]
			else:
				antennas[c].append((x, y))

antinodes: set[tuple[int, int]] = set()

for a in antennas.values():
	sz = len(a)
	for i in range(sz):
		for j in range(i + 1, sz):
			x1, y1 = a[i]
			x2, y2 = a[j]
			dx, dy = x2 - x1, y2 - y1
			antinode_x, antinode_y = x1, y1
			while 0 <= antinode_x < w and 0 <= antinode_y < w:
				antinodes.add((antinode_x, antinode_y))
				antinode_x -= dx
				antinode_y -= dy
			antinode_x, antinode_y = x2, y2
			while 0 <= antinode_x < w and 0 <= antinode_y < h:
				antinodes.add((antinode_x, antinode_y))
				antinode_x += dx
				antinode_y += dy

print(len(antinodes))
