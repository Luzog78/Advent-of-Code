with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-04.txt') as f:
	input = f.read()

# input = '''MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX
# '''

input = input.strip().split('\n')
w, h = len(input[0]) - 1, len(input) - 1
count = 0

'''
X-MAS (MMSS) Patterns:
0.1
.A.
3.2
'''

def x_mas_0(x, y):
	return input[y - 1][x - 1] == 'M' \
			and input[y - 1][x + 1] == 'M' \
			and input[y + 1][x + 1] == 'S' \
			and input[y + 1][x - 1] == 'S'

def x_mas_1(x, y):
	return input[y - 1][x - 1] == 'S' \
			and input[y - 1][x + 1] == 'M' \
			and input[y + 1][x + 1] == 'M' \
			and input[y + 1][x - 1] == 'S'

def x_mas_2(x, y):
	return input[y - 1][x - 1] == 'S' \
			and input[y - 1][x + 1] == 'S' \
			and input[y + 1][x + 1] == 'M' \
			and input[y + 1][x - 1] == 'M'

def x_mas_3(x, y):
	return input[y - 1][x - 1] == 'M' \
			and input[y - 1][x + 1] == 'S' \
			and input[y + 1][x + 1] == 'S' \
			and input[y + 1][x - 1] == 'M'

def x_mas(x, y) -> int:
	return x_mas_0(x, y) \
			+ x_mas_1(x, y) \
			+ x_mas_2(x, y) \
			+ x_mas_3(x, y)

y = 1
while y < h:
	x = 1
	while x < w:
		if input[y][x] == 'A':
			count += x_mas(x, y)
		x += 1
	y += 1

print(count)
