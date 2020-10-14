# coding: utf-8

import pprint
import re

import six





class ListAllDCSInstancesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'include_failure': 'str',
        'name': 'str',
        'offset': 'int',
        'limit': 'int',
        'status': 'str',
        'name_equal': 'str',
        'tags': 'str',
        'ip': 'str'
    }

    attribute_map = {
        'id': 'id',
        'include_failure': 'include_failure',
        'name': 'name',
        'offset': 'offset',
        'limit': 'limit',
        'status': 'status',
        'name_equal': 'name_equal',
        'tags': 'tags',
        'ip': 'ip'
    }

    def __init__(self, id=None, include_failure=None, name=None, offset=None, limit=None, status=None, name_equal=None, tags=None, ip=None):
        """ListAllDCSInstancesRequest - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._include_failure = None
        self._name = None
        self._offset = None
        self._limit = None
        self._status = None
        self._name_equal = None
        self._tags = None
        self._ip = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if include_failure is not None:
            self.include_failure = include_failure
        if name is not None:
            self.name = name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if status is not None:
            self.status = status
        if name_equal is not None:
            self.name_equal = name_equal
        if tags is not None:
            self.tags = tags
        if ip is not None:
            self.ip = ip

    @property
    def id(self):
        """Gets the id of this ListAllDCSInstancesRequest.


        :return: The id of this ListAllDCSInstancesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListAllDCSInstancesRequest.


        :param id: The id of this ListAllDCSInstancesRequest.
        :type: str
        """
        self._id = id

    @property
    def include_failure(self):
        """Gets the include_failure of this ListAllDCSInstancesRequest.


        :return: The include_failure of this ListAllDCSInstancesRequest.
        :rtype: str
        """
        return self._include_failure

    @include_failure.setter
    def include_failure(self, include_failure):
        """Sets the include_failure of this ListAllDCSInstancesRequest.


        :param include_failure: The include_failure of this ListAllDCSInstancesRequest.
        :type: str
        """
        self._include_failure = include_failure

    @property
    def name(self):
        """Gets the name of this ListAllDCSInstancesRequest.


        :return: The name of this ListAllDCSInstancesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListAllDCSInstancesRequest.


        :param name: The name of this ListAllDCSInstancesRequest.
        :type: str
        """
        self._name = name

    @property
    def offset(self):
        """Gets the offset of this ListAllDCSInstancesRequest.


        :return: The offset of this ListAllDCSInstancesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAllDCSInstancesRequest.


        :param offset: The offset of this ListAllDCSInstancesRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListAllDCSInstancesRequest.


        :return: The limit of this ListAllDCSInstancesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAllDCSInstancesRequest.


        :param limit: The limit of this ListAllDCSInstancesRequest.
        :type: int
        """
        self._limit = limit

    @property
    def status(self):
        """Gets the status of this ListAllDCSInstancesRequest.


        :return: The status of this ListAllDCSInstancesRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListAllDCSInstancesRequest.


        :param status: The status of this ListAllDCSInstancesRequest.
        :type: str
        """
        self._status = status

    @property
    def name_equal(self):
        """Gets the name_equal of this ListAllDCSInstancesRequest.


        :return: The name_equal of this ListAllDCSInstancesRequest.
        :rtype: str
        """
        return self._name_equal

    @name_equal.setter
    def name_equal(self, name_equal):
        """Sets the name_equal of this ListAllDCSInstancesRequest.


        :param name_equal: The name_equal of this ListAllDCSInstancesRequest.
        :type: str
        """
        self._name_equal = name_equal

    @property
    def tags(self):
        """Gets the tags of this ListAllDCSInstancesRequest.


        :return: The tags of this ListAllDCSInstancesRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListAllDCSInstancesRequest.


        :param tags: The tags of this ListAllDCSInstancesRequest.
        :type: str
        """
        self._tags = tags

    @property
    def ip(self):
        """Gets the ip of this ListAllDCSInstancesRequest.


        :return: The ip of this ListAllDCSInstancesRequest.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this ListAllDCSInstancesRequest.


        :param ip: The ip of this ListAllDCSInstancesRequest.
        :type: str
        """
        self._ip = ip

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
        if not isinstance(other, ListAllDCSInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
