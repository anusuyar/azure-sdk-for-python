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


class DataLakeAnalyticsAccount(Resource):
    """A Data Lake Analytics account object, containing all information associated
    with the named Data Lake Analytics account.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The resource identifer.
    :vartype id: str
    :ivar name: The resource name.
    :vartype name: str
    :ivar type: The resource type.
    :vartype type: str
    :ivar location: The resource location.
    :vartype location: str
    :ivar tags: The resource tags.
    :vartype tags: dict[str, str]
    :ivar account_id: The unique identifier associated with this Data Lake
     Analytics account.
    :vartype account_id: str
    :ivar provisioning_state: The provisioning status of the Data Lake
     Analytics account. Possible values include: 'Failed', 'Creating',
     'Running', 'Succeeded', 'Patching', 'Suspending', 'Resuming', 'Deleting',
     'Deleted', 'Undeleting', 'Canceled'
    :vartype provisioning_state: str or
     ~azure.mgmt.datalake.analytics.account.models.DataLakeAnalyticsAccountStatus
    :ivar state: The state of the Data Lake Analytics account. Possible values
     include: 'Active', 'Suspended'
    :vartype state: str or
     ~azure.mgmt.datalake.analytics.account.models.DataLakeAnalyticsAccountState
    :ivar creation_time: The account creation time.
    :vartype creation_time: datetime
    :ivar last_modified_time: The account last modified time.
    :vartype last_modified_time: datetime
    :ivar endpoint: The full CName endpoint for this account.
    :vartype endpoint: str
    :ivar default_data_lake_store_account: The default Data Lake Store account
     associated with this account.
    :vartype default_data_lake_store_account: str
    :ivar data_lake_store_accounts: The list of Data Lake Store accounts
     associated with this account.
    :vartype data_lake_store_accounts:
     list[~azure.mgmt.datalake.analytics.account.models.DataLakeStoreAccountInformation]
    :ivar storage_accounts: The list of Azure Blob Storage accounts associated
     with this account.
    :vartype storage_accounts:
     list[~azure.mgmt.datalake.analytics.account.models.StorageAccountInformation]
    :ivar compute_policies: The list of compute policies associated with this
     account.
    :vartype compute_policies:
     list[~azure.mgmt.datalake.analytics.account.models.ComputePolicy]
    :ivar firewall_rules: The list of firewall rules associated with this
     account.
    :vartype firewall_rules:
     list[~azure.mgmt.datalake.analytics.account.models.FirewallRule]
    :ivar firewall_state: The current state of the IP address firewall for
     this account. Possible values include: 'Enabled', 'Disabled'
    :vartype firewall_state: str or
     ~azure.mgmt.datalake.analytics.account.models.FirewallState
    :ivar firewall_allow_azure_ips: The current state of allowing or
     disallowing IPs originating within Azure through the firewall. If the
     firewall is disabled, this is not enforced. Possible values include:
     'Enabled', 'Disabled'
    :vartype firewall_allow_azure_ips: str or
     ~azure.mgmt.datalake.analytics.account.models.FirewallAllowAzureIpsState
    :ivar new_tier: The commitment tier for the next month. Possible values
     include: 'Consumption', 'Commitment_100AUHours', 'Commitment_500AUHours',
     'Commitment_1000AUHours', 'Commitment_5000AUHours',
     'Commitment_10000AUHours', 'Commitment_50000AUHours',
     'Commitment_100000AUHours', 'Commitment_500000AUHours'
    :vartype new_tier: str or
     ~azure.mgmt.datalake.analytics.account.models.TierType
    :ivar current_tier: The commitment tier in use for the current month.
     Possible values include: 'Consumption', 'Commitment_100AUHours',
     'Commitment_500AUHours', 'Commitment_1000AUHours',
     'Commitment_5000AUHours', 'Commitment_10000AUHours',
     'Commitment_50000AUHours', 'Commitment_100000AUHours',
     'Commitment_500000AUHours'
    :vartype current_tier: str or
     ~azure.mgmt.datalake.analytics.account.models.TierType
    :ivar max_job_count: The maximum supported jobs running under the account
     at the same time. Default value: 3 .
    :vartype max_job_count: int
    :ivar system_max_job_count: The system defined maximum supported jobs
     running under the account at the same time, which restricts the maximum
     number of running jobs the user can set for the account.
    :vartype system_max_job_count: int
    :ivar max_degree_of_parallelism: The maximum supported degree of
     parallelism for this account. Default value: 30 .
    :vartype max_degree_of_parallelism: int
    :ivar system_max_degree_of_parallelism: The system defined maximum
     supported degree of parallelism for this account, which restricts the
     maximum value of parallelism the user can set for the account.
    :vartype system_max_degree_of_parallelism: int
    :ivar max_degree_of_parallelism_per_job: The maximum supported degree of
     parallelism per job for this account.
    :vartype max_degree_of_parallelism_per_job: int
    :ivar min_priority_per_job: The minimum supported priority per job for
     this account.
    :vartype min_priority_per_job: int
    :ivar query_store_retention: The number of days that job metadata is
     retained. Default value: 30 .
    :vartype query_store_retention: int
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'readonly': True},
        'tags': {'readonly': True},
        'account_id': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'state': {'readonly': True},
        'creation_time': {'readonly': True},
        'last_modified_time': {'readonly': True},
        'endpoint': {'readonly': True},
        'default_data_lake_store_account': {'readonly': True},
        'data_lake_store_accounts': {'readonly': True},
        'storage_accounts': {'readonly': True},
        'compute_policies': {'readonly': True},
        'firewall_rules': {'readonly': True},
        'firewall_state': {'readonly': True},
        'firewall_allow_azure_ips': {'readonly': True},
        'new_tier': {'readonly': True},
        'current_tier': {'readonly': True},
        'max_job_count': {'readonly': True, 'minimum': 1},
        'system_max_job_count': {'readonly': True},
        'max_degree_of_parallelism': {'readonly': True, 'minimum': 1},
        'system_max_degree_of_parallelism': {'readonly': True},
        'max_degree_of_parallelism_per_job': {'readonly': True, 'minimum': 1},
        'min_priority_per_job': {'readonly': True, 'minimum': 1},
        'query_store_retention': {'readonly': True, 'maximum': 180, 'minimum': 1},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'account_id': {'key': 'properties.accountId', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'DataLakeAnalyticsAccountStatus'},
        'state': {'key': 'properties.state', 'type': 'DataLakeAnalyticsAccountState'},
        'creation_time': {'key': 'properties.creationTime', 'type': 'iso-8601'},
        'last_modified_time': {'key': 'properties.lastModifiedTime', 'type': 'iso-8601'},
        'endpoint': {'key': 'properties.endpoint', 'type': 'str'},
        'default_data_lake_store_account': {'key': 'properties.defaultDataLakeStoreAccount', 'type': 'str'},
        'data_lake_store_accounts': {'key': 'properties.dataLakeStoreAccounts', 'type': '[DataLakeStoreAccountInformation]'},
        'storage_accounts': {'key': 'properties.storageAccounts', 'type': '[StorageAccountInformation]'},
        'compute_policies': {'key': 'properties.computePolicies', 'type': '[ComputePolicy]'},
        'firewall_rules': {'key': 'properties.firewallRules', 'type': '[FirewallRule]'},
        'firewall_state': {'key': 'properties.firewallState', 'type': 'FirewallState'},
        'firewall_allow_azure_ips': {'key': 'properties.firewallAllowAzureIps', 'type': 'FirewallAllowAzureIpsState'},
        'new_tier': {'key': 'properties.newTier', 'type': 'TierType'},
        'current_tier': {'key': 'properties.currentTier', 'type': 'TierType'},
        'max_job_count': {'key': 'properties.maxJobCount', 'type': 'int'},
        'system_max_job_count': {'key': 'properties.systemMaxJobCount', 'type': 'int'},
        'max_degree_of_parallelism': {'key': 'properties.maxDegreeOfParallelism', 'type': 'int'},
        'system_max_degree_of_parallelism': {'key': 'properties.systemMaxDegreeOfParallelism', 'type': 'int'},
        'max_degree_of_parallelism_per_job': {'key': 'properties.maxDegreeOfParallelismPerJob', 'type': 'int'},
        'min_priority_per_job': {'key': 'properties.minPriorityPerJob', 'type': 'int'},
        'query_store_retention': {'key': 'properties.queryStoreRetention', 'type': 'int'},
    }

    def __init__(self, **kwargs) -> None:
        super(DataLakeAnalyticsAccount, self).__init__(, **kwargs)
        self.account_id = None
        self.provisioning_state = None
        self.state = None
        self.creation_time = None
        self.last_modified_time = None
        self.endpoint = None
        self.default_data_lake_store_account = None
        self.data_lake_store_accounts = None
        self.storage_accounts = None
        self.compute_policies = None
        self.firewall_rules = None
        self.firewall_state = None
        self.firewall_allow_azure_ips = None
        self.new_tier = None
        self.current_tier = None
        self.max_job_count = None
        self.system_max_job_count = None
        self.max_degree_of_parallelism = None
        self.system_max_degree_of_parallelism = None
        self.max_degree_of_parallelism_per_job = None
        self.min_priority_per_job = None
        self.query_store_retention = None
