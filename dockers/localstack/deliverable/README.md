# Readme
Docker compose with a redis cluster does not work on a mac as the redis cluster
cannot forward ip address on a mac due to how networking works. Run:
`docker compose -f ./docker-compose.yml up` and you will see all of the nodes
are running fine in Docker. It will then connect fine by running `redis-cli`.
However it will hang when redis puts the `key -> value` pair in another node.
It will look like this:
```bash
127.0.0.1:6370> SET hello world
-> Redirected to slot [3028] located at 172.18.0.6:6379
```
Putting the nodes in a specific subnet 


To get around this problem I have supplied a script for creating a cluster
locally and `docker-compose.yml` file for _just_ creating a redis server. There
is no way around this in docker I'm afraid :(.

## Supplied:
Bellow is how to run the scripts and what they do

- `install.sh` -> install dependencies on a mac (awslocal & redis)
```bash
./install.sh
```

- `redis_cluster_create.py` -> commandline tool for creating a redis cluster
```bash
./redis_cluster_create.py --node-count <int>
```

- `s3-test.sh` -> Test that local stack is up and running

- `docker-compose.yml` -> create localstack, mysql & a redis cluster
```bash
docker compose -f ./docker-compose.yml up
```

- `docker-compose-no-cluster.yml` -> create localstack, mysql & a redis instance 
```bash
docker compose -f ./docker-compose-no-cluster.yml up
```

## Connect to MySQL
password is test

```bash
mysql -h 127.0.0.1 -P 3306 -u root -p
```

## Connect to redis
For all methods of starting redis the command is the same
```bash
redis-cli -c -p 6370
```
