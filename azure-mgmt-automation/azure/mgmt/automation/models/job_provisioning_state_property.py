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


class JobProvisioningStateProperty(Model):
    """The provisioning state property.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar provisioning_state: The provisioning state of the resource. Possible
     values include: 'Failed', 'Succeeded', 'Suspended', 'Processing'
    :vartype provisioning_state: str or
     ~azure.mgmt.automation.models.JobProvisioningState
    """

    _validation = {
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(JobProvisioningStateProperty, self).__init__(**kwargs)
        self.provisioning_state = None
