# coding: utf-8

import pprint
import re

import six





class ListDeploymentsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'status': 'str',
        'id': 'str',
        'edgecloud_id': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'status': 'status',
        'id': 'id',
        'edgecloud_id': 'edgecloud_id'
    }

    def __init__(self, offset=None, limit=None, status=None, id=None, edgecloud_id=None):
        """ListDeploymentsRequest - a model defined in huaweicloud sdk"""
        
        

        self._offset = None
        self._limit = None
        self._status = None
        self._id = None
        self._edgecloud_id = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if status is not None:
            self.status = status
        if id is not None:
            self.id = id
        if edgecloud_id is not None:
            self.edgecloud_id = edgecloud_id

    @property
    def offset(self):
        """Gets the offset of this ListDeploymentsRequest.


        :return: The offset of this ListDeploymentsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDeploymentsRequest.


        :param offset: The offset of this ListDeploymentsRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListDeploymentsRequest.


        :return: The limit of this ListDeploymentsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDeploymentsRequest.


        :param limit: The limit of this ListDeploymentsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def status(self):
        """Gets the status of this ListDeploymentsRequest.


        :return: The status of this ListDeploymentsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListDeploymentsRequest.


        :param status: The status of this ListDeploymentsRequest.
        :type: str
        """
        self._status = status

    @property
    def id(self):
        """Gets the id of this ListDeploymentsRequest.


        :return: The id of this ListDeploymentsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListDeploymentsRequest.


        :param id: The id of this ListDeploymentsRequest.
        :type: str
        """
        self._id = id

    @property
    def edgecloud_id(self):
        """Gets the edgecloud_id of this ListDeploymentsRequest.


        :return: The edgecloud_id of this ListDeploymentsRequest.
        :rtype: str
        """
        return self._edgecloud_id

    @edgecloud_id.setter
    def edgecloud_id(self, edgecloud_id):
        """Sets the edgecloud_id of this ListDeploymentsRequest.


        :param edgecloud_id: The edgecloud_id of this ListDeploymentsRequest.
        :type: str
        """
        self._edgecloud_id = edgecloud_id

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
        if not isinstance(other, ListDeploymentsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other