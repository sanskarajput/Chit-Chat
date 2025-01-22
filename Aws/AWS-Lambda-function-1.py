import json

def lambda_handler(event, context):
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

    num1 = data.get('num1')
    num2 = data.get('num2')

    if num1 is None or num2 is None:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Both num1 and num2 must be provided.'})
        }
    
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid input. Please provide valid numbers.'})
        }
    
    result = num1 + num2
    
    return {
        'statusCode': 200,
        'body': json.dumps({'result': result})
    }
