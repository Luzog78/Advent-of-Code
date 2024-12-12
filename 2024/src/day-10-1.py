with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-10.txt') as f:
	input = f.read()

map = [[int(c) for c in l] for l in input.strip().split('\n')]
w, h = len(map[0]), len(map)

def find(x: int, y: int) -> set[tuple[int, int]]:
	global w, h
	ret = set()
	v = map[y][x]
	if v == 9:
		return {(x, y)}
	v += 1
	if x < w - 1 and map[y][x + 1] == v:
		ret |= find(x + 1, y)
	if x >= 1 and map[y][x - 1] == v:
		ret |= find(x - 1, y)
	if y < h - 1 and map[y + 1][x] == v:
		ret |= find(x, y + 1)
	if y >= 1 and map[y - 1][x] == v:
		ret |= find(x, y - 1)
	return ret

scores = 0

for y in range(h):
	for x in range(w):
		if map[y][x] == 0:
			scores += len(find(x, y))

print(scores)
