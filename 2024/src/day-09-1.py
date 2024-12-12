with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-09.txt') as f:
	input = f.read()

map = input.strip()

i, j, k = 0, len(map) - 1, 0
if j % 2 == 1:
	j -= 1

result = 0

stack: list[int] = []

def fill_stack():
	global stack, map, j
	jj = int(map[j])
	for _ in range(jj):
		stack.append(j // 2)
	j -= 2

while i <= j:
	ii = int(map[i])
	for _ in range(ii):
		result += (i // 2) * k
		k += 1
	i += 1

	if i > j:
		break

	ii = int(map[i])
	while len(stack) < ii:
		fill_stack()
	for _ in range(ii):
		result += stack.pop(0) * k
		k += 1
	i += 1

for _ in range(len(stack)):
	result += stack.pop() * k
	k += 1

print(result)
