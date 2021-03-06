.. :changelog:

Release History
===============

1.0.1 (2018-04-16)
++++++++++++++++++

**Bugfixes**

- Fix some invalid models in Python 3
- Compatibility of the sdist with wheel 0.31.0

1.0.0 (2018-03-19)
++++++++++++++++++

**General Breaking changes**

This version uses a next-generation code generator that *might* introduce breaking changes.

- Model signatures now use only keyword-argument syntax. All positional arguments must be re-written as keyword-arguments.
  To keep auto-completion in most cases, models are now generated for Python 2 and Python 3. Python 3 uses the "*" syntax for keyword-only arguments.
- Enum types now use the "str" mixin (class AzureEnum(str, Enum)) to improve the behavior when unrecognized enum values are encountered.
  While this is not a breaking change, the distinctions are important, and are documented here:
  https://docs.python.org/3/library/enum.html#others
  At a glance:

  - "is" should not be used at all.
  - "format" will return the string value, where "%s" string formatting will return `NameOfEnum.stringvalue`. Format syntax should be prefered.

- New Long Running Operation:

  - Return type changes from `msrestazure.azure_operation.AzureOperationPoller` to `msrest.polling.LROPoller`. External API is the same.
  - Return type is now **always** a `msrest.polling.LROPoller`, regardless of the optional parameters used.
  - The behavior has changed when using `raw=True`. Instead of returning the initial call result as `ClientRawResponse`, 
    without polling, now this returns an LROPoller. After polling, the final resource will be returned as a `ClientRawResponse`.
  - New `polling` parameter. The default behavior is `Polling=True` which will poll using ARM algorithm. When `Polling=False`,
    the response of the initial call will be returned without polling.
  - `polling` parameter accepts instances of subclasses of `msrest.polling.PollingMethod`.
  - `add_done_callback` will no longer raise if called after polling is finished, but will instead execute the callback right away.

**Features**

- added support for job level mounting
- added support for environment variables with secret values
- added support for performance counters reporting in Azure Application Insights
- added support for custom images
- added support for pyTorch deep learning framework
- added API for usage and limits reporting
- added API for listing job files in subdirectories
- now user can choose caching type during NFS creation
- get cluster now reports a path segment generated for storing start task output logs
- get job now reports a path segment generated for job's output directories
- renamed EnvironmentSetting to EnvironmentVariable

0.2.0 (2017-10-05)
++++++++++++++++++

* credentials_info property got renamed to credentials.
* removed unused class FileServerStatus and Code enum
* renamed enums for CachingType and VmPriority
* removed 'statuses' attribute on FileServer

0.1.0 (2017-10-03)
++++++++++++++++++

* Initial Release
