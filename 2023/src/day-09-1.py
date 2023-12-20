with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-09.txt') as f:
	input = f.read()

history = [[[int(n) for n in l.split(" ")]] for l in input.split('\n')]

for i in range(len(history)):
	j = 0
	l = []
	while l.count(0) != len(l) or not l:
		l = []
		for k in range(len(history[i][j]) - 1):
			l.append(history[i][j][k + 1] - history[i][j][k])
		history[i].append(l)
		j += 1

for i in range(1, len(history) + 1):
	for j in range(1, len(history[-i]) + 1):
		if j == 1:
			history[-i][-j].append(0)
		else:
			history[-i][-j].append(history[-i][-j][-1] + history[-i][-j + 1][-1])

new_history = []

for h in history:
	new_history.append(h[0][-1])

print(sum(new_history))
