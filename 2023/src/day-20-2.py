from math import lcm
_inp = input

with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-20.txt') as f:
	input = f.read()

input = input.split('\n')

rules = {str(line.split(' -> ')[0][1:]): [line.split(' -> ')[0][0], line.split(' -> ')[1].split(', ')] for line in input}
rules = {k: [v[0], v[1], False if v[0] == '%' else {} if v[0] == '&' else None] for k, v in rules.items()}
rules['broadcaster'] = rules['roadcaster'].copy()
del rules['roadcaster']

for k, v in rules.items():
	for w in v[1]:
		if w in rules and rules[w][0] == '&':
			rules[w][2][k] = False

sent = [0, 0]

signals = []

def send(origin: str | None, wire: str, signal: bool):
	signals.append((origin, wire, signal))

def exec(origin: str | None, wire: str, signal: bool):
	'''
	:param signal: True if signal is high, False if signal is low
	'''
	global sent, end, cycles
	sent[0 if signal else 1] += 1
	if wire in rules and rules[wire][0] == '%':
		if not signal:
			rules[wire][2] = not rules[wire][2]
			for w in rules[wire][1]:
				send(wire, w, rules[wire][2])
	elif wire in rules and rules[wire][0] == '&':
		rules[wire][2][origin] = signal
		all_on = True
		for w in rules[wire][2].values():
			if not w:
				all_on = False
				break
		if all_on:
			for w in rules[wire][1]:
				send(wire, w, False)
		else:
			for w in rules[wire][1]:
				send(wire, w, True)
				if w == objective:
					rules[wire][-1][1] = False
	elif wire in rules and rules[wire][0] == 'b':
		for w in rules[wire][1]:
			send(wire, w, signal)

for k, v in rules.items():
	if 'rx' in v[1]:
		objective = k
		for w in v[2].keys():
			if w in rules and rules[w][0] == '&':
				rules[w] = [*rules[w], [0, True]]

presses = 0

end = False

while not end:
	presses += 1
	for w in rules[objective][2].keys():
		if w in rules and rules[w][-1][1]:
			rules[w][-1][0] += 1
	send('button', 'broadcaster', False)

	while signals:
		signal = signals.pop(0)
		exec(*signal)

	end = True
	for w in rules[objective][2].keys():
		if w in rules and rules[w][-1][1]:
			end = False
			break

# print([rules[w] for w in rules[objective][2]])
print(lcm(*[rules[w][-1][0] for w in rules[objective][2]]))
