# coding: utf-8

"""
    Qase.io TestOps API v1

    Qase TestOps API v1 Specification.

    The version of the OpenAPI document: 1.0.0
    Contact: support@qase.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from src.qase.api_client_v1.api.runs_api import RunsApi


class TestRunsApi(unittest.TestCase):
    """RunsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RunsApi()

    def tearDown(self) -> None:
        pass

    def test_complete_run(self) -> None:
        """Test case for complete_run

        Complete a specific run
        """
        pass

    def test_create_run(self) -> None:
        """Test case for create_run

        Create a new run
        """
        pass

    def test_delete_run(self) -> None:
        """Test case for delete_run

        Delete run
        """
        pass

    def test_get_run(self) -> None:
        """Test case for get_run

        Get a specific run
        """
        pass

    def test_get_runs(self) -> None:
        """Test case for get_runs

        Get all runs
        """
        pass

    def test_update_run_publicity(self) -> None:
        """Test case for update_run_publicity

        Update publicity of a specific run
        """
        pass


if __name__ == '__main__':
    unittest.main()
