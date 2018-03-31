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


class MonitorConfig(Model):
    """Class containing endpoint monitoring settings in a Traffic Manager profile.

    :param profile_monitor_status: The profile-level monitoring status of the
     Traffic Manager profile. Possible values include: 'CheckingEndpoints',
     'Online', 'Degraded', 'Disabled', 'Inactive'
    :type profile_monitor_status: str or
     ~azure.mgmt.trafficmanager.models.ProfileMonitorStatus
    :param protocol: The protocol (HTTP, HTTPS or TCP) used to probe for
     endpoint health. Possible values include: 'HTTP', 'HTTPS', 'TCP'
    :type protocol: str or ~azure.mgmt.trafficmanager.models.MonitorProtocol
    :param port: The TCP port used to probe for endpoint health.
    :type port: long
    :param path: The path relative to the endpoint domain name used to probe
     for endpoint health.
    :type path: str
    :param interval_in_seconds: The monitor interval for endpoints in this
     profile. This is the interval at which Traffic Manager will check the
     health of each endpoint in this profile.
    :type interval_in_seconds: long
    :param timeout_in_seconds: The monitor timeout for endpoints in this
     profile. This is the time that Traffic Manager allows endpoints in this
     profile to response to the health check.
    :type timeout_in_seconds: long
    :param tolerated_number_of_failures: The number of consecutive failed
     health check that Traffic Manager tolerates before declaring an endpoint
     in this profile Degraded after the next failed health check.
    :type tolerated_number_of_failures: long
    """

    _attribute_map = {
        'profile_monitor_status': {'key': 'profileMonitorStatus', 'type': 'str'},
        'protocol': {'key': 'protocol', 'type': 'str'},
        'port': {'key': 'port', 'type': 'long'},
        'path': {'key': 'path', 'type': 'str'},
        'interval_in_seconds': {'key': 'intervalInSeconds', 'type': 'long'},
        'timeout_in_seconds': {'key': 'timeoutInSeconds', 'type': 'long'},
        'tolerated_number_of_failures': {'key': 'toleratedNumberOfFailures', 'type': 'long'},
    }

    def __init__(self, **kwargs):
        super(MonitorConfig, self).__init__(**kwargs)
        self.profile_monitor_status = kwargs.get('profile_monitor_status', None)
        self.protocol = kwargs.get('protocol', None)
        self.port = kwargs.get('port', None)
        self.path = kwargs.get('path', None)
        self.interval_in_seconds = kwargs.get('interval_in_seconds', None)
        self.timeout_in_seconds = kwargs.get('timeout_in_seconds', None)
        self.tolerated_number_of_failures = kwargs.get('tolerated_number_of_failures', None)
