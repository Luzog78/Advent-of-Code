with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-07.txt') as f:
	input = f.read()

hands = {(c.split(' ')[0], int(c.split(' ')[1])): 0 for c in input.split('\n')}

types = "J23456789TQKA"

def check_n_of_a_kind(hand, n):
	presents = []
	for type in types:
		count = 0
		J_used = 0
		if type != 'J':
			for card in hand[0]:
				if card == type:
					count += 1
		if count < n:
			for card in hand[0]:
				if card == 'J':
					J_used += 1
					count += 1
					if count == n:
						break
		if count >= n:
			presents.append((type, J_used))
	return presents

for h in list(hands.keys()):
	if check_n_of_a_kind(h, 5):
		hands[h] = 6
	elif check_n_of_a_kind(h, 4):
		hands[h] = 5
	else:
		threes = check_n_of_a_kind(h, 3)
		twos = check_n_of_a_kind(h, 2)
		Js = h[0].count('J')
		full_house = False
		if threes and twos:
			for t in threes:
				for u in twos:
					if t[0] != u[0] and t[1] + u[1] <= Js:
						full_house = True
		two_pairs = False
		if len(twos) >= 2:
			for i in range(len(twos)):
				for j in range(i + 1, len(twos)):
					if twos[i][0] != twos[j][0] and twos[i][1] + twos[j][1] <= Js:
						two_pairs = True
		if full_house:
			hands[h] = 4
		elif threes:
			hands[h] = 3
		elif two_pairs:
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

# print(hands)
# print(sorted_hands)

print(score)
