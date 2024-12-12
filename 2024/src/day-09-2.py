with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-09.txt') as f:
	input = f.read()

map = input.strip()

full: list[tuple[int, int, int]] = [] # (index, value, length)
free: list[tuple[int, int]] = [] # (index, length)

k = 0
for i, c in enumerate(map):
	ii = int(c)
	if ii == 0:
		continue
	if i % 2 == 0:
		full.append((k, i // 2, ii))
	else:
		free.append((k, ii))
	k += ii

for a, (k, v, l) in enumerate(full[::-1]):
	for b, (i, ii) in enumerate(free.copy()):
		if ii < l or i >= k:
			continue
		full.pop(-a - 1)
		free.pop(b)
		if ii > l:
			free.insert(b, (i + l, ii - l))
		full.append((i, v, l))
		break

result = 0
for k, v, l in full:
	for _ in range(l):
		result += v * k
		k += 1

print(result)
