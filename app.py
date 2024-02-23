#!/usr/bin/env python3
import os

import aws_cdk as cdk

from serverless_api.serverless_api_stack import ServerlessApiStack
from serverless_api.test_s3_stack import testS3Stack


app = cdk.App()
ServerlessApiStack(
    app,
    "ServerlessApiStack",
    env=cdk.Environment(account="316770681739", region="ap-south-1"),
)

# testS3Stack(app, "testS3Stack", env=cdk.Environment(account='316770681739', region='us-east-1'),)

# Add tags to all resources in the app
cdk.Tags.of(app).add("source", "cdk-serverless-api")


app.synth()
