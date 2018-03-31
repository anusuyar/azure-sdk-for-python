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

from .execution_activity import ExecutionActivity


class HDInsightStreamingActivity(ExecutionActivity):
    """HDInsight streaming activity type.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param name: Required. Activity name.
    :type name: str
    :param description: Activity description.
    :type description: str
    :param depends_on: Activity depends on condition.
    :type depends_on: list[~azure.mgmt.datafactory.models.ActivityDependency]
    :param type: Required. Constant filled by server.
    :type type: str
    :param linked_service_name: Linked service reference.
    :type linked_service_name:
     ~azure.mgmt.datafactory.models.LinkedServiceReference
    :param policy: Activity policy.
    :type policy: ~azure.mgmt.datafactory.models.ActivityPolicy
    :param storage_linked_services: Storage linked service references.
    :type storage_linked_services:
     list[~azure.mgmt.datafactory.models.LinkedServiceReference]
    :param arguments: User specified arguments to HDInsightActivity.
    :type arguments: list[object]
    :param get_debug_info: Debug info option. Possible values include: 'None',
     'Always', 'Failure'
    :type get_debug_info: str or
     ~azure.mgmt.datafactory.models.HDInsightActivityDebugInfoOption
    :param mapper: Required. Mapper executable name. Type: string (or
     Expression with resultType string).
    :type mapper: object
    :param reducer: Required. Reducer executable name. Type: string (or
     Expression with resultType string).
    :type reducer: object
    :param input: Required. Input blob path. Type: string (or Expression with
     resultType string).
    :type input: object
    :param output: Required. Output blob path. Type: string (or Expression
     with resultType string).
    :type output: object
    :param file_paths: Required. Paths to streaming job files. Can be
     directories.
    :type file_paths: list[object]
    :param file_linked_service: Linked service reference where the files are
     located.
    :type file_linked_service:
     ~azure.mgmt.datafactory.models.LinkedServiceReference
    :param combiner: Combiner executable name. Type: string (or Expression
     with resultType string).
    :type combiner: object
    :param command_environment: Command line environment values.
    :type command_environment: list[object]
    :param defines: Allows user to specify defines for streaming job request.
    :type defines: dict[str, object]
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True},
        'mapper': {'required': True},
        'reducer': {'required': True},
        'input': {'required': True},
        'output': {'required': True},
        'file_paths': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'depends_on': {'key': 'dependsOn', 'type': '[ActivityDependency]'},
        'type': {'key': 'type', 'type': 'str'},
        'linked_service_name': {'key': 'linkedServiceName', 'type': 'LinkedServiceReference'},
        'policy': {'key': 'policy', 'type': 'ActivityPolicy'},
        'storage_linked_services': {'key': 'typeProperties.storageLinkedServices', 'type': '[LinkedServiceReference]'},
        'arguments': {'key': 'typeProperties.arguments', 'type': '[object]'},
        'get_debug_info': {'key': 'typeProperties.getDebugInfo', 'type': 'str'},
        'mapper': {'key': 'typeProperties.mapper', 'type': 'object'},
        'reducer': {'key': 'typeProperties.reducer', 'type': 'object'},
        'input': {'key': 'typeProperties.input', 'type': 'object'},
        'output': {'key': 'typeProperties.output', 'type': 'object'},
        'file_paths': {'key': 'typeProperties.filePaths', 'type': '[object]'},
        'file_linked_service': {'key': 'typeProperties.fileLinkedService', 'type': 'LinkedServiceReference'},
        'combiner': {'key': 'typeProperties.combiner', 'type': 'object'},
        'command_environment': {'key': 'typeProperties.commandEnvironment', 'type': '[object]'},
        'defines': {'key': 'typeProperties.defines', 'type': '{object}'},
    }

    def __init__(self, *, name: str, mapper, reducer, input, output, file_paths, additional_properties=None, description: str=None, depends_on=None, linked_service_name=None, policy=None, storage_linked_services=None, arguments=None, get_debug_info=None, file_linked_service=None, combiner=None, command_environment=None, defines=None, **kwargs) -> None:
        super(HDInsightStreamingActivity, self).__init__(additional_properties=additional_properties, name=name, description=description, depends_on=depends_on, linked_service_name=linked_service_name, policy=policy, **kwargs)
        self.storage_linked_services = storage_linked_services
        self.arguments = arguments
        self.get_debug_info = get_debug_info
        self.mapper = mapper
        self.reducer = reducer
        self.input = input
        self.output = output
        self.file_paths = file_paths
        self.file_linked_service = file_linked_service
        self.combiner = combiner
        self.command_environment = command_environment
        self.defines = defines
        self.type = 'HDInsightStreaming'
