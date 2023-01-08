/bin/bash


   docker compose -f    noredis/docker-compose.yml    up

   
   ###### Need to send the Host IP to RedisCluster
   export HOSTIP=(ipconfig)

   docker compose  -e $HOSTIP:HOSTIP          -f    rredis/docker_rediscluster.yml       up



   ./check_localstack.sh



