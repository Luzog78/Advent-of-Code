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

for y in range(len(expension[0]) - 1, -1, -1):
	universe.insert(expension[0][y], '.' * len(universe[0]))

for x in range(len(expension[1]) - 1, -1, -1):
	for y in range(len(universe)):
		universe[y] = universe[y][:expension[1][x]] + '.' + universe[y][expension[1][x]:]

galaxies = []

for y in range(len(universe)):
	for x in range(len(universe[0])):
		if universe[y][x] == '.':
			continue
		galaxies.append((x, y))

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

# for line in universe:
# 	print(line)

print(sum(p[0] for p in paths))
