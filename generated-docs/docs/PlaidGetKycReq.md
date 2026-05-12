# PlaidGetKycReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List[PlaidIdvField]**](PlaidIdvField.md) |  | [optional] 
**user_id** | **str** |  | 

## Example

```python
from tomo_idv_client.generated.models.plaid_get_kyc_req import PlaidGetKycReq

# TODO update the JSON string below
json = "{}"
# create an instance of PlaidGetKycReq from a JSON string
plaid_get_kyc_req_instance = PlaidGetKycReq.from_json(json)
# print the JSON string representation of the object
print(PlaidGetKycReq.to_json())

# convert the object into a dict
plaid_get_kyc_req_dict = plaid_get_kyc_req_instance.to_dict()
# create an instance of PlaidGetKycReq from a dict
plaid_get_kyc_req_from_dict = PlaidGetKycReq.from_dict(plaid_get_kyc_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


