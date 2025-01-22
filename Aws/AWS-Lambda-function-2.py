import json
import os
import base64
import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    """
    AWS Lambda function that stores a document/PDF file in an S3 bucket
    
    Parameters:
    event (dict): Must contain:
        - fileName: name of the file to be stored
        - fileContent: base64 encoded file content
        - contentType: MIME type of the file (e.g., 'application/pdf')
    
    Returns:
    dict: Contains statusCode and response message
    """
    body = event.get('body')

    if body is None:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Request body is missing.'})
        }

    try:
        data = json.loads(body)
    except (ValueError, TypeError, OverflowError):
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid JSON format in request body.'})
        }

    try:
        bucket_name = os.environ['S3_BUCKET_NAME']
        file_name = data['fileName']
        file_content = data['fileContent']
        content_type = data['contentType']
        
        decoded_content = base64.b64decode(file_content)
        
        file_key = f"uploads/{file_name}"
        
        s3_client.put_object(
            Bucket=bucket_name,
            Key=file_key,
            Body=decoded_content,
            ContentType=content_type
        )
        presigned_url = s3_client.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': bucket_name,
                'Key': file_key
            },
            ExpiresIn=3600
        )
        
        logger.info(f"Successfully uploaded file {file_name} to {bucket_name}/{file_key}")
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'File uploaded successfully',
                'fileKey': file_key,
                'presignedUrl': presigned_url
            })
        }

    except KeyError as e:
        logger.error(f"Missing required field: {str(e)}")
        return {
            'statusCode': 400,
            'body': json.dumps({
                'error': 'Missing required field',
                'details': str(e)
            })
        }
        
    except ClientError as e:
        logger.error(f"S3 operation failed: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': 'Failed to upload file to S3',
                'details': str(e)
            })
        }
        
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': 'Internal server error',
                'details': str(e)
            })
        }