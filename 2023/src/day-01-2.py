with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-01.txt') as f:
	input = f.read()

input = input.split('\n')

def replace(line: str):
	nums = [('one', 1), ('two', 2), ('three', 3), ('four', 4), ('five', 5), ('six', 6), ('seven', 7), ('eight', 8), ('nine', 9)]

	def find():
		nonlocal line
		for num, n in nums:
			if line[i:].find(str(n)) == 0:
				return True
			if line[i:].find(num) == 0:
				line = line[:i] + line[i:].replace(num, f"{n}", 1)
				True
		return False

	i = 0
	while i < len(line):
		if find():
			break
		i += 1

	i = len(line) - 1
	while i >= 0:
		if find():
			break
		i -= 1

	return line

print(f"{sum(int(x[0]) * 10 + int(x[-1]) for x in (replace(line[:]).strip('abcdefghijklmnopqrstuvwxyz') for line in input))}")
