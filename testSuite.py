import unittest
from DistanceTable import *

class TestDistanceTable(unittest.TestCase):
	
	def test_not_a_valid_file(self):
		'''Test to make sure an IOError is raised for an invalid file name'''
		with self.assertRaises(FileNotFoundError):
			DistanceTable.readCSV(self, 'does-not-exist.csv')
		#self.assertRaises(IOError, DistanceTable.readCSV, 'does-not-exist.csv')

	def test_get_a_saved_distance(self):
	#	self.assertEquals()
		pass

	def test_get_a_distance_not_yet_calculated(self):
		pass

	def test_add_a_new_value_to_table(self):
		pass


	#def test_save_

if __name__ == '__main__':
    unittest.main()