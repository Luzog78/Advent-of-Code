with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-02.txt') as f:
	input = f.read()

reports = [[int(v) for v in line.split(' ') if v] for line in input.strip().split('\n')]
safe_count = 0

def is_safe(r: list):
	last = r[0]
	if r[1] - last > 0:
		for v in r[1:]:
			diff = v - last
			if diff < 1 or diff > 3:
				return False
			last = v
	else:
		for v in r[1:]:
			diff = last - v
			if diff < 1 or diff > 3:
				return False
			last = v
	return True

for r in reports:
	if is_safe(r):
		safe_count += 1
	else:
		for i in range(len(r)):
			copy = r.copy()
			copy.pop(i)
			if is_safe(copy):
				safe_count += 1
				break

print(safe_count)
