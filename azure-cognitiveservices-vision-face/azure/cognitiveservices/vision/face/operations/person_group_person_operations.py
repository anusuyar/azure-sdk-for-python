# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.pipeline import ClientRawResponse

from .. import models


class PersonGroupPersonOperations(object):
    """PersonGroupPersonOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def create(
            self, person_group_id, name=None, user_data=None, custom_headers=None, raw=False, **operation_config):
        """Create a new person in a specified person group.

        :param person_group_id: Id referencing a particular person group.
        :type person_group_id: str
        :param name: User defined name, maximum length is 128.
        :type name: str
        :param user_data: User specified data. Length should not exceed 16KB.
        :type user_data: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Person or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.vision.face.models.Person or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.face.models.APIErrorException>`
        """
        body = models.NameAndUserDataContract(name=name, user_data=user_data)

        # Construct URL
        url = self.create.metadata['url']
        path_format_arguments = {
            'AzureRegion': self._serialize.url("self.config.azure_region", self.config.azure_region, 'AzureRegions', skip_quote=True),
            'personGroupId': self._serialize.url("person_group_id", person_group_id, 'str', max_length=64, pattern=r'^[a-z0-9-_]+$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(body, 'NameAndUserDataContract')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Person', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create.metadata = {'url': '/persongroups/{personGroupId}/persons'}

    def list(
            self, person_group_id, start=None, top=None, custom_headers=None, raw=False, **operation_config):
        """List all persons in a person group, and retrieve person information
        (including personId, name, userData and persistedFaceIds of registered
        faces of the person).

        :param person_group_id: Id referencing a particular person group.
        :type person_group_id: str
        :param start: Starting person id to return (used to list a range of
         persons).
        :type start: str
        :param top: Number of persons to return starting with the person id
         indicated by the 'start' parameter.
        :type top: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: list or ClientRawResponse if raw=true
        :rtype: list[~azure.cognitiveservices.vision.face.models.Person] or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.face.models.APIErrorException>`
        """
        # Construct URL
        url = self.list.metadata['url']
        path_format_arguments = {
            'AzureRegion': self._serialize.url("self.config.azure_region", self.config.azure_region, 'AzureRegions', skip_quote=True),
            'personGroupId': self._serialize.url("person_group_id", person_group_id, 'str', max_length=64, pattern=r'^[a-z0-9-_]+$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if start is not None:
            query_parameters['start'] = self._serialize.query("start", start, 'str')
        if top is not None:
            query_parameters['top'] = self._serialize.query("top", top, 'int', maximum=1000, minimum=1)

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('[Person]', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list.metadata = {'url': '/persongroups/{personGroupId}/persons'}

    def delete(
            self, person_group_id, person_id, custom_headers=None, raw=False, **operation_config):
        """Delete an existing person from a person group. Persisted face images of
        the person will also be deleted.

        :param person_group_id: Id referencing a particular person group.
        :type person_group_id: str
        :param person_id: Id referencing a particular person.
        :type person_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.face.models.APIErrorException>`
        """
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'AzureRegion': self._serialize.url("self.config.azure_region", self.config.azure_region, 'AzureRegions', skip_quote=True),
            'personGroupId': self._serialize.url("person_group_id", person_group_id, 'str', max_length=64, pattern=r'^[a-z0-9-_]+$'),
            'personId': self._serialize.url("person_id", person_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    delete.metadata = {'url': '/persongroups/{personGroupId}/persons/{personId}'}

    def get(
            self, person_group_id, person_id, custom_headers=None, raw=False, **operation_config):
        """Retrieve a person's information, including registered persisted faces,
        name and userData.

        :param person_group_id: Id referencing a particular person group.
        :type person_group_id: str
        :param person_id: Id referencing a particular person.
        :type person_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Person or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.vision.face.models.Person or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.face.models.APIErrorException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'AzureRegion': self._serialize.url("self.config.azure_region", self.config.azure_region, 'AzureRegions', skip_quote=True),
            'personGroupId': self._serialize.url("person_group_id", person_group_id, 'str', max_length=64, pattern=r'^[a-z0-9-_]+$'),
            'personId': self._serialize.url("person_id", person_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Person', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/persongroups/{personGroupId}/persons/{personId}'}

    def update(
            self, person_group_id, person_id, name=None, user_data=None, custom_headers=None, raw=False, **operation_config):
        """Update name or userData of a person.

        :param person_group_id: Id referencing a particular person group.
        :type person_group_id: str
        :param person_id: Id referencing a particular person.
        :type person_id: str
        :param name: User defined name, maximum length is 128.
        :type name: str
        :param user_data: User specified data. Length should not exceed 16KB.
        :type user_data: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.face.models.APIErrorException>`
        """
        body = models.NameAndUserDataContract(name=name, user_data=user_data)

        # Construct URL
        url = self.update.metadata['url']
        path_format_arguments = {
            'AzureRegion': self._serialize.url("self.config.azure_region", self.config.azure_region, 'AzureRegions', skip_quote=True),
            'personGroupId': self._serialize.url("person_group_id", person_group_id, 'str', max_length=64, pattern=r'^[a-z0-9-_]+$'),
            'personId': self._serialize.url("person_id", person_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(body, 'NameAndUserDataContract')

        # Construct and send request
        request = self._client.patch(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    update.metadata = {'url': '/persongroups/{personGroupId}/persons/{personId}'}

    def delete_face(
            self, person_group_id, person_id, persisted_face_id, custom_headers=None, raw=False, **operation_config):
        """Delete a face from a person. Relative image for the persisted face will
        also be deleted.

        :param person_group_id: Id referencing a particular person group.
        :type person_group_id: str
        :param person_id: Id referencing a particular person.
        :type person_id: str
        :param persisted_face_id: Id referencing a particular persistedFaceId
         of an existing face.
        :type persisted_face_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.face.models.APIErrorException>`
        """
        # Construct URL
        url = self.delete_face.metadata['url']
        path_format_arguments = {
            'AzureRegion': self._serialize.url("self.config.azure_region", self.config.azure_region, 'AzureRegions', skip_quote=True),
            'personGroupId': self._serialize.url("person_group_id", person_group_id, 'str', max_length=64, pattern=r'^[a-z0-9-_]+$'),
            'personId': self._serialize.url("person_id", person_id, 'str'),
            'persistedFaceId': self._serialize.url("persisted_face_id", persisted_face_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    delete_face.metadata = {'url': '/persongroups/{personGroupId}/persons/{personId}/persistedFaces/{persistedFaceId}'}

    def get_face(
            self, person_group_id, person_id, persisted_face_id, custom_headers=None, raw=False, **operation_config):
        """Retrieve information about a persisted face (specified by
        persistedFaceId, personId and its belonging personGroupId).

        :param person_group_id: Id referencing a particular person group.
        :type person_group_id: str
        :param person_id: Id referencing a particular person.
        :type person_id: str
        :param persisted_face_id: Id referencing a particular persistedFaceId
         of an existing face.
        :type persisted_face_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PersistedFace or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.vision.face.models.PersistedFace or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.face.models.APIErrorException>`
        """
        # Construct URL
        url = self.get_face.metadata['url']
        path_format_arguments = {
            'AzureRegion': self._serialize.url("self.config.azure_region", self.config.azure_region, 'AzureRegions', skip_quote=True),
            'personGroupId': self._serialize.url("person_group_id", person_group_id, 'str', max_length=64, pattern=r'^[a-z0-9-_]+$'),
            'personId': self._serialize.url("person_id", person_id, 'str'),
            'persistedFaceId': self._serialize.url("persisted_face_id", persisted_face_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PersistedFace', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_face.metadata = {'url': '/persongroups/{personGroupId}/persons/{personId}/persistedFaces/{persistedFaceId}'}

    def update_face(
            self, person_group_id, person_id, persisted_face_id, user_data=None, custom_headers=None, raw=False, **operation_config):
        """Update a person persisted face's userData field.

        :param person_group_id: Id referencing a particular person group.
        :type person_group_id: str
        :param person_id: Id referencing a particular person.
        :type person_id: str
        :param persisted_face_id: Id referencing a particular persistedFaceId
         of an existing face.
        :type persisted_face_id: str
        :param user_data: User-provided data attached to the face. The size
         limit is 1KB.
        :type user_data: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.face.models.APIErrorException>`
        """
        body = models.UpdatePersonFaceRequest(user_data=user_data)

        # Construct URL
        url = self.update_face.metadata['url']
        path_format_arguments = {
            'AzureRegion': self._serialize.url("self.config.azure_region", self.config.azure_region, 'AzureRegions', skip_quote=True),
            'personGroupId': self._serialize.url("person_group_id", person_group_id, 'str', max_length=64, pattern=r'^[a-z0-9-_]+$'),
            'personId': self._serialize.url("person_id", person_id, 'str'),
            'persistedFaceId': self._serialize.url("persisted_face_id", persisted_face_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(body, 'UpdatePersonFaceRequest')

        # Construct and send request
        request = self._client.patch(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    update_face.metadata = {'url': '/persongroups/{personGroupId}/persons/{personId}/persistedFaces/{persistedFaceId}'}

    def add_person_face_from_url(
            self, person_group_id, person_id, url, user_data=None, target_face=None, custom_headers=None, raw=False, **operation_config):
        """Add a representative face to a person for identification. The input
        face is specified as an image with a targetFace rectangle.

        :param person_group_id: Id referencing a particular person group.
        :type person_group_id: str
        :param person_id: Id referencing a particular person.
        :type person_id: str
        :param url:
        :type url: str
        :param user_data: User-specified data about the face for any purpose.
         The maximum length is 1KB.
        :type user_data: str
        :param target_face: A face rectangle to specify the target face to be
         added to a person in the format of "targetFace=left,top,width,height".
         E.g. "targetFace=10,10,100,100". If there is more than one face in the
         image, targetFace is required to specify which face to add. No
         targetFace means there is only one face detected in the entire image.
        :type target_face: list[int]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PersistedFace or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.vision.face.models.PersistedFace or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.face.models.APIErrorException>`
        """
        image_url = models.ImageUrl(url=url)

        # Construct URL
        url = self.add_person_face_from_url.metadata['url']
        path_format_arguments = {
            'AzureRegion': self._serialize.url("self.config.azure_region", self.config.azure_region, 'AzureRegions', skip_quote=True),
            'personGroupId': self._serialize.url("person_group_id", person_group_id, 'str', max_length=64, pattern=r'^[a-z0-9-_]+$'),
            'personId': self._serialize.url("person_id", person_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if user_data is not None:
            query_parameters['userData'] = self._serialize.query("user_data", user_data, 'str', max_length=1024)
        if target_face is not None:
            query_parameters['targetFace'] = self._serialize.query("target_face", target_face, '[int]', div=',')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(image_url, 'ImageUrl')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PersistedFace', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    add_person_face_from_url.metadata = {'url': '/persongroups/{personGroupId}/persons/{personId}/persistedFaces'}

    def add_person_face_from_stream(
            self, person_group_id, person_id, image, user_data=None, target_face=None, custom_headers=None, raw=False, callback=None, **operation_config):
        """Add a representative face to a person for identification. The input
        face is specified as an image with a targetFace rectangle.

        :param person_group_id: Id referencing a particular person group.
        :type person_group_id: str
        :param person_id: Id referencing a particular person.
        :type person_id: str
        :param image: An image stream.
        :type image: Generator
        :param user_data: User-specified data about the face for any purpose.
         The maximum length is 1KB.
        :type user_data: str
        :param target_face: A face rectangle to specify the target face to be
         added to a person in the format of "targetFace=left,top,width,height".
         E.g. "targetFace=10,10,100,100". If there is more than one face in the
         image, targetFace is required to specify which face to add. No
         targetFace means there is only one face detected in the entire image.
        :type target_face: list[int]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param callback: When specified, will be called with each chunk of
         data that is streamed. The callback should take two arguments, the
         bytes of the current chunk of data and the response object. If the
         data is uploading, response will be None.
        :type callback: Callable[Bytes, response=None]
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PersistedFace or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.vision.face.models.PersistedFace or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.face.models.APIErrorException>`
        """
        # Construct URL
        url = self.add_person_face_from_stream.metadata['url']
        path_format_arguments = {
            'AzureRegion': self._serialize.url("self.config.azure_region", self.config.azure_region, 'AzureRegions', skip_quote=True),
            'personGroupId': self._serialize.url("person_group_id", person_group_id, 'str', max_length=64, pattern=r'^[a-z0-9-_]+$'),
            'personId': self._serialize.url("person_id", person_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if user_data is not None:
            query_parameters['userData'] = self._serialize.query("user_data", user_data, 'str', max_length=1024)
        if target_face is not None:
            query_parameters['targetFace'] = self._serialize.query("target_face", target_face, '[int]', div=',')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/octet-stream'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._client.stream_upload(image, callback)

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PersistedFace', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    add_person_face_from_stream.metadata = {'url': '/persongroups/{personGroupId}/persons/{personId}/persistedFaces'}
