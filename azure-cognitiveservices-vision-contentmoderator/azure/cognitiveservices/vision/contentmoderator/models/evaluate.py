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

from msrest.serialization import Model


class Evaluate(Model):
    """Evaluate response object.

    :param cache_id: The cache id.
    :type cache_id: str
    :param result: Evaluate result.
    :type result: bool
    :param tracking_id: The tracking id.
    :type tracking_id: str
    :param adult_classification_score: The adult classification score.
    :type adult_classification_score: float
    :param is_image_adult_classified: Indicates if an image is classified as
     adult.
    :type is_image_adult_classified: bool
    :param racy_classification_score: The racy classication score.
    :type racy_classification_score: float
    :param is_image_racy_classified: Indicates if the image is classified as
     racy.
    :type is_image_racy_classified: bool
    :param advanced_info: The advanced info.
    :type advanced_info:
     list[~azure.cognitiveservices.vision.contentmoderator.models.KeyValuePair]
    :param status: The evaluate status
    :type status:
     ~azure.cognitiveservices.vision.contentmoderator.models.Status
    """

    _attribute_map = {
        'cache_id': {'key': 'CacheID', 'type': 'str'},
        'result': {'key': 'Result', 'type': 'bool'},
        'tracking_id': {'key': 'TrackingId', 'type': 'str'},
        'adult_classification_score': {'key': 'AdultClassificationScore', 'type': 'float'},
        'is_image_adult_classified': {'key': 'IsImageAdultClassified', 'type': 'bool'},
        'racy_classification_score': {'key': 'RacyClassificationScore', 'type': 'float'},
        'is_image_racy_classified': {'key': 'IsImageRacyClassified', 'type': 'bool'},
        'advanced_info': {'key': 'AdvancedInfo', 'type': '[KeyValuePair]'},
        'status': {'key': 'Status', 'type': 'Status'},
    }

    def __init__(self, **kwargs):
        super(Evaluate, self).__init__(**kwargs)
        self.cache_id = kwargs.get('cache_id', None)
        self.result = kwargs.get('result', None)
        self.tracking_id = kwargs.get('tracking_id', None)
        self.adult_classification_score = kwargs.get('adult_classification_score', None)
        self.is_image_adult_classified = kwargs.get('is_image_adult_classified', None)
        self.racy_classification_score = kwargs.get('racy_classification_score', None)
        self.is_image_racy_classified = kwargs.get('is_image_racy_classified', None)
        self.advanced_info = kwargs.get('advanced_info', None)
        self.status = kwargs.get('status', None)
