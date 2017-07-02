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


class ScoreCommentCreation(object):
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
        'revision': 'str',
        'comment': 'str',
        'raw_comment': 'str',
        'mentions': 'list[str]',
        'reply_to': 'str',
        'context': 'ScoreCommentContext'
    }

    attribute_map = {
        'revision': 'revision',
        'comment': 'comment',
        'raw_comment': 'rawComment',
        'mentions': 'mentions',
        'reply_to': 'replyTo',
        'context': 'context'
    }

    def __init__(self, revision=None, comment=None, raw_comment=None, mentions=None, reply_to=None, context=None):
        """
        ScoreCommentCreation - a model defined in Swagger
        """

        self._revision = None
        self._comment = None
        self._raw_comment = None
        self._mentions = None
        self._reply_to = None
        self._context = None

        if revision is not None:
          self.revision = revision
        self.comment = comment
        if raw_comment is not None:
          self.raw_comment = raw_comment
        if mentions is not None:
          self.mentions = mentions
        if reply_to is not None:
          self.reply_to = reply_to
        if context is not None:
          self.context = context

    @property
    def revision(self):
        """
        Gets the revision of this ScoreCommentCreation.
        The unique indentifier of the revision of the score where the comment was added. If this property is unspecified or contains \"last\", the API will automatically take the last revision created. 

        :return: The revision of this ScoreCommentCreation.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this ScoreCommentCreation.
        The unique indentifier of the revision of the score where the comment was added. If this property is unspecified or contains \"last\", the API will automatically take the last revision created. 

        :param revision: The revision of this ScoreCommentCreation.
        :type: str
        """

        self._revision = revision

    @property
    def comment(self):
        """
        Gets the comment of this ScoreCommentCreation.
        The comment text that can includes mentions using the following format: `@[id:username]`. 

        :return: The comment of this ScoreCommentCreation.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this ScoreCommentCreation.
        The comment text that can includes mentions using the following format: `@[id:username]`. 

        :param comment: The comment of this ScoreCommentCreation.
        :type: str
        """
        if comment is None:
            raise ValueError("Invalid value for `comment`, must not be `None`")

        self._comment = comment

    @property
    def raw_comment(self):
        """
        Gets the raw_comment of this ScoreCommentCreation.
        A raw version of the comment, that can be displayed without the mentions. If you use mentions, this property must be set. 

        :return: The raw_comment of this ScoreCommentCreation.
        :rtype: str
        """
        return self._raw_comment

    @raw_comment.setter
    def raw_comment(self, raw_comment):
        """
        Sets the raw_comment of this ScoreCommentCreation.
        A raw version of the comment, that can be displayed without the mentions. If you use mentions, this property must be set. 

        :param raw_comment: The raw_comment of this ScoreCommentCreation.
        :type: str
        """

        self._raw_comment = raw_comment

    @property
    def mentions(self):
        """
        Gets the mentions of this ScoreCommentCreation.
        The list of user identifiers mentioned in this comment

        :return: The mentions of this ScoreCommentCreation.
        :rtype: list[str]
        """
        return self._mentions

    @mentions.setter
    def mentions(self, mentions):
        """
        Sets the mentions of this ScoreCommentCreation.
        The list of user identifiers mentioned in this comment

        :param mentions: The mentions of this ScoreCommentCreation.
        :type: list[str]
        """

        self._mentions = mentions

    @property
    def reply_to(self):
        """
        Gets the reply_to of this ScoreCommentCreation.
        When the comment is a reply to another comment, the unique identifier of the parent comment 

        :return: The reply_to of this ScoreCommentCreation.
        :rtype: str
        """
        return self._reply_to

    @reply_to.setter
    def reply_to(self, reply_to):
        """
        Sets the reply_to of this ScoreCommentCreation.
        When the comment is a reply to another comment, the unique identifier of the parent comment 

        :param reply_to: The reply_to of this ScoreCommentCreation.
        :type: str
        """

        self._reply_to = reply_to

    @property
    def context(self):
        """
        Gets the context of this ScoreCommentCreation.

        :return: The context of this ScoreCommentCreation.
        :rtype: ScoreCommentContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """
        Sets the context of this ScoreCommentCreation.

        :param context: The context of this ScoreCommentCreation.
        :type: ScoreCommentContext
        """

        self._context = context

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
        if not isinstance(other, ScoreCommentCreation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
