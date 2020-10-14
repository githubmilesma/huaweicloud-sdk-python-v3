# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListDomainBandwidthSummaryV2Response(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bandwidth_list': 'list[PeakBandwidthData]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'bandwidth_list': 'bandwidth_list',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, bandwidth_list=None, x_request_id=None):
        """ListDomainBandwidthSummaryV2Response - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._bandwidth_list = None
        self._x_request_id = None
        self.discriminator = None

        if bandwidth_list is not None:
            self.bandwidth_list = bandwidth_list
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def bandwidth_list(self):
        """Gets the bandwidth_list of this ListDomainBandwidthSummaryV2Response.

        域名对应的带宽峰值列表。

        :return: The bandwidth_list of this ListDomainBandwidthSummaryV2Response.
        :rtype: list[PeakBandwidthData]
        """
        return self._bandwidth_list

    @bandwidth_list.setter
    def bandwidth_list(self, bandwidth_list):
        """Sets the bandwidth_list of this ListDomainBandwidthSummaryV2Response.

        域名对应的带宽峰值列表。

        :param bandwidth_list: The bandwidth_list of this ListDomainBandwidthSummaryV2Response.
        :type: list[PeakBandwidthData]
        """
        self._bandwidth_list = bandwidth_list

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ListDomainBandwidthSummaryV2Response.


        :return: The x_request_id of this ListDomainBandwidthSummaryV2Response.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ListDomainBandwidthSummaryV2Response.


        :param x_request_id: The x_request_id of this ListDomainBandwidthSummaryV2Response.
        :type: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListDomainBandwidthSummaryV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
