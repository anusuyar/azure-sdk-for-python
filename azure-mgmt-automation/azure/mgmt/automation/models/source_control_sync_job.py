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


class SourceControlSyncJob(Model):
    """Definition of the source control sync job.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar id: Resource id.
    :vartype id: str
    :param source_control_sync_job_id: Gets the source control sync job id.
    :type source_control_sync_job_id: str
    :ivar creation_time: Gets the creation time of the job.
    :vartype creation_time: datetime
    :param provisioning_state: Gets the provisioning state of the job.
     Possible values include: 'Completed', 'Failed', 'Running'
    :type provisioning_state: str or
     ~azure.mgmt.automation.models.ProvisioningState
    :ivar start_time: Gets the start time of the job.
    :vartype start_time: datetime
    :ivar end_time: Gets the end time of the job.
    :vartype end_time: datetime
    :param started_by: Gets the user who started the sync job.
    :type started_by: str
    """

    _validation = {
        'name': {'readonly': True},
        'type': {'readonly': True},
        'id': {'readonly': True},
        'creation_time': {'readonly': True},
        'start_time': {'readonly': True},
        'end_time': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'source_control_sync_job_id': {'key': 'properties.sourceControlSyncJobId', 'type': 'str'},
        'creation_time': {'key': 'properties.creationTime', 'type': 'iso-8601'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'start_time': {'key': 'properties.startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'properties.endTime', 'type': 'iso-8601'},
        'started_by': {'key': 'properties.startedBy', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SourceControlSyncJob, self).__init__(**kwargs)
        self.name = None
        self.type = None
        self.id = None
        self.source_control_sync_job_id = kwargs.get('source_control_sync_job_id', None)
        self.creation_time = None
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.start_time = None
        self.end_time = None
        self.started_by = kwargs.get('started_by', None)
