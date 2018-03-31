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

from .replica_health_state import ReplicaHealthState


class StatelessServiceInstanceHealthState(ReplicaHealthState):
    """Represents the health state of the stateless service instance, which
    contains the instance id and the aggregated health state.

    All required parameters must be populated in order to send to Azure.

    :param aggregated_health_state: The health state of a Service Fabric
     entity such as Cluster, Node, Application, Service, Partition, Replica
     etc. Possible values include: 'Invalid', 'Ok', 'Warning', 'Error',
     'Unknown'
    :type aggregated_health_state: str or
     ~azure.servicefabric.models.HealthState
    :param partition_id: The ID of the partition to which this replica
     belongs.
    :type partition_id: str
    :param service_kind: Required. Constant filled by server.
    :type service_kind: str
    :param replica_id: Id of the stateless service instance on the wire this
     field is called ReplicaId.
    :type replica_id: str
    """

    _validation = {
        'service_kind': {'required': True},
    }

    _attribute_map = {
        'aggregated_health_state': {'key': 'AggregatedHealthState', 'type': 'str'},
        'partition_id': {'key': 'PartitionId', 'type': 'str'},
        'service_kind': {'key': 'ServiceKind', 'type': 'str'},
        'replica_id': {'key': 'ReplicaId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(StatelessServiceInstanceHealthState, self).__init__(**kwargs)
        self.replica_id = kwargs.get('replica_id', None)
        self.service_kind = 'Stateless'
