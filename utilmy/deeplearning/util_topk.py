# -*- coding: utf-8 -*-
""" Top-k retrieval vectors for Rec
Doc::



"""
import os, glob, sys, math, time, json, functools, random, yaml, gc, copy, pandas as pd, numpy as np
import datetime
from box import Box

import warnings ;warnings.filterwarnings("ignore")
from warnings import simplefilter  ; simplefilter(action='ignore', category=FutureWarning)
with warnings.catch_warnings():
    pass


from utilmy import pd_read_file, os_makedirs, pd_to_file, glob_glob


#### Optional imports
try :
    import faiss
    import diskcache
except:
    print('pip install faiss-cpu')



from utilmy.deeplearning.util_embedding import (
    embedding_extract_fromtransformer,
    embedding_load_pickle,
    embedding_load_parquet,
    embedding_load_word2vec,
    embedding_torchtensor_to_parquet,
    embedding_rawtext_to_parquet,


    db_load_dict,
    np_norm_l2,
    np_matrix_to_str,
    np_str_to_array,
    np_array_to_str,
    np_matrix_to_str2,
    np_matrix_to_str_sim

)


#############################################################################################
from utilmy import log, log2, os_module_name

def help():
    """function help        """
    from utilmy import help_create
    print( help_create(__file__) )



#############################################################################################
def test_all() -> None:
    """ python  $utilmy/deeplearning/util_topk.py test_all         """
    log(os_module_name(__file__))
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
   

def test1() -> None:
    """function test1     
    """
    dirtmp ="./ztmp/"

    dd = test_create_fake_df(dirout= dirtmp)
    log(dd)


def test2():
  """  tests
  Docs ::

        Test Cases  pd_add_onehot_encoding
        1. check if id column is present in dfref
        2. check if labels_col are present in dfref   
  """ 

  res = pd.DataFrame({'id': [1,2,3,4], 'gender': [0,1,0,1], 'masterCategory': [2,1,3,4]})
  
  path = './temp/tem/'
  if not os.path.exists(path):
    os.makedirs(path)

  res.to_csv(f'{path}1.csv', index=False)
  pd_add_onehot_encoding(res, f'{path}/1.csv', ['gender', 'masterCategory'])


def test3():
  """  tests
  Docs ::

        Test Cases  embedding_cosinus_scores_pairwise
        1. check if length of word_list is same as length of emb
  """ 
  embedding_cosinus_scores_pairwise(embs=np.random.random((5,5)), word_list=np.array([1,2,3,4,5]))


def test4():
  """  tests
  Docs ::

        Test Cases  KNNClassifierFAISS
        1. In fit function check if input and output dimensions are same
        2. If algorithm is vornoni, check if number of input vecs >= number of clusters
  """ 
  k = KNNClassifierFAISS()
  k = k.fit(np.random.random((5,5)), np.array([0,1,2,3,4]))

  
  def test5():
  """  tests
  Docs ::

        Test Cases  faiss_create_index
        1. check if df_or_path is not a string instance mentioning dirout is mandatory
        2. check if id column in present in input dataframe
        3. check if mentioned col parameter value is present in input dataframe
        4. check if dimension of dataframe embs is same as emb_dim
        5. Check if dimension D is a multiple of number of sub_quantizers
        6. Check if number of training inputs >= number of clusters   

  """   
  emb_list = []
  for i in range(4):
      emb_list.append( ','.join([str(x) for x in np.random.random(200)]))
      
  res = pd.DataFrame({'id': [1,2,3,4] * 6000, 
                      'emb': emb_list * 6000})
  
  path = './temp/tem/'
  if not os.path.exists(path):
    os.makedirs(path)
  res.to_csv(f'{path}1.csv', index=False)

  faiss_create_index(df_or_path=f'{path}1.csv')

