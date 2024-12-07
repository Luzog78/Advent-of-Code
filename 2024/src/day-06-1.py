with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-06.txt') as f:
	input = f.read()

map = [list(s) for s in input.strip().split('\n')]
w, h = len(map[0]), len(map)

def start_pos():
	for y in range(h):
		for x in range(w):
			if map[y][x] == '^':
				return x, y
	return -1, -1

px, py = start_pos()
facing = 0  # 0: ^, 1: >, 2: v, 3: <

while True:
	map[py][px] = 'X'
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
		break
	if map[ny][nx] == '#':
		facing += 1
		facing %= 4
	else:
		px, py = nx, ny

print(sum(l.count('X') for l in map))
