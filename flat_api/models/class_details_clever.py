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


class ClassDetailsClever(object):
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
        'creation_date': 'datetime',
        'modification_date': 'datetime',
        'subject': 'str',
        'term_name': 'str',
        'term_start_date': 'datetime',
        'term_end_date': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'creation_date': 'creationDate',
        'modification_date': 'modificationDate',
        'subject': 'subject',
        'term_name': 'termName',
        'term_start_date': 'termStartDate',
        'term_end_date': 'termEndDate'
    }

    def __init__(self, id=None, creation_date=None, modification_date=None, subject=None, term_name=None, term_start_date=None, term_end_date=None, local_vars_configuration=None):  # noqa: E501
        """ClassDetailsClever - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._creation_date = None
        self._modification_date = None
        self._subject = None
        self._term_name = None
        self._term_start_date = None
        self._term_end_date = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if creation_date is not None:
            self.creation_date = creation_date
        if modification_date is not None:
            self.modification_date = modification_date
        if subject is not None:
            self.subject = subject
        if term_name is not None:
            self.term_name = term_name
        if term_start_date is not None:
            self.term_start_date = term_start_date
        if term_end_date is not None:
            self.term_end_date = term_end_date

    @property
    def id(self):
        """Gets the id of this ClassDetailsClever.  # noqa: E501

        Clever section unique identifier  # noqa: E501

        :return: The id of this ClassDetailsClever.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClassDetailsClever.

        Clever section unique identifier  # noqa: E501

        :param id: The id of this ClassDetailsClever.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def creation_date(self):
        """Gets the creation_date of this ClassDetailsClever.  # noqa: E501

        The creation date of the section on clever  # noqa: E501

        :return: The creation_date of this ClassDetailsClever.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this ClassDetailsClever.

        The creation date of the section on clever  # noqa: E501

        :param creation_date: The creation_date of this ClassDetailsClever.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def modification_date(self):
        """Gets the modification_date of this ClassDetailsClever.  # noqa: E501

        The last modification date of the section on clever  # noqa: E501

        :return: The modification_date of this ClassDetailsClever.  # noqa: E501
        :rtype: datetime
        """
        return self._modification_date

    @modification_date.setter
    def modification_date(self, modification_date):
        """Sets the modification_date of this ClassDetailsClever.

        The last modification date of the section on clever  # noqa: E501

        :param modification_date: The modification_date of this ClassDetailsClever.  # noqa: E501
        :type: datetime
        """

        self._modification_date = modification_date

    @property
    def subject(self):
        """Gets the subject of this ClassDetailsClever.  # noqa: E501

        Normalized subject of the course  # noqa: E501

        :return: The subject of this ClassDetailsClever.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this ClassDetailsClever.

        Normalized subject of the course  # noqa: E501

        :param subject: The subject of this ClassDetailsClever.  # noqa: E501
        :type: str
        """
        allowed_values = ["english/language arts", "math", "science", "social studies", "language", "homeroom/advisory", "interventions/online learning", "technology and engineering", "PE and health", "arts and music", "other"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and subject not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `subject` ({0}), must be one of {1}"  # noqa: E501
                .format(subject, allowed_values)
            )

        self._subject = subject

    @property
    def term_name(self):
        """Gets the term_name of this ClassDetailsClever.  # noqa: E501

        Name of the term when this course happens  # noqa: E501

        :return: The term_name of this ClassDetailsClever.  # noqa: E501
        :rtype: str
        """
        return self._term_name

    @term_name.setter
    def term_name(self, term_name):
        """Sets the term_name of this ClassDetailsClever.

        Name of the term when this course happens  # noqa: E501

        :param term_name: The term_name of this ClassDetailsClever.  # noqa: E501
        :type: str
        """

        self._term_name = term_name

    @property
    def term_start_date(self):
        """Gets the term_start_date of this ClassDetailsClever.  # noqa: E501

        Beginning date of the term  # noqa: E501

        :return: The term_start_date of this ClassDetailsClever.  # noqa: E501
        :rtype: datetime
        """
        return self._term_start_date

    @term_start_date.setter
    def term_start_date(self, term_start_date):
        """Sets the term_start_date of this ClassDetailsClever.

        Beginning date of the term  # noqa: E501

        :param term_start_date: The term_start_date of this ClassDetailsClever.  # noqa: E501
        :type: datetime
        """

        self._term_start_date = term_start_date

    @property
    def term_end_date(self):
        """Gets the term_end_date of this ClassDetailsClever.  # noqa: E501

        End date of the term  # noqa: E501

        :return: The term_end_date of this ClassDetailsClever.  # noqa: E501
        :rtype: datetime
        """
        return self._term_end_date

    @term_end_date.setter
    def term_end_date(self, term_end_date):
        """Sets the term_end_date of this ClassDetailsClever.

        End date of the term  # noqa: E501

        :param term_end_date: The term_end_date of this ClassDetailsClever.  # noqa: E501
        :type: datetime
        """

        self._term_end_date = term_end_date

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
        if not isinstance(other, ClassDetailsClever):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClassDetailsClever):
            return True

        return self.to_dict() != other.to_dict()
