with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-05.txt') as f:
	input = f.read()

ordering, updates = input.strip().split('\n\n')

ordering = ordering.strip().split('\n')
ordering = [[int(v) for v in rule.split('|')] for rule in ordering]

updates = updates.strip().split('\n')
updates = [[int(v) for v in u.split(',')] for u in updates]

result = 0

def is_valid(u):
	d = {v: i for i, v in enumerate(u)}
	for o in ordering:
		if o[0] in u and o[1] in u:
			if d[o[0]] > d[o[1]]:
				return False
	return True

def arrange(u):
	u = u.copy()
	swapped = True
	while swapped:
		swapped = False
		d = {v: i for i, v in enumerate(u)}
		for o in ordering:
			if o[0] in u and o[1] in u:
				if d[o[0]] > d[o[1]]:
					u[d[o[0]]], u[d[o[1]]] = u[d[o[1]]], u[d[o[0]]]
					swapped = True
					break
	return u

for u in updates:
	if not is_valid(u):
		result += arrange(u)[len(u) // 2]

print(result)
