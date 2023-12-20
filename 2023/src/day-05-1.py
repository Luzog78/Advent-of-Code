with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-05.txt') as f:
	input = f.read()

input = input.split("\n\n")

seeds = [int(i) for i in input[0].split(" ")]
new_seeds = []

maps = [[[int(g) for g in f.split(" ")] for f in e.split("\n")] for e in input[1:]]

for s in seeds:
	for m in maps:
		for l in m:
			if l[1] <= s < l[1] + l[2]:
				s += l[0] - l[1]
				break
	new_seeds.append(s)

print(min(new_seeds))
