with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-01.txt') as f:
	input = f.read()

input = input.split('\n')

print(f"{sum(int(x[0]) * 10 + int(x[-1]) for x in (line.strip('abcdefghijklmnopqrstuvwxyz') for line in input))}")
