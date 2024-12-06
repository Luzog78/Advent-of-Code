with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-03.txt') as f:
	input = f.read()

NUMS = '0123456789'
result = 0
active = True
i = 0

def is_at(input: str, i: int, s: str) -> bool:
	return all(input[i + j] == s[j] for j in range(len(s)))

while i < len(input):
	if not active and is_at(input, i, 'do()'):
		i += 4
		active = True
	elif active and is_at(input, i, 'don\'t()'):
		i += 7
		active = False
	elif active and is_at(input, i, 'mul('):
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
