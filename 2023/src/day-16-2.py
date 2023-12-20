with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-16.txt') as f:
	input = f.read()

input = input.split('\n')

mirr_map, light_map, beams = None, None, None

class Beam:
	def __init__(self, x, y, vx, vy):
		self.x = x
		self.y = y
		self.vx = vx
		self.vy = vy

	def move(self):
		light_map[self.y][self.x] += 1

		if mirr_map[self.y][self.x]:
			if mirr_map[self.y][self.x][-1] == '/':
				if self.vx == 1 and self.vy == 0:
					self.vx = 0
					self.vy = -1
				elif self.vx == 0 and self.vy == 1:
					self.vx = -1
					self.vy = 0
				elif self.vx == -1 and self.vy == 0:
					self.vx = 0
					self.vy = 1
				elif self.vx == 0 and self.vy == -1:
					self.vx = 1
					self.vy = 0
			elif mirr_map[self.y][self.x][-1] == '\\':
				if self.vx == 1 and self.vy == 0:
					self.vx = 0
					self.vy = 1
				elif self.vx == 0 and self.vy == 1:
					self.vx = 1
					self.vy = 0
				elif self.vx == -1 and self.vy == 0:
					self.vx = 0
					self.vy = -1
				elif self.vx == 0 and self.vy == -1:
					self.vx = -1
					self.vy = 0
			elif mirr_map[self.y][self.x][-1] == '-':
				if self.vx == 0 and self.vy != 0:
					self.vx = -1
					self.vy = 0
					beams.append(Beam(self.x, self.y, 1, 0))
					beams[-1].move()
			elif mirr_map[self.y][self.x][-1] == '|':
				if self.vx != 0 and self.vy == 0:
					self.vx = 0
					self.vy = -1
					beams.append(Beam(self.x, self.y, 0, 1))
					beams[-1].move()
			
			if self.vx == 1 and self.vy == 0:
				if mirr_map[self.y][self.x][0]:
					beams.remove(self)
					return
				mirr_map[self.y][self.x][0] = True
			elif self.vx == 0 and self.vy == 1:
				if mirr_map[self.y][self.x][1]:
					beams.remove(self)
					return
				mirr_map[self.y][self.x][1] = True
			elif self.vx == -1 and self.vy == 0:
				if mirr_map[self.y][self.x][2]:
					beams.remove(self)
					return
				mirr_map[self.y][self.x][2] = True
			elif self.vx == 0 and self.vy == -1:
				if mirr_map[self.y][self.x][3]:
					beams.remove(self)
					return
				mirr_map[self.y][self.x][3] = True

		self.x += self.vx
		self.y += self.vy

		if self.x < 0 or self.x >= len(mirr_map[0]) or self.y < 0 or self.y >= len(mirr_map):
			beams.remove(self)
			return
	
	def copy(self):
		return Beam(self.x, self.y, self.vx, self.vy)

	def __repr__(self):
		return f"Beam({self.x}, {self.y}, {self.vx}, {self.vy})"

simulations = [[Beam(0, y, 1, 0), 0] for y in range(len(input))] \
			+ [[Beam(x, 0, 0, 1), 0] for x in range(len(input[0]))] \
			+ [[Beam(len(input[0]) - 1, y, -1, 0), 0] for y in range(len(input))] \
			+ [[Beam(x, len(input) - 1, 0, -1), 0] for x in range(len(input[0]))]

for i in range(len(simulations)):
	mirr_map = [[[False, False, False, False, c] if c != '.' else None for c in l] for l in input]

	light_map = [[0 for _ in range(len(mirr_map[0]))] for _ in range(len(mirr_map))]

	beams = []

	beams.append(simulations[i][0].copy())

	while beams:
		for b in beams[:]:
			b.move()

	# for l1, l2 in zip(input, light_map):
	# 	print(l1, end=' ')
	# 	print(''.join(['#' if c else '.' for c in l2]))
	
	simulations[i][1] = sum(sum(1 if c > 0 else 0 for c in l) for l in light_map)

result = max(simulations, key=lambda s: s[1])
print(result[1])
