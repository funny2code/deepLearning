/bin/bash


   docker compose -f    noredis/docker-compose.yml    up

   
   ###### Need to send the Host IP to RedisCluster
   export HOSTIP=(ipconfig)

   docker compose  -e $HOSTIP:HOSTIP          -f    rredis/docker_rediscluster.yml       up


   #### Set permanent endpoints
   #### https://stackoverflow.com/questions/52494196/is-there-any-way-to-specify-endpoint-url-in-aws-cli-config-file
   


   ./check_localstack.sh



