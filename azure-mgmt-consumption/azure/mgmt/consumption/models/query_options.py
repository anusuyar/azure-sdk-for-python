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


class QueryOptions(Model):
    """Additional parameters for a set of operations, such as: UsageDetails_list,
    UsageDetails_list_by_billing_period.

    :param apply: OData apply expression to aggregatie usageDetails by tags or
     (tags and properties/usageStart)
    :type apply: str
    """

    _attribute_map = {
        'apply': {'key': '', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(QueryOptions, self).__init__(**kwargs)
        self.apply = kwargs.get('apply', None)
