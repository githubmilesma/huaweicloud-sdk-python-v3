# coding: utf-8

import pprint
import re

import six





class ChangeOsMetadata:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'user_data': 'str'
    }

    attribute_map = {
        'user_data': 'user_data'
    }

    def __init__(self, user_data=None):
        """ChangeOsMetadata - a model defined in huaweicloud sdk"""
        
        

        self._user_data = None
        self.discriminator = None

        if user_data is not None:
            self.user_data = user_data

    @property
    def user_data(self):
        """Gets the user_data of this ChangeOsMetadata.

        切换边缘实例操作系统过程中注入的用户数据。

        :return: The user_data of this ChangeOsMetadata.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this ChangeOsMetadata.

        切换边缘实例操作系统过程中注入的用户数据。

        :param user_data: The user_data of this ChangeOsMetadata.
        :type: str
        """
        self._user_data = user_data

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ChangeOsMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other