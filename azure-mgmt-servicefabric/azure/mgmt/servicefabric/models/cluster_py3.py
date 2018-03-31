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

from .resource import Resource


class Cluster(Resource):
    """The cluster resource
    .

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource ID.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :param location: Required. Resource location.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param available_cluster_versions: The Service Fabric runtime versions
     available for this cluster.
    :type available_cluster_versions:
     list[~azure.mgmt.servicefabric.models.ClusterVersionDetails]
    :ivar cluster_id: A service generated unique identifier for the cluster
     resource.
    :vartype cluster_id: str
    :param cluster_state: Possible values include: 'WaitingForNodes',
     'Deploying', 'BaselineUpgrade', 'UpdatingUserConfiguration',
     'UpdatingUserCertificate', 'UpdatingInfrastructure',
     'EnforcingClusterVersion', 'UpgradeServiceUnreachable', 'AutoScale',
     'Ready'
    :type cluster_state: str or ~azure.mgmt.servicefabric.models.enum
    :ivar cluster_endpoint: The Azure Resource Provider endpoint. A system
     service in the cluster connects to this  endpoint.
    :vartype cluster_endpoint: str
    :param cluster_code_version: The Service Fabric runtime version of the
     cluster. This property can only by set the user when **upgradeMode** is
     set to 'Manual'. To get list of available Service Fabric versions for new
     clusters use [ClusterVersion API](./ClusterVersion.md). To get the list of
     available version for existing clusters use **availableClusterVersions**.
    :type cluster_code_version: str
    :param certificate: The certificate to use for securing the cluster. The
     certificate provided will be used for  node to node security within the
     cluster, SSL certificate for cluster management endpoint and default
     admin client.
    :type certificate: ~azure.mgmt.servicefabric.models.CertificateDescription
    :param reliability_level: Possible values include: 'None', 'Bronze',
     'Silver', 'Gold', 'Platinum'
    :type reliability_level: str or ~azure.mgmt.servicefabric.models.enum
    :param upgrade_mode: Possible values include: 'Automatic', 'Manual'
    :type upgrade_mode: str or ~azure.mgmt.servicefabric.models.enum
    :param client_certificate_thumbprints: The list of client certificates
     referenced by thumbprint that are allowed to manage the cluster.
    :type client_certificate_thumbprints:
     list[~azure.mgmt.servicefabric.models.ClientCertificateThumbprint]
    :param client_certificate_common_names: The list of client certificates
     referenced by common name that are allowed to manage the cluster.
    :type client_certificate_common_names:
     list[~azure.mgmt.servicefabric.models.ClientCertificateCommonName]
    :param fabric_settings: The list of custom fabric settings to configure
     the cluster.
    :type fabric_settings:
     list[~azure.mgmt.servicefabric.models.SettingsSectionDescription]
    :param reverse_proxy_certificate: The server certificate used by reverse
     proxy.
    :type reverse_proxy_certificate:
     ~azure.mgmt.servicefabric.models.CertificateDescription
    :param management_endpoint: Required. The http management endpoint of the
     cluster.
    :type management_endpoint: str
    :param node_types: Required. The list of node types in the cluster.
    :type node_types:
     list[~azure.mgmt.servicefabric.models.NodeTypeDescription]
    :param azure_active_directory: The AAD authentication settings of the
     cluster.
    :type azure_active_directory:
     ~azure.mgmt.servicefabric.models.AzureActiveDirectory
    :ivar provisioning_state: The provisioning state of the cluster resource.
     Possible values include: 'Updating', 'Succeeded', 'Failed', 'Canceled'
    :vartype provisioning_state: str or
     ~azure.mgmt.servicefabric.models.ProvisioningState
    :param vm_image: The VM image VMSS has been configured with. Generic names
     such as Windows or Linux can be used.
    :type vm_image: str
    :param diagnostics_storage_account_config: The storage account information
     for storing Service Fabric diagnostic logs.
    :type diagnostics_storage_account_config:
     ~azure.mgmt.servicefabric.models.DiagnosticsStorageAccountConfig
    :param upgrade_description: The policy to use when upgrading the cluster.
    :type upgrade_description:
     ~azure.mgmt.servicefabric.models.ClusterUpgradePolicy
    :param add_on_features: The list of add-on features to enable in the
     cluster.
    :type add_on_features: list[str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'cluster_id': {'readonly': True},
        'cluster_endpoint': {'readonly': True},
        'management_endpoint': {'required': True},
        'node_types': {'required': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'available_cluster_versions': {'key': 'properties.availableClusterVersions', 'type': '[ClusterVersionDetails]'},
        'cluster_id': {'key': 'properties.clusterId', 'type': 'str'},
        'cluster_state': {'key': 'properties.clusterState', 'type': 'str'},
        'cluster_endpoint': {'key': 'properties.clusterEndpoint', 'type': 'str'},
        'cluster_code_version': {'key': 'properties.clusterCodeVersion', 'type': 'str'},
        'certificate': {'key': 'properties.certificate', 'type': 'CertificateDescription'},
        'reliability_level': {'key': 'properties.reliabilityLevel', 'type': 'str'},
        'upgrade_mode': {'key': 'properties.upgradeMode', 'type': 'str'},
        'client_certificate_thumbprints': {'key': 'properties.clientCertificateThumbprints', 'type': '[ClientCertificateThumbprint]'},
        'client_certificate_common_names': {'key': 'properties.clientCertificateCommonNames', 'type': '[ClientCertificateCommonName]'},
        'fabric_settings': {'key': 'properties.fabricSettings', 'type': '[SettingsSectionDescription]'},
        'reverse_proxy_certificate': {'key': 'properties.reverseProxyCertificate', 'type': 'CertificateDescription'},
        'management_endpoint': {'key': 'properties.managementEndpoint', 'type': 'str'},
        'node_types': {'key': 'properties.nodeTypes', 'type': '[NodeTypeDescription]'},
        'azure_active_directory': {'key': 'properties.azureActiveDirectory', 'type': 'AzureActiveDirectory'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'vm_image': {'key': 'properties.vmImage', 'type': 'str'},
        'diagnostics_storage_account_config': {'key': 'properties.diagnosticsStorageAccountConfig', 'type': 'DiagnosticsStorageAccountConfig'},
        'upgrade_description': {'key': 'properties.upgradeDescription', 'type': 'ClusterUpgradePolicy'},
        'add_on_features': {'key': 'properties.addOnFeatures', 'type': '[str]'},
    }

    def __init__(self, *, location: str, management_endpoint: str, node_types, tags=None, available_cluster_versions=None, cluster_state=None, cluster_code_version: str=None, certificate=None, reliability_level=None, upgrade_mode=None, client_certificate_thumbprints=None, client_certificate_common_names=None, fabric_settings=None, reverse_proxy_certificate=None, azure_active_directory=None, vm_image: str=None, diagnostics_storage_account_config=None, upgrade_description=None, add_on_features=None, **kwargs) -> None:
        super(Cluster, self).__init__(location=location, tags=tags, **kwargs)
        self.available_cluster_versions = available_cluster_versions
        self.cluster_id = None
        self.cluster_state = cluster_state
        self.cluster_endpoint = None
        self.cluster_code_version = cluster_code_version
        self.certificate = certificate
        self.reliability_level = reliability_level
        self.upgrade_mode = upgrade_mode
        self.client_certificate_thumbprints = client_certificate_thumbprints
        self.client_certificate_common_names = client_certificate_common_names
        self.fabric_settings = fabric_settings
        self.reverse_proxy_certificate = reverse_proxy_certificate
        self.management_endpoint = management_endpoint
        self.node_types = node_types
        self.azure_active_directory = azure_active_directory
        self.provisioning_state = None
        self.vm_image = vm_image
        self.diagnostics_storage_account_config = diagnostics_storage_account_config
        self.upgrade_description = upgrade_description
        self.add_on_features = add_on_features
