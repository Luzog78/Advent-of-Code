with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-04.txt') as f:
	input = f.read()

input = input.strip().split('\n')
w, h = len(input[0]), len(input)
count = 0

'''
XMAS Patterns:
5..6..7
.5.6.7.
..567..
444X000
..321..
.3.2.1.
3..2..1
'''

def xmas_0(x, y):
	if x + 3 >= w:
		return False
	return input[y][x + 1] == 'M' \
			and input[y][x + 2] == 'A' \
			and input[y][x + 3] == 'S'

def xmas_1(x, y):
	if x + 3 >= w or y + 3 >= h:
		return False
	return input[y + 1][x + 1] == 'M' \
			and input[y + 2][x + 2] == 'A' \
			and input[y + 3][x + 3] == 'S'

def xmas_2(x, y):
	if y + 3 >= h:
		return False
	return input[y + 1][x] == 'M' \
			and input[y + 2][x] == 'A' \
			and input[y + 3][x] == 'S'

def xmas_3(x, y):
	if x - 3 < 0 or y + 3 >= h:
		return False
	return input[y + 1][x - 1] == 'M' \
			and input[y + 2][x - 2] == 'A' \
			and input[y + 3][x - 3] == 'S'

def xmas_4(x, y):
	if x - 3 < 0:
		return False
	return input[y][x - 1] == 'M' \
			and input[y][x - 2] == 'A' \
			and input[y][x - 3] == 'S'

def xmas_5(x, y):
	if x - 3 < 0 or y - 3 < 0:
		return False
	return input[y - 1][x - 1] == 'M' \
			and input[y - 2][x - 2] == 'A' \
			and input[y - 3][x - 3] == 'S'

def xmas_6(x, y):
	if y - 3 < 0:
		return False
	return input[y - 1][x] == 'M' \
			and input[y - 2][x] == 'A' \
			and input[y - 3][x] == 'S'

def xmas_7(x, y):
	if x + 3 >= w or y - 3 < 0:
		return False
	return input[y - 1][x + 1] == 'M' \
			and input[y - 2][x + 2] == 'A' \
			and input[y - 3][x + 3] == 'S'

def xmas(x, y) -> int:
	return xmas_0(x, y) \
			+ xmas_1(x, y) \
			+ xmas_2(x, y) \
			+ xmas_3(x, y) \
			+ xmas_4(x, y) \
			+ xmas_5(x, y) \
			+ xmas_6(x, y) \
			+ xmas_7(x, y)

y = 0
while y < h:
	x = 0
	while x < w:
		if input[y][x] == 'X':
			count += xmas(x, y)
		x += 1
	y += 1

print(count)
