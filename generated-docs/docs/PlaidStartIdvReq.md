# PlaidStartIdvReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_url** | **str** |  | 
**email** | **str** |  | [optional] 
**kyc_policy_id** | **str** |  | [optional] 
**user_id** | **str** |  | 

## Example

```python
from tomo_idv_client.generated.models.plaid_start_idv_req import PlaidStartIdvReq

# TODO update the JSON string below
json = "{}"
# create an instance of PlaidStartIdvReq from a JSON string
plaid_start_idv_req_instance = PlaidStartIdvReq.from_json(json)
# print the JSON string representation of the object
print(PlaidStartIdvReq.to_json())

# convert the object into a dict
plaid_start_idv_req_dict = plaid_start_idv_req_instance.to_dict()
# create an instance of PlaidStartIdvReq from a dict
plaid_start_idv_req_from_dict = PlaidStartIdvReq.from_dict(plaid_start_idv_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


