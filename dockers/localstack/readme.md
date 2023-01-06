



```
TODO

   1) Create and test
         template_localstack.yaml


   2) and Re-direct all AWS acccess to this docker
       AWS IAM
       AWS Redis
       AWS RDS Mysql
       AWS S3

    
    So, when we start this docker + Shell Script ===> All AWS Code works with this docker !!!!




Infos

https://stackoverflow.com/questions/45551496/redirect-aws-sdks-default-endpoint-to-mocked-localstack-endpoints


```










```

###### LocalStack

https://baptiste.bouchereau.pro/tutorial/mock-aws-services-with-localstack/

https://github.com/Ovski4/tutorials/tree/master/localstack-part-1

https://docs.LocalStack.cloud/developer-guide/basics/


https://onexlab-io.medium.com/docker-compose-localstack-fadee1e88a49



https://zenn.dev/dove/articles/c0bc8aca695f07


https://recruit.gmo.jp/engineer/jisedai/blog/localstack-ec2-rds/



###### fake-S3




```


Infos
```
##### Docker Compose with Postgres
version: '3.3'
services:
  localstack:
    image: localstack/localstack:latest
    environment:
     - DEFAULT_REGION=ap-southeast-3
     - SERVICES=s3,lambda
     - DEBUG=${DEBUG-}
     - PERSISTENCE=${PERSISTENCE-}
     - LAMBDA_EXECUTOR=${LAMBDA_EXECUTOR-}
    ports:
     - "127.0.0.1:4566:4566"
     - "127.0.0.1:4510-4559:4510-4559"
    volumes:
      - "${LOCALSTACK_VOLUME_DIR:-./volume}:/var/lib/localstack"
      - "/var/run/docker.sock:/var/run/docker.sock"
  postgres:
    image: postgres:alpine
    ports:
      - "5432:5432"
    volumes:
      - ./volume/postgres:/var/lib/postgresql/data
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_DB=postgres
    restart: always


















##### Docker Compose with redis
version: '3.8'
services:
    redis:
      container_name: "redis"
      image: redis:alpine
      ports:
        - "6379:6379" # To Connect redis from local cmd use : docker exec -it cores-redis redis-cli
    localstack:
        container_name: "localstack" # Container name in your docker
        image: localstack/localstack:latest # Will download latest version of localstack
        #image: localstack/localstack-full:latest # Full image support WebUI
        ports:
          - "4566:4566" # Default port forward
          - "9200:4571" # Elasticsearch port forward
          #- "8080:8080: # WebUI port forward
        environment:
          - SERVICES=es, s3, ec2, dynamodb, elasticcache, sqs #AWS Services that you want in your localstack
          - DEBUG=1 # Debug level 1 if you want to logs, 0 if you want to disable
          - START_WEB=0 # Flag to control whether the Web UI should be started in Docker
          - LAMBDA_REMOTE_DOCKER=0
          - DATA_DIR=/tmp/localstack/data #  Local directory for saving persistent data(Example: es storage)
          - DEFAULT_REGION=us-east-1
        volumes:
          - './.localstack:/tmp/localstack'
          - '/var/run/docker.sock:/var/run/docker.sock'



#### localstack-s3-example.txt
1) Create s3 bucket - 
# aws --endpoint-url=http://localhost:4566 s3 mb s3://my-test-bucket

2) List s3 buckets - 
# aws --endpoint-url="http://localhost:4566" s3 ls

3) Upload file on s3 bucket -
# aws --endpoint-url="http://localhost:4566" s3 sync "myfiles" s3://my-test-bucket

4) List files from AWS CLI -
# aws --endpoint-url="http://localhost:4566" s3 ls s3://my-test-bucket

6) Access file via URL(File name was download.jpg) - 
# http://localhost:4566/my-test-bucket/download.jpg

7) Delete object from bucket -
# aws --endpoint-url=http://localhost:4566 s3api delete-object --bucket <bucket-name> --key <file-name.format>

8) Create bucket notification configuration - 
# aws --endpoint-url=http://localhost:4566 s3api put-bucket-notification-configuration --bucket <bucket-name> --notification-configuration file://<configuration-file-name>.json

9) Get bucket notification configuration - 
# aws --endpoint-url=http://localhost:4566 s3api get-bucket-notification-configuration --bucket <bucket-name>

10) Set bucket policy - 
# aws --endpoint-url=http://localhost:4566 s3api put-bucket-policy --bucket <bucket-name> --policy file://<policy-file>.json

10) Get bukcet policy - 
# aws --endpoint-url=http://localhost:4566 s3api get-bucket-policy --bucket <bucket-name>





#### localstack-sns-examples.txt
1) Create sns topic -
# aws --endpoint-url=http://localhost:4566 sns create-topic --name my-test-topic

2) list all sns topics -
# aws --endpoint-url=http://localhost:4566 sns list-topics

3) list subscriptions -
# aws --endpoint-url=http://localhost:4566 sns list-subscriptions

4) publish message - 
# aws --endpoint-url=http://localhost:4566 sns publish --topic-arn "arn:aws:sns:us-east-1:000000000000:ingest-topic" --message file://message.txt --message-attributes file://attributes.json

-- message.txt
my message to publish

-- attributes.json
{
    "key": {
        "DataType": "String",
        "StringValue": "value"
    }
}





##### localstack-sqs-example.txt
1) Create queue - 
# aws --endpoint-url=http://localhost:4566 sqs create-queue --queue-name my-test-queue

2) Get queue url -
# aws --endpoint-url=http://localhost:4566 sqs get-queue-url --queue-name <queue-name>

3) list queue - 
# aws --endpoint-url=http://localhost:4566 sqs list-queues

4) send message - 
# aws --endpoint-url=http://localhost:4566 sqs send-message --queue-url <queue-url> --message-body <message>

5) receive message - 
# aws --endpoint-url=http://localhost:4566 sqs receive-message --queue-url <queue-url>

6) purge queue - 
# aws --endpoint-url=http://localhost:4566 sqs purge-queue --queue-url <queue-url>

7) delete queue - 
# aws --endpoint-url=http://localhost:4566 sqs delete-queue --queue-url <queue-url>

8) set attributes - 
# aws --endpoint-url=http://localhost:4566 sqs set-queue-attributes --queue-url=<queue-url> --attributes file://<file-name>.json

9) get attributes - 
# aws --endpoint-url=http://localhost:4566 sqs  get-queue-attributes --queue-url=<queue-url>


```
