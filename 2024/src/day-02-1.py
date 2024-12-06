with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-02.txt') as f:
	input = f.read()

reports = [[int(v) for v in line.split(' ') if v] for line in input.strip().split('\n')]
safe_count = 0

for r in reports:
	safe = True
	last = r[0]
	if r[1] - last > 0:
		for v in r[1:]:
			diff = v - last
			if diff < 1 or diff > 3:
				safe = False
				break
			last = v
	else:
		for v in r[1:]:
			diff = last - v
			if diff < 1 or diff > 3:
				safe = False
				break
			last = v
	if safe:
		safe_count += 1

print(safe_count)
