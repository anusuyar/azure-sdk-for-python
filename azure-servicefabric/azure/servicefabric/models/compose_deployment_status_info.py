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


class ComposeDeploymentStatusInfo(Model):
    """Information about a Service Fabric compose deployment.

    :param name: The name of the deployment.
    :type name: str
    :param application_name: The name of the application, including the
     'fabric:' URI scheme.
    :type application_name: str
    :param status: The status of the compose deployment. Possible values
     include: 'Invalid', 'Provisioning', 'Creating', 'Ready', 'Unprovisioning',
     'Deleting', 'Failed', 'Upgrading'
    :type status: str or ~azure.servicefabric.models.ComposeDeploymentStatus
    :param status_details: The status details of compose deployment including
     failure message.
    :type status_details: str
    """

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'application_name': {'key': 'ApplicationName', 'type': 'str'},
        'status': {'key': 'Status', 'type': 'str'},
        'status_details': {'key': 'StatusDetails', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ComposeDeploymentStatusInfo, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.application_name = kwargs.get('application_name', None)
        self.status = kwargs.get('status', None)
        self.status_details = kwargs.get('status_details', None)
