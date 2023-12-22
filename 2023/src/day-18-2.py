import sys
sys.setrecursionlimit(2147483647)

with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-18.txt') as f:
	input = f.read()

input = input.split('\n')

moves = [(int(l.split(' ')[2][2:-2], base=16), l.split(' ')[2][-2:-1]) for l in input]

pos = [0, 0]

positions = [tuple(pos)]

perimeter = 0

for dist, dir in moves:
	step = None
	if dir == '3':
		step = [0, 1]
	elif dir == '1':
		step = [0, -1]
	elif dir == '2':
		step = [-1, 0]
	elif dir == '0':
		step = [1, 0]
	perimeter += dist
	pos[0] += step[0] * dist
	pos[1] += step[1] * dist
	positions.append(tuple(pos))

# See https://en.wikipedia.org/wiki/Shoelace_formula
result = int(abs(sum(positions[i][0] * positions[i + 1][1] - positions[i + 1][0] * positions[i][1] for i in range(len(positions) - 1))) / 2)
result += int(perimeter / 2) + 1

print(result)
