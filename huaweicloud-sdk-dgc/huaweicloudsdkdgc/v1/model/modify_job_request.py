# coding: utf-8

import pprint
import re

import six





class ModifyJobRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'job_name': 'str',
        'body': 'JobInfo'
    }

    attribute_map = {
        'job_name': 'job_name',
        'body': 'body'
    }

    def __init__(self, job_name=None, body=None):
        """ModifyJobRequest - a model defined in huaweicloud sdk"""
        
        

        self._job_name = None
        self._body = None
        self.discriminator = None

        self.job_name = job_name
        if body is not None:
            self.body = body

    @property
    def job_name(self):
        """Gets the job_name of this ModifyJobRequest.


        :return: The job_name of this ModifyJobRequest.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this ModifyJobRequest.


        :param job_name: The job_name of this ModifyJobRequest.
        :type: str
        """
        self._job_name = job_name

    @property
    def body(self):
        """Gets the body of this ModifyJobRequest.


        :return: The body of this ModifyJobRequest.
        :rtype: JobInfo
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ModifyJobRequest.


        :param body: The body of this ModifyJobRequest.
        :type: JobInfo
        """
        self._body = body

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
        if not isinstance(other, ModifyJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
