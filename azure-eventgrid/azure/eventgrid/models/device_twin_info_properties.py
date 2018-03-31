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


class DeviceTwinInfoProperties(Model):
    """Properties JSON element.

    :param desired: A portion of the properties that can be written only by
     the application back-end, and read by the device.
    :type desired: ~azure.eventgrid.models.DeviceTwinProperties
    :param reported: A portion of the properties that can be written only by
     the device, and read by the application back-end.
    :type reported: ~azure.eventgrid.models.DeviceTwinProperties
    """

    _attribute_map = {
        'desired': {'key': 'desired', 'type': 'DeviceTwinProperties'},
        'reported': {'key': 'reported', 'type': 'DeviceTwinProperties'},
    }

    def __init__(self, **kwargs):
        super(DeviceTwinInfoProperties, self).__init__(**kwargs)
        self.desired = kwargs.get('desired', None)
        self.reported = kwargs.get('reported', None)
