""" Fast redis client
  


"""

import redis


class redisClient:
    def __init__(self, host: str = 'localhost', port: int = 6333, config_file: str=None, db=0, config_keyname= 'redis', config_dict=None):
        if isinstance(config_dict, dict) :
            self.cfg = config_dict

        elif isinstance(config_file, str):    
            from utilmy  import config_load
            self.cfg = config_load(config_file)
            self.cfg = self.cfg[config_keyname]

        else:
            self.cfg = {
                'host': host,
                'port': port,
                'db': db
            }

        self.host = self.cfg['host']
        self.port = self.cfg['port']
        self.db = self.cfg['db']

        self.client = redis.Redis(host=self.host, port=self.port, db=self.db)
        try:
            self.client.ping()
        except redis.exceptions.ConnectionError: 
            raise ConnectionFailed("Failed to connect to redis")

    def get(self, key):
        return self.client.get(key)

    def put(self, key, val):
        self.client.set(key, val)
        return True

    def put_multi(self, key_values, batch_size=500, transaction=False, nretry=3):
        n       = len(key_values)
        n_batch = n // batch_size + 1
        self.pipe =   self.client.pipeline(transaction=transaction)

        for k in range(n_batch):
            i = 0
            while i < batch_size and k*batch_size+i < n:   
                self.pipe.hset(i, key_values[k*batch_size+ i][0], key_values[k*batch_size + i][1] )
                i += 1

            flag = 0 
            ii   = 0
            while flag and ii < nretry:
                ii =  ii + 1 
                try :      
                    self.pipe.execute()
                    flag = False
                    ntotal = batch_size
                except Exception as e: 
                    return ntotal             

    def get_multi(self, keys, batch_size=500, transaction=False):
        pipe = self.client.pipeline(transaction=transaction)

        n_batch = len(keys) // batch_size
        res = []
        for k in range(n_batch):
            for i in range(batch_size):
                pipe.hget(i, keys[k*batch_size + i])

            res = res + self.pipe.execute()

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

class ConnectionFailed(Exception):
    pass