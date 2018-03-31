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

from .collection_page import CollectionPage


class ImageGallery(CollectionPage):
    """Defines a link to a webpage that contains a collection of related images.

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
    :ivar name: The name of the thing represented by this object.
    :vartype name: str
    :ivar url: The URL to get more information about the thing represented by
     this object.
    :vartype url: str
    :ivar image: An image of the item.
    :vartype image:
     ~azure.cognitiveservices.search.imagesearch.models.ImageObject
    :ivar description: A short description of the item.
    :vartype description: str
    :ivar alternate_name: An alias for the item
    :vartype alternate_name: str
    :ivar bing_id: An ID that uniquely identifies this item.
    :vartype bing_id: str
    :ivar thumbnail_url: The URL to a thumbnail of the item.
    :vartype thumbnail_url: str
    :ivar provider: The source of the creative work.
    :vartype provider:
     list[~azure.cognitiveservices.search.imagesearch.models.Thing]
    :ivar date_published: The date on which the CreativeWork was published.
    :vartype date_published: str
    :ivar text: Text content of this creative work
    :vartype text: str
    :ivar source: The publisher or social network where the images were found.
     You must attribute the publisher as the source where the collection was
     found.
    :vartype source: str
    :ivar images_count: The number of related images found in the collection.
    :vartype images_count: long
    :ivar followers_count: The number of users on the social network that
     follow the creator.
    :vartype followers_count: long
    """

    _validation = {
        '_type': {'required': True},
        'id': {'readonly': True},
        'read_link': {'readonly': True},
        'web_search_url': {'readonly': True},
        'name': {'readonly': True},
        'url': {'readonly': True},
        'image': {'readonly': True},
        'description': {'readonly': True},
        'alternate_name': {'readonly': True},
        'bing_id': {'readonly': True},
        'thumbnail_url': {'readonly': True},
        'provider': {'readonly': True},
        'date_published': {'readonly': True},
        'text': {'readonly': True},
        'source': {'readonly': True},
        'images_count': {'readonly': True},
        'followers_count': {'readonly': True},
    }

    _attribute_map = {
        '_type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'read_link': {'key': 'readLink', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'image': {'key': 'image', 'type': 'ImageObject'},
        'description': {'key': 'description', 'type': 'str'},
        'alternate_name': {'key': 'alternateName', 'type': 'str'},
        'bing_id': {'key': 'bingId', 'type': 'str'},
        'thumbnail_url': {'key': 'thumbnailUrl', 'type': 'str'},
        'provider': {'key': 'provider', 'type': '[Thing]'},
        'date_published': {'key': 'datePublished', 'type': 'str'},
        'text': {'key': 'text', 'type': 'str'},
        'source': {'key': 'source', 'type': 'str'},
        'images_count': {'key': 'imagesCount', 'type': 'long'},
        'followers_count': {'key': 'followersCount', 'type': 'long'},
    }

    def __init__(self, **kwargs) -> None:
        super(ImageGallery, self).__init__(, **kwargs)
        self.source = None
        self.images_count = None
        self.followers_count = None
        self._type = 'ImageGallery'
