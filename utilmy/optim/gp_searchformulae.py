""" Search Formulae using GP
Docs::

    Install

       DCGP
          https://darioizzo.github.io/dcgp/installation.html#python

          https://darioizzo.github.io/dcgp/notebooks/real_world1.html

       DSO
           https://github.com/brendenpetersen/deep-symbolic-optimization


    -- Test Problem
    2) Goal is to find a formulae, which make merge_list as much sorted as possible
    Example :
        myproblem1 = myProblem()
        ## myproblem1.get_cost(formuale_str, symbols  )

        from lib2to3.pygram import Symbols
        from dcgpy import expression_gdual_double as expression
        from dcgpy import kernel_set_gdual_double as kernel_set
        from pyaudi import gdual_double as gdual

        p               = Box({})
        p.nvars_in      = 2  ### nb of variables
        p.nvars_out     = 1

        p.ks            = kernel_set(["sum", "diff", "div", "mul"])
        p.print_after   = 100
        p.print_best    = True
        p.n             = 20  ## Population (Suggested: 10~20)
        p.pa            = 0.3  ## Parasitic Probability (Suggested: 0.3)
        p.kmax          = 100000  ## Max iterations
        p.nc,nr         = 10,1  ## Graph columns x rows
        p.a             = 2  # Arity
        p.n_cuckoo_eggs = round(p.pa * p.n)
        p.n_replace     = round(p.pa * p.n)
        p.f_trace       = 'trace'
        p.seed          = 43


        #### Run Search
        search_formuale_algo1(myproblem1, pars_dict=p, verbose=True)


        #### Parallel version   ------------------------------------
        for i in range(npool):
            p2         = copy.deepcopy(p)
            p2.f_trace = f'trace_{i}.log'
            input_list.append(p2)

        #### parallel Runs
        multiproc_run(search_formuale_dcgpy, input_fixed={"myproblem": myproblem1, 'verbose':False},
                      input_list=input_list,
                      npool=3)

"""
import random, math, numpy as np, warnings, copy
import scipy.stats
from operator import itemgetter
from copy import deepcopy
warnings.filterwarnings("ignore")
from box import Box


####################################################################################################
def log(*s):
    print(*s, flush=True)


def test_all():
    test1()


def test1():
    myproblem1 = myProblem()

    from lib2to3.pygram import Symbols
    from dcgpy import expression_gdual_double as expression
    from dcgpy import kernel_set_gdual_double as kernel_set
    from pyaudi import gdual_double as gdual

    p               = Box({})
    p.log_file      = 'trace.log'
    p.print_after   = 100
    p.print_best    = True


    p.nvars_in      = 2  ### nb of variables
    p.nvars_out     = 1
    p.ks            = ["sum", "diff", "div", "mul"]

    p.n             = 20  ## Population (Suggested: 10~20)
    p.pa            = 0.3  ## Parasitic Probability (Suggested: 0.3)
    p.kmax          = 100000  ## Max iterations
    p.nc,nr         = 10,1  ## Graph columns x rows
    p.arity         = 2  # Arity
    p.seed          = 43


    #### Run Search
    search_formuale_dcgpy(myproblem1, pars_dict=p, verbose=True)



def test2():

    from utilmy.parallel import multiproc_run

    from lib2to3.pygram import Symbols
    from dcgpy import expression_gdual_double as expression
    from dcgpy import kernel_set_gdual_double as kernel_set
    from pyaudi import gdual_double as gdual

    myproblem1 = myProblem()

    p               = Box({})
    p.log_file      = 'trace.log'

    p.nvars_in      = 2  ### nb of variables
    p.nvars_out     = 1

    p.ks            = ["sum", "diff", "div", "mul", "log"]
    p.print_after   = 100
    p.print_best    = True
    p.n             = 20  ## Population (Suggested: 10~20)
    p.pa            = 0.3  ## Parasitic Probability (Suggested: 0.3)

    p.kmax          = 100000  ## Max iterations
    p.nc,nr         = 10,1  ## Graph columns x rows
    p.arity         = 2  # Arity

    npool= 2
    input_list = []
    for i in range(npool):
        p2 = copy.deepcopy(p)
        p2.f_trace = f'trace_{i}.log'
        input_list.append(p2)

    ### parallel Runs
    multiproc_run(search_formuale_dcgpy, input_fixed={"myproblem": myproblem1, 'verbose':False},
                  input_list=input_list,
                  npool=3)




