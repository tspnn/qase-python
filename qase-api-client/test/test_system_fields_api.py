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

from src.qase.api_client_v1.api.system_fields_api import SystemFieldsApi


class TestSystemFieldsApi(unittest.TestCase):
    """SystemFieldsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SystemFieldsApi()

    def tearDown(self) -> None:
        pass

    def test_get_system_fields(self) -> None:
        """Test case for get_system_fields

        Get all System Fields
        """
        pass


if __name__ == '__main__':
    unittest.main()
