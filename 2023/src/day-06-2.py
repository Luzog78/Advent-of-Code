with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-06.txt') as f:
	input = f.read()

times = [int(input.split('\n')[0].split(":")[1].replace(" ", ""))]
distances = [int(input.split('\n')[1].split(":")[1].replace(" ", ""))]

scores = [0] * len(times)

for i in range(len(times)):
	for x in range(times[i]):
		if -x**2 + times[i]*x > distances[i]:
			scores[i] += 1

score = 1
for s in scores:
	score *= s

print(score)
