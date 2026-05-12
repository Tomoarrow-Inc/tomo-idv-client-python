# LiquidGetKycReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List[LiquidIdvField]**](LiquidIdvField.md) |  | [optional] 
**user_id** | **str** |  | 

## Example

```python
from tomo_idv_client.generated.models.liquid_get_kyc_req import LiquidGetKycReq

# TODO update the JSON string below
json = "{}"
# create an instance of LiquidGetKycReq from a JSON string
liquid_get_kyc_req_instance = LiquidGetKycReq.from_json(json)
# print the JSON string representation of the object
print(LiquidGetKycReq.to_json())

# convert the object into a dict
liquid_get_kyc_req_dict = liquid_get_kyc_req_instance.to_dict()
# create an instance of LiquidGetKycReq from a dict
liquid_get_kyc_req_from_dict = LiquidGetKycReq.from_dict(liquid_get_kyc_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