####################################################################################################
class myProblem:
    def __init__(self,n_sample = 5,kk = 1.0,nsize = 100,ncorrect1 = 40,ncorrect2 = 50,adjust=1.0):
        """  Define the problem and cost calculation using formulae_str
        Docs::

            myProblem.get_cost(   )

            ---- My Problem
            2)  list with scores (ie randomly generated)
            We use 1 formulae to merge  2 list --> merge_list with score
               Ojective to maximize  correlation(merge_list,  True_ordered_list)

            Goal is to find a formulae, which make merge_list as much sorted as possible

        """
        self.n_sample  = n_sample
        self.kk        = kk
        self.nsize     = nsize
        self.ncorrect1 = ncorrect1
        self.ncorrect2 = ncorrect2
        self.adjust    = adjust



    def get_cost(self, expr:None, symbols):
        """     ######### Objective to Maximize


        """
        # def normalize(val,Rmin,Rmax,Tmin,Tmax):
        #     return (((val-Rmin)/(Rmax-Rmin)*(Tmax-Tmin))+Tmin)

        # def denormalize(val,Rmin,Rmax,Tmin,Tmax):
        #     return (((val-Tmin)/(Tmax-Tmin)*(Rmax-Rmin))+Rmin)

        try:
            correlm = self.get_correlm(formulae_str=expr(symbols)[0])
        except:
            correlm = 1.0

        return(correlm)


    def get_correlm(self, formulae_str:str):
        """  Compare 2 lists lnew, ltrue and output correlation.
             Goal is to find rank_score such Max(correl(lnew(rank_score), ltrue ))
        
        """
        ##### True list
        ltrue = [ str(i)  for i in range(0, 100) ]   

        #### Create noisy list 
        ltrue_rank = {i:x for i,x in enumerate(ltrue)}
        list_overlap =  ltrue[:70]  #### Common elements
        
        
        correls = []
        for i in range(self.n_sample):
            ll1  = self.rank_generate_fake(ltrue_rank, list_overlap,nsize=self.nsize, ncorrect=self.ncorrect1)
            ll2  = self.rank_generate_fake(ltrue_rank, list_overlap,nsize=self.nsize, ncorrect=self.ncorrect2)

            #### Merge them using rank_score
            lnew = self.rank_merge_v5(ll1, ll2, formulae_str= formulae_str)
            lnew = lnew[:100]
            # log(lnew) 

            ### Eval with True Rank
            correls.append(scipy.stats.spearmanr(ltrue,  lnew).correlation)

        correlm = np.mean(correls)
        return -correlm  ### minimize correlation val


    def rank_score(self, fornulae_str:str, rank1:list, rank2:list)-> list:
        """  ## Example of rank_scores0 = Formulae(list_ score1, list_score2)
             ## Take 2 np.array and calculate one list of float (ie NEW scores for position)
        Docs::
    
            list of items:  a,b,c,d, ...
            item      a,b,c,d,e
            rank1 :   1,2,3,4 ,,n     (  a: 1,  b:2, ..)
            rank2 :   5,7,2,1 ,,n     (  a: 5,  b:6, ..)

            scores_new :   a: -7.999,  b:-2.2323
            (item has new scores)
        
        """

        x0 = 1/(self.kk + rank1)
        x1 = 1/(self.kk + rank2*self.adjust)

        scores_new =  eval(fornulae_str)
        return scores_new


    
    def rank_merge_v5(self, ll1:list, ll2:list, formulae_str:str):
        """ ## Merge 2 list using a FORMULAE
        Docs::
        
            Re-rank elements of list1 using ranking of list2
            20k dataframe : 6 sec ,  4sec if dict is pre-build
            Fastest possible in python
        """
        if len(ll2) < 1: return ll1
        n1, n2 = len(ll1), len(ll2)

        if not isinstance(ll2, dict) :
            ll2 = {x:i for i,x in enumerate( ll2 )  }  ### Most costly op, 50% time.

        adjust, mrank = (1.0 * n1) / n2, n2
        rank2 = np.array([ll2.get(sid, mrank) for sid in ll1])
        rank1 = np.arange(n1)
        rank3 = self.rank_score(fornulae_str=formulae_str, rank1=rank1, rank2= rank2) ### Score

        #### re-rank  based on NEW Scores.
        v = [ll1[i] for i in np.argsort(rank3)]
        return v  #### for later preprocess


    #### Generate fake list to be merged.
    def rank_generate_fake(self,dict_full, list_overlap, nsize=100, ncorrect=20):
        """  Returns a list of random rankings of size nsize where ncorrect elements have correct ranks
        Docs::

            dict_full    : a dictionary of 1000 objects and their ranks
            list_overlap : list items common to all lists
            nsize        : the total number of elements to be ranked
            ncorrect     : the number of correctly ranked objects
        """
        # first randomly sample nsize - len(list_overlap) elements from dict_full
        # of those, ncorrect of them must be correctly ranked
        random_vals = []
        while len(random_vals) <= nsize - len(list_overlap):
            rand = random.sample(list(dict_full), 1)
            if (rand not in random_vals and rand not in list_overlap):
                random_vals.append(rand[0])

        # next create list as aggregate of random_vals and list_overlap
        list2 = random_vals + list_overlap
        
        # shuffle nsize - ncorrect elements from list2 
        copy = list2[0:nsize - ncorrect]
        random.shuffle(copy)
        list2[0:nsize - ncorrect] = copy

        # ensure there are ncorrect elements in correct places
        if ncorrect == 0: 
            return list2
        rands = random.sample(list(dict_full)[0:nsize + 1], ncorrect + 1)
        for r in rands:
            list2[r] = list(dict_full)[r]
        return list2






