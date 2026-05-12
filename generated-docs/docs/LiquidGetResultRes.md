# LiquidGetResultRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 
**date_of_birth** | **str** |  | 
**name** | **str** |  | 
**postal_code** | **str** |  | [optional] 
**sex** | **str** |  | 

## Example

```python
from tomo_idv_client.generated.models.liquid_get_result_res import LiquidGetResultRes

# TODO update the JSON string below
json = "{}"
# create an instance of LiquidGetResultRes from a JSON string
liquid_get_result_res_instance = LiquidGetResultRes.from_json(json)
# print the JSON string representation of the object
print(LiquidGetResultRes.to_json())

# convert the object into a dict
liquid_get_result_res_dict = liquid_get_result_res_instance.to_dict()
# create an instance of LiquidGetResultRes from a dict
liquid_get_result_res_from_dict = LiquidGetResultRes.from_dict(liquid_get_result_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


