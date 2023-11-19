import base64

import boto3


def lambda_handler(event, context):
    print(f"{event=}")
    print(f"{context=}")

    clt = boto3.client("rekognition")

    # body部分にエンコードされた送信データが含まれている
    body = event["body"]
    print(f"{body=}")
    decoded = base64.b64decode(body)
    print(f"{decoded=}")

    return "OK"
