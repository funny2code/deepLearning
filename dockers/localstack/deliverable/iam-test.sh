#!/usr/bin/env bash

: '
    Simple unit test to ensure localstack IAM is up and running
'

USER_NAME="Brian Kernighan"
AWS_TOOL="awslocal"

awsInvoke() {
    awslocal "$@"
}

iamCreateUser() {
    local name="${1}"
    awsInvoke iam create-user --user-name "${name}" --endpoint-url=http://localhost:4566
}

iamUserList() {
    awsInvoke iam list-users --endpoint-url=http://localhost:4566
}

iamDeleteUser() {
    local name="${1}"
    awsInvoke iam delete-user --user-name "${name}" --endpoint-url=http://localhost:4566
}

main() {
    iamCreateUser "${USER_NAME}"
    iamUserList
    iamDeleteUser "${USER_NAME}"
    iamUserList
}

main
