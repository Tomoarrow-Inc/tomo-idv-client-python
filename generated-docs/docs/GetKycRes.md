# GetKycRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** |  | [optional] 
**country** | **str** |  | 
**date_of_birth** | **str** |  | 
**email_address** | **str** |  | [optional] 
**family_name** | **str** |  | [optional] 
**full_address** | **str** |  | 
**full_name** | **str** |  | 
**given_name** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**sex** | **str** |  | [optional] 
**street** | **str** |  | [optional] 

## Example

```python
from tomo_idv_client.generated.models.get_kyc_res import GetKycRes

# TODO update the JSON string below
json = "{}"
# create an instance of GetKycRes from a JSON string
get_kyc_res_instance = GetKycRes.from_json(json)
# print the JSON string representation of the object
print(GetKycRes.to_json())

# convert the object into a dict
get_kyc_res_dict = get_kyc_res_instance.to_dict()
# create an instance of GetKycRes from a dict
get_kyc_res_from_dict = GetKycRes.from_dict(get_kyc_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


