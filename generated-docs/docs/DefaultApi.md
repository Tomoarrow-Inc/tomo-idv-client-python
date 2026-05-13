# tomo_idv_client.generated.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_idv_ca_health_get**](DefaultApi.md#v1_idv_ca_health_get) | **GET** /v1/idv/ca/health | 
[**v1_idv_ca_kyc_get_post**](DefaultApi.md#v1_idv_ca_kyc_get_post) | **POST** /v1/idv/ca/kyc/get | 
[**v1_idv_ca_start_post**](DefaultApi.md#v1_idv_ca_start_post) | **POST** /v1/idv/ca/start | 
[**v1_idv_cn_health_get**](DefaultApi.md#v1_idv_cn_health_get) | **GET** /v1/idv/cn/health | 
[**v1_idv_cn_kyc_get_post**](DefaultApi.md#v1_idv_cn_kyc_get_post) | **POST** /v1/idv/cn/kyc/get | 
[**v1_idv_cn_start_post**](DefaultApi.md#v1_idv_cn_start_post) | **POST** /v1/idv/cn/start | 
[**v1_idv_cn_token_post**](DefaultApi.md#v1_idv_cn_token_post) | **POST** /v1/idv/cn/token | 
[**v1_idv_health_get**](DefaultApi.md#v1_idv_health_get) | **GET** /v1/idv/health | 
[**v1_idv_jp_health_get**](DefaultApi.md#v1_idv_jp_health_get) | **GET** /v1/idv/jp/health | 
[**v1_idv_jp_kyc_get_post**](DefaultApi.md#v1_idv_jp_kyc_get_post) | **POST** /v1/idv/jp/kyc/get | 
[**v1_idv_jp_start_post**](DefaultApi.md#v1_idv_jp_start_post) | **POST** /v1/idv/jp/start | 
[**v1_idv_kyc_get_post**](DefaultApi.md#v1_idv_kyc_get_post) | **POST** /v1/idv/kyc/get | 
[**v1_idv_result_post**](DefaultApi.md#v1_idv_result_post) | **POST** /v1/idv/result | 
[**v1_idv_sessions_start_post**](DefaultApi.md#v1_idv_sessions_start_post) | **POST** /v1/idv/sessions/start | 
[**v1_idv_start_post**](DefaultApi.md#v1_idv_start_post) | **POST** /v1/idv/start | 
[**v1_idv_uk_health_get**](DefaultApi.md#v1_idv_uk_health_get) | **GET** /v1/idv/uk/health | 
[**v1_idv_uk_kyc_get_post**](DefaultApi.md#v1_idv_uk_kyc_get_post) | **POST** /v1/idv/uk/kyc/get | 
[**v1_idv_uk_start_post**](DefaultApi.md#v1_idv_uk_start_post) | **POST** /v1/idv/uk/start | 
[**v1_idv_us_health_get**](DefaultApi.md#v1_idv_us_health_get) | **GET** /v1/idv/us/health | 
[**v1_idv_us_kyc_get_post**](DefaultApi.md#v1_idv_us_kyc_get_post) | **POST** /v1/idv/us/kyc/get | 
[**v1_idv_us_start_post**](DefaultApi.md#v1_idv_us_start_post) | **POST** /v1/idv/us/start | 
[**v1_oauth2_token_post**](DefaultApi.md#v1_oauth2_token_post) | **POST** /v1/oauth2/token | 


# **v1_idv_ca_health_get**
> str v1_idv_ca_health_get()

[DEPRECATED] Use /v1/idv/health.

### Example


```python
import tomo_idv_client.generated
from tomo_idv_client.generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tomo_idv_client.generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with tomo_idv_client.generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tomo_idv_client.generated.DefaultApi(api_client)

    try:
        api_response = api_instance.v1_idv_ca_health_get()
        print("The response of DefaultApi->v1_idv_ca_health_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_idv_ca_health_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_idv_ca_kyc_get_post**
> UsGetUnionResultRes v1_idv_ca_kyc_get_post(authorization=authorization, us_get_kyc_req=us_get_kyc_req)

[DEPRECATED] Use /v1/idv/result with country=ca.

### Example


```python
import tomo_idv_client.generated
from tomo_idv_client.generated.models.us_get_kyc_req import UsGetKycReq
from tomo_idv_client.generated.models.us_get_union_result_res import UsGetUnionResultRes
from tomo_idv_client.generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tomo_idv_client.generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with tomo_idv_client.generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tomo_idv_client.generated.DefaultApi(api_client)
    authorization = 'authorization_example' # str |  (optional)
    us_get_kyc_req = tomo_idv_client.generated.UsGetKycReq() # UsGetKycReq |  (optional)

    try:
        api_response = api_instance.v1_idv_ca_kyc_get_post(authorization=authorization, us_get_kyc_req=us_get_kyc_req)
        print("The response of DefaultApi->v1_idv_ca_kyc_get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_idv_ca_kyc_get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **us_get_kyc_req** | [**UsGetKycReq**](UsGetKycReq.md)|  | [optional] 

### Return type

[**UsGetUnionResultRes**](UsGetUnionResultRes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid &#x60;body&#x60; or &#x60;Authorization&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_idv_ca_start_post**
> StartIdvRes v1_idv_ca_start_post(authorization=authorization, ca_start_idv_req=ca_start_idv_req)

[DEPRECATED] Use /v1/idv/start with country=ca.

### Example


```python
import tomo_idv_client.generated
from tomo_idv_client.generated.models.ca_start_idv_req import CaStartIdvReq
from tomo_idv_client.generated.models.start_idv_res import StartIdvRes
from tomo_idv_client.generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tomo_idv_client.generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with tomo_idv_client.generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tomo_idv_client.generated.DefaultApi(api_client)
    authorization = 'authorization_example' # str |  (optional)
    ca_start_idv_req = tomo_idv_client.generated.CaStartIdvReq() # CaStartIdvReq |  (optional)

    try:
        api_response = api_instance.v1_idv_ca_start_post(authorization=authorization, ca_start_idv_req=ca_start_idv_req)
        print("The response of DefaultApi->v1_idv_ca_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_idv_ca_start_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **ca_start_idv_req** | [**CaStartIdvReq**](CaStartIdvReq.md)|  | [optional] 

### Return type

[**StartIdvRes**](StartIdvRes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid &#x60;body&#x60; or &#x60;Authorization&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_idv_cn_health_get**
> str v1_idv_cn_health_get()

[DEPRECATED] Use /v1/idv/health.

### Example


```python
import tomo_idv_client.generated
from tomo_idv_client.generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tomo_idv_client.generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with tomo_idv_client.generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tomo_idv_client.generated.DefaultApi(api_client)

    try:
        api_response = api_instance.v1_idv_cn_health_get()
        print("The response of DefaultApi->v1_idv_cn_health_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_idv_cn_health_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_idv_cn_kyc_get_post**
> CnGetUnionResultRes v1_idv_cn_kyc_get_post(authorization=authorization, cn_get_kyc_req=cn_get_kyc_req)

[DEPRECATED] Use /v1/idv/result with country=cn.

### Example


```python
import tomo_idv_client.generated
from tomo_idv_client.generated.models.cn_get_kyc_req import CnGetKycReq
from tomo_idv_client.generated.models.cn_get_union_result_res import CnGetUnionResultRes
from tomo_idv_client.generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tomo_idv_client.generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with tomo_idv_client.generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tomo_idv_client.generated.DefaultApi(api_client)
    authorization = 'authorization_example' # str |  (optional)
    cn_get_kyc_req = tomo_idv_client.generated.CnGetKycReq() # CnGetKycReq |  (optional)

    try:
        api_response = api_instance.v1_idv_cn_kyc_get_post(authorization=authorization, cn_get_kyc_req=cn_get_kyc_req)
        print("The response of DefaultApi->v1_idv_cn_kyc_get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_idv_cn_kyc_get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **cn_get_kyc_req** | [**CnGetKycReq**](CnGetKycReq.md)|  | [optional] 

### Return type

[**CnGetUnionResultRes**](CnGetUnionResultRes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid &#x60;body&#x60; or &#x60;Authorization&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_idv_cn_start_post**
> StartIdvRes v1_idv_cn_start_post(authorization=authorization, cn_start_idv_req=cn_start_idv_req)

[DEPRECATED] Use /v1/idv/start with country=cn.

### Example


```python
import tomo_idv_client.generated
from tomo_idv_client.generated.models.cn_start_idv_req import CnStartIdvReq
from tomo_idv_client.generated.models.start_idv_res import StartIdvRes
from tomo_idv_client.generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tomo_idv_client.generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with tomo_idv_client.generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tomo_idv_client.generated.DefaultApi(api_client)
    authorization = 'authorization_example' # str |  (optional)
    cn_start_idv_req = tomo_idv_client.generated.CnStartIdvReq() # CnStartIdvReq |  (optional)

    try:
        api_response = api_instance.v1_idv_cn_start_post(authorization=authorization, cn_start_idv_req=cn_start_idv_req)
        print("The response of DefaultApi->v1_idv_cn_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_idv_cn_start_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **cn_start_idv_req** | [**CnStartIdvReq**](CnStartIdvReq.md)|  | [optional] 

### Return type

[**StartIdvRes**](StartIdvRes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid &#x60;body&#x60; or &#x60;Authorization&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_idv_cn_token_post**
> TomoIdvIssueTokenRes v1_idv_cn_token_post(authorization=authorization, tomo_idv_issue_token_req=tomo_idv_issue_token_req)

[DEPRECATED] Use the OAuth2 token endpoint.

### Example


```python
import tomo_idv_client.generated
from tomo_idv_client.generated.models.tomo_idv_issue_token_req import TomoIdvIssueTokenReq
from tomo_idv_client.generated.models.tomo_idv_issue_token_res import TomoIdvIssueTokenRes
from tomo_idv_client.generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tomo_idv_client.generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with tomo_idv_client.generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tomo_idv_client.generated.DefaultApi(api_client)
    authorization = 'authorization_example' # str |  (optional)
    tomo_idv_issue_token_req = tomo_idv_client.generated.TomoIdvIssueTokenReq() # TomoIdvIssueTokenReq |  (optional)

    try:
        api_response = api_instance.v1_idv_cn_token_post(authorization=authorization, tomo_idv_issue_token_req=tomo_idv_issue_token_req)
        print("The response of DefaultApi->v1_idv_cn_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_idv_cn_token_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **tomo_idv_issue_token_req** | [**TomoIdvIssueTokenReq**](TomoIdvIssueTokenReq.md)|  | [optional] 

### Return type

[**TomoIdvIssueTokenRes**](TomoIdvIssueTokenRes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid &#x60;body&#x60; or &#x60;Authorization&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_idv_health_get**
> str v1_idv_health_get()

### Example


```python
import tomo_idv_client.generated
from tomo_idv_client.generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tomo_idv_client.generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with tomo_idv_client.generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tomo_idv_client.generated.DefaultApi(api_client)

    try:
        api_response = api_instance.v1_idv_health_get()
        print("The response of DefaultApi->v1_idv_health_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_idv_health_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_idv_jp_health_get**
> str v1_idv_jp_health_get()

[DEPRECATED] Use /v1/idv/health.

### Example


```python
import tomo_idv_client.generated
from tomo_idv_client.generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tomo_idv_client.generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with tomo_idv_client.generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tomo_idv_client.generated.DefaultApi(api_client)

    try:
        api_response = api_instance.v1_idv_jp_health_get()
        print("The response of DefaultApi->v1_idv_jp_health_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_idv_jp_health_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_idv_jp_kyc_get_post**
> JpGetUnionResultRes v1_idv_jp_kyc_get_post(authorization=authorization, jp_get_kyc_req=jp_get_kyc_req)

[DEPRECATED] Use /v1/idv/result with country=jp.

### Example


```python
import tomo_idv_client.generated
from tomo_idv_client.generated.models.jp_get_kyc_req import JpGetKycReq
from tomo_idv_client.generated.models.jp_get_union_result_res import JpGetUnionResultRes
from tomo_idv_client.generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tomo_idv_client.generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with tomo_idv_client.generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tomo_idv_client.generated.DefaultApi(api_client)
    authorization = 'authorization_example' # str |  (optional)
    jp_get_kyc_req = tomo_idv_client.generated.JpGetKycReq() # JpGetKycReq |  (optional)

    try:
        api_response = api_instance.v1_idv_jp_kyc_get_post(authorization=authorization, jp_get_kyc_req=jp_get_kyc_req)
        print("The response of DefaultApi->v1_idv_jp_kyc_get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_idv_jp_kyc_get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **jp_get_kyc_req** | [**JpGetKycReq**](JpGetKycReq.md)|  | [optional] 

### Return type

[**JpGetUnionResultRes**](JpGetUnionResultRes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid &#x60;body&#x60; or &#x60;Authorization&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_idv_jp_start_post**
> StartIdvRes v1_idv_jp_start_post(authorization=authorization, jp_start_idv_req=jp_start_idv_req)

[DEPRECATED] Use /v1/idv/start with country=jp.

### Example


```python
import tomo_idv_client.generated
from tomo_idv_client.generated.models.jp_start_idv_req import JpStartIdvReq
from tomo_idv_client.generated.models.start_idv_res import StartIdvRes
from tomo_idv_client.generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tomo_idv_client.generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with tomo_idv_client.generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tomo_idv_client.generated.DefaultApi(api_client)
    authorization = 'authorization_example' # str |  (optional)
    jp_start_idv_req = tomo_idv_client.generated.JpStartIdvReq() # JpStartIdvReq |  (optional)

    try:
        api_response = api_instance.v1_idv_jp_start_post(authorization=authorization, jp_start_idv_req=jp_start_idv_req)
        print("The response of DefaultApi->v1_idv_jp_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_idv_jp_start_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **jp_start_idv_req** | [**JpStartIdvReq**](JpStartIdvReq.md)|  | [optional] 

### Return type

[**StartIdvRes**](StartIdvRes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid &#x60;body&#x60; or &#x60;Authorization&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_idv_kyc_get_post**
> GetKycRes v1_idv_kyc_get_post(authorization=authorization, get_kyc_req=get_kyc_req)

[DEPRECATED] Use /v1/idv/result.

### Example


```python
import tomo_idv_client.generated
from tomo_idv_client.generated.models.get_kyc_req import GetKycReq
from tomo_idv_client.generated.models.get_kyc_res import GetKycRes
from tomo_idv_client.generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tomo_idv_client.generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with tomo_idv_client.generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tomo_idv_client.generated.DefaultApi(api_client)
    authorization = 'authorization_example' # str |  (optional)
    get_kyc_req = tomo_idv_client.generated.GetKycReq() # GetKycReq |  (optional)

    try:
        api_response = api_instance.v1_idv_kyc_get_post(authorization=authorization, get_kyc_req=get_kyc_req)
        print("The response of DefaultApi->v1_idv_kyc_get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_idv_kyc_get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **get_kyc_req** | [**GetKycReq**](GetKycReq.md)|  | [optional] 

### Return type

[**GetKycRes**](GetKycRes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid &#x60;body&#x60; or &#x60;Authorization&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_idv_result_post**
> ResultRes v1_idv_result_post(authorization=authorization, result_req=result_req)

### Example


```python
import tomo_idv_client.generated
from tomo_idv_client.generated.models.result_req import ResultReq
from tomo_idv_client.generated.models.result_res import ResultRes
from tomo_idv_client.generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tomo_idv_client.generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with tomo_idv_client.generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tomo_idv_client.generated.DefaultApi(api_client)
    authorization = 'authorization_example' # str |  (optional)
    result_req = tomo_idv_client.generated.ResultReq() # ResultReq |  (optional)

    try:
        api_response = api_instance.v1_idv_result_post(authorization=authorization, result_req=result_req)
        print("The response of DefaultApi->v1_idv_result_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_idv_result_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **result_req** | [**ResultReq**](ResultReq.md)|  | [optional] 

### Return type

[**ResultRes**](ResultRes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid &#x60;body&#x60; or &#x60;Authorization&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_idv_sessions_start_post**
> SessionStartRes v1_idv_sessions_start_post(authorization=authorization, session_start_req=session_start_req)

[DEPRECATED] Use /v1/idv/start.

### Example


```python
import tomo_idv_client.generated
from tomo_idv_client.generated.models.session_start_req import SessionStartReq
from tomo_idv_client.generated.models.session_start_res import SessionStartRes
from tomo_idv_client.generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tomo_idv_client.generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with tomo_idv_client.generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tomo_idv_client.generated.DefaultApi(api_client)
    authorization = 'authorization_example' # str |  (optional)
    session_start_req = tomo_idv_client.generated.SessionStartReq() # SessionStartReq |  (optional)

    try:
        api_response = api_instance.v1_idv_sessions_start_post(authorization=authorization, session_start_req=session_start_req)
        print("The response of DefaultApi->v1_idv_sessions_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_idv_sessions_start_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **session_start_req** | [**SessionStartReq**](SessionStartReq.md)|  | [optional] 

### Return type

[**SessionStartRes**](SessionStartRes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid &#x60;body&#x60; or &#x60;Authorization&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_idv_start_post**
> StartIdvRes v1_idv_start_post(authorization=authorization, start_idv_req=start_idv_req)

### Example


```python
import tomo_idv_client.generated
from tomo_idv_client.generated.models.start_idv_req import StartIdvReq
from tomo_idv_client.generated.models.start_idv_res import StartIdvRes
from tomo_idv_client.generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tomo_idv_client.generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with tomo_idv_client.generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tomo_idv_client.generated.DefaultApi(api_client)
    authorization = 'authorization_example' # str |  (optional)
    start_idv_req = tomo_idv_client.generated.StartIdvReq() # StartIdvReq |  (optional)

    try:
        api_response = api_instance.v1_idv_start_post(authorization=authorization, start_idv_req=start_idv_req)
        print("The response of DefaultApi->v1_idv_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_idv_start_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **start_idv_req** | [**StartIdvReq**](StartIdvReq.md)|  | [optional] 

### Return type

[**StartIdvRes**](StartIdvRes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid &#x60;body&#x60; or &#x60;Authorization&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_idv_uk_health_get**
> str v1_idv_uk_health_get()

[DEPRECATED] Use /v1/idv/health.

### Example


```python
import tomo_idv_client.generated
from tomo_idv_client.generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tomo_idv_client.generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with tomo_idv_client.generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tomo_idv_client.generated.DefaultApi(api_client)

    try:
        api_response = api_instance.v1_idv_uk_health_get()
        print("The response of DefaultApi->v1_idv_uk_health_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_idv_uk_health_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_idv_uk_kyc_get_post**
> UsGetUnionResultRes v1_idv_uk_kyc_get_post(authorization=authorization, us_get_kyc_req=us_get_kyc_req)

[DEPRECATED] Use /v1/idv/result with country=uk.

### Example


```python
import tomo_idv_client.generated
from tomo_idv_client.generated.models.us_get_kyc_req import UsGetKycReq
from tomo_idv_client.generated.models.us_get_union_result_res import UsGetUnionResultRes
from tomo_idv_client.generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tomo_idv_client.generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with tomo_idv_client.generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tomo_idv_client.generated.DefaultApi(api_client)
    authorization = 'authorization_example' # str |  (optional)
    us_get_kyc_req = tomo_idv_client.generated.UsGetKycReq() # UsGetKycReq |  (optional)

    try:
        api_response = api_instance.v1_idv_uk_kyc_get_post(authorization=authorization, us_get_kyc_req=us_get_kyc_req)
        print("The response of DefaultApi->v1_idv_uk_kyc_get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_idv_uk_kyc_get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **us_get_kyc_req** | [**UsGetKycReq**](UsGetKycReq.md)|  | [optional] 

### Return type

[**UsGetUnionResultRes**](UsGetUnionResultRes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid &#x60;body&#x60; or &#x60;Authorization&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_idv_uk_start_post**
> StartIdvRes v1_idv_uk_start_post(authorization=authorization, uk_start_idv_req=uk_start_idv_req)

[DEPRECATED] Use /v1/idv/start with country=uk.

### Example


```python
import tomo_idv_client.generated
from tomo_idv_client.generated.models.start_idv_res import StartIdvRes
from tomo_idv_client.generated.models.uk_start_idv_req import UkStartIdvReq
from tomo_idv_client.generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tomo_idv_client.generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with tomo_idv_client.generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tomo_idv_client.generated.DefaultApi(api_client)
    authorization = 'authorization_example' # str |  (optional)
    uk_start_idv_req = tomo_idv_client.generated.UkStartIdvReq() # UkStartIdvReq |  (optional)

    try:
        api_response = api_instance.v1_idv_uk_start_post(authorization=authorization, uk_start_idv_req=uk_start_idv_req)
        print("The response of DefaultApi->v1_idv_uk_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_idv_uk_start_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **uk_start_idv_req** | [**UkStartIdvReq**](UkStartIdvReq.md)|  | [optional] 

### Return type

[**StartIdvRes**](StartIdvRes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid &#x60;body&#x60; or &#x60;Authorization&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_idv_us_health_get**
> str v1_idv_us_health_get()

[DEPRECATED] Use /v1/idv/health.

### Example


```python
import tomo_idv_client.generated
from tomo_idv_client.generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tomo_idv_client.generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with tomo_idv_client.generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tomo_idv_client.generated.DefaultApi(api_client)

    try:
        api_response = api_instance.v1_idv_us_health_get()
        print("The response of DefaultApi->v1_idv_us_health_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_idv_us_health_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_idv_us_kyc_get_post**
> UsGetUnionResultRes v1_idv_us_kyc_get_post(authorization=authorization, us_get_kyc_req=us_get_kyc_req)

[DEPRECATED] Use /v1/idv/result with country=us.

### Example


```python
import tomo_idv_client.generated
from tomo_idv_client.generated.models.us_get_kyc_req import UsGetKycReq
from tomo_idv_client.generated.models.us_get_union_result_res import UsGetUnionResultRes
from tomo_idv_client.generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tomo_idv_client.generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with tomo_idv_client.generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tomo_idv_client.generated.DefaultApi(api_client)
    authorization = 'authorization_example' # str |  (optional)
    us_get_kyc_req = tomo_idv_client.generated.UsGetKycReq() # UsGetKycReq |  (optional)

    try:
        api_response = api_instance.v1_idv_us_kyc_get_post(authorization=authorization, us_get_kyc_req=us_get_kyc_req)
        print("The response of DefaultApi->v1_idv_us_kyc_get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_idv_us_kyc_get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **us_get_kyc_req** | [**UsGetKycReq**](UsGetKycReq.md)|  | [optional] 

### Return type

[**UsGetUnionResultRes**](UsGetUnionResultRes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid &#x60;body&#x60; or &#x60;Authorization&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_idv_us_start_post**
> StartIdvRes v1_idv_us_start_post(authorization=authorization, us_start_idv_req=us_start_idv_req)

[DEPRECATED] Use /v1/idv/start with country=us.

### Example


```python
import tomo_idv_client.generated
from tomo_idv_client.generated.models.start_idv_res import StartIdvRes
from tomo_idv_client.generated.models.us_start_idv_req import UsStartIdvReq
from tomo_idv_client.generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tomo_idv_client.generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with tomo_idv_client.generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tomo_idv_client.generated.DefaultApi(api_client)
    authorization = 'authorization_example' # str |  (optional)
    us_start_idv_req = tomo_idv_client.generated.UsStartIdvReq() # UsStartIdvReq |  (optional)

    try:
        api_response = api_instance.v1_idv_us_start_post(authorization=authorization, us_start_idv_req=us_start_idv_req)
        print("The response of DefaultApi->v1_idv_us_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_idv_us_start_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **us_start_idv_req** | [**UsStartIdvReq**](UsStartIdvReq.md)|  | [optional] 

### Return type

[**StartIdvRes**](StartIdvRes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid &#x60;body&#x60; or &#x60;Authorization&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_oauth2_token_post**
> TokenRes v1_oauth2_token_post(client_assertion, client_assertion_type, grant_type, resource=resource, scope=scope)

### Example


```python
import tomo_idv_client.generated
from tomo_idv_client.generated.models.token_res import TokenRes
from tomo_idv_client.generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = tomo_idv_client.generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with tomo_idv_client.generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tomo_idv_client.generated.DefaultApi(api_client)
    client_assertion = 'client_assertion_example' # str | 
    client_assertion_type = 'client_assertion_type_example' # str | 
    grant_type = 'grant_type_example' # str | 
    resource = 'resource_example' # str |  (optional)
    scope = 'scope_example' # str |  (optional)

    try:
        api_response = api_instance.v1_oauth2_token_post(client_assertion, client_assertion_type, grant_type, resource=resource, scope=scope)
        print("The response of DefaultApi->v1_oauth2_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_oauth2_token_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_assertion** | **str**|  | 
 **client_assertion_type** | **str**|  | 
 **grant_type** | **str**|  | 
 **resource** | **str**|  | [optional] 
 **scope** | **str**|  | [optional] 

### Return type

[**TokenRes**](TokenRes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json;charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid &#x60;body&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

