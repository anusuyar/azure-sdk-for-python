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

from .tracked_resource import TrackedResource


class Profile(TrackedResource):
    """Class representing a Traffic Manager profile.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficManagerProfiles/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Network/trafficmanagerProfiles.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: The Azure Region where the resource lives
    :type location: str
    :param profile_status: The status of the Traffic Manager profile. Possible
     values include: 'Enabled', 'Disabled'
    :type profile_status: str or
     ~azure.mgmt.trafficmanager.models.ProfileStatus
    :param traffic_routing_method: The traffic routing method of the Traffic
     Manager profile. Possible values include: 'Performance', 'Priority',
     'Weighted', 'Geographic'
    :type traffic_routing_method: str or
     ~azure.mgmt.trafficmanager.models.TrafficRoutingMethod
    :param dns_config: The DNS settings of the Traffic Manager profile.
    :type dns_config: ~azure.mgmt.trafficmanager.models.DnsConfig
    :param monitor_config: The endpoint monitoring settings of the Traffic
     Manager profile.
    :type monitor_config: ~azure.mgmt.trafficmanager.models.MonitorConfig
    :param endpoints: The list of endpoints in the Traffic Manager profile.
    :type endpoints: list[~azure.mgmt.trafficmanager.models.Endpoint]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'profile_status': {'key': 'properties.profileStatus', 'type': 'str'},
        'traffic_routing_method': {'key': 'properties.trafficRoutingMethod', 'type': 'str'},
        'dns_config': {'key': 'properties.dnsConfig', 'type': 'DnsConfig'},
        'monitor_config': {'key': 'properties.monitorConfig', 'type': 'MonitorConfig'},
        'endpoints': {'key': 'properties.endpoints', 'type': '[Endpoint]'},
    }

    def __init__(self, **kwargs):
        super(Profile, self).__init__(**kwargs)
        self.profile_status = kwargs.get('profile_status', None)
        self.traffic_routing_method = kwargs.get('traffic_routing_method', None)
        self.dns_config = kwargs.get('dns_config', None)
        self.monitor_config = kwargs.get('monitor_config', None)
        self.endpoints = kwargs.get('endpoints', None)
