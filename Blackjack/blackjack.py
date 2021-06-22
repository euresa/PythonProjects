import random

class CardsException(Exception):
	def __init__(self):
		pass

class Deck:
	"""A class representing a standard deck of 52 playing cards."""

	def __init__(self):
		self.ranks = [str(r) for r in (2,3,4,5,6,7,8,9,10,"J", "Q", "K", "A")]
		self.rank_value = {"2":2,"3":3,"4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10,"J": 10,"Q": 10,"K": 10,"A": 11}
		self.suits = [chr(9824), chr(9825) , chr(9826) , chr(9827)]
		self.deck = self.new_deck

	@property
	def ranks(self):
		return self._ranks
	
	@ranks.setter
	def ranks(self, value):
		self._ranks = value

	@property
	def suits(self):
		return self._suits

	@suits.setter
	def suits(self, value):
		self._suits = value

	@property
	def new_deck(self):
		full_deck = [r+s for r in self.ranks for s in self.suits]
		random.shuffle(full_deck)
		return full_deck

	def shuffle(self):
		random.shuffle(self.deck)

	def draw(self, n=1):
		if n > len(self.new_deck):
			raise CardsException(f"Only {len(self.deck)} cards left in deck, but {n} were asked for.")

		cards_drew = []
		for _ in range(n):
			cards_drew.append(self.deck.pop())
		return cards_drew


class Player:
	def __init__(self, chips = 100):
		self.deck = Deck()
		self.round = 0
		self.chips = chips
		self.hand = []
		self.rank_value = {"2":2,"3":3,"4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10,"J": 10,"Q": 10,"K": 10,"A": 11}

	@property
	def hand(self):
		return self._hand

	@hand.setter
	def hand(self, value):
		self._hand = value

	@hand.deleter
	def hand(self):
		del self._hand

	@property
	def hand_value(self):
		return sum([self.rank_value[c[:-1]] for c in self.hand])

if __name__ == '__main__':
	print("""
###################################################
		Welcome to Blackjack!  


""")
	sam = Player()
	while True:
		sam.round += 1
		sam.hand = sam.deck.draw(2)



