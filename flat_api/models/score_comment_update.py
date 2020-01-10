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


class ScoreCommentUpdate(object):
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
        'revision': 'str',
        'comment': 'str',
        'raw_comment': 'str',
        'context': 'ScoreCommentContext'
    }

    attribute_map = {
        'revision': 'revision',
        'comment': 'comment',
        'raw_comment': 'rawComment',
        'context': 'context'
    }

    def __init__(self, revision=None, comment=None, raw_comment=None, context=None, local_vars_configuration=None):  # noqa: E501
        """ScoreCommentUpdate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._revision = None
        self._comment = None
        self._raw_comment = None
        self._context = None
        self.discriminator = None

        if revision is not None:
            self.revision = revision
        if comment is not None:
            self.comment = comment
        if raw_comment is not None:
            self.raw_comment = raw_comment
        if context is not None:
            self.context = context

    @property
    def revision(self):
        """Gets the revision of this ScoreCommentUpdate.  # noqa: E501

        The unique indentifier of the revision of the score where the comment was added. If this property is unspecified or contains \"last\", the API will automatically take the last revision created.   # noqa: E501

        :return: The revision of this ScoreCommentUpdate.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this ScoreCommentUpdate.

        The unique indentifier of the revision of the score where the comment was added. If this property is unspecified or contains \"last\", the API will automatically take the last revision created.   # noqa: E501

        :param revision: The revision of this ScoreCommentUpdate.  # noqa: E501
        :type: str
        """

        self._revision = revision

    @property
    def comment(self):
        """Gets the comment of this ScoreCommentUpdate.  # noqa: E501

        The comment text that can includes mentions using the following format: `@[id:username]`.   # noqa: E501

        :return: The comment of this ScoreCommentUpdate.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this ScoreCommentUpdate.

        The comment text that can includes mentions using the following format: `@[id:username]`.   # noqa: E501

        :param comment: The comment of this ScoreCommentUpdate.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                comment is not None and len(comment) > 10000):
            raise ValueError("Invalid value for `comment`, length must be less than or equal to `10000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                comment is not None and len(comment) < 1):
            raise ValueError("Invalid value for `comment`, length must be greater than or equal to `1`")  # noqa: E501

        self._comment = comment

    @property
    def raw_comment(self):
        """Gets the raw_comment of this ScoreCommentUpdate.  # noqa: E501

        A raw version of the comment, that can be displayed without the mentions. If you use mentions, this property must be set.   # noqa: E501

        :return: The raw_comment of this ScoreCommentUpdate.  # noqa: E501
        :rtype: str
        """
        return self._raw_comment

    @raw_comment.setter
    def raw_comment(self, raw_comment):
        """Sets the raw_comment of this ScoreCommentUpdate.

        A raw version of the comment, that can be displayed without the mentions. If you use mentions, this property must be set.   # noqa: E501

        :param raw_comment: The raw_comment of this ScoreCommentUpdate.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                raw_comment is not None and len(raw_comment) > 10000):
            raise ValueError("Invalid value for `raw_comment`, length must be less than or equal to `10000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                raw_comment is not None and len(raw_comment) < 1):
            raise ValueError("Invalid value for `raw_comment`, length must be greater than or equal to `1`")  # noqa: E501

        self._raw_comment = raw_comment

    @property
    def context(self):
        """Gets the context of this ScoreCommentUpdate.  # noqa: E501


        :return: The context of this ScoreCommentUpdate.  # noqa: E501
        :rtype: ScoreCommentContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this ScoreCommentUpdate.


        :param context: The context of this ScoreCommentUpdate.  # noqa: E501
        :type: ScoreCommentContext
        """

        self._context = context

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
        if not isinstance(other, ScoreCommentUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScoreCommentUpdate):
            return True

        return self.to_dict() != other.to_dict()
