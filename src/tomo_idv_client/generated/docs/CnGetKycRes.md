# CnGetKycRes


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
from tomo_idv_client.generated.models.cn_get_kyc_res import CnGetKycRes

# TODO update the JSON string below
json = "{}"
# create an instance of CnGetKycRes from a JSON string
cn_get_kyc_res_instance = CnGetKycRes.from_json(json)
# print the JSON string representation of the object
print(CnGetKycRes.to_json())

# convert the object into a dict
cn_get_kyc_res_dict = cn_get_kyc_res_instance.to_dict()
# create an instance of CnGetKycRes from a dict
cn_get_kyc_res_from_dict = CnGetKycRes.from_dict(cn_get_kyc_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


