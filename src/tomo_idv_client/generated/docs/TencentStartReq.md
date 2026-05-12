# TencentStartReq


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
from tomo_idv_client.generated.models.tencent_start_req import TencentStartReq

# TODO update the JSON string below
json = "{}"
# create an instance of TencentStartReq from a JSON string
tencent_start_req_instance = TencentStartReq.from_json(json)
# print the JSON string representation of the object
print(TencentStartReq.to_json())

# convert the object into a dict
tencent_start_req_dict = tencent_start_req_instance.to_dict()
# create an instance of TencentStartReq from a dict
tencent_start_req_from_dict = TencentStartReq.from_dict(tencent_start_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


