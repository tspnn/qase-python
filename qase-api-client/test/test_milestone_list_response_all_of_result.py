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

from src.qase.api_client_v1.models.milestone_list_response_all_of_result import MilestoneListResponseAllOfResult

class TestMilestoneListResponseAllOfResult(unittest.TestCase):
    """MilestoneListResponseAllOfResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MilestoneListResponseAllOfResult:
        """Test MilestoneListResponseAllOfResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MilestoneListResponseAllOfResult`
        """
        model = MilestoneListResponseAllOfResult()
        if include_optional:
            return MilestoneListResponseAllOfResult(
                total = 56,
                filtered = 56,
                count = 56,
                entities = [
                    src.qase.api_client_v1.models.milestone.Milestone(
                        id = 56, 
                        title = '', 
                        description = '', 
                        status = 'completed', 
                        due_date = '2021-12-30T19:23:59Z', 
                        created = '2021-12-30 19:23:59', 
                        updated = '2021-12-30 19:23:59', 
                        created_at = '2021-12-30T19:23:59Z', 
                        updated_at = '2021-12-30T19:23:59Z', )
                    ]
            )
        else:
            return MilestoneListResponseAllOfResult(
        )
        """

    def testMilestoneListResponseAllOfResult(self):
        """Test MilestoneListResponseAllOfResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
