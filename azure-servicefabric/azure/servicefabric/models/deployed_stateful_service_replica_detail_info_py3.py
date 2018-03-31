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

from .deployed_service_replica_detail_info import DeployedServiceReplicaDetailInfo


class DeployedStatefulServiceReplicaDetailInfo(DeployedServiceReplicaDetailInfo):
    """Information about a stateful replica running in a code package. Please note
    DeployedServiceReplicaQueryResult will contain duplicate data like
    ServiceKind, ServiceName, PartitionId and replicaId.

    All required parameters must be populated in order to send to Azure.

    :param service_name: Full hierarchical name of the service in URI format
     starting with `fabric:`.
    :type service_name: str
    :param partition_id: An internal ID used by Service Fabric to uniquely
     identify a partition. This is a randomly generated GUID when the service
     was created. The partition id is unique and does not change for the
     lifetime of the service. If the same service was deleted and recreated the
     ids of its partitions would be different.
    :type partition_id: str
    :param current_service_operation: Specifies the current active life-cycle
     operation on a stateful service replica or stateless service instance.
     Possible values include: 'Unknown', 'None', 'Open', 'ChangeRole', 'Close',
     'Abort'
    :type current_service_operation: str or
     ~azure.servicefabric.models.ServiceOperationName
    :param current_service_operation_start_time_utc: The start time of the
     current service operation in UTC format.
    :type current_service_operation_start_time_utc: datetime
    :param reported_load: List of load reported by replica.
    :type reported_load:
     list[~azure.servicefabric.models.LoadMetricReportInfo]
    :param service_kind: Required. Constant filled by server.
    :type service_kind: str
    :param replica_id: Id of a stateful service replica. ReplicaId is used by
     Service Fabric to uniquely identify a replica of a partition. It is unique
     within a partition and does not change for the lifetime of the replica. If
     a replica gets dropped and another replica gets created on the same node
     for the same partition, it will get a different value for the id.
     Sometimes the id of a stateless service instance is also referred as a
     replica id.
    :type replica_id: str
    :param current_replicator_operation: Specifies the operation currently
     being executed by the Replicator. Possible values include: 'Invalid',
     'None', 'Open', 'ChangeRole', 'UpdateEpoch', 'Close', 'Abort',
     'OnDataLoss', 'WaitForCatchup', 'Build'
    :type current_replicator_operation: str or
     ~azure.servicefabric.models.ReplicatorOperationName
    :param read_status: Specifies the access status of the partition. Possible
     values include: 'Invalid', 'Granted', 'ReconfigurationPending',
     'NotPrimary', 'NoWriteQuorum'
    :type read_status: str or
     ~azure.servicefabric.models.PartitionAccessStatus
    :param write_status: Specifies the access status of the partition.
     Possible values include: 'Invalid', 'Granted', 'ReconfigurationPending',
     'NotPrimary', 'NoWriteQuorum'
    :type write_status: str or
     ~azure.servicefabric.models.PartitionAccessStatus
    :param replicator_status: Represents a base class for primary or secondary
     replicator status.
     Contains information about the service fabric replicator like the
     replication/copy queue utilization, last acknowledgement received
     timestamp, etc.
    :type replicator_status: ~azure.servicefabric.models.ReplicatorStatus
    :param replica_status: Key value store related information for the
     replica.
    :type replica_status:
     ~azure.servicefabric.models.KeyValueStoreReplicaStatus
    :param deployed_service_replica_query_result: Information about a stateful
     service replica deployed on a node.
    :type deployed_service_replica_query_result:
     ~azure.servicefabric.models.DeployedStatefulServiceReplicaInfo
    """

    _validation = {
        'service_kind': {'required': True},
    }

    _attribute_map = {
        'service_name': {'key': 'ServiceName', 'type': 'str'},
        'partition_id': {'key': 'PartitionId', 'type': 'str'},
        'current_service_operation': {'key': 'CurrentServiceOperation', 'type': 'str'},
        'current_service_operation_start_time_utc': {'key': 'CurrentServiceOperationStartTimeUtc', 'type': 'iso-8601'},
        'reported_load': {'key': 'ReportedLoad', 'type': '[LoadMetricReportInfo]'},
        'service_kind': {'key': 'ServiceKind', 'type': 'str'},
        'replica_id': {'key': 'ReplicaId', 'type': 'str'},
        'current_replicator_operation': {'key': 'CurrentReplicatorOperation', 'type': 'str'},
        'read_status': {'key': 'ReadStatus', 'type': 'str'},
        'write_status': {'key': 'WriteStatus', 'type': 'str'},
        'replicator_status': {'key': 'ReplicatorStatus', 'type': 'ReplicatorStatus'},
        'replica_status': {'key': 'ReplicaStatus', 'type': 'KeyValueStoreReplicaStatus'},
        'deployed_service_replica_query_result': {'key': 'DeployedServiceReplicaQueryResult', 'type': 'DeployedStatefulServiceReplicaInfo'},
    }

    def __init__(self, *, service_name: str=None, partition_id: str=None, current_service_operation=None, current_service_operation_start_time_utc=None, reported_load=None, replica_id: str=None, current_replicator_operation=None, read_status=None, write_status=None, replicator_status=None, replica_status=None, deployed_service_replica_query_result=None, **kwargs) -> None:
        super(DeployedStatefulServiceReplicaDetailInfo, self).__init__(service_name=service_name, partition_id=partition_id, current_service_operation=current_service_operation, current_service_operation_start_time_utc=current_service_operation_start_time_utc, reported_load=reported_load, **kwargs)
        self.replica_id = replica_id
        self.current_replicator_operation = current_replicator_operation
        self.read_status = read_status
        self.write_status = write_status
        self.replicator_status = replicator_status
        self.replica_status = replica_status
        self.deployed_service_replica_query_result = deployed_service_replica_query_result
        self.service_kind = 'Stateful'
