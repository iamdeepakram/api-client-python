# coding: utf-8

"""
    Flat API

    The Flat API allows you to easily extend the abilities of the [Flat Platform](https://flat.io), with a wide range of use cases including the following:  * Creating and importing new music scores using MusicXML or MIDI files * Browsing, updating, copying, exporting the user's scores (for example in MP3, WAV or MIDI) * Managing educational resources with Flat for Education: creating & updating the organization accounts, the classes, rosters and assignments.  The Flat API is built on HTTP. Our API is RESTful It has predictable resource URLs. It returns HTTP response codes to indicate errors. It also accepts and returns JSON in the HTTP body. The [schema](/swagger.yaml) of this API follows the [OpenAPI Initiative (OAI) specification](https://www.openapis.org/), you can use and work with [compatible Swagger tools](http://swagger.io/open-source-integrations/). This API features Cross-Origin Resource Sharing (CORS) implemented in compliance with [W3C spec](https://www.w3.org/TR/cors/).  You can use your favorite HTTP/REST library for your programming language to use Flat's API. This specification and reference is [available on Github](https://github.com/FlatIO/api-reference).  Getting Started and learn more:  * [API Overview and interoduction](https://flat.io/developers/docs/api/) * [Authentication (Personal Access Tokens or OAuth2)](https://flat.io/developers/docs/api/authentication.html) * [SDKs](https://flat.io/developers/docs/api/sdks.html) * [Rate Limits](https://flat.io/developers/docs/api/rate-limits.html) * [Changelog](https://flat.io/developers/docs/api/changelog.html) 

    OpenAPI spec version: 2.4.0
    Contact: developers@flat.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UserPublicSummary(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'username': 'str',
        'name': 'str',
        'printable_name': 'str',
        'picture': 'str',
        'is_power_user': 'bool',
        'organization': 'str',
        'organization_role': 'OrganizationRoles',
        'class_role': 'ClassRoles',
        'html_url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'username': 'username',
        'name': 'name',
        'printable_name': 'printableName',
        'picture': 'picture',
        'is_power_user': 'isPowerUser',
        'organization': 'organization',
        'organization_role': 'organizationRole',
        'class_role': 'classRole',
        'html_url': 'htmlUrl'
    }

    def __init__(self, id=None, username=None, name=None, printable_name=None, picture=None, is_power_user=None, organization=None, organization_role=None, class_role=None, html_url=None):
        """
        UserPublicSummary - a model defined in Swagger
        """

        self._id = None
        self._username = None
        self._name = None
        self._printable_name = None
        self._picture = None
        self._is_power_user = None
        self._organization = None
        self._organization_role = None
        self._class_role = None
        self._html_url = None

        if id is not None:
          self.id = id
        if username is not None:
          self.username = username
        if name is not None:
          self.name = name
        if printable_name is not None:
          self.printable_name = printable_name
        if picture is not None:
          self.picture = picture
        if is_power_user is not None:
          self.is_power_user = is_power_user
        if organization is not None:
          self.organization = organization
        if organization_role is not None:
          self.organization_role = organization_role
        if class_role is not None:
          self.class_role = class_role
        if html_url is not None:
          self.html_url = html_url

    @property
    def id(self):
        """
        Gets the id of this UserPublicSummary.
        The user unique identifier

        :return: The id of this UserPublicSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UserPublicSummary.
        The user unique identifier

        :param id: The id of this UserPublicSummary.
        :type: str
        """

        self._id = id

    @property
    def username(self):
        """
        Gets the username of this UserPublicSummary.
        The user name (unique for the organization)

        :return: The username of this UserPublicSummary.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this UserPublicSummary.
        The user name (unique for the organization)

        :param username: The username of this UserPublicSummary.
        :type: str
        """

        self._username = username

    @property
    def name(self):
        """
        Gets the name of this UserPublicSummary.
        A displayable name for the user

        :return: The name of this UserPublicSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UserPublicSummary.
        A displayable name for the user

        :param name: The name of this UserPublicSummary.
        :type: str
        """

        self._name = name

    @property
    def printable_name(self):
        """
        Gets the printable_name of this UserPublicSummary.
        The name that can be directly printed (name or username)

        :return: The printable_name of this UserPublicSummary.
        :rtype: str
        """
        return self._printable_name

    @printable_name.setter
    def printable_name(self, printable_name):
        """
        Sets the printable_name of this UserPublicSummary.
        The name that can be directly printed (name or username)

        :param printable_name: The printable_name of this UserPublicSummary.
        :type: str
        """

        self._printable_name = printable_name

    @property
    def picture(self):
        """
        Gets the picture of this UserPublicSummary.
        User pictue

        :return: The picture of this UserPublicSummary.
        :rtype: str
        """
        return self._picture

    @picture.setter
    def picture(self, picture):
        """
        Sets the picture of this UserPublicSummary.
        User pictue

        :param picture: The picture of this UserPublicSummary.
        :type: str
        """

        self._picture = picture

    @property
    def is_power_user(self):
        """
        Gets the is_power_user of this UserPublicSummary.
        User license status. 'True' if user is an individual Power user

        :return: The is_power_user of this UserPublicSummary.
        :rtype: bool
        """
        return self._is_power_user

    @is_power_user.setter
    def is_power_user(self, is_power_user):
        """
        Sets the is_power_user of this UserPublicSummary.
        User license status. 'True' if user is an individual Power user

        :param is_power_user: The is_power_user of this UserPublicSummary.
        :type: bool
        """

        self._is_power_user = is_power_user

    @property
    def organization(self):
        """
        Gets the organization of this UserPublicSummary.
        Organization ID (for Edu users only)

        :return: The organization of this UserPublicSummary.
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this UserPublicSummary.
        Organization ID (for Edu users only)

        :param organization: The organization of this UserPublicSummary.
        :type: str
        """

        self._organization = organization

    @property
    def organization_role(self):
        """
        Gets the organization_role of this UserPublicSummary.

        :return: The organization_role of this UserPublicSummary.
        :rtype: OrganizationRoles
        """
        return self._organization_role

    @organization_role.setter
    def organization_role(self, organization_role):
        """
        Sets the organization_role of this UserPublicSummary.

        :param organization_role: The organization_role of this UserPublicSummary.
        :type: OrganizationRoles
        """

        self._organization_role = organization_role

    @property
    def class_role(self):
        """
        Gets the class_role of this UserPublicSummary.

        :return: The class_role of this UserPublicSummary.
        :rtype: ClassRoles
        """
        return self._class_role

    @class_role.setter
    def class_role(self, class_role):
        """
        Sets the class_role of this UserPublicSummary.

        :param class_role: The class_role of this UserPublicSummary.
        :type: ClassRoles
        """

        self._class_role = class_role

    @property
    def html_url(self):
        """
        Gets the html_url of this UserPublicSummary.
        Link to user profile (for Indiv. users only)

        :return: The html_url of this UserPublicSummary.
        :rtype: str
        """
        return self._html_url

    @html_url.setter
    def html_url(self, html_url):
        """
        Sets the html_url of this UserPublicSummary.
        Link to user profile (for Indiv. users only)

        :param html_url: The html_url of this UserPublicSummary.
        :type: str
        """

        self._html_url = html_url

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, UserPublicSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
