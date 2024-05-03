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

from src.qase.api_client_v1.models.defect_create import DefectCreate

class TestDefectCreate(unittest.TestCase):
    """DefectCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DefectCreate:
        """Test DefectCreate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DefectCreate`
        """
        model = DefectCreate()
        if include_optional:
            return DefectCreate(
                title = '',
                actual_result = '',
                severity = 56,
                milestone_id = 56,
                attachments = [
                    ''
                    ],
                custom_field = {
                    'key' : ''
                    },
                tags = [
                    ''
                    ]
            )
        else:
            return DefectCreate(
                title = '',
                actual_result = '',
                severity = 56,
        )
        """

    def testDefectCreate(self):
        """Test DefectCreate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
