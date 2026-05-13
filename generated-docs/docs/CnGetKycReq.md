# CnGetKycReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List[CnIdvField]**](CnIdvField.md) |  | [optional] 
**user_id** | **str** |  | 

## Example

```python
from tomo_idv_client.generated.models.cn_get_kyc_req import CnGetKycReq

# TODO update the JSON string below
json = "{}"
# create an instance of CnGetKycReq from a JSON string
cn_get_kyc_req_instance = CnGetKycReq.from_json(json)
# print the JSON string representation of the object
print(CnGetKycReq.to_json())

# convert the object into a dict
cn_get_kyc_req_dict = cn_get_kyc_req_instance.to_dict()
# create an instance of CnGetKycReq from a dict
cn_get_kyc_req_from_dict = CnGetKycReq.from_dict(cn_get_kyc_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


