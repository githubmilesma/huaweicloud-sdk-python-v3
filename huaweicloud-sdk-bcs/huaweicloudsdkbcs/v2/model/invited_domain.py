# coding: utf-8

import pprint
import re

import six





class InvitedDomain:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'invited_user': 'str'
    }

    attribute_map = {
        'invited_user': 'invited_user'
    }

    def __init__(self, invited_user=None):
        """InvitedDomain - a model defined in huaweicloud sdk"""
        
        

        self._invited_user = None
        self.discriminator = None

        self.invited_user = invited_user

    @property
    def invited_user(self):
        """Gets the invited_user of this InvitedDomain.

        被邀请方租户，hcs模式下是邀请方的租户ID

        :return: The invited_user of this InvitedDomain.
        :rtype: str
        """
        return self._invited_user

    @invited_user.setter
    def invited_user(self, invited_user):
        """Sets the invited_user of this InvitedDomain.

        被邀请方租户，hcs模式下是邀请方的租户ID

        :param invited_user: The invited_user of this InvitedDomain.
        :type: str
        """
        self._invited_user = invited_user

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
        if not isinstance(other, InvitedDomain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
