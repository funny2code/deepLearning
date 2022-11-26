from utilmy.db.kvs.util_redis_cluster import RedisClusterClient, RedisClusterConfig
import random, string
import redis

def test_connection_failed():
    # test connection failed
    try:
        config = RedisClusterConfig('localssss', 6379, [6379, 6380, 6381, 6382, 6383, 6384], 'bitnami')
        client = RedisClusterClient(config)
        assert False
    except redis.exceptions.RedisClusterException:
        assert True

def test_connection_success():
    # test connection success
    try:
        config = RedisClusterConfig('localhost', 6379, [6379, 6380, 6381, 6382, 6383, 6384], 'bitnami')
        client = RedisClusterClient(config)
        assert True
    except redis.exceptions.RedisClusterException:
        assert False


def test_getput():
    config = RedisClusterConfig('localhost', 6379, [6379, 6380, 6381, 6382, 6383, 6384], 'bitnami')
    client = RedisClusterClient(config)
    client.put('foo', 'bar')
    res = client.get('foo').decode('utf8')
    assert res == 'bar'

def randomStringGenerator(size, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# def test_getputmulti():
#     config = RedisClusterConfig('localhost', 6379, [6379, 6380, 6381, 6382, 6383, 6384], 'bitnami')
#     client = RedisClusterClient(config)
#     keyvalues = [['a', '1'], ['b', '2'], ['c', '3']]
#     keys = ['a', 'b', 'c']

#     client.put_multi(keyvalues, 1)
#     res = client.get_multi(keys, 1)
#     print()
#     for i in range(len(keys)):
#         print(f'index {i}: key {keys[i]}; value {res[i]}')
        