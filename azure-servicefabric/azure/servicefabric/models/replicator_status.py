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


class ReplicatorStatus(Model):
    """Represents a base class for primary or secondary replicator status.
    Contains information about the service fabric replicator like the
    replication/copy queue utilization, last acknowledgement received
    timestamp, etc.
    .

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: PrimaryReplicatorStatus, SecondaryReplicatorStatus

    All required parameters must be populated in order to send to Azure.

    :param kind: Required. Constant filled by server.
    :type kind: str
    """

    _validation = {
        'kind': {'required': True},
    }

    _attribute_map = {
        'kind': {'key': 'Kind', 'type': 'str'},
    }

    _subtype_map = {
        'kind': {'Primary': 'PrimaryReplicatorStatus', 'SecondaryReplicatorStatus': 'SecondaryReplicatorStatus'}
    }

    def __init__(self, **kwargs):
        super(ReplicatorStatus, self).__init__(**kwargs)
        self.kind = None
