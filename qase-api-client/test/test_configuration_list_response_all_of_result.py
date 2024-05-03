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

from src.qase.api_client_v1.models.configuration_list_response_all_of_result import ConfigurationListResponseAllOfResult

class TestConfigurationListResponseAllOfResult(unittest.TestCase):
    """ConfigurationListResponseAllOfResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigurationListResponseAllOfResult:
        """Test ConfigurationListResponseAllOfResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigurationListResponseAllOfResult`
        """
        model = ConfigurationListResponseAllOfResult()
        if include_optional:
            return ConfigurationListResponseAllOfResult(
                total = 56,
                filtered = 56,
                count = 56,
                entities = [
                    src.qase.api_client_v1.models.configuration_group.ConfigurationGroup(
                        id = 56, 
                        title = '', 
                        configurations = [
                            src.qase.api_client_v1.models.configuration.Configuration(
                                id = 56, 
                                title = '', )
                            ], )
                    ]
            )
        else:
            return ConfigurationListResponseAllOfResult(
        )
        """

    def testConfigurationListResponseAllOfResult(self):
        """Test ConfigurationListResponseAllOfResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
