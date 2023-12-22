with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-14.txt') as f:
	input = f.read()

input = input.split('\n')

plateform = [[c for c in l] for l in input]

results = []

def north():
	global plateform
	for x in range(len(plateform[0])):
		old = None
		y = 0
		while y < len(plateform):
			if plateform[y][x] == 'O' and old == '.':
				plateform[y][x] = '.'
				plateform[y-1][x] = 'O'
				old = None
				y = max(0, y - 2)
				continue
			old = plateform[y][x]
			y += 1

def south():
	global plateform
	for x in range(len(plateform[0])):
		old = None
		y = len(plateform) - 1
		while y >= 0:
			if plateform[y][x] == 'O' and old == '.':
				plateform[y][x] = '.'
				plateform[y+1][x] = 'O'
				old = None
				y = min(len(plateform) - 1, y + 2)
				continue
			old = plateform[y][x]
			y -= 1

def east():
	global plateform
	for y in range(len(plateform)):
		old = None
		x = len(plateform[0]) - 1
		while x >= 0:
			if plateform[y][x] == 'O' and old == '.':
				plateform[y][x] = '.'
				plateform[y][x+1] = 'O'
				old = None
				x = min(len(plateform[0]) - 1, x + 2)
				continue
			old = plateform[y][x]
			x -= 1

def west():
	global plateform
	for y in range(len(plateform)):
		old = None
		x = 0
		while x < len(plateform[0]):
			if plateform[y][x] == 'O' and old == '.':
				plateform[y][x] = '.'
				plateform[y][x-1] = 'O'
				old = None
				x = max(0, x - 2)
				continue
			old = plateform[y][x]
			x += 1

memory = []

i = 0
while i < 1000000:
	# print(f"Step {i} out of 1000000 ({i / 1000000 * 100:.2f}%)")
	north()
	west()
	south()
	east()
	i += 1
	if plateform in memory:
		# print(f"Loop found at step {i} !")
		first = memory.index(plateform)
		length = len(memory[first:])
		plateform = memory[(1000000000 - i) % length + first]
		break
	else:
		memory.append([list(l) for l in plateform])

for i, line in enumerate(plateform):
	# print(''.join(line))
	results.append(line.count('O') * (len(plateform) - i))

print(sum(results))
