""" Fast redis client
  


"""


class redisClient:
	def __init__(self, host = 'localhost', port = 6333, config_file=None, config_keyname= 'redis', config_dict=None):
      if isinstance(config_dict, dict) :
         self.cfg = config_dict

      elif isinstance(config_file, str):    
         from utilmy  import config_load
         self.cfg = config_load(config_file)
         self.cfg = self.cfg[config_keyname]

      PORT = self.cfg['port']
      HOST = self.cfg['host']
      transaction  = cfg['transaction']

      self.client = redis.Redis(host='localhost', port=6379, db=0)
      self.pipe =   self.client.pipeline(transaction=transaction)


 	def connect(self, table):
		self.client = redisClient(host=self.HOST, port=self.PORT)


   def get(key):
      return val

   def put(key, val):     
       return True

   def put_multi(self, key_values, batch_size=500, transaction=False, nretry=3):

      n       = len(key_values)
      n_batch = n // batch_size + 1

      for k in range(n_batch):
         i = 0
         while i < batch_size and k*batch_size+i < n :   
               self.pipe.hset(i, key_values[k*batch_size+ i][0], key_values[k*batch_size + i][1] )
               i += 1

         flag = 0 
         ii   = 0
         while flag and ii < nretry:0
            ii =  ii + 1 
            try :      
               self.pipe.execute()
               flag = False
               ntotal = batch_size
            except Exception as e: 


      return ntotal             

   def get_multi(self, keys, batch_size=500, transaction=False):
      # pipe = self.client.pipeline(transaction= transaction)

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

















import redis
import random
import string

def hiredisPipeleineSetXTimes(client, keys, values):
    keylen = len(keys)
    pipe = client.pipeline(transaction=False)
    for i in range(keylen):
        pipe.set(keys[random.randint(0, keylen-1)], values[random.randint(0, keylen-1)])
    pipe.execute()

def hiredisPipeleineGetXTimes(client , keys):
    pipe = client.pipeline(transaction=False)
    for i in keys:
        pipe.get(i)
    pipe.execute()

def hiredisPipeleineHSetXTimes(client: redis.Redis, keys, values, batch_size=500):
    pipe = client.pipeline(transaction=False)

    keylen = len(keys)
    n_batch = keylen // batch_size

    for k in range(n_batch):
        for i in range(batch_size):
            pipe.hset(i, keys[random.randint(0, keylen-1)], values[random.randint(0, keylen-1)])

        pipe.execute()
        

def hiredisPipeleineHGetXTimes(client: redis.Redis ,keys, batch_size=500):
    pipe = client.pipeline(transaction=False)

    n_batch = len(keys) // batch_size

    for k in range(n_batch):
        for i in range(batch_size):
            pipe.hget(i, keys[i])

        pipe.execute()


def redis_get_batch(client: redis.Redis ,keys, batch_size=500):
    pipe = client.pipeline(transaction=False)
    n_batch = len(keys) // batch_size
    result = []

    for k in range(n_batch):
        for i in range(batch_size):
            pipe.hget(i, keys[i])

        result.append(pipe.execute())

    return result


def randomStringGenerator(size, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

keys = []
values = []

for i in range(100000):
    keys.append(randomStringGenerator(15))
    values.append(randomStringGenerator(1000))

def test_hiredisSet():
    client = redis.Redis(host='localhost', port=6379, db=0)
    hiredisPipeleineSetXTimes(client=client, keys=keys, values=values)

def test_hiredisGet():
    client = redis.Redis(host='localhost', port=6379, db=0)
    hiredisPipeleineGetXTimes(client=client, keys=keys)

def test_hiredisHSet():
    client = redis.Redis(host='localhost', port=6379, db=0)
    hiredisPipeleineHSetXTimes(client=client, keys=keys, values=values)

def test_hiredisHGet():
    client = redis.Redis(host='localhost', port=6379, db=0)
    hiredisPipeleineHGetXTimes(client=client, keys=keys)

