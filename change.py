# Given a set of denominations, yields all possible ways of obtaining a value.

from itertools import takewhile

def abstractMethod(): raise NotImplementedError('Abstract method')

class CoinChanger(object):
	def __init__(self, denominations):
		CoinChanger.verify_denominations(denominations)
		self.denominations = tuple(sorted(denominations))
		self.cache = dict()

	@staticmethod
	def verify_denominations(denominations):
		assert len(set(denominations)) == len(denominations)
		assert all(type(d) == int for d in denominations)
		assert all(d > 0 for d in denominations)

	def change_for(self, amount):
		if amount not in self.cache:
			self.cache[amount] = self._value_to_store_for_amount(self._change_for(amount))

		for change in self.cache[amount]:
			yield change

	def _change_for(self, amount):
		if amount == 0:
			yield self._get_value_for_zero_change()
			return

		for i, d in self.denominations_less_than_or_equal_to(amount):
			remaining_amount = amount - d
			for change in self.change_for(remaining_amount):
				yield self._get_change_for_denomination(change, d, i)

	def denominations_less_than_or_equal_to(self, amount):
		'''Yields (index, denomination)'''
		return takewhile(lambda (i, d): d <= amount, enumerate(self.denominations))

	def _get_value_for_zero_change(self):
		abstractMethod()

	def _get_change_for_denomination(self, change, denomination, denomination_index):
		abstractMethod()

	def _value_to_store_for_amount(self, value):
		abstractMethod()


class AllPossibilitiesCoinChanger(CoinChanger):
	def __init__(self, denominations):
		super(AllPossibilitiesCoinChanger, self).__init__(denominations)

	def _get_value_for_zero_change(self):
		return tuple([0] * len(self.denominations))

	def _get_change_for_denomination(self, change, denomination, denomination_index):
		new_change = list(change)
		new_change[denomination_index] += 1
		return tuple(new_change)

	def _value_to_store_for_amount(self, value):
		return list(value)


class MinimumCoinChanger(CoinChanger):
	def __init__(self, denominations):
		super(MinimumCoinChanger, self).__init__(denominations)

	def _get_value_for_zero_change(self):
		return tuple([0] * len(self.denominations))

	def _get_change_for_denomination(self, change, denomination, denomination_index):
		new_change = list(change)
		new_change[denomination_index] += 1
		return tuple(new_change)

	def _value_to_store_for_amount(self, value):
		try:
			return [ min(value, key=sum) ]
		except ValueError:
			return []


class BooleanCoinChanger(CoinChanger):
	def __init__(self, denominations):
		super(BooleanCoinChanger, self).__init__(denominations)

	def _get_value_for_zero_change(self):
		return True

	def _get_change_for_denomination(self, change, denomination, denomination_index):
		assert change == True
		return change

	def _value_to_store_for_amount(self, value):
		for v in value:
			return [ True ]
		else:
			return []
