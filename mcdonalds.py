from itertools import count
from change import BooleanCoinChanger

class McDonalds(object):
	def __init__(self, denominations):
		self.denominations = denominations
		self.changer = BooleanCoinChanger(denominations)

	def is_changeable(self, amount):
		return any(True for _ in self.changer.change_for(amount))

	def list_non_changeable(self, maximum=None):
		numbers = count() if maximum is None else xrange(maximum+1)
		for n in numbers:
			if not self.is_changeable(n):
				yield n

	def list_changeable(self, maximum=None):
		numbers = count() if maximum is None else xrange(maximum+1)
		for n in numbers:
			if self.is_changeable(n):
				yield n


if __name__ == '__main__':
	mcd = McDonalds((6,9,20))

	for i in mcd.list_non_changeable():
		print i


