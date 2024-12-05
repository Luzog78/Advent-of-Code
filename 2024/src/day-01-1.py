with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-01.txt') as f:
	input = f.read()

input = input.strip().split('\n')
list1, list2 = [], []

for l in input:
	v = l.split('   ')
	list1.append(int(v[0]))
	list2.append(int(v[1]))

list1 = sorted(list1)
list2 = sorted(list2)

print(f"{sum(abs(v1 - v2) for v1, v2 in zip(list1, list2))}")
