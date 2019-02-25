# coding: utf-8

from bitmovin_python.models.input_type import InputType
import pprint
import six
from datetime import datetime
from enum import Enum


class InputTypeResponse(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = {
            'type': 'InputType'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'type': 'type'
        }
        return attributes

    def __init__(self, type=None, *args, **kwargs):

        self._type = None
        self.discriminator = None

        if type is not None:
            self.type = type

    @property
    def type(self):
        """Gets the type of this InputTypeResponse.

        The type of the input

        :return: The type of this InputTypeResponse.
        :rtype: InputType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InputTypeResponse.

        The type of the input

        :param type: The type of this InputTypeResponse.
        :type: InputType
        """

        if type is not None:
            if not isinstance(type, InputType):
                raise TypeError("Invalid type for `type`, type has to be `InputType`")

            self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map.get(attr)] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[self.attribute_map.get(attr)] = value
            if issubclass(InputTypeResponse, dict):
                for key, value in self.items():
                    result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InputTypeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other