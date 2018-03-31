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

from .service_info import ServiceInfo


class StatelessServiceInfo(ServiceInfo):
    """Information about a stateless Service Fabric service.

    All required parameters must be populated in order to send to Azure.

    :param id: The identity of the service. This is an encoded representation
     of the service name. This is used in the REST APIs to identify the service
     resource.
     Starting in version 6.0, hierarchical names are delimited with the "\\~"
     character. For example, if the service name is "fabric:/myapp/app1/svc1",
     the service identity would be "myapp~app1\\~svc1" in 6.0+ and
     "myapp/app1/svc1" in previous versions.
    :type id: str
    :param name: The full name of the service with 'fabric:' URI scheme.
    :type name: str
    :param type_name: Name of the service type as specified in the service
     manifest.
    :type type_name: str
    :param manifest_version: The version of the service manifest.
    :type manifest_version: str
    :param health_state: The health state of a Service Fabric entity such as
     Cluster, Node, Application, Service, Partition, Replica etc. Possible
     values include: 'Invalid', 'Ok', 'Warning', 'Error', 'Unknown'
    :type health_state: str or ~azure.servicefabric.models.HealthState
    :param service_status: The status of the application. Possible values
     include: 'Unknown', 'Active', 'Upgrading', 'Deleting', 'Creating',
     'Failed'
    :type service_status: str or ~azure.servicefabric.models.ServiceStatus
    :param is_service_group: Whether the service is in a service group.
    :type is_service_group: bool
    :param service_kind: Required. Constant filled by server.
    :type service_kind: str
    """

    _validation = {
        'service_kind': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'Id', 'type': 'str'},
        'name': {'key': 'Name', 'type': 'str'},
        'type_name': {'key': 'TypeName', 'type': 'str'},
        'manifest_version': {'key': 'ManifestVersion', 'type': 'str'},
        'health_state': {'key': 'HealthState', 'type': 'str'},
        'service_status': {'key': 'ServiceStatus', 'type': 'str'},
        'is_service_group': {'key': 'IsServiceGroup', 'type': 'bool'},
        'service_kind': {'key': 'ServiceKind', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(StatelessServiceInfo, self).__init__(**kwargs)
        self.service_kind = 'Stateless'
