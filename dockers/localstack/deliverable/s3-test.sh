#!/usr/bin/env bash

: '
    Simple unit test to ensure localstack S3 is up and running
'

BUCKET_NAME="example-bucket"

awsInvoke() {
    aws "$@"
}

s3CreateBucket() {
    local name="${1}"
    awsInvoke s3api create-bucket \
        --bucket "${name}" \
        --region us-east-1 \
        --endpoint-url=http://localhost:4566
}

s3BucketList() {
    awsInvoke s3 ls --endpoint-url=http://localhost:4566
}

s3DeleteBucket() {
    local name="${1}"
    awsInvoke s3api delete-bucket \
        --bucket "${name}" \
        --endpoint-url=http://localhost:4566
}

main() {
    s3CreateBucket "${BUCKET_NAME}"
    s3BucketList
    s3DeleteBucket "${BUCKET_NAME}"
    s3BucketList
}

main
