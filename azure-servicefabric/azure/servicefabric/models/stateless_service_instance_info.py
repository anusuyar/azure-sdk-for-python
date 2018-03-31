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

from .replica_info import ReplicaInfo


class StatelessServiceInstanceInfo(ReplicaInfo):
    """Represents a stateless service instance. This includes information about
    the identity, status, health, node name, uptime, and other details about
    the instance.

    All required parameters must be populated in order to send to Azure.

    :param replica_status: The status of a replica of a service. Possible
     values are following.
     -Invalid - Indicates the replica status is invalid. All Service Fabric
     enumerations have the invalid type. The value is zero.
     -InBuild - The replica is being built. This means that a primary replica
     is seeding this replica. The value is 1.
     -Standby - The replica is in standby. The value is 2.
     -Ready - The replica is ready. The value is 3.
     -Down - The replica is down. The value is 4.
     -Dropped - Replica is dropped. This means that the replica has been
     removed from the replica set. If it is persisted, its state has been
     deleted. The value is 5.
     . Possible values include: 'Invalid', 'InBuild', 'Standby', 'Ready',
     'Down', 'Dropped'
    :type replica_status: str or ~azure.servicefabric.models.enum
    :param health_state: The health state of a Service Fabric entity such as
     Cluster, Node, Application, Service, Partition, Replica etc. Possible
     values include: 'Invalid', 'Ok', 'Warning', 'Error', 'Unknown'
    :type health_state: str or ~azure.servicefabric.models.HealthState
    :param node_name: The name of a Service Fabric node.
    :type node_name: str
    :param address: The address the replica is listening on.
    :type address: str
    :param last_in_build_duration_in_seconds: The last in build duration of
     the replica in seconds.
    :type last_in_build_duration_in_seconds: str
    :param service_kind: Required. Constant filled by server.
    :type service_kind: str
    :param instance_id: Id of a stateless service instance. InstanceId is used
     by Service Fabric to uniquely identify an instance of a partition of a
     stateless service. It is unique within a partition and does not change for
     the lifetime of the instance. If the instance has failed over on the same
     or different node, it will get a different value for the InstanceId.
    :type instance_id: str
    """

    _validation = {
        'service_kind': {'required': True},
    }

    _attribute_map = {
        'replica_status': {'key': 'ReplicaStatus', 'type': 'str'},
        'health_state': {'key': 'HealthState', 'type': 'str'},
        'node_name': {'key': 'NodeName', 'type': 'str'},
        'address': {'key': 'Address', 'type': 'str'},
        'last_in_build_duration_in_seconds': {'key': 'LastInBuildDurationInSeconds', 'type': 'str'},
        'service_kind': {'key': 'ServiceKind', 'type': 'str'},
        'instance_id': {'key': 'InstanceId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(StatelessServiceInstanceInfo, self).__init__(**kwargs)
        self.instance_id = kwargs.get('instance_id', None)
        self.service_kind = 'Stateless'
