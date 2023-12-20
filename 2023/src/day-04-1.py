with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-04.txt') as f:
	input = f.read()

cards = input.split("\n")

cards = [card.split(":")[1].split("|") for card in cards]

points = [0] * len(cards)

for i in range(len(cards)):
	for j in range(len(cards[i])):
		cards[i][j] = list(filter(None, cards[i][j].strip().split(" ")))

for i in range(len(cards)):
	for nums in cards[i][1]:
		for winning_num in cards[i][0]:
			if nums == winning_num:
				if points[i] == 0:
					points[i] = 1
				else:
					points[i] *= 2

print(sum(points))
