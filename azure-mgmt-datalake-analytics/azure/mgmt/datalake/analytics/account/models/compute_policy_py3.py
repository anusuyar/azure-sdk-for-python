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

from .sub_resource import SubResource


class ComputePolicy(SubResource):
    """Data Lake Analytics compute policy information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The resource identifier.
    :vartype id: str
    :ivar name: The resource name.
    :vartype name: str
    :ivar type: The resource type.
    :vartype type: str
    :ivar object_id: The AAD object identifier for the entity to create a
     policy for.
    :vartype object_id: str
    :ivar object_type: The type of AAD object the object identifier refers to.
     Possible values include: 'User', 'Group', 'ServicePrincipal'
    :vartype object_type: str or
     ~azure.mgmt.datalake.analytics.account.models.AADObjectType
    :ivar max_degree_of_parallelism_per_job: The maximum degree of parallelism
     per job this user can use to submit jobs.
    :vartype max_degree_of_parallelism_per_job: int
    :ivar min_priority_per_job: The minimum priority per job this user can use
     to submit jobs.
    :vartype min_priority_per_job: int
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'object_id': {'readonly': True},
        'object_type': {'readonly': True},
        'max_degree_of_parallelism_per_job': {'readonly': True, 'minimum': 1},
        'min_priority_per_job': {'readonly': True, 'minimum': 1},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'object_id': {'key': 'properties.objectId', 'type': 'str'},
        'object_type': {'key': 'properties.objectType', 'type': 'str'},
        'max_degree_of_parallelism_per_job': {'key': 'properties.maxDegreeOfParallelismPerJob', 'type': 'int'},
        'min_priority_per_job': {'key': 'properties.minPriorityPerJob', 'type': 'int'},
    }

    def __init__(self, **kwargs) -> None:
        super(ComputePolicy, self).__init__(, **kwargs)
        self.object_id = None
        self.object_type = None
        self.max_degree_of_parallelism_per_job = None
        self.min_priority_per_job = None
