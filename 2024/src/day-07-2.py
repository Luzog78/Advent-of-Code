with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-07.txt') as f:
	input = f.read()

equations = [[int(e.split(': ')[0]),
					[int(v) for v in e.split(': ')[1].split(' ')]]
				for e in input.strip().split('\n')]

def solve(equations: list[list[int, list[int]]], __: int = 1, _: int = 0) -> int:
	left, right = equations
	r_len = len(right) - 1
	operators = 0  # 0: ||, 1: *, 2: +
	max_op = 4 ** r_len

	print(f'[{_/__*100:0>5.2f}%] Solving {left} = {" ".join(str(r) for r in right)}: ', end='')

	def is_invalid():
		nonlocal operators
		i = 0
		while i < r_len:
			op = (operators & (3 << (i * 2))) >> (i * 2)
			if op == 3:
				return True
			i += 1
		return False

	def solve_eq():
		nonlocal operators
		while operators < max_op:
			result = right[0]
			i = 0
			while i < r_len:
				op = (operators & (3 << (i * 2))) >> (i * 2)
				if op == 2:
					result = result + right[i + 1]
				elif op == 1:
					result = result * right[i + 1]
				else:
					result = int(str(result) + str(right[i + 1]))
				if result > left:
					break
				i += 1
			if result == left:
				return True
			operators += 1
			while is_invalid():
				operators += 1
		return False

	solved = solve_eq()
	print('OK' if solved else 'FAIL')
	return solved


e_len = len(equations)
solved = [e[0] for i, e in enumerate(equations) if solve(e, e_len, i)]

print(solved)
print(sum(solved))
