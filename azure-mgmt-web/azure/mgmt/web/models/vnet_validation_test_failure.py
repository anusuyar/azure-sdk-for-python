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

from .proxy_only_resource import ProxyOnlyResource


class VnetValidationTestFailure(ProxyOnlyResource):
    """A class that describes a test that failed during NSG and UDR validation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :ivar type: Resource type.
    :vartype type: str
    :param test_name: The name of the test that failed.
    :type test_name: str
    :param details: The details of what caused the failure, e.g. the blocking
     rule name, etc.
    :type details: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'test_name': {'key': 'properties.testName', 'type': 'str'},
        'details': {'key': 'properties.details', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(VnetValidationTestFailure, self).__init__(**kwargs)
        self.test_name = kwargs.get('test_name', None)
        self.details = kwargs.get('details', None)
