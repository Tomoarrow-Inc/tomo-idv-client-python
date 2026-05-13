# KycPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** |  | 
**owner_assurance** | **object** |  | 
**subject** | **object** |  | 

## Example

```python
from tomo_idv_client.generated.models.kyc_policy import KycPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of KycPolicy from a JSON string
kyc_policy_instance = KycPolicy.from_json(json)
# print the JSON string representation of the object
print(KycPolicy.to_json())

# convert the object into a dict
kyc_policy_dict = kyc_policy_instance.to_dict()
# create an instance of KycPolicy from a dict
kyc_policy_from_dict = KycPolicy.from_dict(kyc_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