def test6():
  
  """  tests
  Docs ::
        Test Cases  topk_calc
        1. check if dimension of dataframe embs is same as emb_dim
  """   

  emb_list = []
  for i in range(4):
      emb_list.append( ','.join([str(x) for x in np.random.random(200)]))
      
  res = pd.DataFrame({'id': [1,2,3,4], 
                      'emb': emb_list})
  path = './temp/tem/'
  if not os.path.exists(path):
    os.makedirs(path)
  res.to_csv(f'{path}1.csv', index=False)

  topk_calc(diremb=f'{path}1.csv')


def test7():
  """  tests
  Docs ::
        Test Cases  topk_calc
        1. check if colid, colemb exists in input data
  """ 
  y = test_create_fake_df()
  path = './temp/tem/'

  if not os.path.exists(path):
    os.makedirs(path)

  y.df.to_csv(f'{path}data.csv')
  faiss_topk_calc(df='./temp/tem/data.csv', root=path, colid='id', colemb='emb',
                    colkey='idx', colval='id',
                    faiss_index="./temp/faiss/faiss_trained_24000.index", dirout=path) 









########################################################################################################
######## Nearest #######################################################################################
from sklearn.utils.validation import check_is_fitted

def is_available():
    try:
        import faiss
        return True
    except ImportError:
        return False


class faiss_KNNClassifier:
    """ Scikit-learn wrapper interface for Faiss KNN.
    Docs::

        n_neighbors : int (Default = 5)
                    Number of neighbors used in the nearest neighbor search.
        n_jobs : int (Default = None)
                 The number of jobs to run in parallel for both fit and predict.
                  If -1, then the number of jobs is set to the number of cores.
        algorithm : {'brute', 'voronoi'} (Default = 'brute')
            Algorithm used to compute the nearest neighbors:
                - 'brute' will use the :class: `IndexFlatL2` class from faiss.
                - 'voronoi' will use :class:`IndexIVFFlat` class from faiss.
                - 'hierarchical' will use :class:`IndexHNSWFlat` class from faiss.
            Note that selecting 'voronoi' the system takes more time during
            training, however it can significantly improve the search time
            on inference. 'hierarchical' produce very fast and accurate indexes,
            however it has a higher memory requirement. It's recommended when
            you have a lots of RAM or the dataset is small.
            For more information see: https://github.com/facebookresearch/faiss/wiki/Guidelines-to-choose-an-index
        n_cells : int (Default = 100)
            Number of voronoi cells. Only used when algorithm=='voronoi'.
        n_probes : int (Default = 1)
            Number of cells that are visited to perform the search. Note that the
            search time roughly increases linearly with the number of probes.
            Only used when algorithm=='voronoi'.
        References
        ----------
        Johnson Jeff, Matthijs Douze, and Hervé Jégou. "Billion-scale similarity
        search with gpus." arXiv preprint arXiv:1702.08734 (2017).
    """

    def __init__(self,
                 n_neighbors=5,
                 n_jobs=None,
                 algorithm='brute',
                 n_cells=100,
                 n_probes=1):

        self.n_neighbors = n_neighbors
        self.n_jobs = n_jobs
        self.algorithm = algorithm
        self.n_cells = n_cells
        self.n_probes = n_probes

        import faiss
        self.faiss = faiss

    def predict(self, X):
        """Predict the class label for each sample in X.
        Parameters
        ----------
        X : array of shape (n_samples, n_features)
            The input data.
        Returns
        -------
        preds : array, shape (n_samples,)
                Class labels for samples in X.
        """
        idx = self.get_topk(X, self.n_neighbors, return_distance=False)
        class_idx = self.y_[idx]
        counts = np.apply_along_axis(
            lambda x: np.bincount(x, minlength=self.n_classes_), axis=1,
            arr=class_idx.astype(np.int16))
        preds = np.argmax(counts, axis=1)
        return preds

    def get_topk(self, X, n_neighbors=None, return_distance=True):
        """Finds the K-neighbors of a point.
        Docs::

            X : array of shape (n_samples, n_features)
                The input data.
            n_neighbors : int
                Number of neighbors to get (default is the value passed to the
                constructor).
            return_distance : boolean, optional. Defaults to True.
                If False, distances will not be returned
            Returns
            -------
            dists : list of shape = [n_samples, k]
                The distances between the query and each sample in the region of
                competence. The vector is ordered in an ascending fashion.
            idx : list of shape = [n_samples, k]
                Indices of the instances belonging to the region of competence of
                the given query sample.
        """
        if n_neighbors is None:
            n_neighbors = self.n_neighbors

        elif n_neighbors <= 0:
            raise ValueError("Expected n_neighbors > 0."
                             " Got {}" .format(n_neighbors))
        else:
            if not np.issubdtype(type(n_neighbors), np.integer):
                raise TypeError(
                    "n_neighbors does not take {} value, "
                    "enter integer value" .format(type(n_neighbors)))

        check_is_fitted(self, 'index_')

        X = np.atleast_2d(X).astype(np.float32)
        dist, idx = self.index_.search(X, n_neighbors)
        if return_distance:
            return dist, idx
        else:
            return idx

    def predict_proba(self, X):
        """Estimates the posterior probabilities for sample in X.
        Parameters
        ----------
        X : array of shape (n_samples, n_features)
            The input data.
        Returns
        -------
        preds_proba : array of shape (n_samples, n_classes)
                          Probabilities estimates for each sample in X.
        """
        idx = self.get_topk(X, self.n_neighbors, return_distance=False)
        class_idx = self.y_[idx]
        counts = np.apply_along_axis(
            lambda x: np.bincount(x, minlength=self.n_classes_), axis=1,
            arr=class_idx.astype(np.int16))

        preds_proba = counts / self.n_neighbors

        return preds_proba

    def fit(self, X, y):
        """Fit the model according to the given training data.
        Parameters
        ----------
        X : array of shape (n_samples, n_features)
            Data used to fit the model.
        y : array of shape (n_samples)
            class labels of each example in X.
        """
        X = np.atleast_2d(X).astype(np.float32)
        X = np.ascontiguousarray(X)
        d = X.shape[1]  # dimensionality of the feature vector
        self._prepare_knn_algorithm(X, d)
        self.index_.add(X)
        self.y_ = y
        self.n_classes_ = np.unique(y).size
        return self

    def _prepare_knn_algorithm(self, X, d):
        if self.algorithm == 'brute':
            self.index_ = self.faiss.IndexFlatL2(d)
        elif self.algorithm == 'voronoi':
            quantizer = self.faiss.IndexFlatL2(d)
            self.index_ = self.faiss.IndexIVFFlat(quantizer, d, self.n_cells)
            self.index_.train(X)
            self.index_.nprobe = self.n_probes
        elif self.algorithm == 'hierarchical':
            self.index_ = self.faiss.IndexHNSWFlat(d, 32)
            self.index_.hnsw.efConstruction = 40
        else:
            raise ValueError("Invalid algorithm option."
                             " Expected ['brute', 'voronoi', 'hierarchical'], "
                             "got {}" .format(self.algorithm))









