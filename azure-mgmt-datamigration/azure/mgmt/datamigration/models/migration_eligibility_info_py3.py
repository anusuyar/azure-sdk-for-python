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


class MigrationEligibilityInfo(Model):
    """Information about migration eligibility of a server object.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar is_eligibile_for_migration: Whether object is eligible for migration
     or not.
    :vartype is_eligibile_for_migration: bool
    :ivar validation_messages: Information about eligibility failure for the
     server object.
    :vartype validation_messages: list[str]
    """

    _validation = {
        'is_eligibile_for_migration': {'readonly': True},
        'validation_messages': {'readonly': True},
    }

    _attribute_map = {
        'is_eligibile_for_migration': {'key': 'isEligibileForMigration', 'type': 'bool'},
        'validation_messages': {'key': 'validationMessages', 'type': '[str]'},
    }

    def __init__(self, **kwargs) -> None:
        super(MigrationEligibilityInfo, self).__init__(**kwargs)
        self.is_eligibile_for_migration = None
        self.validation_messages = None
