def lambda_handler(event, context):
    with open("index.html") as source_file:
        source_code = source_file.read()

    return {
        "statusCode": 200,
        "body": source_code,
        "headers": {"Content-Type": "text/html"},
    }
