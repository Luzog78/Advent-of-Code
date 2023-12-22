with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-03.txt') as f:
	input = f.read()

tab = input.split('\n')

gears = []

for i in range(len(tab)):
	for j in range(len(tab[i])):
		if tab[i][j] == '*':
			gears.append((i, j))

ratios = []

def get_num(point):
	i, j = point
	while j > 0 and tab[i][j - 1].isdigit():
		j -= 1
	num = ''
	while j < len(tab[i]) and tab[i][j].isdigit():
		num += tab[i][j]
		j += 1
	return int(num)

for i, j in gears:
	nums = []

	if j > 0 and tab[i][j - 1] in '0123456789':
		nums.append((i, j - 1))
	if j < len(tab[i]) - 1 and tab[i][j + 1] in '0123456789':
		nums.append((i, j + 1))

	for off in [-1, 1]:
		tmp = [None, None, None]
		if i > 0 and tab[i + off][j - 1] in '0123456789':
			tmp[0] = (i + off, j - 1)
		if i > 0 and tab[i + off][j] in '0123456789':
			tmp[1] = (i + off, j)
		if i > 0 and tab[i + off][j + 1] in '0123456789':
			tmp[2] = (i + off, j + 1)
		if tmp.count(None) == 0:
			nums.append(tmp[0])
		elif tmp.count(None) == 1:
			if tmp[0] is None:
				nums.append(tmp[1])
			else:
				nums.append(tmp[0])
				if tmp[1] is None:
					nums.append(tmp[2])
		elif tmp.count(None) == 2:
			if tmp[0] is not None:
				nums.append(tmp[0])
			elif tmp[1] is not None:
				nums.append(tmp[1])
			else:
				nums.append(tmp[2])

	if len(nums) == 2:
		num1, num2 = get_num(nums[0]), get_num(nums[1])
		ratios.append(num1 * num2)

print(sum(ratios))
