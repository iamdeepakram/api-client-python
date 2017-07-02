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


class AssignmentSubmissionUpdate(object):
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
        'attachments': 'list[ClassAttachmentCreation]',
        'student_comment': 'str',
        'submit': 'bool',
        'return_feedback': 'str'
    }

    attribute_map = {
        'attachments': 'attachments',
        'student_comment': 'studentComment',
        'submit': 'submit',
        'return_feedback': 'returnFeedback'
    }

    def __init__(self, attachments=None, student_comment=None, submit=None, return_feedback=None):
        """
        AssignmentSubmissionUpdate - a model defined in Swagger
        """

        self._attachments = None
        self._student_comment = None
        self._submit = None
        self._return_feedback = None

        if attachments is not None:
          self.attachments = attachments
        if student_comment is not None:
          self.student_comment = student_comment
        if submit is not None:
          self.submit = submit
        if return_feedback is not None:
          self.return_feedback = return_feedback

    @property
    def attachments(self):
        """
        Gets the attachments of this AssignmentSubmissionUpdate.

        :return: The attachments of this AssignmentSubmissionUpdate.
        :rtype: list[ClassAttachmentCreation]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """
        Sets the attachments of this AssignmentSubmissionUpdate.

        :param attachments: The attachments of this AssignmentSubmissionUpdate.
        :type: list[ClassAttachmentCreation]
        """

        self._attachments = attachments

    @property
    def student_comment(self):
        """
        Gets the student_comment of this AssignmentSubmissionUpdate.
        An optionnal comment sent by the student when submitting his work 

        :return: The student_comment of this AssignmentSubmissionUpdate.
        :rtype: str
        """
        return self._student_comment

    @student_comment.setter
    def student_comment(self, student_comment):
        """
        Sets the student_comment of this AssignmentSubmissionUpdate.
        An optionnal comment sent by the student when submitting his work 

        :param student_comment: The student_comment of this AssignmentSubmissionUpdate.
        :type: str
        """

        self._student_comment = student_comment

    @property
    def submit(self):
        """
        Gets the submit of this AssignmentSubmissionUpdate.
        If `true`, the submission will be marked as done

        :return: The submit of this AssignmentSubmissionUpdate.
        :rtype: bool
        """
        return self._submit

    @submit.setter
    def submit(self, submit):
        """
        Sets the submit of this AssignmentSubmissionUpdate.
        If `true`, the submission will be marked as done

        :param submit: The submit of this AssignmentSubmissionUpdate.
        :type: bool
        """

        self._submit = submit

    @property
    def return_feedback(self):
        """
        Gets the return_feedback of this AssignmentSubmissionUpdate.
        The feedback associated with the return

        :return: The return_feedback of this AssignmentSubmissionUpdate.
        :rtype: str
        """
        return self._return_feedback

    @return_feedback.setter
    def return_feedback(self, return_feedback):
        """
        Sets the return_feedback of this AssignmentSubmissionUpdate.
        The feedback associated with the return

        :param return_feedback: The return_feedback of this AssignmentSubmissionUpdate.
        :type: str
        """

        self._return_feedback = return_feedback

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
        if not isinstance(other, AssignmentSubmissionUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
