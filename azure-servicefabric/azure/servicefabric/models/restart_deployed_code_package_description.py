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


class RestartDeployedCodePackageDescription(Model):
    """Defines description for restarting a deployed code package on Service
    Fabric node.
    .

    All required parameters must be populated in order to send to Azure.

    :param service_manifest_name: Required. The name of service manifest that
     specified this code package.
    :type service_manifest_name: str
    :param service_package_activation_id: The ActivationId of a deployed
     service package. If ServicePackageActivationMode specified at the time of
     creating the service
     is 'SharedProcess' (or if it is not specified, in which case it defaults
     to 'SharedProcess'), then value of ServicePackageActivationId
     is always an empty string.
    :type service_package_activation_id: str
    :param code_package_name: Required. The name of the code package defined
     in the service manifest.
    :type code_package_name: str
    :param code_package_instance_id: Required. The instance ID for currently
     running entry point. For a code package setup entry point (if specified)
     runs first and after it finishes main entry point is started.
     Each time entry point executable is run, its instance id will change. If 0
     is passed in as the code package instance ID, the API will restart the
     code package with whatever instance ID it is currently running.
     If an instance ID other than 0 is passed in, the API will restart the code
     package only if the current Instance ID matches the passed in instance ID.
     Note, passing in the exact instance ID (not 0) in the API is safer,
     because if ensures at most one restart of the code package.
    :type code_package_instance_id: str
    """

    _validation = {
        'service_manifest_name': {'required': True},
        'code_package_name': {'required': True},
        'code_package_instance_id': {'required': True},
    }

    _attribute_map = {
        'service_manifest_name': {'key': 'ServiceManifestName', 'type': 'str'},
        'service_package_activation_id': {'key': 'ServicePackageActivationId', 'type': 'str'},
        'code_package_name': {'key': 'CodePackageName', 'type': 'str'},
        'code_package_instance_id': {'key': 'CodePackageInstanceId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(RestartDeployedCodePackageDescription, self).__init__(**kwargs)
        self.service_manifest_name = kwargs.get('service_manifest_name', None)
        self.service_package_activation_id = kwargs.get('service_package_activation_id', None)
        self.code_package_name = kwargs.get('code_package_name', None)
        self.code_package_instance_id = kwargs.get('code_package_instance_id', None)
