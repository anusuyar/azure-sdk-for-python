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


class ClusterUpgradeProgressObject(Model):
    """Information about a cluster upgrade.

    :param code_version: The ServiceFabric code version of the cluster.
    :type code_version: str
    :param config_version: The cluster configuration version (specified in the
     cluster manifest).
    :type config_version: str
    :param upgrade_domains: List of upgrade domains and their statuses.
    :type upgrade_domains: list[~azure.servicefabric.models.UpgradeDomainInfo]
    :param upgrade_state: The state of the upgrade domain. Possible values
     include: 'Invalid', 'RollingBackInProgress', 'RollingBackCompleted',
     'RollingForwardPending', 'RollingForwardInProgress',
     'RollingForwardCompleted', 'Failed'
    :type upgrade_state: str or ~azure.servicefabric.models.UpgradeState
    :param next_upgrade_domain: The name of the next upgrade domain to be
     processed.
    :type next_upgrade_domain: str
    :param rolling_upgrade_mode: The mode used to monitor health during a
     rolling upgrade. Possible values include: 'Invalid', 'UnmonitoredAuto',
     'UnmonitoredManual', 'Monitored'. Default value: "UnmonitoredAuto" .
    :type rolling_upgrade_mode: str or ~azure.servicefabric.models.UpgradeMode
    :param upgrade_description: Represents a ServiceFabric cluster upgrade
    :type upgrade_description:
     ~azure.servicefabric.models.ClusterUpgradeDescriptionObject
    :param upgrade_duration_in_milliseconds: The estimated elapsed time spent
     processing the current overall upgrade.
    :type upgrade_duration_in_milliseconds: str
    :param upgrade_domain_duration_in_milliseconds: The estimated elapsed time
     spent processing the current upgrade domain.
    :type upgrade_domain_duration_in_milliseconds: str
    :param unhealthy_evaluations: List of health evaluations that resulted in
     the current aggregated health state.
    :type unhealthy_evaluations:
     list[~azure.servicefabric.models.HealthEvaluationWrapper]
    :param current_upgrade_domain_progress: Information about the current
     in-progress upgrade domain.
    :type current_upgrade_domain_progress:
     ~azure.servicefabric.models.CurrentUpgradeDomainProgressInfo
    :param start_timestamp_utc: The start time of the upgrade in UTC.
    :type start_timestamp_utc: str
    :param failure_timestamp_utc: The failure time of the upgrade in UTC.
    :type failure_timestamp_utc: str
    :param failure_reason: The cause of an upgrade failure that resulted in
     FailureAction being executed. Possible values include: 'None',
     'Interrupted', 'HealthCheck', 'UpgradeDomainTimeout',
     'OverallUpgradeTimeout'
    :type failure_reason: str or ~azure.servicefabric.models.FailureReason
    :param upgrade_domain_progress_at_failure: The detailed upgrade progress
     for nodes in the current upgrade domain at the point of failure.
    :type upgrade_domain_progress_at_failure:
     ~azure.servicefabric.models.FailedUpgradeDomainProgressObject
    """

    _attribute_map = {
        'code_version': {'key': 'CodeVersion', 'type': 'str'},
        'config_version': {'key': 'ConfigVersion', 'type': 'str'},
        'upgrade_domains': {'key': 'UpgradeDomains', 'type': '[UpgradeDomainInfo]'},
        'upgrade_state': {'key': 'UpgradeState', 'type': 'str'},
        'next_upgrade_domain': {'key': 'NextUpgradeDomain', 'type': 'str'},
        'rolling_upgrade_mode': {'key': 'RollingUpgradeMode', 'type': 'str'},
        'upgrade_description': {'key': 'UpgradeDescription', 'type': 'ClusterUpgradeDescriptionObject'},
        'upgrade_duration_in_milliseconds': {'key': 'UpgradeDurationInMilliseconds', 'type': 'str'},
        'upgrade_domain_duration_in_milliseconds': {'key': 'UpgradeDomainDurationInMilliseconds', 'type': 'str'},
        'unhealthy_evaluations': {'key': 'UnhealthyEvaluations', 'type': '[HealthEvaluationWrapper]'},
        'current_upgrade_domain_progress': {'key': 'CurrentUpgradeDomainProgress', 'type': 'CurrentUpgradeDomainProgressInfo'},
        'start_timestamp_utc': {'key': 'StartTimestampUtc', 'type': 'str'},
        'failure_timestamp_utc': {'key': 'FailureTimestampUtc', 'type': 'str'},
        'failure_reason': {'key': 'FailureReason', 'type': 'str'},
        'upgrade_domain_progress_at_failure': {'key': 'UpgradeDomainProgressAtFailure', 'type': 'FailedUpgradeDomainProgressObject'},
    }

    def __init__(self, *, code_version: str=None, config_version: str=None, upgrade_domains=None, upgrade_state=None, next_upgrade_domain: str=None, rolling_upgrade_mode="UnmonitoredAuto", upgrade_description=None, upgrade_duration_in_milliseconds: str=None, upgrade_domain_duration_in_milliseconds: str=None, unhealthy_evaluations=None, current_upgrade_domain_progress=None, start_timestamp_utc: str=None, failure_timestamp_utc: str=None, failure_reason=None, upgrade_domain_progress_at_failure=None, **kwargs) -> None:
        super(ClusterUpgradeProgressObject, self).__init__(**kwargs)
        self.code_version = code_version
        self.config_version = config_version
        self.upgrade_domains = upgrade_domains
        self.upgrade_state = upgrade_state
        self.next_upgrade_domain = next_upgrade_domain
        self.rolling_upgrade_mode = rolling_upgrade_mode
        self.upgrade_description = upgrade_description
        self.upgrade_duration_in_milliseconds = upgrade_duration_in_milliseconds
        self.upgrade_domain_duration_in_milliseconds = upgrade_domain_duration_in_milliseconds
        self.unhealthy_evaluations = unhealthy_evaluations
        self.current_upgrade_domain_progress = current_upgrade_domain_progress
        self.start_timestamp_utc = start_timestamp_utc
        self.failure_timestamp_utc = failure_timestamp_utc
        self.failure_reason = failure_reason
        self.upgrade_domain_progress_at_failure = upgrade_domain_progress_at_failure
