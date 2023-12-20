with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-07.txt') as f:
	input = f.read()

hands = {(c.split(' ')[0], int(c.split(' ')[1])): 0 for c in input.split('\n')}

types = "23456789TJQKA"

def check_n_of_a_kind(hand, n):
	presents = ""
	for type in types:
		count = 0
		for card in hand[0]:
			if card == type:
				count += 1
		if count >= n:
			presents += type
	return presents

for h in list(hands.keys()):
	if check_n_of_a_kind(h, 5):
		hands[h] = 6
	elif check_n_of_a_kind(h, 4):
		hands[h] = 5
	else:
		threes = check_n_of_a_kind(h, 3)
		twos = check_n_of_a_kind(h, 2)
		if threes and twos and threes.replace(twos, ""):
			hands[h] = 4
		elif threes:
			hands[h] = 3
		elif len(twos) >= 2:
			hands[h] = 2
		elif twos:
			hands[h] = 1
		else:
			hands[h] = 0

def atoi_base(s):
	i = 0
	for c in s:
		i *= len(types)
		i += types.index(c)
	return i

def sort_hands(hands):
	tab = [(atoi_base(h[0]), h[0], h[1]) for h in hands]
	tab.sort(key=lambda x: x[0])
	return [(h[1], h[2]) for h in tab]

sorted_hands = []

for r in range(max(hands.values()) + 1):
	for h in sort_hands(h for h in hands if hands[h] == r):
		sorted_hands.append(h)

score = 0

for rank, (cards, bid) in enumerate(sorted_hands):
	score += (rank + 1) * bid

print(score)
