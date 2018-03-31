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


class CreateDataLakeStoreAccountParameters(Model):
    """CreateDataLakeStoreAccountParameters.

    All required parameters must be populated in order to send to Azure.

    :param location: Required. The resource location.
    :type location: str
    :param tags: The resource tags.
    :type tags: dict[str, str]
    :param identity: The Key Vault encryption identity, if any.
    :type identity: ~azure.mgmt.datalake.store.models.EncryptionIdentity
    :param default_group: The default owner group for all new folders and
     files created in the Data Lake Store account.
    :type default_group: str
    :param encryption_config: The Key Vault encryption configuration.
    :type encryption_config:
     ~azure.mgmt.datalake.store.models.EncryptionConfig
    :param encryption_state: The current state of encryption for this Data
     Lake Store account. Possible values include: 'Enabled', 'Disabled'
    :type encryption_state: str or
     ~azure.mgmt.datalake.store.models.EncryptionState
    :param firewall_rules: The list of firewall rules associated with this
     Data Lake Store account.
    :type firewall_rules:
     list[~azure.mgmt.datalake.store.models.CreateFirewallRuleWithAccountParameters]
    :param firewall_state: The current state of the IP address firewall for
     this Data Lake Store account. Possible values include: 'Enabled',
     'Disabled'
    :type firewall_state: str or
     ~azure.mgmt.datalake.store.models.FirewallState
    :param firewall_allow_azure_ips: The current state of allowing or
     disallowing IPs originating within Azure through the firewall. If the
     firewall is disabled, this is not enforced. Possible values include:
     'Enabled', 'Disabled'
    :type firewall_allow_azure_ips: str or
     ~azure.mgmt.datalake.store.models.FirewallAllowAzureIpsState
    :param trusted_id_providers: The list of trusted identity providers
     associated with this Data Lake Store account.
    :type trusted_id_providers:
     list[~azure.mgmt.datalake.store.models.CreateTrustedIdProviderWithAccountParameters]
    :param trusted_id_provider_state: The current state of the trusted
     identity provider feature for this Data Lake Store account. Possible
     values include: 'Enabled', 'Disabled'
    :type trusted_id_provider_state: str or
     ~azure.mgmt.datalake.store.models.TrustedIdProviderState
    :param new_tier: The commitment tier to use for next month. Possible
     values include: 'Consumption', 'Commitment_1TB', 'Commitment_10TB',
     'Commitment_100TB', 'Commitment_500TB', 'Commitment_1PB', 'Commitment_5PB'
    :type new_tier: str or ~azure.mgmt.datalake.store.models.TierType
    """

    _validation = {
        'location': {'required': True},
    }

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'identity': {'key': 'identity', 'type': 'EncryptionIdentity'},
        'default_group': {'key': 'properties.defaultGroup', 'type': 'str'},
        'encryption_config': {'key': 'properties.encryptionConfig', 'type': 'EncryptionConfig'},
        'encryption_state': {'key': 'properties.encryptionState', 'type': 'EncryptionState'},
        'firewall_rules': {'key': 'properties.firewallRules', 'type': '[CreateFirewallRuleWithAccountParameters]'},
        'firewall_state': {'key': 'properties.firewallState', 'type': 'FirewallState'},
        'firewall_allow_azure_ips': {'key': 'properties.firewallAllowAzureIps', 'type': 'FirewallAllowAzureIpsState'},
        'trusted_id_providers': {'key': 'properties.trustedIdProviders', 'type': '[CreateTrustedIdProviderWithAccountParameters]'},
        'trusted_id_provider_state': {'key': 'properties.trustedIdProviderState', 'type': 'TrustedIdProviderState'},
        'new_tier': {'key': 'properties.newTier', 'type': 'TierType'},
    }

    def __init__(self, **kwargs):
        super(CreateDataLakeStoreAccountParameters, self).__init__(**kwargs)
        self.location = kwargs.get('location', None)
        self.tags = kwargs.get('tags', None)
        self.identity = kwargs.get('identity', None)
        self.default_group = kwargs.get('default_group', None)
        self.encryption_config = kwargs.get('encryption_config', None)
        self.encryption_state = kwargs.get('encryption_state', None)
        self.firewall_rules = kwargs.get('firewall_rules', None)
        self.firewall_state = kwargs.get('firewall_state', None)
        self.firewall_allow_azure_ips = kwargs.get('firewall_allow_azure_ips', None)
        self.trusted_id_providers = kwargs.get('trusted_id_providers', None)
        self.trusted_id_provider_state = kwargs.get('trusted_id_provider_state', None)
        self.new_tier = kwargs.get('new_tier', None)
