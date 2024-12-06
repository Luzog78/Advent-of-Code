with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-05.txt') as f:
	input = f.read()

ordering, updates = input.strip().split('\n\n')

ordering = ordering.strip().split('\n')
ordering = [[int(v) for v in rule.split('|')] for rule in ordering]

updates = updates.strip().split('\n')
updates = [[int(v) for v in u.split(',')] for u in updates]

result = 0

for u in updates:
	d = {v: i for i, v in enumerate(u)}
	valid = True
	for o in ordering:
		if o[0] in u and o[1] in u:
			if d[o[0]] > d[o[1]]:
				valid = False
				break
	if valid:
		result += u[len(u) // 2]

print(result)
