with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-14.txt') as f:
	input = f.read()

input = input.split('\n')

plateform = [[c for c in l] for l in input]

results = []

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

for i, line in enumerate(plateform):
# 	print(''.join(line))
	results.append(line.count('O') * (len(plateform) - i))

print(sum(results))
