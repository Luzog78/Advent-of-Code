with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-11.txt') as f:
	input = f.read()

LIMIT = 75
stones = [[int(v), 1] for v in input.strip().split(' ')] # (value, amount)
num = 0

seen: dict[int, tuple[int, int]] = {0: (1, -1)} # (next_value, next_right)
next_stones: list[list[int, int]] = [] # (value, amount)

def handle_stone(value: int, amount: int):
	global seen, next_stones
	if value == 0:
		next_stones.append([1, amount])
		return
	if value in seen:
		value, right = seen[value]
		next_stones.append([value, amount])
		if right != -1:
			next_stones.append([right, amount])
		return
	s = str(value)
	l = len(s)
	old = value
	if l % 2 == 1:
		value *= 2024
		seen[old] = (value, -1)
	else:
		h = l // 2
		value, right = int(s[:h]), int(s[h:])
		seen[old] = (value, right)
		next_stones.append([right, amount])
	next_stones.append([value, amount])

def merge_stones(stones: list[tuple[int, int]]):
	for i, a in enumerate(stones):
		edited = True
		while edited:
			edited = False
			for j, b in enumerate(stones):
				if i == j:
					continue
				if a[0] == b[0]:
					a[1] += b[1]
					stones.pop(j)
					edited = True
					break

depth = 0
while depth < LIMIT:
	merge_stones(stones)
	for v, a in stones:
		handle_stone(v, a)
	stones = next_stones
	next_stones = []
	depth += 1

print(sum([a for _, a in stones]))
