# ClassAttachmentCreation

Attachment creation for an assignment or stream post. This attachment must contain a `score` or an `url`, all the details of this one will be resolved and returned as `ClassAttachment` once the assignment or stream post is created. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the attachment posted | [optional] 
**score** | **str** | A unique Flat score identifier. The user creating the assignment must at least have read access to the document. If the user has admin rights, new group permissions will be automatically added for the teachers and students of the class.  | [optional] 
**sharing_mode** | [**MediaScoreSharingMode**](MediaScoreSharingMode.md) |  | [optional] 
**url** | **str** | The URL of the attachment. | [optional] 
**google_drive_file_id** | **str** | The ID of the Google Drive File | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


