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


class MigrationValidationDatabaseSummaryResult(Model):
    """Migration Validation Database level summary result.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Result identifier
    :vartype id: str
    :ivar migration_id: Migration Identifier
    :vartype migration_id: str
    :ivar source_database_name: Name of the source database
    :vartype source_database_name: str
    :ivar target_database_name: Name of the target database
    :vartype target_database_name: str
    :ivar started_on: Validation start time
    :vartype started_on: datetime
    :ivar ended_on: Validation end time
    :vartype ended_on: datetime
    :ivar status: Current status of validation at the database level. Possible
     values include: 'Default', 'NotStarted', 'Initialized', 'InProgress',
     'Completed', 'CompletedWithIssues', 'Failed', 'Stopped'
    :vartype status: str or ~azure.mgmt.datamigration.models.ValidationStatus
    """

    _validation = {
        'id': {'readonly': True},
        'migration_id': {'readonly': True},
        'source_database_name': {'readonly': True},
        'target_database_name': {'readonly': True},
        'started_on': {'readonly': True},
        'ended_on': {'readonly': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'migration_id': {'key': 'migrationId', 'type': 'str'},
        'source_database_name': {'key': 'sourceDatabaseName', 'type': 'str'},
        'target_database_name': {'key': 'targetDatabaseName', 'type': 'str'},
        'started_on': {'key': 'startedOn', 'type': 'iso-8601'},
        'ended_on': {'key': 'endedOn', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(MigrationValidationDatabaseSummaryResult, self).__init__(**kwargs)
        self.id = None
        self.migration_id = None
        self.source_database_name = None
        self.target_database_name = None
        self.started_on = None
        self.ended_on = None
        self.status = None
