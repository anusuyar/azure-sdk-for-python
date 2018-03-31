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

from .retention_policy import RetentionPolicy


class LongTermRetentionPolicy(RetentionPolicy):
    """Long term retention policy.

    All required parameters must be populated in order to send to Azure.

    :param retention_policy_type: Required. Constant filled by server.
    :type retention_policy_type: str
    :param daily_schedule: Daily retention schedule of the protection policy.
    :type daily_schedule:
     ~azure.mgmt.recoveryservicesbackup.models.DailyRetentionSchedule
    :param weekly_schedule: Weekly retention schedule of the protection
     policy.
    :type weekly_schedule:
     ~azure.mgmt.recoveryservicesbackup.models.WeeklyRetentionSchedule
    :param monthly_schedule: Monthly retention schedule of the protection
     policy.
    :type monthly_schedule:
     ~azure.mgmt.recoveryservicesbackup.models.MonthlyRetentionSchedule
    :param yearly_schedule: Yearly retention schedule of the protection
     policy.
    :type yearly_schedule:
     ~azure.mgmt.recoveryservicesbackup.models.YearlyRetentionSchedule
    """

    _validation = {
        'retention_policy_type': {'required': True},
    }

    _attribute_map = {
        'retention_policy_type': {'key': 'retentionPolicyType', 'type': 'str'},
        'daily_schedule': {'key': 'dailySchedule', 'type': 'DailyRetentionSchedule'},
        'weekly_schedule': {'key': 'weeklySchedule', 'type': 'WeeklyRetentionSchedule'},
        'monthly_schedule': {'key': 'monthlySchedule', 'type': 'MonthlyRetentionSchedule'},
        'yearly_schedule': {'key': 'yearlySchedule', 'type': 'YearlyRetentionSchedule'},
    }

    def __init__(self, *, daily_schedule=None, weekly_schedule=None, monthly_schedule=None, yearly_schedule=None, **kwargs) -> None:
        super(LongTermRetentionPolicy, self).__init__(, **kwargs)
        self.daily_schedule = daily_schedule
        self.weekly_schedule = weekly_schedule
        self.monthly_schedule = monthly_schedule
        self.yearly_schedule = yearly_schedule
        self.retention_policy_type = 'LongTermRetentionPolicy'
