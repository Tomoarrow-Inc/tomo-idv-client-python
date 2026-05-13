# ResultReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | [**Country**](Country.md) |  | [optional]
**policy** | [**KycPolicy**](KycPolicy.md) |  | [optional]
**user_id** | **str** |  |

## Example

```python
from tomo_idv_client.generated.models.result_req import ResultReq

# TODO update the JSON string below
json = "{}"
# create an instance of ResultReq from a JSON string
result_req_instance = ResultReq.from_json(json)
# print the JSON string representation of the object
print(ResultReq.to_json())

# convert the object into a dict
result_req_dict = result_req_instance.to_dict()
# create an instance of ResultReq from a dict
result_req_from_dict = ResultReq.from_dict(result_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

