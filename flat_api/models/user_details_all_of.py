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


class UserDetailsAllOf(object):
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
        'type': 'str',
        'private_profile': 'bool',
        'locale': 'FlatLocales'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'private_profile': 'privateProfile',
        'locale': 'locale'
    }

    def __init__(self, id=None, type=None, private_profile=None, locale=None, local_vars_configuration=None):  # noqa: E501
        """UserDetailsAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._type = None
        self._private_profile = None
        self._locale = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if private_profile is not None:
            self.private_profile = private_profile
        if locale is not None:
            self.locale = locale

    @property
    def id(self):
        """Gets the id of this UserDetailsAllOf.  # noqa: E501

        Identifier of the user  # noqa: E501

        :return: The id of this UserDetailsAllOf.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserDetailsAllOf.

        Identifier of the user  # noqa: E501

        :param id: The id of this UserDetailsAllOf.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this UserDetailsAllOf.  # noqa: E501

        The type of account  # noqa: E501

        :return: The type of this UserDetailsAllOf.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UserDetailsAllOf.

        The type of account  # noqa: E501

        :param type: The type of this UserDetailsAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["user", "guest"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def private_profile(self):
        """Gets the private_profile of this UserDetailsAllOf.  # noqa: E501

        Tell either this user profile is private or not (individual accounts only)  # noqa: E501

        :return: The private_profile of this UserDetailsAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._private_profile

    @private_profile.setter
    def private_profile(self, private_profile):
        """Sets the private_profile of this UserDetailsAllOf.

        Tell either this user profile is private or not (individual accounts only)  # noqa: E501

        :param private_profile: The private_profile of this UserDetailsAllOf.  # noqa: E501
        :type: bool
        """

        self._private_profile = private_profile

    @property
    def locale(self):
        """Gets the locale of this UserDetailsAllOf.  # noqa: E501


        :return: The locale of this UserDetailsAllOf.  # noqa: E501
        :rtype: FlatLocales
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this UserDetailsAllOf.


        :param locale: The locale of this UserDetailsAllOf.  # noqa: E501
        :type: FlatLocales
        """

        self._locale = locale

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
        if not isinstance(other, UserDetailsAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserDetailsAllOf):
            return True

        return self.to_dict() != other.to_dict()
