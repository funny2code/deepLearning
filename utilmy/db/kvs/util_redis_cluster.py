from dataclasses import dataclass
from redis.cluster import RedisCluster, ClusterNode

import redis, time
from utilmy import log

@dataclass
class RedisClusterConfig:
    host: str
    port: str | int
    node_ports: list()
    password: str

class RedisClusterClient:
    def __init__(self, clusterConfig : RedisClusterConfig, read_from_replicas=True, encoding='utf-8', decode_response=True):
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

        return res
