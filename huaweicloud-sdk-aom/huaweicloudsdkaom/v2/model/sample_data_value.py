# coding: utf-8

import pprint
import re

import six





class SampleDataValue:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'sample': 'QuerySample',
        'data_points': 'list[MetricDataPoints]'
    }

    attribute_map = {
        'sample': 'sample',
        'data_points': 'data_points'
    }

    def __init__(self, sample=None, data_points=None):
        """SampleDataValue - a model defined in huaweicloud sdk"""
        
        

        self._sample = None
        self._data_points = None
        self.discriminator = None

        if sample is not None:
            self.sample = sample
        if data_points is not None:
            self.data_points = data_points

    @property
    def sample(self):
        """Gets the sample of this SampleDataValue.


        :return: The sample of this SampleDataValue.
        :rtype: QuerySample
        """
        return self._sample

    @sample.setter
    def sample(self, sample):
        """Sets the sample of this SampleDataValue.


        :param sample: The sample of this SampleDataValue.
        :type: QuerySample
        """
        self._sample = sample

    @property
    def data_points(self):
        """Gets the data_points of this SampleDataValue.

        时序数据。

        :return: The data_points of this SampleDataValue.
        :rtype: list[MetricDataPoints]
        """
        return self._data_points

    @data_points.setter
    def data_points(self, data_points):
        """Sets the data_points of this SampleDataValue.

        时序数据。

        :param data_points: The data_points of this SampleDataValue.
        :type: list[MetricDataPoints]
        """
        self._data_points = data_points

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
        if not isinstance(other, SampleDataValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
