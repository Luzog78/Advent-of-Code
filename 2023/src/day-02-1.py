with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-02.txt') as f:
	input = f.read()

input = input.split('\n')

incorrec_ids = set()

for line in input:
	i = int(line[5:].split(": ")[0])
	line = line[5:].split(": ")[1]
	for e in line.split("; "):
		for f in e.split(", "):
			if (f.split(" ")[1] == "red" and int(f.split(" ")[0]) > 12) \
				or (f.split(" ")[1] == "green" and int(f.split(" ")[0]) > 13) \
				or (f.split(" ")[1] == "blue" and int(f.split(" ")[0]) > 14):
				incorrec_ids.add(i)

sum = 0

for line in input:
	i = int(line[5:].split(": ")[0])
	if i not in incorrec_ids:
		sum += i

print(sum)
