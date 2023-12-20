with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-15.txt') as f:
	input = f.read()

input = input.split('\n')

words = input[0].split(',')

def hash(word):
	nb = 0
	for c in word:
		nb = ((nb + ord(c)) * 17) % 256
	return nb

results = [hash(word) for word in words]

print(sum(results))
