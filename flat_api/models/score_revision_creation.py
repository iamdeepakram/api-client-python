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


class ScoreRevisionCreation(object):
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
        'data': 'ScoreData',
        'data_encoding': 'ScoreDataEncoding',
        'autosave': 'bool',
        'description': 'str'
    }

    attribute_map = {
        'data': 'data',
        'data_encoding': 'dataEncoding',
        'autosave': 'autosave',
        'description': 'description'
    }

    def __init__(self, data=None, data_encoding=None, autosave=None, description=None):
        """
        ScoreRevisionCreation - a model defined in Swagger
        """

        self._data = None
        self._data_encoding = None
        self._autosave = None
        self._description = None

        self.data = data
        if data_encoding is not None:
          self.data_encoding = data_encoding
        if autosave is not None:
          self.autosave = autosave
        if description is not None:
          self.description = description

    @property
    def data(self):
        """
        Gets the data of this ScoreRevisionCreation.

        :return: The data of this ScoreRevisionCreation.
        :rtype: ScoreData
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this ScoreRevisionCreation.

        :param data: The data of this ScoreRevisionCreation.
        :type: ScoreData
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")

        self._data = data

    @property
    def data_encoding(self):
        """
        Gets the data_encoding of this ScoreRevisionCreation.

        :return: The data_encoding of this ScoreRevisionCreation.
        :rtype: ScoreDataEncoding
        """
        return self._data_encoding

    @data_encoding.setter
    def data_encoding(self, data_encoding):
        """
        Sets the data_encoding of this ScoreRevisionCreation.

        :param data_encoding: The data_encoding of this ScoreRevisionCreation.
        :type: ScoreDataEncoding
        """

        self._data_encoding = data_encoding

    @property
    def autosave(self):
        """
        Gets the autosave of this ScoreRevisionCreation.
        Must be set to `true` if the revision was created automatically. 

        :return: The autosave of this ScoreRevisionCreation.
        :rtype: bool
        """
        return self._autosave

    @autosave.setter
    def autosave(self, autosave):
        """
        Sets the autosave of this ScoreRevisionCreation.
        Must be set to `true` if the revision was created automatically. 

        :param autosave: The autosave of this ScoreRevisionCreation.
        :type: bool
        """

        self._autosave = autosave

    @property
    def description(self):
        """
        Gets the description of this ScoreRevisionCreation.
        A description associated to the revision

        :return: The description of this ScoreRevisionCreation.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ScoreRevisionCreation.
        A description associated to the revision

        :param description: The description of this ScoreRevisionCreation.
        :type: str
        """

        self._description = description

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
        if not isinstance(other, ScoreRevisionCreation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
