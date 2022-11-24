from util_redis import redisClient, ConnectionFailed, AuthenticationFailed
import random, string

def test_connection():
    # test connection failed
    try:
        client = redisClient(host='localsss', port=1123)
        assert False
    except ConnectionFailed:
        assert True

    # test connection success
    try:
        client = redisClient(host='localhost', port=6379, db=0)
        assert True
    except ConnectionFailed:
        assert False

    # test connection invalid password
    try:
        client = redisClient(host='localhost', port=6379, db=0, password='secret')
        assert False
    except AuthenticationFailed:
        assert True

    # test connection valid password
    try:
        client = redisClient(host='localhost', port=6379, db=0, password='')
        assert True
    except AuthenticationFailed:
        assert False

def test_getput():
    client = redisClient(host='localhost', port=6379, db=0)
    client.put('foo', 'bar')
    res = client.get('foo').decode('utf8')
    assert res == 'bar'

def randomStringGenerator(size, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def test_getputmulti():
    client = redisClient(host='localhost', port=6379, db=0)
    keyvalues = [['a', '1'], ['b', '2'], ['c', '3']]
    keys = ['a', 'b', 'c']

    client.put_multi(keyvalues, 3)
    res = client.get_multi(keys, 3)
    print()
    for i in range(len(keys)):
        print(f'index {i}: key {keys[i]}; value {res[i]}')
        