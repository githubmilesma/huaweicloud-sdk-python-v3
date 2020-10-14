# coding: utf-8

import pprint
import re

import six





class ListHistoryStreamsV2Request:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'domain': 'str',
        'app': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'domain': 'domain',
        'app': 'app',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, domain=None, app=None, offset=0, limit=10):
        """ListHistoryStreamsV2Request - a model defined in huaweicloud sdk"""
        
        

        self._domain = None
        self._app = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.domain = domain
        if app is not None:
            self.app = app
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def domain(self):
        """Gets the domain of this ListHistoryStreamsV2Request.


        :return: The domain of this ListHistoryStreamsV2Request.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ListHistoryStreamsV2Request.


        :param domain: The domain of this ListHistoryStreamsV2Request.
        :type: str
        """
        self._domain = domain

    @property
    def app(self):
        """Gets the app of this ListHistoryStreamsV2Request.


        :return: The app of this ListHistoryStreamsV2Request.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this ListHistoryStreamsV2Request.


        :param app: The app of this ListHistoryStreamsV2Request.
        :type: str
        """
        self._app = app

    @property
    def offset(self):
        """Gets the offset of this ListHistoryStreamsV2Request.


        :return: The offset of this ListHistoryStreamsV2Request.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListHistoryStreamsV2Request.


        :param offset: The offset of this ListHistoryStreamsV2Request.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListHistoryStreamsV2Request.


        :return: The limit of this ListHistoryStreamsV2Request.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListHistoryStreamsV2Request.


        :param limit: The limit of this ListHistoryStreamsV2Request.
        :type: int
        """
        self._limit = limit

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
        if not isinstance(other, ListHistoryStreamsV2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