########################################################################################################
######## Top-K retrieval ###############################################################################
def topk_nearest_vector(x0:np.ndarray, vector_list:list, topk=3, engine='faiss', engine_pars:dict=None) :
    """ Retrieve top k nearest vectors using FAISS, raw retrievail
    """
    if 'faiss' in engine :
        # cc = engine_pars
        import faiss  
        index = faiss.index_factory(x0.shape[1], 'Flat')
        index.add(vector_list)
        dist, indice = index.search(x0, topk)
        return dist, indice



def topk_calc( diremb="", dirout="", topk=100,  idlist=None, nexample=10, emb_dim=200, tag=None, debug=True):
    """ Get Topk vector per each element vector of dirin.
    Example:
        Doc::

           Return  pd.DataFrame( columns=[  'id', 'emb', 'topk', 'dist'  ] )
             id : id of the emb
             emb : [342,325345,343]   X0 embdding
             topk:  2,5,6,5,6
             distL 0,3423.32424.,

    
           python $utilmy/deeplearning/util_topk.py  topk_calc   --diremb     --dirout
    

    """
    from utilmy import pd_read_file

    ##### Load emb data  ###############################################
    flist    = glob_glob(diremb)
    df       = pd_read_file(  flist , n_pool=10 )
    df.index = np.arange(0, len(df))
    log(df)

    assert len(df[['id', 'emb' ]]) > 0


    ##### Element X0 ####################################################
    vectors = np_str_to_array(df['emb'].values,  mdim= emb_dim)
    del df ; gc.collect()

    llids = idlist
    if idlist is None :    
       llids = df['id'].values    
       llids = llids[:nexample]

    dfr = [] 
    for ii in range(0, len(llids)) :        
        x0      = vectors[ii]
        xname   = llids[ii]
        log(xname)
        x0         = x0.reshape(1, -1).astype('float32')  
        dist, rank = topk_nearest_vector(x0, vectors, topk= topk) 
        
        ss_rankid = np_array_to_str( llids[ rank[0] ] )
        ss_distid = np_array_to_str( dist[0]  )

        dfr.append([  xname, x0,  ss_rankid,  ss_distid  ])   

    dfr = pd.DataFrame( dfr, columns=[  'id', 'emb', 'topk', 'dist'  ] )
    pd_read_file( dfr, dirout + f"/topk_{tag}.parquet"  )




