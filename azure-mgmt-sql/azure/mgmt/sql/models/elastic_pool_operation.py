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

from .proxy_resource import ProxyResource


class ElasticPoolOperation(ProxyResource):
    """A elastic pool operation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar elastic_pool_name: The name of the elastic pool the operation is
     being performed on.
    :vartype elastic_pool_name: str
    :ivar operation: The name of operation.
    :vartype operation: str
    :ivar operation_friendly_name: The friendly name of operation.
    :vartype operation_friendly_name: str
    :ivar percent_complete: The percentage of the operation completed.
    :vartype percent_complete: int
    :ivar server_name: The name of the server.
    :vartype server_name: str
    :ivar start_time: The operation start time.
    :vartype start_time: datetime
    :ivar state: The operation state.
    :vartype state: str
    :ivar error_code: The operation error code.
    :vartype error_code: int
    :ivar error_description: The operation error description.
    :vartype error_description: str
    :ivar error_severity: The operation error severity.
    :vartype error_severity: int
    :ivar is_user_error: Whether or not the error is a user error.
    :vartype is_user_error: bool
    :ivar estimated_completion_time: The estimated completion time of the
     operation.
    :vartype estimated_completion_time: datetime
    :ivar description: The operation description.
    :vartype description: str
    :ivar is_cancellable: Whether the operation can be cancelled.
    :vartype is_cancellable: bool
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'elastic_pool_name': {'readonly': True},
        'operation': {'readonly': True},
        'operation_friendly_name': {'readonly': True},
        'percent_complete': {'readonly': True},
        'server_name': {'readonly': True},
        'start_time': {'readonly': True},
        'state': {'readonly': True},
        'error_code': {'readonly': True},
        'error_description': {'readonly': True},
        'error_severity': {'readonly': True},
        'is_user_error': {'readonly': True},
        'estimated_completion_time': {'readonly': True},
        'description': {'readonly': True},
        'is_cancellable': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'elastic_pool_name': {'key': 'properties.elasticPoolName', 'type': 'str'},
        'operation': {'key': 'properties.operation', 'type': 'str'},
        'operation_friendly_name': {'key': 'properties.operationFriendlyName', 'type': 'str'},
        'percent_complete': {'key': 'properties.percentComplete', 'type': 'int'},
        'server_name': {'key': 'properties.serverName', 'type': 'str'},
        'start_time': {'key': 'properties.startTime', 'type': 'iso-8601'},
        'state': {'key': 'properties.state', 'type': 'str'},
        'error_code': {'key': 'properties.errorCode', 'type': 'int'},
        'error_description': {'key': 'properties.errorDescription', 'type': 'str'},
        'error_severity': {'key': 'properties.errorSeverity', 'type': 'int'},
        'is_user_error': {'key': 'properties.isUserError', 'type': 'bool'},
        'estimated_completion_time': {'key': 'properties.estimatedCompletionTime', 'type': 'iso-8601'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'is_cancellable': {'key': 'properties.isCancellable', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(ElasticPoolOperation, self).__init__(**kwargs)
        self.elastic_pool_name = None
        self.operation = None
        self.operation_friendly_name = None
        self.percent_complete = None
        self.server_name = None
        self.start_time = None
        self.state = None
        self.error_code = None
        self.error_description = None
        self.error_severity = None
        self.is_user_error = None
        self.estimated_completion_time = None
        self.description = None
        self.is_cancellable = None
