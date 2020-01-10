# flat_api.AccountApi

All URIs are relative to *https://api.flat.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_authenticated_user**](AccountApi.md#get_authenticated_user) | **GET** /me | Get current user profile


# **get_authenticated_user**
> UserDetails get_authenticated_user()

Get current user profile

Get details about the current authenticated User. 

### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import flat_api
from flat_api.rest import ApiException
from pprint import pprint
configuration = flat_api.Configuration()
# Configure OAuth2 access token for authorization: OAuth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.flat.io/v2
configuration.host = "https://api.flat.io/v2"
# Create an instance of the API class
api_instance = flat_api.AccountApi(flat_api.ApiClient(configuration))

try:
    # Get current user profile
    api_response = api_instance.get_authenticated_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_authenticated_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserDetails**](UserDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current user details |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

