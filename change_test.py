from change import AllPossibilitiesCoinChanger, MinimumCoinChanger, BooleanCoinChanger
import unittest

class AllPossibilitiesCoinChangerTest(unittest.TestCase):
	def test_change_for_zero(self):
		changer = AllPossibilitiesCoinChanger((1,3))
		self.assertChangeForAmountIs(changer, 0, (0,0))

	def test_change_for_one(self):
		changer = AllPossibilitiesCoinChanger((1,3))
		self.assertChangeForAmountIs(changer, 1, (1,0))

	def test_change_for_multiple(self):
		changer = AllPossibilitiesCoinChanger((1,3))
		self.assertChangeForAmountIs(changer, 3, (3,0), (0,1))

	def test_change_for_many(self):
		changer = AllPossibilitiesCoinChanger((1,3,4))
		self.assertChangeForAmountIs(changer, 6, (6,0,0), (3,1,0), (2,0,1), (0,2,0))

	def test_impossible_change(self):
		changer = AllPossibilitiesCoinChanger((3,5))
		self.assertChangeForAmountIs(changer, 4)
		self.assertChangeForAmountIs(changer, 2)

	def assertChangeForAmountIs(self, changer, amount, *values):
		actual_values = set(changer.change_for(amount))
		unordered_values = set(values)
		self.assertEquals(unordered_values, actual_values)
		self.assertEquals(len(values), len(unordered_values))


class MinimumCoinChangerTest(unittest.TestCase):
	def test_change_for_zero(self):
		changer = MinimumCoinChanger((1,3))
		self.assertChangeForAmountIs(changer, 0, (0,0))

	def test_change_for_one(self):
		changer = MinimumCoinChanger((1,3))
		self.assertChangeForAmountIs(changer, 1, (1,0))

	def test_change_for_multiple(self):
		changer = MinimumCoinChanger((1,3))
		self.assertChangeForAmountIs(changer, 3, (0,1))

	def test_change_for_many(self):
		changer = MinimumCoinChanger((1,3,4))
		self.assertChangeForAmountIs(changer, 6, (0,2,0))

	def test_impossible_change(self):
		changer = MinimumCoinChanger((3,5))
		self.assertNotChangeable(changer, 4)
		self.assertNotChangeable(changer, 2)

	def assertChangeForAmountIs(self, changer, amount, change):
		actual_change = list(changer.change_for(amount))
		self.assertEquals([change], actual_change)

	def assertNotChangeable(self, changer, amount):
		self.assertEquals([], list(changer.change_for(amount)))


class BooleanCoinChangerTest(unittest.TestCase):
	def test_change_for_zero(self):
		changer = BooleanCoinChanger((1,3))
		self.assertChangeable(changer, 0)

	def test_change_for_one(self):
		changer = BooleanCoinChanger((1,3))
		self.assertChangeable(changer, 1)

	def test_change_for_multiple(self):
		changer = BooleanCoinChanger((1,3))
		self.assertChangeable(changer, 3)

	def test_change_for_many(self):
		changer = BooleanCoinChanger((1,3,4))
		self.assertChangeable(changer, 6)

	def test_impossible_change(self):
		changer = BooleanCoinChanger((3,5))
		self.assertNotChangeable(changer, 4)
		self.assertNotChangeable(changer, 2)

	def assertChangeForAmountIs(self, changer, amount, expected_change):
		actual_change = list(changer.change_for(amount))
		self.assertEquals(expected_change, actual_change)

	def assertChangeable(self, changer, amount):
		self.assertChangeForAmountIs(changer, amount, [True])

	def assertNotChangeable(self, changer, amount):
		self.assertChangeForAmountIs(changer, amount, [])