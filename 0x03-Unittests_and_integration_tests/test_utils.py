#!/usr/bin/env python3

import unittest
from utils import memoize
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, memoize, get_json


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
        """Test that access_nested_map returns expected result."""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that a KeyError is raised for invalid key."""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Mock HTTP calls
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test that get_json returns expected result."""
        # Create mock object with json method that returns test_payload
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        # Set mock object as return value of patched requests.get
        mock_get.return_value = mock_response
        # Call get_json and assert expected output
        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        # Assert that mocked get method was called once with test_url
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Test class for the memoize decorator
    """
    def test_memoize(self):
        """
        Test method to test the memoize decorator
        """
        class TestClass:
            """
            test class
            """
            def a_method(self):
                """
                balablu
                """
                return 42

            @memoize
            def a_property(self):
                """
                a_propety
                """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            test_obj = TestClass()
            result1 = test_obj.a_property()
            result2 = test_obj.a_property()
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()
