import random

def roll(number):
	dices = []
	for i in range(number):
		dices.append(random.randint(1,6))
	return dices

def evaluate(dices):
	add_score = 0

	if list(set(dices)) == [1,2,3,4,5,6]:
		add_score += 2000
		for n in range(1,7):
			dices.remove(n)

	if list(set(dices)) in [[1,2,3,4,5], [2,3,4,5,6]]:
		add_score += 1000
		for n in set(dices):
			dices.remove(n)

	for n in set(dices):
		if dices.count(n) >= 3:
			if n != 1:
				add_score += n*100*2**(dices.count(n)-3)
				while n in dices: dices.remove(n)
			else:
				add_score += n*1000*2**(dices.count(n)-3)
				while n in dices: dices.remove(n)

		elif n == 5:
			add_score += 50*dices.count(5)
			while n in dices: dices.remove(n)
		
		elif n == 1:
			add_score += 100*dices.count(1)	
			while n in dices: dices.remove(n)

	return add_score


while True:
	score = 0
	free_dices = 6
	in_game = True

	input("Press enter to roll.")

	while in_game:
		my_dices = roll(free_dices)
		print(my_dices)
		new_score = evaluate(my_dices)
		score += new_score

		if new_score == 0:
			print("You lost. Your score is 0. \n")
			in_game = False
			break

		print(score)

		waiting_for_input = True

		free_dices = len(my_dices)
		if free_dices == 0:
			input("Congratulations, you may roll all dices again! \n")
			free_dices = 6
			waiting_for_input = False
		else:
			my_input = input("Do you want to reroll %s? (y/n) \n" %my_dices)
				
		while waiting_for_input:
			if my_input.lower() == "y":
				free_dices = len(my_dices)
				waiting_for_input = False
			elif my_input.lower() == "n":
				in_game = False
				waiting_for_input = False
				print("You achieved a score of %s! \n" %score)
			else:
				my_input = input("Invalid Input. \n")
