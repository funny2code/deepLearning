
# -*- coding: utf-8 -*-
"""
python test.py   test_all
python test.py   test_viz_vizhtml
Rules to follow :
   Put import only inside the function.
   def  test_{pythonfilename.py}() :
       from utilmy import parallel as m
       m.test_all()
"""
import os, sys, time, datetime,inspect, random, pandas as pd, random, numpy as np, glob


#### NEVER IMPORT HERE  !!!!
# from utilmy import pd_random, pd_generate_data
# from tensorflow.python.ops.gen_array_ops import one_hot

#########################################################################################
def log(*s):
   print(*s, flush=True)

def import_module(mname:str='utilmy.oos'):
    import importlib
    m = importlib.import_module(mname)
    return m

   
def pd_random(ncols=7, nrows=100):
   import pandas as pd
   ll = [[ random.random() for i in range(0, ncols)] for j in range(0, nrows) ]
   df = pd.DataFrame(ll, columns = [str(i) for i in range(0,ncols)])
   return df


def pd_generate_data(ncols=7, nrows=100):
    """ Generate sample data for function testing
    categorical features for anova test
    """
    import numpy as np, pandas as pd
    np.random.seed(444)
    numerical    = [[ random.random() for i in range(0, ncols)] for j in range(0, nrows) ]
    df = pd.DataFrame(numerical, columns = [str(i) for i in range(0,ncols)])
    df['cat1']= np.random.choice(  a=[0, 1],  size=nrows,  p=[0.7, 0.3]  )
    df['cat2']= np.random.choice(  a=[4, 5, 6],  size=nrows,  p=[0.5, 0.3, 0.2]  )
    df['cat1']= np.where( df['cat1'] == 0,'low',np.where(df['cat1'] == 1, 'High','V.High'))
    return df   
   
   
#########################################################################################
def test_utilmy():
   from utilmy import utilmy as m
   m.test_all()
   
   
   #####  Bug of globals() in utilmy.py #################################################
   log("\n##### Session  ")
   sess = m.Session("ztmp/session")

   global mydf
   mydf = pd_generate_data()

   sess.save('mysess', glob=globals(), tag='01')
   os.system("ls ztmp/session")
   sess.show()
   import glob
   flist = glob.glob("ztmp/session/" + "/*")
   for f in flist:
       t = os.path.exists(os.path.abspath(f))
       assert  t == True, "session path not created "

       pickle_created = os.path.exists(os.path.abspath(f + "/mydf.pkl"))
       assert  pickle_created == True, "Pickle file not created"

   sess.load('mysess')
   sess.load('mysess', tag='01')



##########################################################################################
def test_images():
    from utilmy.images import util_image as m
    m.test_all()


##########################################################################################
def test_ppandas():
    from utilmy import ppandas as m
    m.test_all()

   
#########################################################################################
def test_docs_cli():
    """  from utilmy.docs.generate_doc import run_markdown, run_table 
    """
    cmd = "doc-gen  --repo_dir utilmy/      --doc_dir docs/"
    os.system(cmd)
    os.system('ls docs/')
   
   
#########################################################################################
def test_adatasets():
<<<<<<< HEAD
<<<<<<< HEAD
    """ #### python test.py   test_adatasets
    """
    from utilmy import adatasets as m
    m.test_all()      
=======
    """ #### python test.py   test_adatasets """
    from utilmy import adatasets as m ;   m.test_all()      
>>>>>>> origin/main
=======
    """ #### python test.py   test_adatasets """
    from utilmy import adatasets as m ;   m.test_all()      
>>>>>>> origin/main


#########################################################################################
def test_nnumpy():
<<<<<<< HEAD
<<<<<<< HEAD
    """#### python test.py   test_nnumpy
    """
    from utilmy import nnumpy as m
    m.test_all()
=======
    """#### python test.py   test_nnumpy  """
    from utilmy import nnumpy as m ; m.test_all()
>>>>>>> origin/main
=======
    """#### python test.py   test_nnumpy  """
    from utilmy import nnumpy as m ; m.test_all()
>>>>>>> origin/main



#########################################################################################
def test_dates():
    #### python test.py   test_dates
<<<<<<< HEAD
<<<<<<< HEAD
    from utilmy import dates as m
    m.test_all()
=======
    from utilmy import dates as m  ; m.test_all()
>>>>>>> origin/main
=======
    from utilmy import dates as m  ; m.test_all()
>>>>>>> origin/main


#########################################################################################
def test_decorators():
    #### python test.py   test_decorators
<<<<<<< HEAD
<<<<<<< HEAD
    from utilmy import  decorators as m
    m.test_all()
=======
    from utilmy import  decorators as m  ;m.test_all()
>>>>>>> origin/main
=======
    from utilmy import  decorators as m  ;m.test_all()
>>>>>>> origin/main


   
#########################################################################################
<<<<<<< HEAD
<<<<<<< HEAD
def test_text():
    from utilmy.nlp import util_cluster as m
    m.test_all()  

    from utilmy.nlp import util_gensim as m
    m.test_all()  
=======
def test_nlp():
    from utilmy.nlp import util_cluster as m ; m.test_all()  
    from utilmy.nlp import util_gensim as m ;  m.test_all()  
