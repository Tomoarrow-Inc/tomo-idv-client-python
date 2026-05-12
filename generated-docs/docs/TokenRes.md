# TokenRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | 
**expires_in** | **int** |  | 
**scope** | **str** |  | [optional] 
**token_type** | **str** |  | 

## Example

```python
from tomo_idv_client.generated.models.token_res import TokenRes

# TODO update the JSON string below
json = "{}"
# create an instance of TokenRes from a JSON string
token_res_instance = TokenRes.from_json(json)
# print the JSON string representation of the object
print(TokenRes.to_json())

# convert the object into a dict
token_res_dict = token_res_instance.to_dict()
# create an instance of TokenRes from a dict
token_res_from_dict = TokenRes.from_dict(token_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


