import os
import sys
import inspect
import unittest

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from AOCDay102 import possibleMove
from AOCDay102 import getNextMove
from AOCDay102 import getNextCoorPosition

class TestStringMethods(unittest.TestCase):
	def test_getNextMove3040(self):
		self.assertEqual(getNextMove(['3', '0'], ['4', '0']), 'r')
	
	def test_getNextMove4041(self):
		self.assertEqual(getNextMove(['4', '0'], ['4', '1']), 'u')

	def test_possibleMove3040(self):
		self.assertTrue(possibleMove(['3', '0'], ['4', '0']))

	def test_possibleMove3031(self):
		self.assertFalse(possibleMove(['3', '0'], ['3', '1']))

	def test_possibleMove4142(self):
		self.assertFalse(possibleMove(['4', '1'], ['4', '2']))
	
	def test_possibleMove4041(self):
		self.assertTrue(possibleMove(['4', '0'], ['4', '1']))
	
	def test_possibleMove3233(self):
		self.assertTrue(possibleMove(['3', '2'], ['3', '3']))

	def test_getNextCoorPosition4041(self):
		self.assertEqual(getNextCoorPosition(['4', '0'], ['4', '1']), ['3', '1'])
	
if __name__ == '__main__':
    unittest.main(verbosity=2)