""" Fast redis client
Docs::

    pip install hiredis



"""
import time, random, string
from dataclasses import dataclass
from box import Box
import redis
from redis.cluster import RedisCluster, ClusterNode

from utilmy import log


#################################################################################
#################################################################################
def test_all():
   test_connection()
   test_getput()
   test_getput2()


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


def test_getput():
    client = redisClient(host='localhost', port=6379, db=0)
    client.put('foo', 'bar')
    res    = client.get('foo').decode('utf8')
    assert res == 'bar'


def test_getput2():
    client = redisClient(host='localhost', port=6379, db=0)
    keyvalues = [['a', '1'], ['b', '2'], ['c', '3']]
    keys = ['a', 'b', 'c']

    client.put_multi(keyvalues, 3)
    res = client.get_multi(keys, 3)
    print()
    for i in range(len(keys)):
        print(f'index {i}: key {keys[i]}; value {res[i]}')
        


########## Cluster ##################################################################
def test_cluster1():
    # test connection failed
    try:
        config = {'host': 'localhost', 'port': 6379, 'node_ports': [6379, 6380, 6381, 6382, 6383, 6384], 'password': 'bitnami'}
        client = RedisClusterClient(config)
        assert False
    except redis.exceptions.RedisClusterException:
        assert True


def test_cluster2():
    # test connection success
    try:
        config = {'host': 'localhost', 'port': 6379, 'node_ports': [6379, 6380, 6381, 6382, 6383, 6384], 'password': 'bitnami'}
        client = RedisClusterClient(config)
        assert True
    except redis.exceptions.RedisClusterException:
        assert False


def test_cluster3():
    config = {'host': 'localhost', 'port': 6379, 'node_ports': [6379, 6380, 6381, 6382, 6383, 6384], 'password': 'bitnami'}

    client = RedisClusterClient(config)
    client.put('foo', 'bar')
    res = client.get('foo').decode('utf8')
    assert res == 'bar'


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


#################################################################################
#################################################################################
class RedisClusterClient:
    def __init__(self, clusterConfig : dict, read_from_replicas=True, encoding='utf-8', decode_response=True):

        clusterConfig = Box(clusterConfig)
        nodes = list()
        for port in clusterConfig.node_ports:
            nodes.append(ClusterNode(host=clusterConfig.host, port=port))

        self.client = RedisCluster(
            startup_nodes=nodes,
            read_from_replicas=read_from_replicas,
            host=clusterConfig.host,
            password=clusterConfig.password,
            port=clusterConfig.port)

        
        self.client.ping()


    def get(self, key):
        """get value from redis using key
        """
        return self.client.get(key)


    def put(self, key, val):
        """set value to key
        """
        self.client.set(key, val)
        return True

    def put_multi(self, key_values, batch_size=500, transaction=False, nretry=3):
        """set multiple keys and values to redis
        
        Parameters:
            key_values ([[key, value], ]): key and value as 2D list
            batch_size (int): number of batch.
            transaction (bool): enable MULTI and EXEC statements.
            nretry (int): number of retry
        """
        n         =  len(key_values)
        n_batch   =  n // batch_size + 1
        self.pipe =  self.client.pipeline(transaction=transaction)

        ntotal = 0  
        for k in range(n_batch):
            for i in range(batch_size):
                ix  = k*batch_size + i 
                if ix >= n: break 
                key,val = key_values[ix]   
                self.pipe.hset(i, key, val )
                i += 1

            flag = True 
            ii   = 0
            while flag and ii < nretry:
                ii =  ii + 1 
                try :      
                    self.pipe.execute()
                    flag = False
                    ntotal += batch_size
                except Exception as e: 
                    log(e)
                    time.sleep(2)
                  
        return ntotal 


    def get_multi(self, keys, batch_size=500, transaction=False):
        """get multiple value using list of keys
        Parameters:
            keys (list(string)): list of keys
            batch_size (int): number of batch.
            transaction (bool): enable MULTI and EXEC statements.
        """
        pipe = self.client.pipeline(transaction=transaction)

        n       = len(keys)
        n_batch = n // batch_size  + 1
        res = []
        for k in range(n_batch):
            for i in range(batch_size):
                ix  = k*batch_size + i
                if ix >= n : break
                try :
                   pipe.hget(i, keys[ix])
                except Exception as e :
                  log(e)   
                  time.sleep(5)
                  pipe.hget(i, keys[ix])


            resk =  self.pipe.execute()
            res  = res + resk

        return 



