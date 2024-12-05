with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-01.txt') as f:
	input = f.read()

input = input.strip().split('\n')
list1, list2 = [], []

for l in input:
	v = l.split('   ')
	list1.append(int(v[0]))
	list2.append(int(v[1]))

print(f"{sum(v * list2.count(v) for v in list1)}")
