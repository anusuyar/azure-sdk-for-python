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

from .iaa_svm_container import IaaSVMContainer


class AzureIaaSComputeVMContainer(IaaSVMContainer):
    """IaaS VM workload-specific backup item representing an Azure Resource
    Manager virtual machine.

    All required parameters must be populated in order to send to Azure.

    :param friendly_name: Friendly name of the container.
    :type friendly_name: str
    :param backup_management_type: Type of backup managemenent for the
     container. Possible values include: 'Invalid', 'AzureIaasVM', 'MAB',
     'DPM', 'AzureBackupServer', 'AzureSql', 'AzureStorage', 'AzureWorkload',
     'DefaultBackup'
    :type backup_management_type: str or
     ~azure.mgmt.recoveryservicesbackup.models.BackupManagementType
    :param registration_status: Status of registration of the container with
     the Recovery Services Vault.
    :type registration_status: str
    :param health_status: Status of health of the container.
    :type health_status: str
    :param container_type: Required. Constant filled by server.
    :type container_type: str
    :param virtual_machine_id: Fully qualified ARM url of the virtual machine
     represented by this Azure IaaS VM container.
    :type virtual_machine_id: str
    :param virtual_machine_version: Specifies whether the container represents
     a Classic or an Azure Resource Manager VM.
    :type virtual_machine_version: str
    :param resource_group: Resource group name of Recovery Services Vault.
    :type resource_group: str
    """

    _validation = {
        'container_type': {'required': True},
    }

    _attribute_map = {
        'friendly_name': {'key': 'friendlyName', 'type': 'str'},
        'backup_management_type': {'key': 'backupManagementType', 'type': 'str'},
        'registration_status': {'key': 'registrationStatus', 'type': 'str'},
        'health_status': {'key': 'healthStatus', 'type': 'str'},
        'container_type': {'key': 'containerType', 'type': 'str'},
        'virtual_machine_id': {'key': 'virtualMachineId', 'type': 'str'},
        'virtual_machine_version': {'key': 'virtualMachineVersion', 'type': 'str'},
        'resource_group': {'key': 'resourceGroup', 'type': 'str'},
    }

    def __init__(self, *, friendly_name: str=None, backup_management_type=None, registration_status: str=None, health_status: str=None, virtual_machine_id: str=None, virtual_machine_version: str=None, resource_group: str=None, **kwargs) -> None:
        super(AzureIaaSComputeVMContainer, self).__init__(friendly_name=friendly_name, backup_management_type=backup_management_type, registration_status=registration_status, health_status=health_status, virtual_machine_id=virtual_machine_id, virtual_machine_version=virtual_machine_version, resource_group=resource_group, **kwargs)
        self.container_type = 'Microsoft.Compute/virtualMachines'
