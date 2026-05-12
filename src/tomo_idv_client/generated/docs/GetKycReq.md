# GetKycReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | [**Country**](Country.md) |  | 
**user_id** | **str** |  | 

## Example

```python
from tomo_idv_client.generated.models.get_kyc_req import GetKycReq

# TODO update the JSON string below
json = "{}"
# create an instance of GetKycReq from a JSON string
get_kyc_req_instance = GetKycReq.from_json(json)
# print the JSON string representation of the object
print(GetKycReq.to_json())

# convert the object into a dict
get_kyc_req_dict = get_kyc_req_instance.to_dict()
# create an instance of GetKycReq from a dict
get_kyc_req_from_dict = GetKycReq.from_dict(get_kyc_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


