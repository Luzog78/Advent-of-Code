with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-08.txt') as f:
	input = f.read()

seq = input.split('\n\n')[0]
seq_i = 0

rules = input.split('\n\n')[1].split('\n')
rules = {rule.split(' = ')[0]: (*rule.split(' = ')[1][1:-1].split(', '),) for rule in rules}

location = 'AAA'
nb = 0

while location != 'ZZZ':
	location = rules[location][0 if seq[seq_i] == 'L' else 1]
	seq_i = (seq_i + 1) % len(seq)
	nb += 1

print(nb)
