# SessionStartRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**launch** | [**LaunchKind**](LaunchKind.md) |  | 
**session_id** | **str** |  | 

## Example

```python
from tomo_idv_client.generated.models.session_start_res import SessionStartRes

# TODO update the JSON string below
json = "{}"
# create an instance of SessionStartRes from a JSON string
session_start_res_instance = SessionStartRes.from_json(json)
# print the JSON string representation of the object
print(SessionStartRes.to_json())

# convert the object into a dict
session_start_res_dict = session_start_res_instance.to_dict()
# create an instance of SessionStartRes from a dict
session_start_res_from_dict = SessionStartRes.from_dict(session_start_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


