with open('/'.join(__file__.split('/')[:-2]) + '/inputs/day-04.txt') as f:
	input = f.read()

cards = input.split("\n")

cards = [card.split(":")[1].split("|") for card in cards]

cards_len = len(cards)

matches = [0] * (cards_len - 1)
copies = [1] * cards_len

for i in range(cards_len):
	for j in range(len(cards[i])):
		cards[i][j] = list(filter(None, cards[i][j].strip().split(" ")))

for i in range(cards_len - 1):
	for nums in cards[i][1]:
		for winning_num in cards[i][0]:
			if nums == winning_num:
				matches[i] += 1

for i, m in enumerate(matches):
	for _ in range(copies[i]):
		for j in range(m):
			copies[i + j + 1] += 1

print(sum(copies))
