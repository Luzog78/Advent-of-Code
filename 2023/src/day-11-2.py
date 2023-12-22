with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-11.txt') as f:
	input = f.read()

universe = input.split('\n')

expension = [[], []]

for y in range(len(universe)):
	empty = True
	for x in range(len(universe[0])):
		if universe[y][x] != '.':
			empty = False
			break
	if empty:
		expension[0].append(y)

for x in range(len(universe[0])):
	empty = True
	for y in range(len(universe)):
		if universe[y][x] != '.':
			empty = False
			break
	if empty:
		expension[1].append(x)

galaxies = []

for y in range(len(universe)):
	for x in range(len(universe[0])):
		if universe[y][x] == '.':
			continue
		galaxies.append((x, y))

delta = 999999

for y in range(len(expension[0]) - 1, -1, -1):
	for g, gal in enumerate(galaxies):
		if gal[1] > expension[0][y]:
			galaxies[g] = (gal[0], gal[1] + delta)

for x in range(len(expension[1]) - 1, -1, -1):
	for g, gal in enumerate(galaxies):
		if gal[0] > expension[1][x]:
			galaxies[g] = (gal[0] + delta, gal[1])

min_x = min(g[0] for g in galaxies)
min_y = min(g[1] for g in galaxies)

offset_x = 0 if min_x >= 0 else -min_x
offset_y = 0 if min_y >= 0 else -min_y

for g, gal in enumerate(galaxies[:]):
	galaxies[g] = (gal[0] + offset_x, gal[1] + offset_y)

paths = []

def get_dist(point1, point2):
	x1, y1 = point1
	x2, y2 = point2
	return (abs(x1 - x2) + abs(y1 - y2))

for i in range(len(galaxies) - 1):
	for j in range(i + 1, len(galaxies)):
		x1, y1 = galaxies[i]
		x2, y2 = galaxies[j]
		origins = []
		if x1 < x2:
			origins.append((x1 + 1, y1))
		elif x1 > x2:
			origins.append((x1 - 1, y1))
		if y1 < y2:
			origins.append((x1, y1 + 1))
		elif y1 > y2:
			origins.append((x1, y1 - 1))
		best_dist = 9999999999999999
		best_origin = None
		for o in origins:
			dist = get_dist(o, galaxies[j])
			if dist < best_dist:
				best_dist = dist
				best_origin = o
		paths.append([best_dist + 1, best_origin, galaxies[j]])

print(sum(p[0] for p in paths))
