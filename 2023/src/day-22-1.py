with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-22.txt') as f:
	input = f.read()

'''
input = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9"""
'''

input = input.split('\n')

blocks = [[[int(n) for n in b.split(",")] for b in l.split("~")] + [False] for l in input]
blocks = [[b[0], b[1], b[2], [min()], []] for b in blocks]
blocks.sort(key=lambda x: min(x[0][2], x[1][2]))

for b in blocks:
	print(b)
print()

def fall(blocks: list[list[int, int, int], list[int, int, int], bool], check_stability: bool = True):
	blocks_count = len(blocks)
	i = 0
	while i < blocks_count:
		if check_stability and blocks[i][2]:
			i += 1
			continue
		x1, y1, z1 = blocks[i][0]
		x2, y2, z2 = blocks[i][1]
		x1, y1, z1, x2, y2, z2 = min(x1, x2), min(y1, y2), min(z1, z2), max(x1, x2), max(y1, y2), max(z1, z2)
		if z1 <= 1:
			blocks[i][2] = True
			i += 1
			continue
		z1, z2 = z1 - 1, z2 - 1
		overlapping = False
		j = i - 1
		while j >= 0:
			xx1, yy1, zz1 = blocks[j][0]
			xx2, yy2, zz2 = blocks[j][1]
			xx1, yy2, zz2, xx2, yy2, zz2 = min(xx1, xx2), min(yy1, yy2), min(zz1, zz2), max(xx1, xx2), max(yy1, yy2), max(zz1, zz2)
			
			if zz2 > z1:
				break
			for _x in range(xx1, xx2 + 1):
				for _y in range(yy1, yy2 + 1):
					for _z in range(zz1, zz2 + 1):
						if x1 <= _x <= x2 and y1 <= _y <= y2 and z1 <= _z <= z2:
							overlapping = True
							break
					if overlapping:
						break
				if overlapping:
					break
			if overlapping:
				break
			j -= 1
		if not overlapping:
			blocks[i][0][2] -= 1
			blocks[i][1][2] -= 1
			i = max(-1, i - 3)
		else:
			blocks[i][2] = True
		i += 1

fall(blocks)

for b in blocks:
	print(b)
print()

print("FELLLLL")

can_be_removed = []

for i, b in enumerate(blocks):
	old_state = [[bb[0].copy(), bb[1].copy(), bb[2]] for ii, bb in enumerate(blocks) if ii != i]
	new_state = [[bb[0].copy(), bb[1].copy(), bb[2]] for ii, bb in enumerate(blocks) if ii != i]
	fall(new_state, False)
	if old_state == new_state:
		print(f"Block {i} can be removed ({b})")
		can_be_removed.append(i)
	else:
		print(f"Block {i} cannot be removed ({b}):")
		for i, (a, b) in enumerate(zip(old_state, new_state)):
			print(i, a, b, "<<<<<<<" if a != b else "")

print(len(can_be_removed))
