#!/usr/bin/env python3

import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    TestGithubOrgClient class to test the GithubOrgClient methods
    """

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json', return_value={"test": "test"})
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value.

        Parameters:
        - org_name (str): Name of the Github organization to test.

        Mocks:
        - get_json: Mocks the get_json function from the client module.

        Returns:
        - None
        """
        # Arrange
        github_org_client = GithubOrgClient(org_name)

        # Act
        org = github_org_client.org()

        # Assert
        mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(org, {"test": "test"})

    @patch.object(GithubOrgClient, 'org', return_value={
        "repos_url": "https://api.github.com/orgs/test_org/repos"})
    def test_public_repos_url(self, mock_org):
        """
        Test that GithubOrgClient._public_repos_url
        returns the correct value.

        Parameters:
        - mock_org (MagicMock):
            Mock of the GithubOrgClient.org method.

        Returns:
        - None
        """

        # Arrange
        github_org_client = GithubOrgClient("test_org")

        # Act
        public_repos_url = github_org_client._public_repos_url

        # Assert
        mock_org.assert_called_once()
        self.assertEqual(
                public_repos_url,
                "https://api.github.com/orgs/test_org/repos")

    @patch('client.get_json', return_value=[
        {"name": "repo1", "license": {"key": "test"}}, {"name": "repo2"}])
    @patch.object(GithubOrgClient, '_public_repos_url',
                  return_value="https://api.github.com/orgs/test_org/repos")
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """
        Test that GithubOrgClient.public_repos
        returns the correct list of repos.

        Parameters:
        - mock_public_repos_url (MagicMock):
            Mock of the GithubOrgClient._public_repos_url method.
        - mock_get_json (MagicMock): Mock of the
            get_json function from the client module.

        Returns:
        - None
        """
        # Arrange
        github_org_client = GithubOrgClient("test_org")

        # Act
        public_repos = github_org_client.public_repos(license="test")

        # Assert
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/test_org/repos")
        self.assertEqual(public_repos, ["repo1"])

    @parameterized.expand([
        [{"license": {"key": "my_license"}}, "my_license", True],
        [{"license": {"key": "other_license"}}, "my_license", False],
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test the has_license method"""

        result = GithubOrgClient.has_license(repo, license_key)

        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
