# LaunchKind


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** |  | [optional] 
**data** | **str** |  | [optional] 
**fallback_url** | **str** |  | [optional] 
**session_token** | **str** |  | [optional] 
**type** | **str** |  | 
**url** | **str** |  | [optional] 

## Example

```python
from tomo_idv_client.generated.models.launch_kind import LaunchKind

# TODO update the JSON string below
json = "{}"
# create an instance of LaunchKind from a JSON string
launch_kind_instance = LaunchKind.from_json(json)
# print the JSON string representation of the object
print(LaunchKind.to_json())

# convert the object into a dict
launch_kind_dict = launch_kind_instance.to_dict()
# create an instance of LaunchKind from a dict
launch_kind_from_dict = LaunchKind.from_dict(launch_kind_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


