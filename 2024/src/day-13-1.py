with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-13.txt') as f:
	input = f.read()

games: list[tuple[tuple[int, int], tuple[int, int], tuple[int, int]]] = [] # (button a, button b, prize)

for game in input.strip().split('\n\n'):
	button_a, button_b, prize = game \
		.replace('Button A: X+', '') \
		.replace('Button B: X+', '') \
		.replace('Prize: X=', '') \
		.replace(' Y+', '') \
		.replace(' Y=', '') \
		.split('\n')
	button_a = tuple(map(int, button_a.split(',')))
	button_b = tuple(map(int, button_b.split(',')))
	prize = tuple(map(int, prize.split(',')))

	games.append((button_a, button_b, prize))

def compute(ba: tuple[int, int], bb: tuple[int, int], pz: tuple[int, int]) -> int:
	best: int = 1e9
	a, b = 0, 0
	x, y = 0, 0
	while a <= 100:
		x = a * ba[0]
		y = a * ba[1]
		if x > pz[0] or y > pz[1]:
			break
		while x < pz[0] and y < pz[1] and b <= 100:
			x += bb[0]
			y += bb[1]
			if x > pz[0] or y > pz[1]:
				break
			b += 1
		if x == pz[0] and y == pz[1]:
			c = a * 3 + b
			if c < best:
				best = c
			break
		a += 1
		b = 0
	return best

costs: list[int] = []
for game in games:
	c = compute(*game)
	if c != 1e9:
		costs.append(c)

print(sum(costs))
