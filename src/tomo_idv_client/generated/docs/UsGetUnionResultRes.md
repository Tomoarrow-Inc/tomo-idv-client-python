# UsGetUnionResultRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** |  | 
**country** | **str** |  | 
**date_of_birth** | **str** |  | 
**email_address** | **str** |  | 
**family_name** | **str** |  | 
**given_name** | **str** |  | 
**phone_number** | **str** |  | 
**postal_code** | **str** |  | 
**region** | **str** |  | 
**street** | **str** |  | 

## Example

```python
from tomo_idv_client.generated.models.us_get_union_result_res import UsGetUnionResultRes

# TODO update the JSON string below
json = "{}"
# create an instance of UsGetUnionResultRes from a JSON string
us_get_union_result_res_instance = UsGetUnionResultRes.from_json(json)
# print the JSON string representation of the object
print(UsGetUnionResultRes.to_json())

# convert the object into a dict
us_get_union_result_res_dict = us_get_union_result_res_instance.to_dict()
# create an instance of UsGetUnionResultRes from a dict
us_get_union_result_res_from_dict = UsGetUnionResultRes.from_dict(us_get_union_result_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


