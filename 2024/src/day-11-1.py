with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-11.txt') as f:
	input = f.read()

LIMIT = 25
stones = [(1, 1) if v == '0' else (0, int(v)) for v in input.strip().split(' ')]
num = 0

def handle_stone(depth: int, value: int):
	global stones, num
	while depth < LIMIT:
		depth += 1
		s = str(value)
		l = len(s)
		if l % 2 == 1:
			value *= 2024
		else:
			h = l // 2
			value, right = int(s[:h]), int(s[h:])
			if right == 0:
				stones.append((depth + 1, 1))
			else:
				stones.append((depth, right))
	num += 1

try:
	while True:
		d, v = stones.pop(0)
		if d >= LIMIT:
			num += 1
			continue
		handle_stone(d, v)
except IndexError:
	pass

print(num)
