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

from src.qase.api_client_v1.models.custom_field_create_value_inner import CustomFieldCreateValueInner

class TestCustomFieldCreateValueInner(unittest.TestCase):
    """CustomFieldCreateValueInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomFieldCreateValueInner:
        """Test CustomFieldCreateValueInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomFieldCreateValueInner`
        """
        model = CustomFieldCreateValueInner()
        if include_optional:
            return CustomFieldCreateValueInner(
                id = 56,
                title = ''
            )
        else:
            return CustomFieldCreateValueInner(
        )
        """

    def testCustomFieldCreateValueInner(self):
        """Test CustomFieldCreateValueInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()