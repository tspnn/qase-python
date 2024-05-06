# coding: utf-8

"""
    Qase.io TestOps API v1

    Qase TestOps API v1 Specification.

    The version of the OpenAPI document: 1.0.0
    Contact: support@qase.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class TestStepResultCreate(BaseModel):
    """
    TestStepResultCreate
    """ # noqa: E501
    position: Optional[StrictInt] = None
    status: StrictStr
    comment: Optional[StrictStr] = None
    attachments: Optional[List[StrictStr]] = None
    action: Optional[StrictStr] = None
    expected_result: Optional[StrictStr] = None
    data: Optional[StrictStr] = None
    steps: Optional[List[Dict[str, Any]]] = Field(default=None, description="Nested steps results may be passed here. Use same structure for them.")
    __properties: ClassVar[List[str]] = ["position", "status", "comment", "attachments", "action", "expected_result", "data", "steps"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['passed', 'failed', 'blocked']):
            raise ValueError("must be one of enum values ('passed', 'failed', 'blocked')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TestStepResultCreate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if comment (nullable) is None
        # and model_fields_set contains the field
        if self.comment is None and "comment" in self.model_fields_set:
            _dict['comment'] = None

        # set to None if attachments (nullable) is None
        # and model_fields_set contains the field
        if self.attachments is None and "attachments" in self.model_fields_set:
            _dict['attachments'] = None

        # set to None if expected_result (nullable) is None
        # and model_fields_set contains the field
        if self.expected_result is None and "expected_result" in self.model_fields_set:
            _dict['expected_result'] = None

        # set to None if data (nullable) is None
        # and model_fields_set contains the field
        if self.data is None and "data" in self.model_fields_set:
            _dict['data'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TestStepResultCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "position": obj.get("position"),
            "status": obj.get("status"),
            "comment": obj.get("comment"),
            "attachments": obj.get("attachments"),
            "action": obj.get("action"),
            "expected_result": obj.get("expected_result"),
            "data": obj.get("data"),
            "steps": obj.get("steps")
        })
        return _obj

