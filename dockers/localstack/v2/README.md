# Readme
```
### Install :   (awslocal & redis)  for Mac
    ./install.sh


#### Start the AWS mock Redis
   docker compose -f nocluster/docker-compose.yml up


#### Start the AWS mock rediscluster
   docker compose -f cluster/docker-compose.yml up

   redis_cluster_create.py  --node-count 5



#### Tests
   s3-test.sh    : S3 testing


   mysql -h 127.0.0.1 -P 3306 -u root -p test


   redis-cli -c -p 6370 



#### Mock Permanent Endpoint
      https://stackoverflow.com/questions/52494196/is-there-any-way-to-specify-endpoint-url-in-aws-cli-config-file
      
      https://hackernoon.com/run-your-own-aws-apis-on-openshift-d0acb876d5b6


      aws configure set cli_pager "" --profile integ

      https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html


      https://github.com/ikigeg/localstack-demonstrations



```


#### Issues
```
Docker compose with a redis cluster does not work on a mac as the redis cluster
cannot forward ip address on a mac due to how networking works. Run:
`docker compose -f ./docker-compose.yml up` and you will see all of the nodes
are running fine in Docker. It will then connect fine by running `redis-cli`.
However it will hang when redis puts the `key -> value` pair in another node.
It will look like this:
127.0.0.1:6370> SET hello world
-> Redirected to slot [3028] located at 172.18.0.6:6379
Putting the nodes in a specific subnet 


To get around this problem I have supplied a script for creating a cluster
locally and compose file for just creating a redis server. There is no way
around this.


```