########################################################################################################
######## Top-K retrieval Faiss #########################################################################
def faiss_create_index(df_or_path=None, col='emb', dirout=None,  db_type = "IVF4096,Flat", nfile=1000, emb_dim=200,
                       nrows=-1):
    """ Create Large scale Index
    Docs::

          python util_topk.py   faiss_create_index    --df_or_path myemb/


    """
    import faiss

    
    dirout    =  "/".join( os.path.dirname(df_or_path).split("/")[:-1]) + "/faiss/" if dirout is None else dirout
    os.makedirs(dirout, exist_ok=True)
    log('dirout', dirout)
    log('dirin',  df_or_path)
    
    if isinstance(df_or_path, str) :      
       flist = sorted(glob.glob(df_or_path  ))[:nfile] 
       log('Loading', df_or_path) 
       df = pd_read_file(flist, n_pool=20, verbose=False)
    else :
       df = df_or_path

    df  = df.iloc[:nrows, :]   if nrows>0  else df
    log(df)
        
    tag = f"_" + str(len(df))    
    df  = df.sort_values('id')    
    df[ 'idx' ] = np.arange(0,len(df))
    pd_to_file( df[[ 'idx', 'id' ]], 
                dirout + f"/map_idx{tag}.parquet", show=1)   #### Keeping maping faiss idx, item_tag
    

    log("#### Convert parquet to numpy   ", dirout)
    X  = np.zeros((len(df), emb_dim  ), dtype=np.float32 )    
    vv = df[col].values
    del df; gc.collect()
    for i, r in enumerate(vv) :
        try :
          vi      = [ float(v) for v in r.split(',')]        
          X[i, :] = vi
        except Exception as e:
          log(i, e)
            
    log("#### Preprocess X")
    faiss.normalize_L2(X)  ### Inplace L2 normalization
    log( X ) 
    
    nt = min(len(X), int(max(400000, len(X) *0.075 )) )
    Xt = X[ np.random.randint(len(X), size=nt),:]
    log('Nsample training', nt)

    ####################################################    
    D = emb_dim  ###   actual  embedding size
    N = len(X)   ##### 1000000

    # Param of PQ for 1 billion
    M      = 40 # 16  ###  200 / 5 = 40  The number of sub-vector. Typically this is 8, 16, 32, etc.
    nbits  = 8        ### bits per sub-vector. This is typically 8, so that each sub-vec is encoded by 1 byte    
    nlist  = 6000     ###  # Param of IVF,  Number of cells (space partition). Typical value is sqrt(N)    
    hnsw_m = 32       ###  # Param of HNSW Number of neighbors for HNSW. This is typically 32

    # Setup  distance -> similarity in uncompressed space is  dis = 2 - 2 * sim, https://github.com/facebookresearch/faiss/issues/632
    quantizer = faiss.IndexHNSWFlat(D, hnsw_m)
    index     = faiss.IndexIVFPQ(quantizer, D, nlist, M, nbits)
    
    log('###### Train indexer')
    index.train(Xt)      # Train
    
    log('###### Add vectors')
    index.add(X)        # Add

    log('###### Test values ')
    index.nprobe = 8  # Runtime param. The number of cells that are visited for search.
    dists, ids = index.search(x=X[:3], k=4 )  ## top4
    log(dists, ids)
    
    log("##### Save Index    ")
    dirout2 = dirout + f"/faiss_trained{tag}.index" 
    log( dirout2 )
    faiss.write_index(index, dirout2 )
    return dirout2
        


