""" Fast redis client
  


"""


class Client:
	def __init__(self, host = 'localhost', port = 6333, config_file=None, config_keyname= 'redis', config_dict=None):


    if isinstance(config_dict, dict) :
        self.cfg = config_dict

    elif isinstance(config_file, str):    
       from utilmy  import config_load
       self.cfg = config_load(config_file)
       self.cfg = self.cfg[config_keyname]

		self.PORT = self.cfg['port']
		self.HOST = self.cfg['host']


		self.client = None


	def connect(self, table):
		self.client = redisClient(host=self.HOST, port=self.PORT)


  def get(key):
     return val

  def put(key, val):     


	def get_multi(self, vect_list, query_filter=None, topk=5):
     return ddict





	def put_multi(self, item_dict):
		for key,val in item_dict.items() :
      





def redis_get_batch(keylist, batch_size=500, session):



  n_batch = len(keylist) // 500



  for k in range(n_batch):
     for i in range(batch_size):
        pool.add(key)
     res =  pool.query()

  return res



