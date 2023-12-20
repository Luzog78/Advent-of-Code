from math import lcm

with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-08.txt') as f:
	input = f.read()

seq = input.split('\n\n')[0]

rules = input.split('\n\n')[1].split('\n')
rules = {rule.split(' = ')[0]: (*rule.split(' = ')[1][1:-1].split(', '),) for rule in rules}

locations = [loc for loc in rules.keys() if loc[-1] == 'A']
nb = [0] * len(locations)

def is_valid():
	for loc in locations:
		if loc[-1] != 'Z':
			return False
	return True

for l in range(len(locations)):
	seq_i = 0
	while locations[l][-1] != 'Z':
		locations[l] = rules[locations[l]][0 if seq[seq_i] == 'L' else 1]
		seq_i = (seq_i + 1) % len(seq)
		nb[l] += 1

print(lcm(*nb))
