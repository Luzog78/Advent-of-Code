with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-22.txt') as f:
	input = f.read()

input = input.split('\n')

blocks = [[[int(n) for n in b.split(",")] for b in l.split("~")] + [False] for l in input]
blocks = [[b[0], b[1], b[2], [min(b[0][0], b[1][0]), min(b[0][1], b[1][1]), min(b[0][2], b[1][2])], [max(b[0][0], b[1][0]), max(b[0][1], b[1][1]), max(b[0][2], b[1][2])]] for b in blocks]
blocks.sort(key=lambda x: min(x[0][2], x[1][2]))

def fall(blocks: list[list[int, int, int], list[int, int, int], bool], check_stability: bool = True, return_on_change: bool = False):
	blocks_count = len(blocks)
	changed = {}
	i = 0
	while i < blocks_count:
		if check_stability and blocks[i][2]:
			i += 1
			continue
		x1, y1, z1 = blocks[i][-2]
		x2, y2, z2 = blocks[i][-1]
		if z1 <= 1:
			blocks[i][2] = True
			i += 1
			continue
		z1, z2 = z1 - 1, z2 - 1
		overlapping = False
		j = i - 1
		while j >= 0:
			xx1, yy1, zz1 = blocks[j][-2]
			xx2, yy2, zz2 = blocks[j][-1]

			if z2 >= zz1:
				if x1 <= xx2 and x2 >= xx1 and y1 <= yy2 and y2 >= yy1 and z1 <= zz2:
					overlapping = True
					break
			j -= 1
		if not overlapping:
			blocks[i][0][2] -= 1
			blocks[i][1][2] -= 1
			blocks[i][-2][2] -= 1
			blocks[i][-1][2] -= 1
			if i not in changed:
				changed[i] = 0
			changed[i] += 1
			if return_on_change:
				return changed
			i = max(-1, i - 3)
		else:
			blocks[i][2] = True
		i += 1
	return changed

fall(blocks)

falls = []

for i, b in enumerate(blocks):
	state = [[bb[0].copy(), bb[1].copy(), bb[2], bb[-2].copy(), bb[-1].copy()] for ii, bb in enumerate(blocks) if ii != i]
	falls.append(len(fall(state, False, False).keys()))

# A little slow, but it works :)
# (Slow about 160sec)
print(sum(falls))
