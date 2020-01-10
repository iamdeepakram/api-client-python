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


class ClassDetails(object):
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
        'state': 'ClassState',
        'name': 'str',
        'section': 'str',
        'description': 'str',
        'organization': 'str',
        'owner': 'str',
        'creation_date': 'datetime',
        'enrollment_code': 'str',
        'theme': 'str',
        'assignments_count': 'float',
        'students_group': 'GroupDetails',
        'teachers_group': 'GroupDetails',
        'google_classroom': 'ClassDetailsGoogleClassroom',
        'google_drive': 'ClassDetailsGoogleDrive',
        'microsoft_graph': 'ClassDetailsMicrosoftGraph',
        'lti': 'ClassDetailsLti',
        'canvas': 'ClassDetailsCanvas',
        'clever': 'ClassDetailsClever'
    }

    attribute_map = {
        'id': 'id',
        'state': 'state',
        'name': 'name',
        'section': 'section',
        'description': 'description',
        'organization': 'organization',
        'owner': 'owner',
        'creation_date': 'creationDate',
        'enrollment_code': 'enrollmentCode',
        'theme': 'theme',
        'assignments_count': 'assignmentsCount',
        'students_group': 'studentsGroup',
        'teachers_group': 'teachersGroup',
        'google_classroom': 'googleClassroom',
        'google_drive': 'googleDrive',
        'microsoft_graph': 'microsoftGraph',
        'lti': 'lti',
        'canvas': 'canvas',
        'clever': 'clever'
    }

    def __init__(self, id=None, state=None, name=None, section=None, description=None, organization=None, owner=None, creation_date=None, enrollment_code=None, theme=None, assignments_count=None, students_group=None, teachers_group=None, google_classroom=None, google_drive=None, microsoft_graph=None, lti=None, canvas=None, clever=None, local_vars_configuration=None):  # noqa: E501
        """ClassDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._state = None
        self._name = None
        self._section = None
        self._description = None
        self._organization = None
        self._owner = None
        self._creation_date = None
        self._enrollment_code = None
        self._theme = None
        self._assignments_count = None
        self._students_group = None
        self._teachers_group = None
        self._google_classroom = None
        self._google_drive = None
        self._microsoft_graph = None
        self._lti = None
        self._canvas = None
        self._clever = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if state is not None:
            self.state = state
        if name is not None:
            self.name = name
        if section is not None:
            self.section = section
        if description is not None:
            self.description = description
        if organization is not None:
            self.organization = organization
        if owner is not None:
            self.owner = owner
        if creation_date is not None:
            self.creation_date = creation_date
        if enrollment_code is not None:
            self.enrollment_code = enrollment_code
        if theme is not None:
            self.theme = theme
        if assignments_count is not None:
            self.assignments_count = assignments_count
        if students_group is not None:
            self.students_group = students_group
        if teachers_group is not None:
            self.teachers_group = teachers_group
        if google_classroom is not None:
            self.google_classroom = google_classroom
        if google_drive is not None:
            self.google_drive = google_drive
        if microsoft_graph is not None:
            self.microsoft_graph = microsoft_graph
        if lti is not None:
            self.lti = lti
        if canvas is not None:
            self.canvas = canvas
        if clever is not None:
            self.clever = clever

    @property
    def id(self):
        """Gets the id of this ClassDetails.  # noqa: E501

        The unique identifier of the class  # noqa: E501

        :return: The id of this ClassDetails.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClassDetails.

        The unique identifier of the class  # noqa: E501

        :param id: The id of this ClassDetails.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def state(self):
        """Gets the state of this ClassDetails.  # noqa: E501


        :return: The state of this ClassDetails.  # noqa: E501
        :rtype: ClassState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ClassDetails.


        :param state: The state of this ClassDetails.  # noqa: E501
        :type: ClassState
        """

        self._state = state

    @property
    def name(self):
        """Gets the name of this ClassDetails.  # noqa: E501

        The name of the class  # noqa: E501

        :return: The name of this ClassDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClassDetails.

        The name of the class  # noqa: E501

        :param name: The name of this ClassDetails.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def section(self):
        """Gets the section of this ClassDetails.  # noqa: E501

        The section of the class  # noqa: E501

        :return: The section of this ClassDetails.  # noqa: E501
        :rtype: str
        """
        return self._section

    @section.setter
    def section(self, section):
        """Sets the section of this ClassDetails.

        The section of the class  # noqa: E501

        :param section: The section of this ClassDetails.  # noqa: E501
        :type: str
        """

        self._section = section

    @property
    def description(self):
        """Gets the description of this ClassDetails.  # noqa: E501

        An optionnal description for this class  # noqa: E501

        :return: The description of this ClassDetails.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ClassDetails.

        An optionnal description for this class  # noqa: E501

        :param description: The description of this ClassDetails.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def organization(self):
        """Gets the organization of this ClassDetails.  # noqa: E501

        The unique identifier of the Organization owning this class  # noqa: E501

        :return: The organization of this ClassDetails.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this ClassDetails.

        The unique identifier of the Organization owning this class  # noqa: E501

        :param organization: The organization of this ClassDetails.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def owner(self):
        """Gets the owner of this ClassDetails.  # noqa: E501

        The unique identifier of the User owning this class  # noqa: E501

        :return: The owner of this ClassDetails.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ClassDetails.

        The unique identifier of the User owning this class  # noqa: E501

        :param owner: The owner of this ClassDetails.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def creation_date(self):
        """Gets the creation_date of this ClassDetails.  # noqa: E501

        The date when the class was create  # noqa: E501

        :return: The creation_date of this ClassDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this ClassDetails.

        The date when the class was create  # noqa: E501

        :param creation_date: The creation_date of this ClassDetails.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def enrollment_code(self):
        """Gets the enrollment_code of this ClassDetails.  # noqa: E501

        [Teachers only] The enrollment code that can be used by the students to join the class   # noqa: E501

        :return: The enrollment_code of this ClassDetails.  # noqa: E501
        :rtype: str
        """
        return self._enrollment_code

    @enrollment_code.setter
    def enrollment_code(self, enrollment_code):
        """Sets the enrollment_code of this ClassDetails.

        [Teachers only] The enrollment code that can be used by the students to join the class   # noqa: E501

        :param enrollment_code: The enrollment_code of this ClassDetails.  # noqa: E501
        :type: str
        """

        self._enrollment_code = enrollment_code

    @property
    def theme(self):
        """Gets the theme of this ClassDetails.  # noqa: E501

        The theme identifier using in Flat User Interface  # noqa: E501

        :return: The theme of this ClassDetails.  # noqa: E501
        :rtype: str
        """
        return self._theme

    @theme.setter
    def theme(self, theme):
        """Sets the theme of this ClassDetails.

        The theme identifier using in Flat User Interface  # noqa: E501

        :param theme: The theme of this ClassDetails.  # noqa: E501
        :type: str
        """

        self._theme = theme

    @property
    def assignments_count(self):
        """Gets the assignments_count of this ClassDetails.  # noqa: E501

        The number of assignments created in the class  # noqa: E501

        :return: The assignments_count of this ClassDetails.  # noqa: E501
        :rtype: float
        """
        return self._assignments_count

    @assignments_count.setter
    def assignments_count(self, assignments_count):
        """Sets the assignments_count of this ClassDetails.

        The number of assignments created in the class  # noqa: E501

        :param assignments_count: The assignments_count of this ClassDetails.  # noqa: E501
        :type: float
        """

        self._assignments_count = assignments_count

    @property
    def students_group(self):
        """Gets the students_group of this ClassDetails.  # noqa: E501


        :return: The students_group of this ClassDetails.  # noqa: E501
        :rtype: GroupDetails
        """
        return self._students_group

    @students_group.setter
    def students_group(self, students_group):
        """Sets the students_group of this ClassDetails.


        :param students_group: The students_group of this ClassDetails.  # noqa: E501
        :type: GroupDetails
        """

        self._students_group = students_group

    @property
    def teachers_group(self):
        """Gets the teachers_group of this ClassDetails.  # noqa: E501


        :return: The teachers_group of this ClassDetails.  # noqa: E501
        :rtype: GroupDetails
        """
        return self._teachers_group

    @teachers_group.setter
    def teachers_group(self, teachers_group):
        """Sets the teachers_group of this ClassDetails.


        :param teachers_group: The teachers_group of this ClassDetails.  # noqa: E501
        :type: GroupDetails
        """

        self._teachers_group = teachers_group

    @property
    def google_classroom(self):
        """Gets the google_classroom of this ClassDetails.  # noqa: E501


        :return: The google_classroom of this ClassDetails.  # noqa: E501
        :rtype: ClassDetailsGoogleClassroom
        """
        return self._google_classroom

    @google_classroom.setter
    def google_classroom(self, google_classroom):
        """Sets the google_classroom of this ClassDetails.


        :param google_classroom: The google_classroom of this ClassDetails.  # noqa: E501
        :type: ClassDetailsGoogleClassroom
        """

        self._google_classroom = google_classroom

    @property
    def google_drive(self):
        """Gets the google_drive of this ClassDetails.  # noqa: E501


        :return: The google_drive of this ClassDetails.  # noqa: E501
        :rtype: ClassDetailsGoogleDrive
        """
        return self._google_drive

    @google_drive.setter
    def google_drive(self, google_drive):
        """Sets the google_drive of this ClassDetails.


        :param google_drive: The google_drive of this ClassDetails.  # noqa: E501
        :type: ClassDetailsGoogleDrive
        """

        self._google_drive = google_drive

    @property
    def microsoft_graph(self):
        """Gets the microsoft_graph of this ClassDetails.  # noqa: E501


        :return: The microsoft_graph of this ClassDetails.  # noqa: E501
        :rtype: ClassDetailsMicrosoftGraph
        """
        return self._microsoft_graph

    @microsoft_graph.setter
    def microsoft_graph(self, microsoft_graph):
        """Sets the microsoft_graph of this ClassDetails.


        :param microsoft_graph: The microsoft_graph of this ClassDetails.  # noqa: E501
        :type: ClassDetailsMicrosoftGraph
        """

        self._microsoft_graph = microsoft_graph

    @property
    def lti(self):
        """Gets the lti of this ClassDetails.  # noqa: E501


        :return: The lti of this ClassDetails.  # noqa: E501
        :rtype: ClassDetailsLti
        """
        return self._lti

    @lti.setter
    def lti(self, lti):
        """Sets the lti of this ClassDetails.


        :param lti: The lti of this ClassDetails.  # noqa: E501
        :type: ClassDetailsLti
        """

        self._lti = lti

    @property
    def canvas(self):
        """Gets the canvas of this ClassDetails.  # noqa: E501


        :return: The canvas of this ClassDetails.  # noqa: E501
        :rtype: ClassDetailsCanvas
        """
        return self._canvas

    @canvas.setter
    def canvas(self, canvas):
        """Sets the canvas of this ClassDetails.


        :param canvas: The canvas of this ClassDetails.  # noqa: E501
        :type: ClassDetailsCanvas
        """

        self._canvas = canvas

    @property
    def clever(self):
        """Gets the clever of this ClassDetails.  # noqa: E501


        :return: The clever of this ClassDetails.  # noqa: E501
        :rtype: ClassDetailsClever
        """
        return self._clever

    @clever.setter
    def clever(self, clever):
        """Sets the clever of this ClassDetails.


        :param clever: The clever of this ClassDetails.  # noqa: E501
        :type: ClassDetailsClever
        """

        self._clever = clever

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
        if not isinstance(other, ClassDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClassDetails):
            return True

        return self.to_dict() != other.to_dict()
