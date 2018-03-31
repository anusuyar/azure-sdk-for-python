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


class ApiManagementServiceGetSsoTokenResult(Model):
    """The response of the GetSsoToken operation.

    :param redirect_uri: Redirect URL to the Publisher Portal containing the
     SSO token.
    :type redirect_uri: str
    """

    _attribute_map = {
        'redirect_uri': {'key': 'redirectUri', 'type': 'str'},
    }

    def __init__(self, *, redirect_uri: str=None, **kwargs) -> None:
        super(ApiManagementServiceGetSsoTokenResult, self).__init__(**kwargs)
        self.redirect_uri = redirect_uri
