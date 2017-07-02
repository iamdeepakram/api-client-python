# coding: utf-8

"""
    Flat API

    The Flat API allows you to easily extend the abilities of the [Flat Platform](https://flat.io), with a wide range of use cases including the following:  * Creating and importing new music scores using MusicXML or MIDI files * Browsing, updating, copying, exporting the user's scores (for example in MP3, WAV or MIDI) * Managing educational resources with Flat for Education: creating & updating the organization accounts, the classes, rosters and assignments.  The Flat API is built on HTTP. Our API is RESTful It has predictable resource URLs. It returns HTTP response codes to indicate errors. It also accepts and returns JSON in the HTTP body. The [schema](/swagger.yaml) of this API follows the [OpenAPI Initiative (OAI) specification](https://www.openapis.org/), you can use and work with [compatible Swagger tools](http://swagger.io/open-source-integrations/). This API features Cross-Origin Resource Sharing (CORS) implemented in compliance with [W3C spec](https://www.w3.org/TR/cors/).  You can use your favorite HTTP/REST library for your programming language to use Flat's API. This specification and reference is [available on Github](https://github.com/FlatIO/api-reference).  Getting Started and learn more:  * [API Overview and interoduction](https://flat.io/developers/docs/api/) * [Authentication (Personal Access Tokens or OAuth2)](https://flat.io/developers/docs/api/authentication.html) * [SDKs](https://flat.io/developers/docs/api/sdks.html) * [Rate Limits](https://flat.io/developers/docs/api/rate-limits.html) * [Changelog](https://flat.io/developers/docs/api/changelog.html) 

    OpenAPI spec version: 2.2.0
    Contact: developers@flat.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ClassDetailsLti(object):
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
        'context_id': 'str',
        'context_title': 'str',
        'context_label': 'str'
    }

    attribute_map = {
        'context_id': 'contextId',
        'context_title': 'contextTitle',
        'context_label': 'contextLabel'
    }

    def __init__(self, context_id=None, context_title=None, context_label=None):
        """
        ClassDetailsLti - a model defined in Swagger
        """

        self._context_id = None
        self._context_title = None
        self._context_label = None

        if context_id is not None:
          self.context_id = context_id
        if context_title is not None:
          self.context_title = context_title
        if context_label is not None:
          self.context_label = context_label

    @property
    def context_id(self):
        """
        Gets the context_id of this ClassDetailsLti.
        Unique context identifier provided

        :return: The context_id of this ClassDetailsLti.
        :rtype: str
        """
        return self._context_id

    @context_id.setter
    def context_id(self, context_id):
        """
        Sets the context_id of this ClassDetailsLti.
        Unique context identifier provided

        :param context_id: The context_id of this ClassDetailsLti.
        :type: str
        """

        self._context_id = context_id

    @property
    def context_title(self):
        """
        Gets the context_title of this ClassDetailsLti.
        Context title

        :return: The context_title of this ClassDetailsLti.
        :rtype: str
        """
        return self._context_title

    @context_title.setter
    def context_title(self, context_title):
        """
        Sets the context_title of this ClassDetailsLti.
        Context title

        :param context_title: The context_title of this ClassDetailsLti.
        :type: str
        """

        self._context_title = context_title

    @property
    def context_label(self):
        """
        Gets the context_label of this ClassDetailsLti.
        Context label

        :return: The context_label of this ClassDetailsLti.
        :rtype: str
        """
        return self._context_label

    @context_label.setter
    def context_label(self, context_label):
        """
        Sets the context_label of this ClassDetailsLti.
        Context label

        :param context_label: The context_label of this ClassDetailsLti.
        :type: str
        """

        self._context_label = context_label

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
        if not isinstance(other, ClassDetailsLti):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
