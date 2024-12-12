from functools import cache

with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-12.txt') as f:
	input = f.read()

presets = [('?'.join([l.split(' ')[0]] * 5), tuple(int(e) for e in ','.join([l.split(' ')[1]] * 5).split(','))) for l in input.split('\n')]

results = []

def get_nums(current, raw=False):
	nums = []
	counter = 0

	for c in current:
		if c == '?':
			break
		if c == '#':
			counter += 1
		elif counter:
			nums.append(counter)
			counter = 0
	if counter and not raw:
		nums.append(counter)

	if raw:
		return nums, counter
	return nums

def is_solved(preset, current):
	if '?' in current:
		return False

	nums = get_nums(current)

	if len(preset) != len(nums):
		return False
	for p, n in zip(preset, nums):
		if p != n:
			return False

	return True

@cache
def calc_nb_arrangements(preset, current):
	if '?' not in current:
		return 1 if is_solved(preset, current) else 0

	nums, counter = get_nums(current, True)

	if len(nums) > len(preset):
		return 0
	for p, n in zip(preset[:len(nums)], nums):
		if p != n:
			return 0
	if counter and (len(nums) >= len(preset) or preset[len(nums)] < counter):
		return 0

	i = current.find('?')
	res = 0

	current = current[:i] + '#' + current[i + 1:]
	res += calc_nb_arrangements(preset, current)
	current = current[:i] + '.' + current[i + 1:]
	res += calc_nb_arrangements(preset, current)

	return res

i = 0
for s, p in presets:
	# print(i, "out of", len(presets), f"({i / len(presets) * 100}%)  {s} {','.join(str(e) for e in p)}")
	i += 1
	results.append(calc_nb_arrangements(p, str(s)))

print(sum(results))
