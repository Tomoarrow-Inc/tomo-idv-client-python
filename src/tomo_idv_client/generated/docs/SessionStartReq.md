# SessionStartReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_url** | **str** |  | [optional] 
**country** | [**Country**](Country.md) |  | [optional] 
**email** | **str** |  | [optional] 
**policy_id** | **str** |  | [optional] 
**user_id** | **str** |  | 

## Example

```python
from tomo_idv_client.generated.models.session_start_req import SessionStartReq

# TODO update the JSON string below
json = "{}"
# create an instance of SessionStartReq from a JSON string
session_start_req_instance = SessionStartReq.from_json(json)
# print the JSON string representation of the object
print(SessionStartReq.to_json())

# convert the object into a dict
session_start_req_dict = session_start_req_instance.to_dict()
# create an instance of SessionStartReq from a dict
session_start_req_from_dict = SessionStartReq.from_dict(session_start_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


