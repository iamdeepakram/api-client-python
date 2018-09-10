# coding: utf-8

"""
    Flat API

    The Flat API allows you to easily extend the abilities of the [Flat Platform](https://flat.io), with a wide range of use cases including the following:  * Creating and importing new music scores using MusicXML, MIDI, Guitar Pro (GP3, GP4, GP5, GPX, GP), PowerTab and TuxGuitar files * Browsing, updating, copying, exporting the user's scores (for example in MP3, WAV or MIDI) * Managing educational resources with Flat for Education: creating & updating the organization accounts, the classes, rosters and assignments.  The Flat API is built on HTTP. Our API is RESTful It has predictable resource URLs. It returns HTTP response codes to indicate errors. It also accepts and returns JSON in the HTTP body. The [schema](/swagger.yaml) of this API follows the [OpenAPI Initiative (OAI) specification](https://www.openapis.org/), you can use and work with [compatible Swagger tools](http://swagger.io/open-source-integrations/). This API features Cross-Origin Resource Sharing (CORS) implemented in compliance with [W3C spec](https://www.w3.org/TR/cors/).  You can use your favorite HTTP/REST library for your programming language to use Flat's API. This specification and reference is [available on Github](https://github.com/FlatIO/api-reference).  Getting Started and learn more:  * [API Overview and interoduction](https://flat.io/developers/docs/api/) * [Authentication (Personal Access Tokens or OAuth2)](https://flat.io/developers/docs/api/authentication.html) * [SDKs](https://flat.io/developers/docs/api/sdks.html) * [Rate Limits](https://flat.io/developers/docs/api/rate-limits.html) * [Changelog](https://flat.io/developers/docs/api/changelog.html)   # noqa: E501

    OpenAPI spec version: 2.7.0
    Contact: developers@flat.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ScoreModification(object):
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
        'title': 'str',
        'privacy': 'ScorePrivacy',
        'sharing_key': 'str',
        'description': 'str',
        'tags': 'list[str]',
        'creation_type': 'ScoreCreationType',
        'license': 'ScoreLicense'
    }

    attribute_map = {
        'title': 'title',
        'privacy': 'privacy',
        'sharing_key': 'sharingKey',
        'description': 'description',
        'tags': 'tags',
        'creation_type': 'creationType',
        'license': 'license'
    }

    def __init__(self, title=None, privacy=None, sharing_key=None, description=None, tags=None, creation_type=None, license=None):  # noqa: E501
        """ScoreModification - a model defined in OpenAPI"""  # noqa: E501

        self._title = None
        self._privacy = None
        self._sharing_key = None
        self._description = None
        self._tags = None
        self._creation_type = None
        self._license = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if privacy is not None:
            self.privacy = privacy
        if sharing_key is not None:
            self.sharing_key = sharing_key
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if creation_type is not None:
            self.creation_type = creation_type
        if license is not None:
            self.license = license

    @property
    def title(self):
        """Gets the title of this ScoreModification.  # noqa: E501

        The title of the score  # noqa: E501

        :return: The title of this ScoreModification.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ScoreModification.

        The title of the score  # noqa: E501

        :param title: The title of this ScoreModification.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def privacy(self):
        """Gets the privacy of this ScoreModification.  # noqa: E501


        :return: The privacy of this ScoreModification.  # noqa: E501
        :rtype: ScorePrivacy
        """
        return self._privacy

    @privacy.setter
    def privacy(self, privacy):
        """Sets the privacy of this ScoreModification.


        :param privacy: The privacy of this ScoreModification.  # noqa: E501
        :type: ScorePrivacy
        """

        self._privacy = privacy

    @property
    def sharing_key(self):
        """Gets the sharing_key of this ScoreModification.  # noqa: E501

        When using the `privacy` mode `privateLink`, this property can be used to set a custom sharing key, otherwise a new key will be generated.  # noqa: E501

        :return: The sharing_key of this ScoreModification.  # noqa: E501
        :rtype: str
        """
        return self._sharing_key

    @sharing_key.setter
    def sharing_key(self, sharing_key):
        """Sets the sharing_key of this ScoreModification.

        When using the `privacy` mode `privateLink`, this property can be used to set a custom sharing key, otherwise a new key will be generated.  # noqa: E501

        :param sharing_key: The sharing_key of this ScoreModification.  # noqa: E501
        :type: str
        """
        if sharing_key is not None and not re.search('^[a-f0-9]{128}$', sharing_key):  # noqa: E501
            raise ValueError("Invalid value for `sharing_key`, must be a follow pattern or equal to `/^[a-f0-9]{128}$/`")  # noqa: E501

        self._sharing_key = sharing_key

    @property
    def description(self):
        """Gets the description of this ScoreModification.  # noqa: E501

        Description of the creation  # noqa: E501

        :return: The description of this ScoreModification.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ScoreModification.

        Description of the creation  # noqa: E501

        :param description: The description of this ScoreModification.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 1000:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1000`")  # noqa: E501

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this ScoreModification.  # noqa: E501

        Tags describing the score  # noqa: E501

        :return: The tags of this ScoreModification.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ScoreModification.

        Tags describing the score  # noqa: E501

        :param tags: The tags of this ScoreModification.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def creation_type(self):
        """Gets the creation_type of this ScoreModification.  # noqa: E501


        :return: The creation_type of this ScoreModification.  # noqa: E501
        :rtype: ScoreCreationType
        """
        return self._creation_type

    @creation_type.setter
    def creation_type(self, creation_type):
        """Sets the creation_type of this ScoreModification.


        :param creation_type: The creation_type of this ScoreModification.  # noqa: E501
        :type: ScoreCreationType
        """

        self._creation_type = creation_type

    @property
    def license(self):
        """Gets the license of this ScoreModification.  # noqa: E501


        :return: The license of this ScoreModification.  # noqa: E501
        :rtype: ScoreLicense
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this ScoreModification.


        :param license: The license of this ScoreModification.  # noqa: E501
        :type: ScoreLicense
        """

        self._license = license

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
        if not isinstance(other, ScoreModification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
