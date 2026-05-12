# tomo_idv_client.generated.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_idv_ca_health_get**](DefaultApi.md#v1_idv_ca_health_get) | **GET** /v1/idv/ca/health | 
[**v1_idv_ca_kyc_get_post**](DefaultApi.md#v1_idv_ca_kyc_get_post) | **POST** /v1/idv/ca/kyc/get | 
[**v1_idv_ca_start_post**](DefaultApi.md#v1_idv_ca_start_post) | **POST** /v1/idv/ca/start | 
[**v1_idv_cn_cookie_start_post**](DefaultApi.md#v1_idv_cn_cookie_start_post) | **POST** /v1/idv/cn/cookie/start | 
[**v1_idv_cn_health_get**](DefaultApi.md#v1_idv_cn_health_get) | **GET** /v1/idv/cn/health | 
[**v1_idv_cn_kyc_get_post**](DefaultApi.md#v1_idv_cn_kyc_get_post) | **POST** /v1/idv/cn/kyc/get | 
[**v1_idv_cn_result_web_post**](DefaultApi.md#v1_idv_cn_result_web_post) | **POST** /v1/idv/cn/result/web | 
[**v1_idv_cn_start_post**](DefaultApi.md#v1_idv_cn_start_post) | **POST** /v1/idv/cn/start | 
[**v1_idv_cn_token_post**](DefaultApi.md#v1_idv_cn_token_post) | **POST** /v1/idv/cn/token | 
[**v1_idv_jp_health_get**](DefaultApi.md#v1_idv_jp_health_get) | **GET** /v1/idv/jp/health | 
[**v1_idv_jp_kyc_get_post**](DefaultApi.md#v1_idv_jp_kyc_get_post) | **POST** /v1/idv/jp/kyc/get | 
[**v1_idv_jp_start_post**](DefaultApi.md#v1_idv_jp_start_post) | **POST** /v1/idv/jp/start | 
[**v1_idv_kyc_get_post**](DefaultApi.md#v1_idv_kyc_get_post) | **POST** /v1/idv/kyc/get | 
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
> Dict[str, str] v1_idv_ca_kyc_get_post(authorization=authorization, plaid_get_kyc_req=plaid_get_kyc_req)

### Example


```python
import tomo_idv_client.generated
from tomo_idv_client.generated.models.plaid_get_kyc_req import PlaidGetKycReq
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
    plaid_get_kyc_req = tomo_idv_client.generated.PlaidGetKycReq() # PlaidGetKycReq |  (optional)

    try:
        api_response = api_instance.v1_idv_ca_kyc_get_post(authorization=authorization, plaid_get_kyc_req=plaid_get_kyc_req)
        print("The response of DefaultApi->v1_idv_ca_kyc_get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_idv_ca_kyc_get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **plaid_get_kyc_req** | [**PlaidGetKycReq**](PlaidGetKycReq.md)|  | [optional] 

### Return type

**Dict[str, str]**

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
> PlaidStartIdvRes v1_idv_ca_start_post(authorization=authorization, plaid_start_idv_req=plaid_start_idv_req)

### Example


```python
import tomo_idv_client.generated
from tomo_idv_client.generated.models.plaid_start_idv_req import PlaidStartIdvReq
from tomo_idv_client.generated.models.plaid_start_idv_res import PlaidStartIdvRes
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
    plaid_start_idv_req = tomo_idv_client.generated.PlaidStartIdvReq() # PlaidStartIdvReq |  (optional)

    try:
        api_response = api_instance.v1_idv_ca_start_post(authorization=authorization, plaid_start_idv_req=plaid_start_idv_req)
        print("The response of DefaultApi->v1_idv_ca_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_idv_ca_start_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **plaid_start_idv_req** | [**PlaidStartIdvReq**](PlaidStartIdvReq.md)|  | [optional] 

### Return type

[**PlaidStartIdvRes**](PlaidStartIdvRes.md)

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

# **v1_idv_cn_cookie_start_post**
> TencentStartIdvRes v1_idv_cn_cookie_start_post(tencent_start_req=tencent_start_req)

### Example


```python
import tomo_idv_client.generated
from tomo_idv_client.generated.models.tencent_start_idv_res import TencentStartIdvRes
from tomo_idv_client.generated.models.tencent_start_req import TencentStartReq
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
    tencent_start_req = tomo_idv_client.generated.TencentStartReq() # TencentStartReq |  (optional)

    try:
        api_response = api_instance.v1_idv_cn_cookie_start_post(tencent_start_req=tencent_start_req)
        print("The response of DefaultApi->v1_idv_cn_cookie_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_idv_cn_cookie_start_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tencent_start_req** | [**TencentStartReq**](TencentStartReq.md)|  | [optional] 

### Return type

[**TencentStartIdvRes**](TencentStartIdvRes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * Set-Cookie -  <br>  |
**400** | Invalid &#x60;body&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_idv_cn_health_get**
> str v1_idv_cn_health_get()

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
> TencentGetUnionResultRes v1_idv_cn_kyc_get_post(authorization=authorization, tencent_get_kyc_req=tencent_get_kyc_req)

### Example


```python
import tomo_idv_client.generated
from tomo_idv_client.generated.models.tencent_get_kyc_req import TencentGetKycReq
from tomo_idv_client.generated.models.tencent_get_union_result_res import TencentGetUnionResultRes
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
    tencent_get_kyc_req = tomo_idv_client.generated.TencentGetKycReq() # TencentGetKycReq |  (optional)

    try:
        api_response = api_instance.v1_idv_cn_kyc_get_post(authorization=authorization, tencent_get_kyc_req=tencent_get_kyc_req)
        print("The response of DefaultApi->v1_idv_cn_kyc_get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_idv_cn_kyc_get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **tencent_get_kyc_req** | [**TencentGetKycReq**](TencentGetKycReq.md)|  | [optional] 

### Return type

[**TencentGetUnionResultRes**](TencentGetUnionResultRes.md)

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

# **v1_idv_cn_result_web_post**
> object v1_idv_cn_result_web_post()

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
        api_response = api_instance.v1_idv_cn_result_web_post()
        print("The response of DefaultApi->v1_idv_cn_result_web_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_idv_cn_result_web_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

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

# **v1_idv_cn_start_post**
> TencentStartIdvRes v1_idv_cn_start_post(authorization=authorization, tencent_start_req=tencent_start_req)

### Example


```python
import tomo_idv_client.generated
from tomo_idv_client.generated.models.tencent_start_idv_res import TencentStartIdvRes
from tomo_idv_client.generated.models.tencent_start_req import TencentStartReq
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
    tencent_start_req = tomo_idv_client.generated.TencentStartReq() # TencentStartReq |  (optional)

    try:
        api_response = api_instance.v1_idv_cn_start_post(authorization=authorization, tencent_start_req=tencent_start_req)
        print("The response of DefaultApi->v1_idv_cn_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_idv_cn_start_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **tencent_start_req** | [**TencentStartReq**](TencentStartReq.md)|  | [optional] 

### Return type

[**TencentStartIdvRes**](TencentStartIdvRes.md)

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

# **v1_idv_jp_health_get**
> str v1_idv_jp_health_get()

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
> LiquidGetUnionResultRes v1_idv_jp_kyc_get_post(authorization=authorization, liquid_get_kyc_req=liquid_get_kyc_req)

### Example


```python
import tomo_idv_client.generated
from tomo_idv_client.generated.models.liquid_get_kyc_req import LiquidGetKycReq
from tomo_idv_client.generated.models.liquid_get_union_result_res import LiquidGetUnionResultRes
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
    liquid_get_kyc_req = tomo_idv_client.generated.LiquidGetKycReq() # LiquidGetKycReq |  (optional)

    try:
        api_response = api_instance.v1_idv_jp_kyc_get_post(authorization=authorization, liquid_get_kyc_req=liquid_get_kyc_req)
        print("The response of DefaultApi->v1_idv_jp_kyc_get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_idv_jp_kyc_get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **liquid_get_kyc_req** | [**LiquidGetKycReq**](LiquidGetKycReq.md)|  | [optional] 

### Return type

[**LiquidGetUnionResultRes**](LiquidGetUnionResultRes.md)

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
> LiquidIntegratedAppRes v1_idv_jp_start_post(authorization=authorization, liquid_start_idv_req=liquid_start_idv_req)

### Example


```python
import tomo_idv_client.generated
from tomo_idv_client.generated.models.liquid_integrated_app_res import LiquidIntegratedAppRes
from tomo_idv_client.generated.models.liquid_start_idv_req import LiquidStartIdvReq
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
    liquid_start_idv_req = tomo_idv_client.generated.LiquidStartIdvReq() # LiquidStartIdvReq |  (optional)

    try:
        api_response = api_instance.v1_idv_jp_start_post(authorization=authorization, liquid_start_idv_req=liquid_start_idv_req)
        print("The response of DefaultApi->v1_idv_jp_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_idv_jp_start_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **liquid_start_idv_req** | [**LiquidStartIdvReq**](LiquidStartIdvReq.md)|  | [optional] 

### Return type

[**LiquidIntegratedAppRes**](LiquidIntegratedAppRes.md)

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

# **v1_idv_sessions_start_post**
> SessionStartRes v1_idv_sessions_start_post(authorization=authorization, session_start_req=session_start_req)

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
> Dict[str, str] v1_idv_uk_kyc_get_post(authorization=authorization, plaid_get_kyc_req=plaid_get_kyc_req)

### Example


```python
import tomo_idv_client.generated
from tomo_idv_client.generated.models.plaid_get_kyc_req import PlaidGetKycReq
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
    plaid_get_kyc_req = tomo_idv_client.generated.PlaidGetKycReq() # PlaidGetKycReq |  (optional)

    try:
        api_response = api_instance.v1_idv_uk_kyc_get_post(authorization=authorization, plaid_get_kyc_req=plaid_get_kyc_req)
        print("The response of DefaultApi->v1_idv_uk_kyc_get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_idv_uk_kyc_get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **plaid_get_kyc_req** | [**PlaidGetKycReq**](PlaidGetKycReq.md)|  | [optional] 

### Return type

**Dict[str, str]**

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
> PlaidStartIdvRes v1_idv_uk_start_post(authorization=authorization, plaid_start_idv_req=plaid_start_idv_req)

### Example


```python
import tomo_idv_client.generated
from tomo_idv_client.generated.models.plaid_start_idv_req import PlaidStartIdvReq
from tomo_idv_client.generated.models.plaid_start_idv_res import PlaidStartIdvRes
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
    plaid_start_idv_req = tomo_idv_client.generated.PlaidStartIdvReq() # PlaidStartIdvReq |  (optional)

    try:
        api_response = api_instance.v1_idv_uk_start_post(authorization=authorization, plaid_start_idv_req=plaid_start_idv_req)
        print("The response of DefaultApi->v1_idv_uk_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_idv_uk_start_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **plaid_start_idv_req** | [**PlaidStartIdvReq**](PlaidStartIdvReq.md)|  | [optional] 

### Return type

[**PlaidStartIdvRes**](PlaidStartIdvRes.md)

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
> Dict[str, str] v1_idv_us_kyc_get_post(authorization=authorization, plaid_get_kyc_req=plaid_get_kyc_req)

### Example


```python
import tomo_idv_client.generated
from tomo_idv_client.generated.models.plaid_get_kyc_req import PlaidGetKycReq
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
    plaid_get_kyc_req = tomo_idv_client.generated.PlaidGetKycReq() # PlaidGetKycReq |  (optional)

    try:
        api_response = api_instance.v1_idv_us_kyc_get_post(authorization=authorization, plaid_get_kyc_req=plaid_get_kyc_req)
        print("The response of DefaultApi->v1_idv_us_kyc_get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_idv_us_kyc_get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **plaid_get_kyc_req** | [**PlaidGetKycReq**](PlaidGetKycReq.md)|  | [optional] 

### Return type

**Dict[str, str]**

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
> PlaidStartIdvRes v1_idv_us_start_post(authorization=authorization, plaid_start_idv_req=plaid_start_idv_req)

### Example


```python
import tomo_idv_client.generated
from tomo_idv_client.generated.models.plaid_start_idv_req import PlaidStartIdvReq
from tomo_idv_client.generated.models.plaid_start_idv_res import PlaidStartIdvRes
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
    plaid_start_idv_req = tomo_idv_client.generated.PlaidStartIdvReq() # PlaidStartIdvReq |  (optional)

    try:
        api_response = api_instance.v1_idv_us_start_post(authorization=authorization, plaid_start_idv_req=plaid_start_idv_req)
        print("The response of DefaultApi->v1_idv_us_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_idv_us_start_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **plaid_start_idv_req** | [**PlaidStartIdvReq**](PlaidStartIdvReq.md)|  | [optional] 

### Return type

[**PlaidStartIdvRes**](PlaidStartIdvRes.md)

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

