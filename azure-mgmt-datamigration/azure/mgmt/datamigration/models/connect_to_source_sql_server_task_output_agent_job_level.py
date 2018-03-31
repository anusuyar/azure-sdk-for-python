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

from .connect_to_source_sql_server_task_output import ConnectToSourceSqlServerTaskOutput


class ConnectToSourceSqlServerTaskOutputAgentJobLevel(ConnectToSourceSqlServerTaskOutput):
    """AgentJob level output for the task that validates connection to SQL Server
    and also validates source server requirements.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Result identifier
    :vartype id: str
    :param result_type: Required. Constant filled by server.
    :type result_type: str
    :ivar name: AgentJob name
    :vartype name: str
    :ivar job_category: The type of AgentJob.
    :vartype job_category: str
    :ivar is_enabled: The state of the original AgentJob.
    :vartype is_enabled: bool
    :ivar job_owner: The owner of the AgentJob
    :vartype job_owner: str
    :ivar last_executed_on: UTC Date and time when the AgentJob was last
     executed.
    :vartype last_executed_on: datetime
    :ivar migration_eligibility: Information about eligiblity of agent job for
     migration.
    :vartype migration_eligibility:
     ~azure.mgmt.datamigration.models.MigrationEligibilityInfo
    """

    _validation = {
        'id': {'readonly': True},
        'result_type': {'required': True},
        'name': {'readonly': True},
        'job_category': {'readonly': True},
        'is_enabled': {'readonly': True},
        'job_owner': {'readonly': True},
        'last_executed_on': {'readonly': True},
        'migration_eligibility': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'result_type': {'key': 'resultType', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'job_category': {'key': 'jobCategory', 'type': 'str'},
        'is_enabled': {'key': 'isEnabled', 'type': 'bool'},
        'job_owner': {'key': 'jobOwner', 'type': 'str'},
        'last_executed_on': {'key': 'lastExecutedOn', 'type': 'iso-8601'},
        'migration_eligibility': {'key': 'migrationEligibility', 'type': 'MigrationEligibilityInfo'},
    }

    def __init__(self, **kwargs):
        super(ConnectToSourceSqlServerTaskOutputAgentJobLevel, self).__init__(**kwargs)
        self.name = None
        self.job_category = None
        self.is_enabled = None
        self.job_owner = None
        self.last_executed_on = None
        self.migration_eligibility = None
        self.result_type = 'AgentJobLevelOutput'
