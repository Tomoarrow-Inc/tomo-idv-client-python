# TencentGetKycRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**date_of_birth** | **str** |  | [optional] 
**document_type** | **str** |  | [optional] 
**face_compare_passed** | **bool** |  | [optional] 
**family_name** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**given_name** | **str** |  | [optional] 
**id_number** | **str** |  | [optional] 
**issuing_country** | **str** |  | [optional] 
**liveness_passed** | **bool** |  | [optional] 
**nationality** | **str** |  | [optional] 
**ocr_passed** | **bool** |  | [optional] 
**sex** | **str** |  | [optional] 
**similarity** | **float** |  | [optional] 
**status** | **str** |  | 

## Example

```python
from tomo_idv_client.generated.models.tencent_get_kyc_res import TencentGetKycRes

# TODO update the JSON string below
json = "{}"
# create an instance of TencentGetKycRes from a JSON string
tencent_get_kyc_res_instance = TencentGetKycRes.from_json(json)
# print the JSON string representation of the object
print(TencentGetKycRes.to_json())

# convert the object into a dict
tencent_get_kyc_res_dict = tencent_get_kyc_res_instance.to_dict()
# create an instance of TencentGetKycRes from a dict
tencent_get_kyc_res_from_dict = TencentGetKycRes.from_dict(tencent_get_kyc_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


