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


class LocationBasedServicesKeySpecification(Model):
    """Whether the operation refers to the primary or secondary key.

    All required parameters must be populated in order to send to Azure.

    :param key_type: Required. Whether the operation refers to the primary or
     secondary key. Possible values include: 'primary', 'secondary'
    :type key_type: str or ~azure.mgmt.locationbasedservices.models.KeyType
    """

    _validation = {
        'key_type': {'required': True},
    }

    _attribute_map = {
        'key_type': {'key': 'keyType', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(LocationBasedServicesKeySpecification, self).__init__(**kwargs)
        self.key_type = kwargs.get('key_type', None)
