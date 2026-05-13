# JpStartIdvReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_url** | **str** |  | 
**kyc_policy_id** | **str** |  | [optional] 
**user_id** | **str** |  | 

## Example

```python
from tomo_idv_client.generated.models.jp_start_idv_req import JpStartIdvReq

# TODO update the JSON string below
json = "{}"
# create an instance of JpStartIdvReq from a JSON string
jp_start_idv_req_instance = JpStartIdvReq.from_json(json)
# print the JSON string representation of the object
print(JpStartIdvReq.to_json())

# convert the object into a dict
jp_start_idv_req_dict = jp_start_idv_req_instance.to_dict()
# create an instance of JpStartIdvReq from a dict
jp_start_idv_req_from_dict = JpStartIdvReq.from_dict(jp_start_idv_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


