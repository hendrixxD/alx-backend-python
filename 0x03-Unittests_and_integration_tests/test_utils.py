#!/usr/bin/python3
"""
paramitization
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Parameterize a unit test
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test the access_nested_map function
        with different input/output pairs.

        Parameters:
        -----------
        nested_map : dict
        The nested dictionary to test with.

        path : tuple
        The sequence of keys to access
        the nested value in the dictionary.

        expected_result : any
        The expected result from
        the access_nested_map function.

        Returns
        --------
        None. The test passes if the
        function returns the expected result.

        Raises:
        -------
        AssertionError: if the function
        returns a different value from the expected result.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)


if __name__ == '__main__':
    """
    main method
    """
    unittest.main()
