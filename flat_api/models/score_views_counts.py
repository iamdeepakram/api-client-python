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


class ScoreViewsCounts(object):
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
        'total': 'float',
        'weekly': 'float',
        'monthly': 'float'
    }

    attribute_map = {
        'total': 'total',
        'weekly': 'weekly',
        'monthly': 'monthly'
    }

    def __init__(self, total=None, weekly=None, monthly=None, local_vars_configuration=None):  # noqa: E501
        """ScoreViewsCounts - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._total = None
        self._weekly = None
        self._monthly = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if weekly is not None:
            self.weekly = weekly
        if monthly is not None:
            self.monthly = monthly

    @property
    def total(self):
        """Gets the total of this ScoreViewsCounts.  # noqa: E501

        The total number of views of the score  # noqa: E501

        :return: The total of this ScoreViewsCounts.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ScoreViewsCounts.

        The total number of views of the score  # noqa: E501

        :param total: The total of this ScoreViewsCounts.  # noqa: E501
        :type: float
        """

        self._total = total

    @property
    def weekly(self):
        """Gets the weekly of this ScoreViewsCounts.  # noqa: E501

        The weekly number of views of the score  # noqa: E501

        :return: The weekly of this ScoreViewsCounts.  # noqa: E501
        :rtype: float
        """
        return self._weekly

    @weekly.setter
    def weekly(self, weekly):
        """Sets the weekly of this ScoreViewsCounts.

        The weekly number of views of the score  # noqa: E501

        :param weekly: The weekly of this ScoreViewsCounts.  # noqa: E501
        :type: float
        """

        self._weekly = weekly

    @property
    def monthly(self):
        """Gets the monthly of this ScoreViewsCounts.  # noqa: E501

        The monthly number of views of the score  # noqa: E501

        :return: The monthly of this ScoreViewsCounts.  # noqa: E501
        :rtype: float
        """
        return self._monthly

    @monthly.setter
    def monthly(self, monthly):
        """Sets the monthly of this ScoreViewsCounts.

        The monthly number of views of the score  # noqa: E501

        :param monthly: The monthly of this ScoreViewsCounts.  # noqa: E501
        :type: float
        """

        self._monthly = monthly

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
        if not isinstance(other, ScoreViewsCounts):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScoreViewsCounts):
            return True

        return self.to_dict() != other.to_dict()
