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


class SiteExtensionInfo(ProxyOnlyResource):
    """Site Extension Information.

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
    :param site_extension_info_id: Site extension ID.
    :type site_extension_info_id: str
    :param title: Site extension title.
    :type title: str
    :param site_extension_info_type: Site extension type. Possible values
     include: 'Gallery', 'WebRoot'
    :type site_extension_info_type: str or
     ~azure.mgmt.web.models.SiteExtensionType
    :param summary: Summary description.
    :type summary: str
    :param description: Detailed description.
    :type description: str
    :param version: Version information.
    :type version: str
    :param extension_url: Extension URL.
    :type extension_url: str
    :param project_url: Project URL.
    :type project_url: str
    :param icon_url: Icon URL.
    :type icon_url: str
    :param license_url: License URL.
    :type license_url: str
    :param feed_url: Feed URL.
    :type feed_url: str
    :param authors: List of authors.
    :type authors: list[str]
    :param installation_args: Installer command line parameters.
    :type installation_args: str
    :param published_date_time: Published timestamp.
    :type published_date_time: datetime
    :param download_count: Count of downloads.
    :type download_count: int
    :param local_is_latest_version: <code>true</code> if the local version is
     the latest version; <code>false</code> otherwise.
    :type local_is_latest_version: bool
    :param local_path: Local path.
    :type local_path: str
    :param installed_date_time: Installed timestamp.
    :type installed_date_time: datetime
    :param provisioning_state: Provisioning state.
    :type provisioning_state: str
    :param comment: Site Extension comment.
    :type comment: str
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
        'site_extension_info_id': {'key': 'properties.id', 'type': 'str'},
        'title': {'key': 'properties.title', 'type': 'str'},
        'site_extension_info_type': {'key': 'properties.type', 'type': 'SiteExtensionType'},
        'summary': {'key': 'properties.summary', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'version': {'key': 'properties.version', 'type': 'str'},
        'extension_url': {'key': 'properties.extensionUrl', 'type': 'str'},
        'project_url': {'key': 'properties.projectUrl', 'type': 'str'},
        'icon_url': {'key': 'properties.iconUrl', 'type': 'str'},
        'license_url': {'key': 'properties.licenseUrl', 'type': 'str'},
        'feed_url': {'key': 'properties.feedUrl', 'type': 'str'},
        'authors': {'key': 'properties.authors', 'type': '[str]'},
        'installation_args': {'key': 'properties.installationArgs', 'type': 'str'},
        'published_date_time': {'key': 'properties.publishedDateTime', 'type': 'iso-8601'},
        'download_count': {'key': 'properties.downloadCount', 'type': 'int'},
        'local_is_latest_version': {'key': 'properties.localIsLatestVersion', 'type': 'bool'},
        'local_path': {'key': 'properties.localPath', 'type': 'str'},
        'installed_date_time': {'key': 'properties.installedDateTime', 'type': 'iso-8601'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'comment': {'key': 'properties.comment', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SiteExtensionInfo, self).__init__(**kwargs)
        self.site_extension_info_id = kwargs.get('site_extension_info_id', None)
        self.title = kwargs.get('title', None)
        self.site_extension_info_type = kwargs.get('site_extension_info_type', None)
        self.summary = kwargs.get('summary', None)
        self.description = kwargs.get('description', None)
        self.version = kwargs.get('version', None)
        self.extension_url = kwargs.get('extension_url', None)
        self.project_url = kwargs.get('project_url', None)
        self.icon_url = kwargs.get('icon_url', None)
        self.license_url = kwargs.get('license_url', None)
        self.feed_url = kwargs.get('feed_url', None)
        self.authors = kwargs.get('authors', None)
        self.installation_args = kwargs.get('installation_args', None)
        self.published_date_time = kwargs.get('published_date_time', None)
        self.download_count = kwargs.get('download_count', None)
        self.local_is_latest_version = kwargs.get('local_is_latest_version', None)
        self.local_path = kwargs.get('local_path', None)
        self.installed_date_time = kwargs.get('installed_date_time', None)
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.comment = kwargs.get('comment', None)
