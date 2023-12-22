with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-02.txt') as f:
	input = f.read()

input = input.split('\n')

games = []

for line in input:
	i = int(line[5:].split(': ')[0])
	line = line[5:].split(': ')[1]
	g = [i, [0, 0, 0], 0]
	for e in line.split('; '):
		for f in e.split(', '):
			if f.split(' ')[1] == 'red':
				g[1][0] = max(g[1][0], int(f.split(' ')[0]))
			elif f.split(' ')[1] == 'green':
				g[1][1] = max(g[1][1], int(f.split(' ')[0]))
			elif f.split(' ')[1] == 'blue':
				g[1][2] = max(g[1][2], int(f.split(' ')[0]))
	g[2] = g[1][0] * g[1][1] * g[1][2]
	games.append(g)

print(sum(g[2] for g in games))
