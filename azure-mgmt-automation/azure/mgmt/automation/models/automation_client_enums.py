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

from enum import Enum


class AutomationKeyName(str, Enum):

    primary = "primary"
    secondary = "secondary"


class AutomationKeyPermissions(str, Enum):

    full = "Full"


class JobProvisioningState(str, Enum):

    failed = "Failed"
    succeeded = "Succeeded"
    suspended = "Suspended"
    processing = "Processing"


class JobStatus(str, Enum):

    new = "New"
    activating = "Activating"
    running = "Running"
    completed = "Completed"
    failed = "Failed"
    stopped = "Stopped"
    blocked = "Blocked"
    suspended = "Suspended"
    disconnected = "Disconnected"
    suspending = "Suspending"
    stopping = "Stopping"
    resuming = "Resuming"
    removing = "Removing"


class RunbookTypeEnum(str, Enum):

    script = "Script"
    graph = "Graph"
    power_shell_workflow = "PowerShellWorkflow"
    power_shell = "PowerShell"
    graph_power_shell_workflow = "GraphPowerShellWorkflow"
    graph_power_shell = "GraphPowerShell"


class RunbookState(str, Enum):

    new = "New"
    edit = "Edit"
    published = "Published"


class RunbookProvisioningState(str, Enum):

    succeeded = "Succeeded"


class ModuleProvisioningState(str, Enum):

    created = "Created"
    creating = "Creating"
    starting_import_module_runbook = "StartingImportModuleRunbook"
    running_import_module_runbook = "RunningImportModuleRunbook"
    content_retrieved = "ContentRetrieved"
    content_downloaded = "ContentDownloaded"
    content_validated = "ContentValidated"
    connection_type_imported = "ConnectionTypeImported"
    content_stored = "ContentStored"
    module_data_stored = "ModuleDataStored"
    activities_stored = "ActivitiesStored"
    module_import_runbook_complete = "ModuleImportRunbookComplete"
    succeeded = "Succeeded"
    failed = "Failed"
    cancelled = "Cancelled"
    updating = "Updating"


class ContentSourceType(str, Enum):

    embedded_content = "embeddedContent"
    uri = "uri"


class DscConfigurationProvisioningState(str, Enum):

    succeeded = "Succeeded"


class DscConfigurationState(str, Enum):

    new = "New"
    edit = "Edit"
    published = "Published"


class SkuNameEnum(str, Enum):

    free = "Free"
    basic = "Basic"


class AutomationAccountState(str, Enum):

    ok = "Ok"
    unavailable = "Unavailable"
    suspended = "Suspended"


class ScheduleDay(str, Enum):

    monday = "Monday"
    tuesday = "Tuesday"
    wednesday = "Wednesday"
    thursday = "Thursday"
    friday = "Friday"
    saturday = "Saturday"
    sunday = "Sunday"


class AgentRegistrationKeyName(str, Enum):

    primary = "primary"
    secondary = "secondary"


class JobStreamType(str, Enum):

    progress = "Progress"
    output = "Output"
    warning = "Warning"
    error = "Error"
    debug = "Debug"
    verbose = "Verbose"
    any = "Any"


class HttpStatusCode(str, Enum):

    continue_enum = "Continue"
    switching_protocols = "SwitchingProtocols"
    ok = "OK"
    created = "Created"
    accepted = "Accepted"
    non_authoritative_information = "NonAuthoritativeInformation"
    no_content = "NoContent"
    reset_content = "ResetContent"
    partial_content = "PartialContent"
    multiple_choices = "MultipleChoices"
    ambiguous = "Ambiguous"
    moved_permanently = "MovedPermanently"
    moved = "Moved"
    found = "Found"
    redirect = "Redirect"
    see_other = "SeeOther"
    redirect_method = "RedirectMethod"
    not_modified = "NotModified"
    use_proxy = "UseProxy"
    unused = "Unused"
    temporary_redirect = "TemporaryRedirect"
    redirect_keep_verb = "RedirectKeepVerb"
    bad_request = "BadRequest"
    unauthorized = "Unauthorized"
    payment_required = "PaymentRequired"
    forbidden = "Forbidden"
    not_found = "NotFound"
    method_not_allowed = "MethodNotAllowed"
    not_acceptable = "NotAcceptable"
    proxy_authentication_required = "ProxyAuthenticationRequired"
    request_timeout = "RequestTimeout"
    conflict = "Conflict"
    gone = "Gone"
    length_required = "LengthRequired"
    precondition_failed = "PreconditionFailed"
    request_entity_too_large = "RequestEntityTooLarge"
    request_uri_too_long = "RequestUriTooLong"
    unsupported_media_type = "UnsupportedMediaType"
    requested_range_not_satisfiable = "RequestedRangeNotSatisfiable"
    expectation_failed = "ExpectationFailed"
    upgrade_required = "UpgradeRequired"
    internal_server_error = "InternalServerError"
    not_implemented = "NotImplemented"
    bad_gateway = "BadGateway"
    service_unavailable = "ServiceUnavailable"
    gateway_timeout = "GatewayTimeout"
    http_version_not_supported = "HttpVersionNotSupported"


class ScheduleFrequency(str, Enum):

    one_time = "OneTime"
    day = "Day"
    hour = "Hour"
    week = "Week"
    month = "Month"


class OperatingSystemType(str, Enum):

    windows = "Windows"
    linux = "Linux"


class WindowsUpdateClasses(str, Enum):

    unclassified = "Unclassified"
    critical = "Critical"
    security = "Security"
    update_rollup = "UpdateRollup"
    feature_pack = "FeaturePack"
    service_pack = "ServicePack"
    definition = "Definition"
    tools = "Tools"
    updates = "Updates"


class LinuxUpdateClasses(str, Enum):

    unclassified = "Unclassified"
    critical = "Critical"
    security = "Security"
    other = "Other"


class SourceType(str, Enum):

    vso_git = "VsoGit"
    vso_tfvc = "VsoTfvc"
    git_hub = "GitHub"


class ProvisioningState(str, Enum):

    completed = "Completed"
    failed = "Failed"
    running = "Running"
