import unittest
import get_prefix_indexses as get_i

class test_get_indexses(unittest.TestCase):
	def test_get_indexses(self):
		self.assertEqual(get_i.get_indexses(["an", "circumstance", "circus", "devalue", "embrace", "forecast", "prefix",\
				 "predetermine", "pre-intermediate", "pre-teen", "superfood", "thermometer",\
				 "zen", "unicycled"], "cir"), (1, 2))
		self.assertEqual(get_i.get_indexses(["an", "circumstance", "circus", "devalue", "embrace", "forecast", "prefix",\
				 "predetermine", "pre-intermediate", "pre-teen", "superfood", "thermometer",\
				 "zen", "unicycled"], "damVan"), (-1, -1))
		self.assertEqual(get_i.get_indexses(["an", "circumstance", "circus", "devalue", "embrace", "forecast", "prefix",\
				 "predetermine", "pre-intermediate", "pre-teen", "superfood", "thermometer",\
				 "zen", "unicycled"], "an"), (0, 0))
		self.assertEqual(get_i.get_indexses(["an", "circumstance", "circus", "devalue", "embrace", "forecast", "prefix",\
				 "predetermine", "pre-intermediate", "pre-teen", "superfood", "thermometer",\
				 "zen", "unicycled"], "unicycled"), (13, 13))
		print("All tests passed")


if __name__ == '__main__':
	unittest.main()