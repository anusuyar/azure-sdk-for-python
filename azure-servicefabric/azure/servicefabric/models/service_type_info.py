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


class ServiceTypeInfo(Model):
    """Information about a service type that is defined in a service manifest of a
    provisioned application type.

    :param service_type_description: Describes a service type defined in the
     service manifest of a provisioned application type. The properties the the
     ones defined in the service manifest.
    :type service_type_description:
     ~azure.servicefabric.models.ServiceTypeDescription
    :param service_manifest_name: The name of the service manifest in which
     this service type is defined.
    :type service_manifest_name: str
    :param service_manifest_version: The version of the service manifest in
     which this service type is defined.
    :type service_manifest_version: str
    :param is_service_group: Indicates whether the service is a service group.
     If it is, the property value is true otherwise false.
    :type is_service_group: bool
    """

    _attribute_map = {
        'service_type_description': {'key': 'ServiceTypeDescription', 'type': 'ServiceTypeDescription'},
        'service_manifest_name': {'key': 'ServiceManifestName', 'type': 'str'},
        'service_manifest_version': {'key': 'ServiceManifestVersion', 'type': 'str'},
        'is_service_group': {'key': 'IsServiceGroup', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(ServiceTypeInfo, self).__init__(**kwargs)
        self.service_type_description = kwargs.get('service_type_description', None)
        self.service_manifest_name = kwargs.get('service_manifest_name', None)
        self.service_manifest_version = kwargs.get('service_manifest_version', None)
        self.is_service_group = kwargs.get('is_service_group', None)
