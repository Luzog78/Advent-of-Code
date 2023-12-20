with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-03.txt') as f:
	input = f.read()

tab = input.split("\n")

surrounded = []
nums = []

def is_surrounded(i, j):
	if i < 0 or j < 0 or i >= len(tab) or j >= len(tab[i]):
		return False

	for k in range(-1, 2):
		for l in range(-1, 2):
			if i + k < 0 or j + l < 0 \
				or i + k >= len(tab) or j + l >= len(tab[i + k]):
				pass
			elif tab[i + k][j + l] != "." and not tab[i + k][j + l].isdigit():
				return True

	return False

def parse(i, j):
	num = ""
	while j < len(tab[i]) and tab[i][j].isdigit():
		for s in surrounded[:]:
			if s[0] == i and s[1] == j:
				surrounded.remove(s)
		num += tab[i][j]
		j += 1
	
	return int(num)

for i in range(len(tab)):
	for j in range(len(tab[i])):
		if tab[i][j].isdigit() and is_surrounded(i, j):
			surrounded.append((i, j))

while len(surrounded):
	i, j = surrounded[0]
	while j > 0 and tab[i][j - 1].isdigit():
		j -= 1
	nums.append(parse(i, j))

print(sum(nums))
