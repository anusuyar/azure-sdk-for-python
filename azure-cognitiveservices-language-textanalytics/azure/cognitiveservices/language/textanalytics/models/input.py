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


class Input(Model):
    """Input.

    :param id: Unique, non-empty document identifier.
    :type id: str
    :param text:
    :type text: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'text': {'key': 'text', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Input, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.text = kwargs.get('text', None)
