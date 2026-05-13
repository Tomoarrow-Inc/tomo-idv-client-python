# UkStartIdvReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_url** | **str** |  | 
**email** | **str** |  | [optional] 
**kyc_policy_id** | **str** |  | [optional] 
**user_id** | **str** |  | 

## Example

```python
from tomo_idv_client.generated.models.uk_start_idv_req import UkStartIdvReq

# TODO update the JSON string below
json = "{}"
# create an instance of UkStartIdvReq from a JSON string
uk_start_idv_req_instance = UkStartIdvReq.from_json(json)
# print the JSON string representation of the object
print(UkStartIdvReq.to_json())

# convert the object into a dict
uk_start_idv_req_dict = uk_start_idv_req_instance.to_dict()
# create an instance of UkStartIdvReq from a dict
uk_start_idv_req_from_dict = UkStartIdvReq.from_dict(uk_start_idv_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


