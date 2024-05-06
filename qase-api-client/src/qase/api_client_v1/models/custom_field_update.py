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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from src.qase.api_client_v1.models.custom_field_create_value_inner import CustomFieldCreateValueInner
from typing import Optional, Set
from typing_extensions import Self

class CustomFieldUpdate(BaseModel):
    """
    CustomFieldUpdate
    """ # noqa: E501
    title: Annotated[str, Field(strict=True, max_length=255)]
    value: Optional[List[CustomFieldCreateValueInner]] = None
    replace_values: Optional[Dict[str, StrictStr]] = Field(default=None, description="Dictionary of old values and their replacemants")
    placeholder: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    default_value: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    is_filterable: Optional[StrictBool] = None
    is_visible: Optional[StrictBool] = None
    is_required: Optional[StrictBool] = None
    is_enabled_for_all_projects: Optional[StrictBool] = None
    projects_codes: Optional[List[StrictStr]] = None
    __properties: ClassVar[List[str]] = ["title", "value", "replace_values", "placeholder", "default_value", "is_filterable", "is_visible", "is_required", "is_enabled_for_all_projects", "projects_codes"]

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
        """Create an instance of CustomFieldUpdate from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in value (list)
        _items = []
        if self.value:
            for _item in self.value:
                if _item:
                    _items.append(_item.to_dict())
            _dict['value'] = _items
        # set to None if value (nullable) is None
        # and model_fields_set contains the field
        if self.value is None and "value" in self.model_fields_set:
            _dict['value'] = None

        # set to None if replace_values (nullable) is None
        # and model_fields_set contains the field
        if self.replace_values is None and "replace_values" in self.model_fields_set:
            _dict['replace_values'] = None

        # set to None if placeholder (nullable) is None
        # and model_fields_set contains the field
        if self.placeholder is None and "placeholder" in self.model_fields_set:
            _dict['placeholder'] = None

        # set to None if default_value (nullable) is None
        # and model_fields_set contains the field
        if self.default_value is None and "default_value" in self.model_fields_set:
            _dict['default_value'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CustomFieldUpdate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "value": [CustomFieldCreateValueInner.from_dict(_item) for _item in obj["value"]] if obj.get("value") is not None else None,
            "replace_values": obj.get("replace_values"),
            "placeholder": obj.get("placeholder"),
            "default_value": obj.get("default_value"),
            "is_filterable": obj.get("is_filterable"),
            "is_visible": obj.get("is_visible"),
            "is_required": obj.get("is_required"),
            "is_enabled_for_all_projects": obj.get("is_enabled_for_all_projects"),
            "projects_codes": obj.get("projects_codes")
        })
        return _obj

