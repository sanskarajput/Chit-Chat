def lambda_handler(event, context):
    """
    AWS Lambda function that adds two numbers from the event payload
    
    Parameters:
    event (dict): Must contain 'num1' and 'num2' keys with numeric values
    context (LambdaContext): AWS Lambda Context object
    
    Returns:
    dict: Contains 'statusCode' and 'body' with the sum result
    """
    try:
        num1 = float(event.get('num1', 0))
        num2 = float(event.get('num2', 0))
        
        result = num1 + num2
        
        response = {
            'statusCode': 200,
            'body': {
                'result': result,
                'message': f'Successfully added {num1} and {num2}'
            }
        }
        
    except (ValueError, TypeError) as e:
        response = {
            'statusCode': 400,
            'body': {
                'error': 'Invalid input. Please provide valid numbers.',
                'message': str(e)
            }
        }
    
    return response