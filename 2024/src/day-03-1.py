with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-03.txt') as f:
	input = f.read()

NUMS = '0123456789'
result = 0
i = 0

while i < len(input):
	if input[i] == 'm' and input[i + 1] == 'u' \
		and input[i + 2] == 'l' and input[i + 3] == '(':
		i += 4
		a, b = '', ''
		for _ in range(3):
			if input[i] in NUMS:
				a += input[i]
			else:
				break
			i += 1
		if not a or input[i] != ',':
			continue
		a = int(a)
		i += 1
		for _ in range(3):
			if input[i] in NUMS:
				b += input[i]
			else:
				break
			i += 1
		if not b or input[i] != ')':
			continue
		b = int(b)
		result += a * b
		i += 1
	else:
		i += 1

print(result)
