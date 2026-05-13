# JpGetUnionResultRes


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
from tomo_idv_client.generated.models.jp_get_union_result_res import JpGetUnionResultRes

# TODO update the JSON string below
json = "{}"
# create an instance of JpGetUnionResultRes from a JSON string
jp_get_union_result_res_instance = JpGetUnionResultRes.from_json(json)
# print the JSON string representation of the object
print(JpGetUnionResultRes.to_json())

# convert the object into a dict
jp_get_union_result_res_dict = jp_get_union_result_res_instance.to_dict()
# create an instance of JpGetUnionResultRes from a dict
jp_get_union_result_res_from_dict = JpGetUnionResultRes.from_dict(jp_get_union_result_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


