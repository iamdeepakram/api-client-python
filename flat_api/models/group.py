# coding: utf-8

"""
    Flat API

    The Flat API allows you to easily extend the abilities of the [Flat Platform](https://flat.io), with a wide range of use cases including the following:  * Creating and importing new music scores using MusicXML, MIDI, Guitar Pro (GP3, GP4, GP5, GPX, GP), PowerTab, TuxGuitar and MuseScore files * Browsing, updating, copying, exporting the user's scores (for example in MP3, WAV or MIDI) * Managing educational resources with Flat for Education: creating & updating the organization accounts, the classes, rosters and assignments.  The Flat API is built on HTTP. Our API is RESTful It has predictable resource URLs. It returns HTTP response codes to indicate errors. It also accepts and returns JSON in the HTTP body. The [schema](/swagger.yaml) of this API follows the [OpenAPI Initiative (OAI) specification](https://www.openapis.org/), you can use and work with [compatible Swagger tools](http://swagger.io/open-source-integrations/). This API features Cross-Origin Resource Sharing (CORS) implemented in compliance with [W3C spec](https://www.w3.org/TR/cors/).  You can use your favorite HTTP/REST library for your programming language to use Flat's API. This specification and reference is [available on Github](https://github.com/FlatIO/api-reference).  Getting Started and learn more:  * [API Overview and interoduction](https://flat.io/developers/docs/api/) * [Authentication (Personal Access Tokens or OAuth2)](https://flat.io/developers/docs/api/authentication.html) * [SDKs](https://flat.io/developers/docs/api/sdks.html) * [Rate Limits](https://flat.io/developers/docs/api/rate-limits.html) * [Changelog](https://flat.io/developers/docs/api/changelog.html)   # noqa: E501

    The version of the OpenAPI document: 2.9.0
    Contact: developers@flat.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from flat_api.configuration import Configuration


class Group(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'name': 'str',
        'type': 'str',
        'users_count': 'float',
        'read_only': 'bool',
        'organization': 'str',
        'creation_date': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'users_count': 'usersCount',
        'read_only': 'readOnly',
        'organization': 'organization',
        'creation_date': 'creationDate'
    }

    def __init__(self, id=None, name=None, type=None, users_count=None, read_only=None, organization=None, creation_date=None, local_vars_configuration=None):  # noqa: E501
        """Group - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._type = None
        self._users_count = None
        self._read_only = None
        self._organization = None
        self._creation_date = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if users_count is not None:
            self.users_count = users_count
        if read_only is not None:
            self.read_only = read_only
        if organization is not None:
            self.organization = organization
        if creation_date is not None:
            self.creation_date = creation_date

    @property
    def id(self):
        """Gets the id of this Group.  # noqa: E501

        The unique identifier of the group  # noqa: E501

        :return: The id of this Group.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Group.

        The unique identifier of the group  # noqa: E501

        :param id: The id of this Group.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Group.  # noqa: E501

        The display name of the group  # noqa: E501

        :return: The name of this Group.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Group.

        The display name of the group  # noqa: E501

        :param name: The name of this Group.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this Group.  # noqa: E501

        The type of the group: * `generic`: A group created by a Flat user * `classTeachers`: A group created automaticaly by Flat that contains   the teachers of a class * `classStudents`: A group created automaticaly by Flat that contains   the studnets of a class   # noqa: E501

        :return: The type of this Group.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Group.

        The type of the group: * `generic`: A group created by a Flat user * `classTeachers`: A group created automaticaly by Flat that contains   the teachers of a class * `classStudents`: A group created automaticaly by Flat that contains   the studnets of a class   # noqa: E501

        :param type: The type of this Group.  # noqa: E501
        :type: str
        """
        allowed_values = ["generic", "classTeachers", "classStudents"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def users_count(self):
        """Gets the users_count of this Group.  # noqa: E501

        The number of users in this group  # noqa: E501

        :return: The users_count of this Group.  # noqa: E501
        :rtype: float
        """
        return self._users_count

    @users_count.setter
    def users_count(self, users_count):
        """Sets the users_count of this Group.

        The number of users in this group  # noqa: E501

        :param users_count: The users_count of this Group.  # noqa: E501
        :type: float
        """

        self._users_count = users_count

    @property
    def read_only(self):
        """Gets the read_only of this Group.  # noqa: E501

        `True` if the group is set in read-only   # noqa: E501

        :return: The read_only of this Group.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this Group.

        `True` if the group is set in read-only   # noqa: E501

        :param read_only: The read_only of this Group.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

    @property
    def organization(self):
        """Gets the organization of this Group.  # noqa: E501

        If the group is related to an organization, this field will contain the unique identifier of the organization   # noqa: E501

        :return: The organization of this Group.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this Group.

        If the group is related to an organization, this field will contain the unique identifier of the organization   # noqa: E501

        :param organization: The organization of this Group.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def creation_date(self):
        """Gets the creation_date of this Group.  # noqa: E501

        The creation date of the group  # noqa: E501

        :return: The creation_date of this Group.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this Group.

        The creation date of the group  # noqa: E501

        :param creation_date: The creation_date of this Group.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

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
        if not isinstance(other, Group):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Group):
            return True

        return self.to_dict() != other.to_dict()
