# ResultRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**ResultRecord**](ResultRecord.md) |  | [optional] 
**results** | [**List[ResultRecord]**](ResultRecord.md) |  | [optional] 

## Example

```python
from tomo_idv_client.generated.models.result_res import ResultRes

# TODO update the JSON string below
json = "{}"
# create an instance of ResultRes from a JSON string
result_res_instance = ResultRes.from_json(json)
# print the JSON string representation of the object
print(ResultRes.to_json())

# convert the object into a dict
result_res_dict = result_res_instance.to_dict()
# create an instance of ResultRes from a dict
result_res_from_dict = ResultRes.from_dict(result_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


