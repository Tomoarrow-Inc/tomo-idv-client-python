# TencentGetKycReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List[TencentIdvField]**](TencentIdvField.md) |  | [optional] 
**user_id** | **str** |  | 

## Example

```python
from tomo_idv_client.generated.models.tencent_get_kyc_req import TencentGetKycReq

# TODO update the JSON string below
json = "{}"
# create an instance of TencentGetKycReq from a JSON string
tencent_get_kyc_req_instance = TencentGetKycReq.from_json(json)
# print the JSON string representation of the object
print(TencentGetKycReq.to_json())

# convert the object into a dict
tencent_get_kyc_req_dict = tencent_get_kyc_req_instance.to_dict()
# create an instance of TencentGetKycReq from a dict
tencent_get_kyc_req_from_dict = TencentGetKycReq.from_dict(tencent_get_kyc_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


