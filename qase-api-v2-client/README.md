# qase

Qase TestOps API v2 Specification.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.0.0
- Package version: 1.0.0
- Generator version: 7.4.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
  For more information, please visit [https://qase.io](https://qase.io)

## Requirements.

Python 3.7+

## Installation & Usage

### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```

(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:

```python

import qase
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```

(or `sudo python setup.py install` to install the package for all users)

Then import the package:

```python

import qase
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from qase.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.qase.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = qase.Configuration(
    host="https://api.qase.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TokenAuth
configuration.api_key['TokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TokenAuth'] = 'Bearer'


# Enter a context with an instance of the API client
with qase.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qase.ResultsApi(api_client)
    project_code = 'project_code_example'  # str | 
    run_id = 56  # int | 
    result_create = qase.ResultCreate()  # ResultCreate | 

    try:
        # (Beta) Create test run result
        api_instance.create_result_v2(project_code, run_id, result_create)
    except ApiException as e:
        print("Exception when calling ResultsApi->create_result_v2: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.qase.io/v2*

 Class        | Method                                                        | HTTP request                                  | Description                        
--------------|---------------------------------------------------------------|-----------------------------------------------|------------------------------------
 *ResultsApi* | [**create_result_v2**](docs/ResultsApi.md#create_result_v2)   | **POST** /{project_code}/run/{run_id}/result  | (Beta) Create test run result      
 *ResultsApi* | [**create_results_v2**](docs/ResultsApi.md#create_results_v2) | **POST** /{project_code}/run/{run_id}/results | (Beta) Bulk create test run result 

## Documentation For Models

- [BaseErrorFieldResponse](docs/BaseErrorFieldResponse.md)
- [BaseErrorFieldResponseErrorFieldsInner](docs/BaseErrorFieldResponseErrorFieldsInner.md)
- [BaseErrorResponse](docs/BaseErrorResponse.md)
- [CreateResultV2422Response](docs/CreateResultV2422Response.md)
- [CreateResultsRequestV2](docs/CreateResultsRequestV2.md)
- [RelationSuite](docs/RelationSuite.md)
- [RelationSuiteItem](docs/RelationSuiteItem.md)
- [ResultCreate](docs/ResultCreate.md)
- [ResultExecution](docs/ResultExecution.md)
- [ResultRelations](docs/ResultRelations.md)
- [ResultStep](docs/ResultStep.md)
- [ResultStepData](docs/ResultStepData.md)
- [ResultStepExecution](docs/ResultStepExecution.md)
- [ResultStepStatus](docs/ResultStepStatus.md)
- [ResultStepsType](docs/ResultStepsType.md)

<a id="documentation-for-authorization"></a>

## Documentation For Authorization

Authentication schemes defined for the API:
<a id="TokenAuth"></a>

### TokenAuth

- **Type**: API key
- **API key parameter name**: Token
- **Location**: HTTP header

## Author

support@qase.io

