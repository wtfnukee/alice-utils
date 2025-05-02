#!/bin/bash

set -xe

DIR=$(dirname $0)

function _fail() {
    echo $0
    exit 1
}
which yc > /dev/null || _fail "Please install Yandex Cloud CLI, see: https://cloud.yandex.ru/docs/cli/quickstart"

NAME=alice-util
WANDB_API_KEY=$(cat skill/.env | grep WANDB_API_KEY | cut -d '=' -f 2)
#yc serverless function create \
#   --name  $NAME \
#   --description "Alice Util v0"

yc serverless function version create \
   --function-name=$NAME \
   --runtime=python312 \
   --entrypoint=skill.handler \
   --source-path $DIR/skill\
   --memory=128M \
   --execution-timeout=3s\
   --environment WANDB_API_KEY=$WANDB_API_KEY
