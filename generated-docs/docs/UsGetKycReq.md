# UsGetKycReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List[UsIdvField]**](UsIdvField.md) |  | [optional] 
**user_id** | **str** |  | 

## Example

```python
from tomo_idv_client.generated.models.us_get_kyc_req import UsGetKycReq

# TODO update the JSON string below
json = "{}"
# create an instance of UsGetKycReq from a JSON string
us_get_kyc_req_instance = UsGetKycReq.from_json(json)
# print the JSON string representation of the object
print(UsGetKycReq.to_json())

# convert the object into a dict
us_get_kyc_req_dict = us_get_kyc_req_instance.to_dict()
# create an instance of UsGetKycReq from a dict
us_get_kyc_req_from_dict = UsGetKycReq.from_dict(us_get_kyc_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


