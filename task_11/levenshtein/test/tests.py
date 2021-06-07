
import unittest
from Levenshtein import distance

from levenshtein import distance as my_distance


class LevenshteinTest(unittest.TestCase):
    def setUp(self):
        self.test_data = [
            ("", ""),
            ("", "qwd"),
            ("w", ""),
            ("a", "b"),
            ("import", "import"),
            ("import", "impaet"),
            ("importq", "import"),
            ("import", "imp"),
            ("impo", "import"),
            
        ]

    def test_dist(self):
        for dataset in self.test_data:
            self.assertEqual(
                my_distance(dataset[0], dataset[1]),
                distance(dataset[0], dataset[1])
            )
        