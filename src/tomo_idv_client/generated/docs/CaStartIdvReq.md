# CaStartIdvReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_url** | **str** |  | 
**email** | **str** |  | [optional] 
**kyc_policy_id** | **str** |  | [optional] 
**user_id** | **str** |  | 

## Example

```python
from tomo_idv_client.generated.models.ca_start_idv_req import CaStartIdvReq

# TODO update the JSON string below
json = "{}"
# create an instance of CaStartIdvReq from a JSON string
ca_start_idv_req_instance = CaStartIdvReq.from_json(json)
# print the JSON string representation of the object
print(CaStartIdvReq.to_json())

# convert the object into a dict
ca_start_idv_req_dict = ca_start_idv_req_instance.to_dict()
# create an instance of CaStartIdvReq from a dict
ca_start_idv_req_from_dict = CaStartIdvReq.from_dict(ca_start_idv_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


