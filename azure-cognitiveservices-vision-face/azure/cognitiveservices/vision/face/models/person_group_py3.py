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

from .name_and_user_data_contract import NameAndUserDataContract


class PersonGroup(NameAndUserDataContract):
    """Person group object.

    All required parameters must be populated in order to send to Azure.

    :param name: User defined name, maximum length is 128.
    :type name: str
    :param user_data: User specified data. Length should not exceed 16KB.
    :type user_data: str
    :param person_group_id: Required. PersonGroupId of the existing person
     groups.
    :type person_group_id: str
    """

    _validation = {
        'name': {'max_length': 128},
        'user_data': {'max_length': 16384},
        'person_group_id': {'required': True, 'max_length': 64, 'pattern': r'^[a-z0-9-_]+$'},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'user_data': {'key': 'userData', 'type': 'str'},
        'person_group_id': {'key': 'personGroupId', 'type': 'str'},
    }

    def __init__(self, *, person_group_id: str, name: str=None, user_data: str=None, **kwargs) -> None:
        super(PersonGroup, self).__init__(name=name, user_data=user_data, **kwargs)
        self.person_group_id = person_group_id
