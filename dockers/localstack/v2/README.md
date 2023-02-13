# Readme
```
### Install :  
    ### AWS Mock
    pip3 install awscli-local 

    ### redis client
    brew install redis



#### Start the AWS mock Redis normal
   start_all.sh  redis


#### Start the AWS mock rediscluster
   start_all.sh  rediscluster



#### Tests
   check/check_s3.sh    : S3 testing


   mysql -h 127.0.0.1 -P 3306 -u root -p test


   redis-cli -c -p 6370 



### Docs

https://github.com/ikigeg/localstack-demonstrations


aws s3api create-bucket \
  --bucket my-bucket-name \
  --region ap-northeast-1 \
  --create-bucket-configuration LocationConstraint=ap-northeast-1 \
  --endpoint-url http://localhost:4566

  --region ap-northeast-1 \
  --create-bucket-configuration LocationConstraint=ap-northeast-1 \





#### Mock Permanent Endpoint
alias aws='aws --endpoint-url http://localhost:4566'
And put that in your ~/.bash_profile or ~/.zshrc



      https://stackoverflow.com/questions/52494196/is-there-any-way-to-specify-endpoint-url-in-aws-cli-config-file
      
      https://hackernoon.com/run-your-own-aws-apis-on-openshift-d0acb876d5b6


      aws configure set cli_pager "" --profile integ

      https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html


      https://github.com/ikigeg/localstack-demonstrations



```


#### Issues
```
Redis Cluster fixes

https://github.com/bitnami/bitnami-docker-redis-cluster/issues/3


Docker compose with a redis cluster does not work on a mac as the redis cluster
cannot forward ip address on a mac due to how networking works. Run:
`docker compose -f ./docker-compose.yml up`


127.0.0.1:6370> SET hello world
-> Redirected to slot [3028] located at 172.18.0.6:6379
Putting the nodes in a specific subnet 




```
