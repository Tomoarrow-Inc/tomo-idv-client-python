# JpGetKycReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List[JpIdvField]**](JpIdvField.md) |  | [optional] 
**user_id** | **str** |  | 

## Example

```python
from tomo_idv_client.generated.models.jp_get_kyc_req import JpGetKycReq

# TODO update the JSON string below
json = "{}"
# create an instance of JpGetKycReq from a JSON string
jp_get_kyc_req_instance = JpGetKycReq.from_json(json)
# print the JSON string representation of the object
print(JpGetKycReq.to_json())

# convert the object into a dict
jp_get_kyc_req_dict = jp_get_kyc_req_instance.to_dict()
# create an instance of JpGetKycReq from a dict
jp_get_kyc_req_from_dict = JpGetKycReq.from_dict(jp_get_kyc_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


