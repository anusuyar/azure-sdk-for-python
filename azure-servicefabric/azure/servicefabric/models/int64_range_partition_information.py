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

from .partition_information import PartitionInformation


class Int64RangePartitionInformation(PartitionInformation):
    """Describes the partition information for the integer range that is based on
    partition schemes.

    All required parameters must be populated in order to send to Azure.

    :param id: An internal ID used by Service Fabric to uniquely identify a
     partition. This is a randomly generated GUID when the service was created.
     The partition id is unique and does not change for the lifetime of the
     service. If the same service was deleted and recreated the ids of its
     partitions would be different.
    :type id: str
    :param service_partition_kind: Required. Constant filled by server.
    :type service_partition_kind: str
    :param low_key: Specifies the minimum key value handled by this partition.
    :type low_key: str
    :param high_key: Specifies the maximum key value handled by this
     partition.
    :type high_key: str
    """

    _validation = {
        'service_partition_kind': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'Id', 'type': 'str'},
        'service_partition_kind': {'key': 'ServicePartitionKind', 'type': 'str'},
        'low_key': {'key': 'LowKey', 'type': 'str'},
        'high_key': {'key': 'HighKey', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Int64RangePartitionInformation, self).__init__(**kwargs)
        self.low_key = kwargs.get('low_key', None)
        self.high_key = kwargs.get('high_key', None)
        self.service_partition_kind = 'Int64Range'
