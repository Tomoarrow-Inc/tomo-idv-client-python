# StartIdvReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_url** | **str** |  | 
**country** | [**Country**](Country.md) |  | [optional] 
**email** | **str** |  | [optional] 
**kyc_policy** | [**KycPolicy**](KycPolicy.md) |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from tomo_idv_client.generated.models.start_idv_req import StartIdvReq

# TODO update the JSON string below
json = "{}"
# create an instance of StartIdvReq from a JSON string
start_idv_req_instance = StartIdvReq.from_json(json)
# print the JSON string representation of the object
print(StartIdvReq.to_json())

# convert the object into a dict
start_idv_req_dict = start_idv_req_instance.to_dict()
# create an instance of StartIdvReq from a dict
start_idv_req_from_dict = StartIdvReq.from_dict(start_idv_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