class redisClient:
    def __init__(self, host:  str = 'localhost', port: int = 6333, user='', password='',
                 config_file: str=None, db=0, config_keyname= 'redis', config_dict=None):
        """  hiredis client       
        Docs::

            host (str, ):             'localhost'
            port (int, ):              6333
            config_file (str, ):       None
            db (int, ):                   0
            config_keyname (str, ):  'redis'
            config_dict (_type_, ):   None

         Raises:
            ConnectionFailed: _description_
         """
        if isinstance(config_dict, dict) :
            self.cfg = config_dict

        elif isinstance(config_file, str):    
            from utilmy  import config_load
            self.cfg = config_load(config_file)
            self.cfg = self.cfg[config_keyname]

        else:
            self.cfg = { 'host': host, 'port': port, 'db': db,
                'user' : user, 'password': password
            }

        self.host = self.cfg['host']
        self.port = self.cfg['port']
        self.db = self.cfg['db']
        self.user = self.cfg['db']
        self.password = self.cfg['password']

        self.client = redis.Redis(host=self.host, port=self.port, db=self.db, password=self.password)
        try:
            self.client.ping()
        except redis.exceptions.ConnectionError: 
            raise ConnectionFailed("Failed to connect to redis")
        except redis.exceptions.ResponseError:
            raise AuthenticationFailed("Invalid password")


    def get(self, key):
        """get value from redis using key
        """
        return self.client.get(key)


    def put(self, key, val):
        """set value to key
        """
        self.client.set(key, val)
        return True

    def put_multi(self, key_values, batch_size=500, transaction=False, nretry=3):
        """set multiple keys and values to redis
        
        Parameters:
            key_values ([[key, value], ]): key and value as 2D list
            batch_size (int): number of batch.
            transaction (bool): enable MULTI and EXEC statements.
            nretry (int): number of retry
        """
        n         =  len(key_values)
        n_batch   =  n // batch_size + 1
        self.pipe =  self.client.pipeline(transaction=transaction)

        ntotal = 0  
        for k in range(n_batch):
            for i in range(batch_size):
                ix  = k*batch_size + i 
                if ix >= n: break 
                key,val = key_values[ix]   
                self.pipe.hset(i, key, val )
                i += 1

            flag = True 
            ii   = 0
            while flag and ii < nretry:
                ii =  ii + 1 
                try :      
                    self.pipe.execute()
                    flag = False
                    ntotal += batch_size
                except Exception as e: 
                    log(e)
                    time.sleep(2)
                  
        return ntotal 


    def get_multi(self, keys, batch_size=500, transaction=False):
        """get multiple value using list of keys

        Parameters:
            keys (list(string)): list of keys
            batch_size (int): number of batch.
            transaction (bool): enable MULTI and EXEC statements.
        """
        pipe = self.client.pipeline(transaction=transaction)

        n       = len(keys)
        n_batch = n // batch_size  + 1
        res = []
        for k in range(n_batch):
            for i in range(batch_size):
                ix  = k*batch_size + i
                if ix >= n : break
                try :
                   pipe.hget(i, keys[ix])
                except Exception as e :
                  log(e)   
                  time.sleep(5)
                  pipe.hget(i, keys[ix])


            resk =  self.pipe.execute()
            res  = res + resk

        return res


class RedisQueries(object):
    def __init__(self,config_file=None):
        self.Redis_conn = redisClient(config_file = config_file)
        self.batch_size = 50

    @property
    def version_id(self):
        """
        """
        if not hasattr(self,'_zzz_version_id'):
            control_conn = self.Redis_conn
            self._zzz_version_id = control_conn.get('zzz_cfg_pending')
        return self._zzz_version_id

    def get_siid_to_title(self,siids):
        """
        """
        siid_to_title = dict()
        cad_map = self.Redis_conn.get_multi(keys)
        for siid, vals in cad_map.items():
            if len(vals) > 1:
                siid_to_title[siid] = vals[-1]
        return siid_to_title




#################################################################################
def randomStringGenerator(size, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class ConnectionFailed(Exception):

    pass

class AuthenticationFailed(Exception):
    pass




############################################################################################################
if __name__ == '__main__':
    import fire
    fire.Fire()





