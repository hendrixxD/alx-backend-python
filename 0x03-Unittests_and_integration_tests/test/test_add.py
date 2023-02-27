#!/usr/bin/env python3

import unittest

from Add import add


class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 2), 4)

if __name__ == '__main__':
    unittest.main()
