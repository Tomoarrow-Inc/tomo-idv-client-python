# TomoIdvIssueTokenRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_in** | **int** |  | 
**key** | **str** |  | 
**session_token** | **str** |  | 

## Example

```python
from tomo_idv_client.generated.models.tomo_idv_issue_token_res import TomoIdvIssueTokenRes

# TODO update the JSON string below
json = "{}"
# create an instance of TomoIdvIssueTokenRes from a JSON string
tomo_idv_issue_token_res_instance = TomoIdvIssueTokenRes.from_json(json)
# print the JSON string representation of the object
print(TomoIdvIssueTokenRes.to_json())

# convert the object into a dict
tomo_idv_issue_token_res_dict = tomo_idv_issue_token_res_instance.to_dict()
# create an instance of TomoIdvIssueTokenRes from a dict
tomo_idv_issue_token_res_from_dict = TomoIdvIssueTokenRes.from_dict(tomo_idv_issue_token_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