>>>>>>> origin/main
=======
def test_nlp():
    from utilmy.nlp import util_cluster as m ; m.test_all()  
    from utilmy.nlp import util_gensim as m ;  m.test_all()  
>>>>>>> origin/main

   
#########################################################################################
def test_viz_vizhtml():
   from utilmy.viz import vizhtml as m
   log("Visualization ")
   log(" from utilmy.viz import vizhtml as vi     ")
   m.test_all()





#########################################################################################
def test_parallel():
<<<<<<< HEAD
<<<<<<< HEAD
   from utilmy import parallel as m
   m.test_all()
=======
   from utilmy import parallel as m  ;  m.test_all()
>>>>>>> origin/main
=======
   from utilmy import parallel as m  ;  m.test_all()
>>>>>>> origin/main
   

#########################################################################################
def test_distributed():
<<<<<<< HEAD
<<<<<<< HEAD
   from utilmy import distributed as m
   log("from utilmy import distributed as m ")
   m.test_all()
=======
   from utilmy import distributed as m ;m.test_all()
>>>>>>> origin/main
=======
   from utilmy import distributed as m ;m.test_all()
>>>>>>> origin/main

   
  
#######################################################################################
def test_utils():
<<<<<<< HEAD
<<<<<<< HEAD
    """ #### python test.py   test_utils
    """
    from utilmy import utils as m
    m.test_all() 
=======
    from utilmy import utils as m ;  m.test_all() 
>>>>>>> origin/main
=======
    from utilmy import utils as m ;  m.test_all() 
>>>>>>> origin/main
         

#######################################################################################
def test_oos():
<<<<<<< HEAD
<<<<<<< HEAD
   """#### python test.py   test_oos
   """
   from utilmy import oos as m
   m.test_all() 
=======
   from utilmy import oos as m ;  m.test_all() 
>>>>>>> origin/main
=======
   from utilmy import oos as m ;  m.test_all() 
>>>>>>> origin/main


#######################################################################################
def test_tabular():
   from utilmy.tabular import util_sparse as m    ;     m.test_all()
   from utilmy.tabular import util_explain as m  ;      m.test_all()
   from utilmy.tabular import util_uncertainty as m  ;  m.test_all()

   
#########################################################################################
def test_deeplearning_keras():
<<<<<<< HEAD
<<<<<<< HEAD
    from utilmy.deeplearning.keras import  util_similarity as m
    m.test_tf_cdist()
=======
    from utilmy.deeplearning.keras import  util_similarity as m;  m.test_all()
>>>>>>> origin/main
=======
    from utilmy.deeplearning.keras import  util_similarity as m;  m.test_all()
>>>>>>> origin/main



#########################################################################################
def test_deeplearning_torch():
<<<<<<< HEAD
<<<<<<< HEAD
    from utilmy.deeplearning.torch import  rule_encoder as m
    m.test_all()


#######################################################################################
def test_deeplearning_yolov5():
   from utilmy.deeplearning import util_yolo as m
   m.test_all()
=======
=======
>>>>>>> origin/main
    from utilmy.deeplearning.torch import  rule_encoder as m ;  m.test_all()
    from utilmy.deeplearning.torch import  sentences as m ;  m.test_all()


#######################################################################################
def test_deeplearning():
   from utilmy.deeplearning import util_yolo as m ;  m.test_all()
<<<<<<< HEAD
>>>>>>> origin/main
=======
>>>>>>> origin/main


#######################################################################################
def test_recsys():
<<<<<<< HEAD
<<<<<<< HEAD
   from utilmy.recsys import ab as m
   m.test_all()

   from utilmy.recsys import metric as m
   m.test_all()
=======
   from utilmy.recsys import ab as m ; m.test_all()
   from utilmy.recsys import metric as m ; m.test_all()
>>>>>>> origin/main
=======
   from utilmy.recsys import ab as m ; m.test_all()
   from utilmy.recsys import metric as m ; m.test_all()
>>>>>>> origin/main

  

#######################################################################################
def test_compile():
   from utilmy.docs import format as m
<<<<<<< HEAD
<<<<<<< HEAD
   log("from utilmy.doc import format")
=======
>>>>>>> origin/main
=======
>>>>>>> origin/main



import utilmy as  uu


#######################################################################################
def test_all():
    test_utilmy()
    test_decorators()
    test_ppandas()  
<<<<<<< HEAD
<<<<<<< HEAD
    test_text()
=======
    test_nlp()
>>>>>>> origin/main
=======
    test_nlp()
>>>>>>> origin/main
    test_docs_cli()


    ################
    # test_oos()
    test_tabular()
    test_adatasets()
    test_dates()
    test_utils()


    ################
    test_deeplearning_keras()
<<<<<<< HEAD
<<<<<<< HEAD
    test_deeplearning_yolov5()
=======
    test_deeplearning()
>>>>>>> origin/main
=======
    test_deeplearning()
>>>>>>> origin/main


    ###############
    test_recsys()


      
#######################################################################################
if __name__ == "__main__":
    import fire
    fire.Fire() 

   
   
