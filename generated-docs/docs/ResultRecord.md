# ResultRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_id** | **str** |  | 
**country** | **str** |  | 
**policy_key** | **str** |  | 
**result** | [**GetKycRes**](GetKycRes.md) |  | 

## Example

```python
from tomo_idv_client.generated.models.result_record import ResultRecord

# TODO update the JSON string below
json = "{}"
# create an instance of ResultRecord from a JSON string
result_record_instance = ResultRecord.from_json(json)
# print the JSON string representation of the object
print(ResultRecord.to_json())

# convert the object into a dict
result_record_dict = result_record_instance.to_dict()
# create an instance of ResultRecord from a dict
result_record_from_dict = ResultRecord.from_dict(result_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


