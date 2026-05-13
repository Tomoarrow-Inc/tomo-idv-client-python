# CnStartIdvReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**best_frame_base64** | **str** |  | [optional] 
**callback_url** | **str** |  | [optional] 
**card_image_base64** | **str** |  | [optional] 
**kyc_policy_id** | **str** |  | [optional] 
**user_id** | **str** |  | 

## Example

```python
from tomo_idv_client.generated.models.cn_start_idv_req import CnStartIdvReq

# TODO update the JSON string below
json = "{}"
# create an instance of CnStartIdvReq from a JSON string
cn_start_idv_req_instance = CnStartIdvReq.from_json(json)
# print the JSON string representation of the object
print(CnStartIdvReq.to_json())

# convert the object into a dict
cn_start_idv_req_dict = cn_start_idv_req_instance.to_dict()
# create an instance of CnStartIdvReq from a dict
cn_start_idv_req_from_dict = CnStartIdvReq.from_dict(cn_start_idv_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


