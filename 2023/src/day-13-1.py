with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-13.txt') as f:
	input = f.read()

input = input.split('\n\n')

maps = [l.split('\n') for l in input]

results = [0, 0]

for map in maps:
	for y in range(len(map) - 1):
		simetric = True
		y1, y2 = y, y + 1
		while 0 <= y1 < len(map) and 0 <= y2 < len(map) and simetric:
			for x in range(len(map[0])):
				if map[y1][x] != map[y2][x]:
					simetric = False
					break
			y1 -= 1
			y2 += 1
		if simetric:
			results[0] += y + 1
			break

	for x in range(len(map[0]) - 1):
		simetric = True
		x1, x2 = x, x + 1
		while 0 <= x1 < len(map[0]) and 0 <= x2 < len(map[0]) and simetric:
			for y in range(len(map)):
				if map[y][x1] != map[y][x2]:
					simetric = False
					break
			x1 -= 1
			x2 += 1
		if simetric:
			results[1] += x + 1
			break

print(results[0] * 100 + results[1])
