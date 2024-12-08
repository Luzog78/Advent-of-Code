with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-07.txt') as f:
	input = f.read()

equations = [[int(e.split(': ')[0]),
					[int(v) for v in e.split(': ')[1].split(' ')]]
				for e in input.strip().split('\n')]

def solve(equations: list[list[int, list[int]]]) -> int:
	left, right = equations
	r_len = len(right) - 1
	operators = 0  # 0: *, 1: +
	max_op = 2 ** r_len

	def solve_eq():
		nonlocal operators
		while operators < max_op:
			result = right[0]
			i = 0
			while i < r_len:
				if operators & (1 << i):
					result = result + right[i + 1]
				else:
					result = result * right[i + 1]
				if result > left:
					break
				i += 1
			if result == left:
				return True
			operators += 1
		return False

	return solve_eq()

solved = [e[0] for e in equations if solve(e)]

print(sum(solved))
