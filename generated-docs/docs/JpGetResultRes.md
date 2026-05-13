# JpGetResultRes


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
from tomo_idv_client.generated.models.jp_get_result_res import JpGetResultRes

# TODO update the JSON string below
json = "{}"
# create an instance of JpGetResultRes from a JSON string
jp_get_result_res_instance = JpGetResultRes.from_json(json)
# print the JSON string representation of the object
print(JpGetResultRes.to_json())

# convert the object into a dict
jp_get_result_res_dict = jp_get_result_res_instance.to_dict()
# create an instance of JpGetResultRes from a dict
jp_get_result_res_from_dict = JpGetResultRes.from_dict(jp_get_result_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


