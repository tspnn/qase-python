# coding: utf-8

"""
    Qase.io TestOps API v2

    Qase TestOps API v2 Specification.

    The version of the OpenAPI document: 2.0.0
    Contact: support@qase.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ResultStepsType(str, Enum):
    """
    ResultStepsType
    """

    """
    allowed enum values
    """
    CLASSIC = 'classic'
    GHERKIN = 'gherkin'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ResultStepsType from a JSON string"""
        return cls(json.loads(json_str))

