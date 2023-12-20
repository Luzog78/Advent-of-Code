with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-19.txt') as f:
	input = f.read()

def make_rule(input):
	rule = [[], None]
	for r in input.split(',')[:-1]:
		r = r.split(':')
		char = r[0][0]
		comp = r[0][1]
		value = int(r[0][2:])
		to = r[1]
		i = 0 if char == 'x' else 1 if char == 'm' else 2 if char == 'a' else 3
		rule[0].append((i, comp, value, to))
	rule[1] = input.split(',')[-1]
	return rule

rules = input.split('\n\n')[0].split('\n')
rules = {rule.split('{')[0]: make_rule(rule.split('{')[1][:-1]) for rule in rules}

parts = input.split('\n\n')[1].split('\n')
parts = [tuple(int(e) for e in part[1:-1].replace("=", "").replace("x", "")
			.replace("m", "").replace("a", "").replace("s", "").split(',')) for part in parts]

accepted = []

for i in range(len(parts)):
	rule = rules['in']
	while True:
		next = rule[1]
		for r in rule[0]:
			if (r[1] == '<' and parts[i][r[0]] < r[2]) \
				or (r[1] == '>' and parts[i][r[0]] > r[2]):
				next = r[3]
				break
		if next == 'R':
			break
		if next == 'A':
			accepted.append(parts[i])
			break
		rule = rules[next]

print(sum(sum(part) for part in accepted))