def faiss_load_index(faiss_index_path=""):
    return None



def faiss_topk_calc(df=None, root=None, colid='id', colemb='emb',
                    faiss_index:str="", topk=200, dirout=None, npool=1, nrows=10**7, nfile=1000,
                    return_simscore=False, return_dist=False,

                    ) :
   """  Calculate top-k for each 'emb' vector of dataframe in parallel batch.
   Doc::

       df : path or DF   df[['id', 'embd' ]]
       dirout : results path,   id, topk   :     word id, topk of id



       https://github.com/facebookresearch/faiss/issues/632
       dis = 2 - 2 * sim
   """

   faiss_index = ""  if faiss_index is None  else faiss_index
   if isinstance(faiss_index, str) :
        faiss_path  = faiss_index
        faiss_index = faiss_load_index(db_path=faiss_index) 
   faiss_index.nprobe = 12  # Runtime param. The number of cells that are visited for search.
   log('Faiss Index: ', faiss_index)


   ########################################################################
   if isinstance(df, list):    ### Multi processing part
        if len(df) < 1 : return 1
        flist = df[0]
        root     = os.path.abspath( os.path.dirname( flist[0] + "/../../") )  ### bug in multipro
        dirin    = root + "/df/"
        dir_out  = dirout

   elif isinstance(df, str) : ### df == string path
        root    = df
        dirin   = root
        dir_out = dirout
        flist   = sorted(glob.glob(dirin))
   else :
       raise Exception('Unknonw path')

   log('dir_in',  dirin)
   log('dir_out', dir_out)
   flist = flist[:nfile]
   if len(flist) < 1: return 1 
   log('Nfile', len(flist), flist )


   ####### Parallel Mode ################################################
   if npool > 1 and len(flist) > npool :
        log('Parallel mode')
        from utilmy.parallel  import multiproc_run, multiproc_tochunk
        ll_list = multiproc_tochunk(flist, npool = npool)
        multiproc_run(faiss_topk_calc,  ll_list,  npool, verbose=True, start_delay= 5,
                      input_fixed = { 'faiss_index': faiss_path }, )      
        return 1


   ####### Single Mode #################################################
   dirmap       = faiss_path.replace("faiss_trained", "map_idx").replace(".index", '.parquet')  
   map_idx_dict = db_load_dict(dirmap,  colkey = 'idx', colval = 'item_tag_vran' )

   chunk  = 200000       
   kk     = 0
   os.makedirs(dir_out, exist_ok=True)    
   dirout2 = dir_out 
   flist = [ t for t in flist if len(t)> 8 ]
   log('\n\nN Files', len(flist), str(flist)[-100:]  ) 
   for fi in flist :
       if os.path.isfile( dir_out + "/" + fi.split("/")[-1] ) : continue
       # nrows= 5000
       df = pd_read_file( fi, n_pool=1  ) 
       df = df.iloc[:nrows, :]
       log(fi, df.shape)
       df = df.sort_values('id') 

       dfall  = pd.DataFrame()   ;    nchunk = int(len(df) // chunk)    
       for i in range(0, nchunk+1):
           if i*chunk >= len(df) : break         
           i2 = i+1 if i < nchunk else 3*(i+1)
        
           x0 = np_str_to_array( df[colemb].iloc[ i*chunk:(i2*chunk)].values    )
           log('X topk') 
           topk_dist, topk_idx = faiss_index.search(x0, topk)            
           log('X', topk_idx.shape) 
                
           dfi                   = df.iloc[i*chunk:(i2*chunk), :][[ colid ]]
           dfi[ f'{colid}_list'] = np_matrix_to_str2( topk_idx, map_idx_dict)  ### to actual id
           if return_dist:     dfi[ f'dist_list']  = np_matrix_to_str( topk_dist )
           if return_simscore: dfi[ f'sim_list']     = np_matrix_to_str_sim( topk_dist )
        
           dfall = pd.concat((dfall, dfi))

       dirout2 = dir_out + "/" + fi.split("/")[-1]      

       pd_to_file(dfall, dirout2, show=1)  
       kk    = kk + 1
       if kk == 1 : dfall.iloc[:100,:].to_csv( dirout2.replace(".parquet", ".csv")  , sep="\t" )
             
   log('All finished')    
   return os.path.dirname( dirout2 )



#########################################################################################################
############## Loader of embeddings #####################################################################
def embedding_cosinus_scores_pairwise(embs:np.ndarray, word_list:list=None, is_symmetric=False):
    """ Pairwise Cosinus Sim scores
    Example:
        Doc::

           embs   = np.random.random((10,200))
           idlist = [str(i) for i in range(0,10)]
           df = sim_scores_fast(embs:np, idlist, is_symmetric=False)
           df[[ 'id1', 'id2', 'sim_score'  ]]

    """
    import copy, numpy as np
    # from sklearn.metrics.pairwise import cosine_similarity
    n= len(embs)
    word_list = np.arange(0, n) if word_list is None else word_list
    dfsim = []
    for i in  range(0, len(word_list) - 1) :
        vi = embs[i,:]
        normi = np.sqrt(np.dot(vi,vi))
        for j in range(i+1, len(word_list)) :
            # simij = cosine_similarity( embs[i,:].reshape(1, -1) , embs[j,:].reshape(1, -1)     )
            vj = embs[j,:]
            normj = np.sqrt(np.dot(vj, vj))
            simij = np.dot( vi ,  vj  ) / (normi * normj)
            dfsim.append([ word_list[i], word_list[j],  simij   ])
            # dfsim2.append([ nwords[i], nwords[j],  simij[0][0]  ])

    dfsim  = pd.DataFrame(dfsim, columns= ['id1', 'id2', 'sim_score' ] )

    if is_symmetric:
        ### Add symmetric part
        dfsim3 = copy.deepcopy(dfsim)
        dfsim3.columns = ['id2', 'id1', 'sim_score' ]
        dfsim          = pd.concat(( dfsim, dfsim3 ))
    return dfsim







########################################################################################################
if 'custom_code':
    def test_create_fake_df(dirout="./ztmp/", nrows=100):
        """ Creates a fake embeddingdataframe
        """
        res  = Box({})
        n    = nrows
        mdim = 50

        #### Create fake user ids
        word_list = [ 'a' + str(i) for i in range(n)]
        emb_list  = []
        for i in range(n):
            emb_list.append( ','.join([str(x) for x in np.random.random(mdim) ])  )

        df = pd.DataFrame()
        df['id']  = word_list
        df['emb'] = emb_list
        res.df    = df

        #### export on disk
        res.dir_parquet = dirout + "/emb_parquet/db_emb.parquet"
        pd_to_file(df, res.dir_parquet , show=1)

        #### Write on text:
        res.dir_text   = dirout + "/word2vec_export.vec"
        log( res.dir_text )
        with open(res.dir_text, mode='w') as fp:
            fp.write("word2vec\n")
            for i,x in df.iterrows():
              emb  = x['emb'].replace(",", "")
              fp.write(  f"{x['id']}  {emb}\n")

        return res


    def pd_to_onehot(dflabels: pd.DataFrame, labels_dict: dict = None) -> pd.DataFrame:
        """ Label INTO 1-hot encoding   {'gender': ['one', 'two']  }
    
    
        """
        if labels_dict is not None:
            for ci, catval in labels_dict.items():
                dflabels[ci] = pd.Categorical(dflabels[ci], categories=catval)
    
        labels_col = labels_dict.keys()
    
        for ci in labels_col:
            dfi_1hot = pd.get_dummies(dflabels, columns=[ci])  ### OneHot
            dfi_1hot = dfi_1hot[[t for t in dfi_1hot.columns if ci in t]]  ## keep only OneHot
            dflabels[ci + "_onehot"] = dfi_1hot.apply(lambda x: ','.join([str(t) for t in x]), axis=1)
            #####  0,0,1,0 format   log(dfi_1hot)
        return dflabels



    def topk_custom(topk=100, dirin=None, pattern="df_*", filter1=None):
        """  python prepro.py  topk    |& tee -a  /data/worpoch_261/topk/zzlog.py


        """
        from utilmy import pd_read_file
        import cv2

        filter1 = "all"    #### "article"

        dirout  = dirin + "/topk/"
        os.makedirs(dirout, exist_ok=True)
        log(dirin)

        #### Load emb data  ###############################################
        df        = pd_read_file(  dirin + f"/{pattern}.parquet", n_pool=10 )
        log(df)
        df['id1'] = df['id'].apply(lambda x : x.split(".")[0])


        #### Element X0 ######################################################
        colsx = [  'masterCategory', 'subCategory', 'articleType' ]  # 'gender', , 'baseColour' ]
        df0   = df.drop_duplicates( colsx )
        log('Reference images', df0)
        llids = list(df0.sample(frac=1.0)['id'].values)


        for idr1 in llids :
            log(idr1)
            #### Elements  ####################################################
            ll = [  (  idr1,  'all'     ),
                    # (  idr1,  'article' ),
                    (  idr1,  'color'   )
            ]


            for (idr, filter1) in ll :
                dfi     = df[ df['id'] == idr ]
                log(dfi)
                if len(dfi) < 1: continue
                x0      = np.array(dfi['pred_emb'].values[0])
                xname   = dfi['id'].values[0]
                log(xname)

                #### 'gender',  'masterCategory', 'subCategory',  'articleType',  'baseColour',
                g1 = dfi['gender'].values[0]
                g2 = dfi['masterCategory'].values[0]
                g3 = dfi['subCategory'].values[0]
                g4 = dfi['articleType'].values[0]
                g5 = dfi['baseColour'].values[0]
                log(g1, g2, g3, g4, g5)

                xname = f"{g1}_{g4}_{g5}_{xname}".replace("/", "-")

                if filter1 == 'article' :
                    df1 = df[ (df.articleType == g4) ]

                if filter1 == 'color' :
                    df1 = df[ (df.gender == g1) & (df.subCategory == g3) & (df.articleType == g4) & (df.baseColour == g5)  ]
                else :
                    df1 = copy.deepcopy(df)
                    #log(df)

                ##### Setup Faiss queey ########################################
                x0      = x0.reshape(1, -1).astype('float32')
                vectors = np.array( list(df1['pred_emb'].values) )
                log(x0.shape, vectors.shape)

                dist, rank = topk_nearest_vector(x0, vectors, topk= topk)
                # print(dist)
                df1              = df1.iloc[rank[0], :]
                df1['topk_dist'] = dist[0]
                df1['topk_rank'] = np.arange(0, len(df1))
                log( df1 )
                df1.to_csv( dirout + f"/topk_{xname}_{filter1}.csv"  )

                img_list = df1['id'].values
                log(str(img_list)[:30])

                log('### Writing images on disk  ###########################################')
                import diskcache as dc
                db_path = "/dev/shm/train_npz/small//img_tean_nobg_256_256-1000000.cache"
                cache   = dc.Cache(db_path)
                print('Nimages', len(cache) )

                dir_check = dirout + f"/{xname}_{filter1}/"
                os.makedirs(dir_check, exist_ok=True)
                for i, key in enumerate(img_list) :
                    if i > 15: break
                    img  = cache[key]
                    img  = img[:, :, ::-1]
                    key2 = key.split("/")[-1]
                    cv2.imwrite( dir_check + f"/{i}_{key2}"  , img)
                log( dir_check )


    
    

################################################################################################################




    
 
    
###############################################################################################################
if __name__ == "__main__":
    import fire
    fire.Fire()



    
