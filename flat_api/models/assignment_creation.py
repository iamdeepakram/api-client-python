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


class AssignmentCreation(object):
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
        'title': 'str',
        'description': 'str',
        'attachments': 'list[ClassAttachmentCreation]',
        'due_date': 'datetime',
        'scheduled_date': 'datetime'
    }

    attribute_map = {
        'title': 'title',
        'description': 'description',
        'attachments': 'attachments',
        'due_date': 'dueDate',
        'scheduled_date': 'scheduledDate'
    }

    def __init__(self, title=None, description=None, attachments=None, due_date=None, scheduled_date=None):
        """
        AssignmentCreation - a model defined in Swagger
        """

        self._title = None
        self._description = None
        self._attachments = None
        self._due_date = None
        self._scheduled_date = None

        if title is not None:
          self.title = title
        if description is not None:
          self.description = description
        if attachments is not None:
          self.attachments = attachments
        if due_date is not None:
          self.due_date = due_date
        if scheduled_date is not None:
          self.scheduled_date = scheduled_date

    @property
    def title(self):
        """
        Gets the title of this AssignmentCreation.
        Title of the assignment

        :return: The title of this AssignmentCreation.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this AssignmentCreation.
        Title of the assignment

        :param title: The title of this AssignmentCreation.
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """
        Gets the description of this AssignmentCreation.
        Description and content of the assignment

        :return: The description of this AssignmentCreation.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AssignmentCreation.
        Description and content of the assignment

        :param description: The description of this AssignmentCreation.
        :type: str
        """

        self._description = description

    @property
    def attachments(self):
        """
        Gets the attachments of this AssignmentCreation.

        :return: The attachments of this AssignmentCreation.
        :rtype: list[ClassAttachmentCreation]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """
        Sets the attachments of this AssignmentCreation.

        :param attachments: The attachments of this AssignmentCreation.
        :type: list[ClassAttachmentCreation]
        """

        self._attachments = attachments

    @property
    def due_date(self):
        """
        Gets the due_date of this AssignmentCreation.
        The due date of this assignment, late submissions will be marked as paste due. If not set, the assignment won't have a due date. 

        :return: The due_date of this AssignmentCreation.
        :rtype: datetime
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """
        Sets the due_date of this AssignmentCreation.
        The due date of this assignment, late submissions will be marked as paste due. If not set, the assignment won't have a due date. 

        :param due_date: The due_date of this AssignmentCreation.
        :type: datetime
        """

        self._due_date = due_date

    @property
    def scheduled_date(self):
        """
        Gets the scheduled_date of this AssignmentCreation.
        The publication (scheduled) date of the assignment. If this one is specified, the assignment will only be listed to the teachers of the class. 

        :return: The scheduled_date of this AssignmentCreation.
        :rtype: datetime
        """
        return self._scheduled_date

    @scheduled_date.setter
    def scheduled_date(self, scheduled_date):
        """
        Sets the scheduled_date of this AssignmentCreation.
        The publication (scheduled) date of the assignment. If this one is specified, the assignment will only be listed to the teachers of the class. 

        :param scheduled_date: The scheduled_date of this AssignmentCreation.
        :type: datetime
        """

        self._scheduled_date = scheduled_date

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
        if not isinstance(other, AssignmentCreation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
