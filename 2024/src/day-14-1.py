with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-14.txt') as f:
	input = f.read()

cycles = 100
w, h = 101, 103
robots = [[tuple(map(int, v.split(','))) for v in l.split(' ')]
		for l in input.strip().replace('p=', '').replace('v=', '').split('\n')]

safety_factors = [0, 0, 0, 0]

l = len(robots)
hx, hy = w // 2, h // 2

for i in range(l - 1, -1, -1):
	r = robots[i]
	px, py = r[0]
	vx, vy = r[1]

	px = (px + vx * cycles) % w
	py = (py + vy * cycles) % h

	if px < hx and py < hy:
		safety_factors[0] += 1
	elif px > hx and py < hy:
		safety_factors[1] += 1
	elif px > hx and py > hy:
		safety_factors[2] += 1
	elif px < hx and py > hy:
		safety_factors[3] += 1

safety_factor = safety_factors[0] * safety_factors[1] \
				* safety_factors[2] * safety_factors[3]

print(safety_factor)
