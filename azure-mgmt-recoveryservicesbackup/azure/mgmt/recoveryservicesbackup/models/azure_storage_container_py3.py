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

from .protection_container import ProtectionContainer


class AzureStorageContainer(ProtectionContainer):
    """Azure Storage Account workload-specific container.

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
    :param source_resource_id: Fully qualified ARM url.
    :type source_resource_id: str
    :param storage_account_version: Storage account version.
    :type storage_account_version: str
    :param resource_group: Resource group name of Recovery Services Vault.
    :type resource_group: str
    :param protected_item_count: Number of items backed up in this container.
    :type protected_item_count: long
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
        'source_resource_id': {'key': 'sourceResourceId', 'type': 'str'},
        'storage_account_version': {'key': 'storageAccountVersion', 'type': 'str'},
        'resource_group': {'key': 'resourceGroup', 'type': 'str'},
        'protected_item_count': {'key': 'protectedItemCount', 'type': 'long'},
    }

    def __init__(self, *, friendly_name: str=None, backup_management_type=None, registration_status: str=None, health_status: str=None, source_resource_id: str=None, storage_account_version: str=None, resource_group: str=None, protected_item_count: int=None, **kwargs) -> None:
        super(AzureStorageContainer, self).__init__(friendly_name=friendly_name, backup_management_type=backup_management_type, registration_status=registration_status, health_status=health_status, **kwargs)
        self.source_resource_id = source_resource_id
        self.storage_account_version = storage_account_version
        self.resource_group = resource_group
        self.protected_item_count = protected_item_count
        self.container_type = 'StorageContainer'
