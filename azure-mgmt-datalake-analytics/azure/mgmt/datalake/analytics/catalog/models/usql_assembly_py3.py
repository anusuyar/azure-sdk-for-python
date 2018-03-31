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

from .catalog_item import CatalogItem


class USqlAssembly(CatalogItem):
    """A Data Lake Analytics catalog U-SQL Assembly.

    :param compute_account_name: the name of the Data Lake Analytics account.
    :type compute_account_name: str
    :param version: the version of the catalog item.
    :type version: str
    :param database_name: the name of the database.
    :type database_name: str
    :param name: the name of the assembly.
    :type name: str
    :param clr_name: the name of the CLR.
    :type clr_name: str
    :param is_visible: the switch indicating if this assembly is visible or
     not.
    :type is_visible: bool
    :param is_user_defined: the switch indicating if this assembly is user
     defined or not.
    :type is_user_defined: bool
    :param files: the list of files associated with the assembly
    :type files:
     list[~azure.mgmt.datalake.analytics.catalog.models.USqlAssemblyFileInfo]
    :param dependencies: the list of dependencies associated with the assembly
    :type dependencies:
     list[~azure.mgmt.datalake.analytics.catalog.models.USqlAssemblyDependencyInfo]
    """

    _attribute_map = {
        'compute_account_name': {'key': 'computeAccountName', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
        'database_name': {'key': 'databaseName', 'type': 'str'},
        'name': {'key': 'assemblyName', 'type': 'str'},
        'clr_name': {'key': 'clrName', 'type': 'str'},
        'is_visible': {'key': 'isVisible', 'type': 'bool'},
        'is_user_defined': {'key': 'isUserDefined', 'type': 'bool'},
        'files': {'key': 'files', 'type': '[USqlAssemblyFileInfo]'},
        'dependencies': {'key': 'dependencies', 'type': '[USqlAssemblyDependencyInfo]'},
    }

    def __init__(self, *, compute_account_name: str=None, version: str=None, database_name: str=None, name: str=None, clr_name: str=None, is_visible: bool=None, is_user_defined: bool=None, files=None, dependencies=None, **kwargs) -> None:
        super(USqlAssembly, self).__init__(compute_account_name=compute_account_name, version=version, **kwargs)
        self.database_name = database_name
        self.name = name
        self.clr_name = clr_name
        self.is_visible = is_visible
        self.is_user_defined = is_user_defined
        self.files = files
        self.dependencies = dependencies