###################################################################################################
def search_formuale_dcgpy(myproblem=None, pars_dict:dict=None, verbose=False, ):
    """ Search Optimal Formulae
    Docs::


        myproblem.calc_cost()

        nvars_in      = 2  ### nb of variables
        nvars_out     = 1

        ks            = kernel_set(["sum", "diff", "div", "mul"])
        print_after   = 100
        print_best    = True
        n             = 20  ## Population (Suggested: 10~20)
        pa            = 0.3  ## Parasitic Probability (Suggested: 0.3)
        kmax          = 100000  ## Max iterations
        nc,nr         = 10,1  ## Graph columns x rows
        a             = 2  # Arity
        n_cuckoo_eggs = round(pa*n)
        n_replace     = round(pa*n)
        log_file       = 'trace.py'


    """
    from lib2to3.pygram import Symbols
    from dcgpy import expression_gdual_double as expression
    from dcgpy import kernel_set_gdual_double as kernel_set
    from pyaudi import gdual_double as gdual

    from box import Box
    ######### Problem definition and Cost calculation
    #myproblem = myProblem()


    #### Formulae GP Search params   #################
    p = Box(pars_dict)

    ### Problem
    nvars_in      = p.nvars_in  ### nb of variables
    nvars_out     = p.nvars_out
    operator_list = kernel_set(p.ks, ["sum", "diff", "div", "mul"] )

    ### Log
    print_after   = p.get('print_after', 20)
    print_best    = p.get('print_best', True)
    pop_size      = p.get("pop_size", 5) #20  ## Population (Suggested: 10~20)
    max_iter      = p.get('max_iter', 2) #100000  ## Max iterations
    seed          = p.get('seed', 43)
    log_file      = p.get('log_file', 'log.log') # 'trace.py'

    ### search
    pa            = p.get( 'pa', 0.3)  # 0.3  ## Parasitic Probability (Suggested: 0.3)
    nc,nr         = p.nc, p.nr # 10,1  ## Graph columns x rows
    arity         = p.get( 'arity', 2)   #2  # Arity
    n_cuckoo_eggs = round(p.pa*p.pop_size)
    n_replace     = round(p.pa*p.pop_size)


    ######### Define expression symbols  #######################
    symbols = []
    for i in range(nvars_in):
        symbols.append(f"x{i}")

    ######### Check   ##########################################
    if verbose:
        log(operator_list)
        log(symbols)


    def get_random_solution():
            return expression(inputs = nvars_in,
                            outputs     = nvars_out,
                            rows        = nr,
                            cols        = nc,
                            levels_back = nc,
                            arity       = arity,
                            kernels     = operator_list(),
                            n_eph       = 0,
                            seed        = seed )

    def search():
        def levyFlight(u):
            return (math.pow(u,-1.0/3.0)) # Golden ratio = 1.62

        def randF():
            return (random.uniform(0.0001,0.9999))

        ########### Init  ##########################################################
        var_levy = []
        for i in range(1000):    
            var_levy.append(round(levyFlight(randF())))
        var_choice = random.choice
        
        # Initialize the nest
        nest = []
        for i in range(pop_size):
            expr = get_random_solution()
            cost = myproblem.get_cost(expr=expr, symbols=symbols)
            nest.append((expr, cost))

        # Sort nest
        nest.sort(key = itemgetter(1))


        # # 5 - Mutate the expression with 2 random mutations of active genes and print
        # ex.mutate_active(2)   log("Mutated expression:", ex(symbols)[0])
        # global best_egg, k, dic_front
        ls_trace = []

        ########### Main Loop  ####################################################
        for k in range(max_iter + 1):
            # Lay cuckoo eggs
            for i in range(n_cuckoo_eggs):
                idx         = random.randint(0,pop_size-1)
                egg         = deepcopy(nest[idx]) # Pick an egg at random from the nest
                cuckoo      = egg[0].mutate_active(var_choice(var_levy))
                cost_cuckoo = myproblem.get_cost(cuckoo)
                if (cost_cuckoo <= egg[1]): # Check if the cuckoo egg is better
                    nest[idx] = (cuckoo,cost_cuckoo)

            nest.sort(key = itemgetter(1)) # Sorting

            # Store ratioA for trace
            ls_trace.append(nest[0][1])
                    
            for i in range(n_replace):
                expr = get_random_solution()
                nest[(pop_size-1)-(i)] = (expr, myproblem.get_cost(expr, symbols))

            # Iterational printing
            if (k%print_after == 0):
                
                with open(log_file,'a') as f:
                    for x in ls_trace:
                        f.write(str(round(x, 3))+'\n')
                ls_trace = [] # dump and restart
                
                nest.sort(key = itemgetter(1)) # Rank nests and find current best
                best_egg = deepcopy(nest[0])
                log(f'\n#{k}', f'{best_egg[1]}')

                if print_best :
                    log(best_egg[0](symbols)[0])
                    #log(best_egg[0].simplify(symbols))
                    log('\n')

    search()




###################################################################################################
if __name__ == "__main__":
    import fire
    fire.Fire()

