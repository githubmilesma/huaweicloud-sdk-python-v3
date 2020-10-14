# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListEnterpriseOrganizationsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'root_id': 'str',
        'root_name': 'str',
        'child_nodes': 'list[EmChildNodeV2]'
    }

    attribute_map = {
        'root_id': 'root_id',
        'root_name': 'root_name',
        'child_nodes': 'child_nodes'
    }

    def __init__(self, root_id=None, root_name=None, child_nodes=None):
        """ListEnterpriseOrganizationsResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._root_id = None
        self._root_name = None
        self._child_nodes = None
        self.discriminator = None

        if root_id is not None:
            self.root_id = root_id
        if root_name is not None:
            self.root_name = root_name
        if child_nodes is not None:
            self.child_nodes = child_nodes

    @property
    def root_id(self):
        """Gets the root_id of this ListEnterpriseOrganizationsResponse.

        |参数名称：根节点ID，如果请求有parent_id，则该参数无值。| |参数约束及描述：根节点ID，如果请求有parent_id，则该参数无值。|

        :return: The root_id of this ListEnterpriseOrganizationsResponse.
        :rtype: str
        """
        return self._root_id

    @root_id.setter
    def root_id(self, root_id):
        """Sets the root_id of this ListEnterpriseOrganizationsResponse.

        |参数名称：根节点ID，如果请求有parent_id，则该参数无值。| |参数约束及描述：根节点ID，如果请求有parent_id，则该参数无值。|

        :param root_id: The root_id of this ListEnterpriseOrganizationsResponse.
        :type: str
        """
        self._root_id = root_id

    @property
    def root_name(self):
        """Gets the root_name of this ListEnterpriseOrganizationsResponse.

        |参数名称：根节点名称，如果请求有parent_id，则该参数无值。注：组织根节点没有设置组织名称时，可能为空。| |参数约束及描述：根节点名称，如果请求有parent_id，则该参数无值。注：组织根节点没有设置组织名称时，可能为空。|

        :return: The root_name of this ListEnterpriseOrganizationsResponse.
        :rtype: str
        """
        return self._root_name

    @root_name.setter
    def root_name(self, root_name):
        """Sets the root_name of this ListEnterpriseOrganizationsResponse.

        |参数名称：根节点名称，如果请求有parent_id，则该参数无值。注：组织根节点没有设置组织名称时，可能为空。| |参数约束及描述：根节点名称，如果请求有parent_id，则该参数无值。注：组织根节点没有设置组织名称时，可能为空。|

        :param root_name: The root_name of this ListEnterpriseOrganizationsResponse.
        :type: str
        """
        self._root_name = root_name

    @property
    def child_nodes(self):
        """Gets the child_nodes of this ListEnterpriseOrganizationsResponse.

        |参数名称：企业管理子Party节点列表。注：每一层的节点列表需要按relation_type升序排序。| |参数约束以及描述：企业管理子Party节点列表。注：每一层的节点列表需要按relation_type升序排序。|

        :return: The child_nodes of this ListEnterpriseOrganizationsResponse.
        :rtype: list[EmChildNodeV2]
        """
        return self._child_nodes

    @child_nodes.setter
    def child_nodes(self, child_nodes):
        """Sets the child_nodes of this ListEnterpriseOrganizationsResponse.

        |参数名称：企业管理子Party节点列表。注：每一层的节点列表需要按relation_type升序排序。| |参数约束以及描述：企业管理子Party节点列表。注：每一层的节点列表需要按relation_type升序排序。|

        :param child_nodes: The child_nodes of this ListEnterpriseOrganizationsResponse.
        :type: list[EmChildNodeV2]
        """
        self._child_nodes = child_nodes

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
        if not isinstance(other, ListEnterpriseOrganizationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
