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

from .response import Response


class RecognizedEntity(Response):
    """Defines a recognized entity.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param _type: Required. Constant filled by server.
    :type _type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar read_link: The URL that returns this resource.
    :vartype read_link: str
    :ivar web_search_url: The URL To Bing's search result for this item.
    :vartype web_search_url: str
    :ivar entity: The entity that was recognized. The following are the
     possible entity objects: Person
    :vartype entity: ~azure.cognitiveservices.search.imagesearch.models.Thing
    :ivar match_confidence: The confidence that Bing has that the entity in
     the image matches this entity. The confidence ranges from 0.0 through 1.0
     with 1.0 being very confident.
    :vartype match_confidence: float
    """

    _validation = {
        '_type': {'required': True},
        'id': {'readonly': True},
        'read_link': {'readonly': True},
        'web_search_url': {'readonly': True},
        'entity': {'readonly': True},
        'match_confidence': {'readonly': True},
    }

    _attribute_map = {
        '_type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'read_link': {'key': 'readLink', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'entity': {'key': 'entity', 'type': 'Thing'},
        'match_confidence': {'key': 'matchConfidence', 'type': 'float'},
    }

    def __init__(self, **kwargs) -> None:
        super(RecognizedEntity, self).__init__(, **kwargs)
        self.entity = None
        self.match_confidence = None
        self._type = 'RecognizedEntity'
