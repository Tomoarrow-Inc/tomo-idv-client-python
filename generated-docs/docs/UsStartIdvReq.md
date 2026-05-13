# UsStartIdvReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_url** | **str** |  | 
**email** | **str** |  | [optional] 
**kyc_policy_id** | **str** |  | [optional] 
**user_id** | **str** |  | 

## Example

```python
from tomo_idv_client.generated.models.us_start_idv_req import UsStartIdvReq

# TODO update the JSON string below
json = "{}"
# create an instance of UsStartIdvReq from a JSON string
us_start_idv_req_instance = UsStartIdvReq.from_json(json)
# print the JSON string representation of the object
print(UsStartIdvReq.to_json())

# convert the object into a dict
us_start_idv_req_dict = us_start_idv_req_instance.to_dict()
# create an instance of UsStartIdvReq from a dict
us_start_idv_req_from_dict = UsStartIdvReq.from_dict(us_start_idv_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


