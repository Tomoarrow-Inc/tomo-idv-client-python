# LiquidGetUnionResultRes


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
from tomo_idv_client.generated.models.liquid_get_union_result_res import LiquidGetUnionResultRes

# TODO update the JSON string below
json = "{}"
# create an instance of LiquidGetUnionResultRes from a JSON string
liquid_get_union_result_res_instance = LiquidGetUnionResultRes.from_json(json)
# print the JSON string representation of the object
print(LiquidGetUnionResultRes.to_json())

# convert the object into a dict
liquid_get_union_result_res_dict = liquid_get_union_result_res_instance.to_dict()
# create an instance of LiquidGetUnionResultRes from a dict
liquid_get_union_result_res_from_dict = LiquidGetUnionResultRes.from_dict(liquid_get_union_result_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


