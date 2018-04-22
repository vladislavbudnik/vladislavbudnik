import random

class Player():
	def __init__(self):
		self.card = []

	def addCard(self):
		self.card.append(random.randint(1, 11))

	def getValue(self):
		return sum(self.card)

class Bot():
	def __init__(self):
		self.card = []

	def addCard(self):
		self.card.append(random.randint(1,11))

	def getValue(self):
		return sum(self.card)

	def change(self):
		change = random.randint(1,2)
		if(change == 1):
			self.addCard()

def main():
	player = Player()
	bot = Bot()
	print("="*20 + "\nGame start")
	while(True):
		print("="*20)
		print("The sum of your cards is " + str(player.getValue()))
		change = input("Want to take more? (y/n) ")
		if(change == "y"):
			player.addCard()
		bot.change()
		if((player.getValue() == 21) or (bot.getValue() == 21)):
			if(player.getValue() == 21):
				print("="*20 + "\nPlayer win")
				print("Bot lose\nGame end" + "\n" + "="*20)
			else:
				print("="*20 + "\nBot win")
				print("Player lose\nGame end" + "\n" + "="*20)
			break
		elif((player.getValue() > 21) or (bot.getValue() > 21)):
			if(player.getValue() > 21):
				print("="*20 + "\nPlayer lose")
				print("Bot win\nGame end" + "\n" + "="*20)
			else:
				print("="*20 + "\nBot lose")
				print("Player win\nGame end" + "\n" + "="*20)
			break

if __name__ == "__main__":
    main()
