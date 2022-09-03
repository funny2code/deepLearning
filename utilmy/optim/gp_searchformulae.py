""" Search  mathematical Formulae using Genetic Algorithm , Genetic Programming

Docs::

    Install  DCGP

          conda create -n dcgp  python==3.8.1
          source activate dcgp
          conda install   -y  -c conda-forge dcgp-python  scipy
          pip install python-box fire utilmy

          python -c "from dcgpy import test; test.run_test_suite(); import pygmo; pygmo.mp_island.shutdown_pool(); pygmo.mp_bfe.shutdown_pool()"


          https://darioizzo.github.io/dcgp/installation.html#python

          https://darioizzo.github.io/dcgp/notebooks/real_world1.html


    Install  DSO
           https://github.com/brendenpetersen/deep-symbolic-optimization

           https://iclr.cc/virtual/2021/poster/2578



    Install  Operon

        https://github.com/heal-research/pyoperon

        https://github.com/heal-research/pyoperon/blob/main/example/operon-bindings.py



    Docs:
        https://esa.github.io/pygmo2/archipelago.html#pygmo.archipelago.status



    -- Test Problem
        cd $utilmy/optim/
        python gp_searchformulae.py  test1

        2) Goal is to find a formulae, which make merge_list as much sorted as possible
        Example :
            ## 1) Define Problem Class with get_cost methods
            myproblem1 = myProblem()
            ## myproblem1.get_cost(formulae_str, symbols  )

            ## 2) Param Search
            p               = Box({})
            ...


            ## 3) Run Search
            from utilmy.optim.gp_formulaesearch import search_formulae_algo1
            search_formulae_algo1(myproblem1, pars_dict=p, verbose=True)


            #### Parallel version   ------------------------------------
            for i in range(npool):
                p2         = copy.deepcopy(p)
                p2.f_trace = f'trace_{i}.log'
                input_list.append(p2)

            #### parallel Runs
            from utilmy.parallel import multiproc_run
            multiproc_run(search_formulae_dcgpy, input_fixed={"myproblem": myproblem1, 'verbose':False},
                          input_list=input_list,
                          npool=3)



"""
import os, random, math, numpy as np, warnings, copy
from box import Box
np.seterr(all='ignore') 

####################################################################################################
from utilmy.utilmy import log, log2

# def log(*s):
#     """Log/Print"""
#     print(*s, flush=True)


def help():
    from utilmy import help_create
    print(help_create("utilmy.parallel") )



####################################################################################################
def test_all():
    """function test_all
    """
    test1()


def test_pars_values():
    """ return test params
    docs::

        myproblem1 = myProblem()

        p               = Box({})
        p.log_file      = 'trace.log'
        p.print_after   = 5
        p.print_best    = True


        p.nvars_in      = 2  ### nb of variables
        p.nvars_out     = 1
        p.operators     = ["sum", "diff", "div", "mul"]

        p.max_iter      = 10
        p.pop_size      = 20  ## Population (Suggested: 10~20)
        p.pa            = 0.3  ## Parasitic Probability (Suggested: 0.3)
        p.kmax          = 100000  ## Max iterations
        p.nc, p.nr       = 10,1  ## Graph columns x rows
        p.arity         = 2  # Arity
        p.seed          = 43

    """
    myproblem1 = myProblem1()

    p               = Box({})
    p.log_file      = 'trace.log'
    p.print_after   = 5
    p.print_best    = True


    p.nvars_in      = 2  ### nb of variables
    p.nvars_out     = 1
    p.operators     = ["sum", "diff", "div", "mul", 'sin']

    p.max_iter      = 10
    p.pop_size      = 20  ## Population (Suggested: 10~20)
    p.pa            = 0.3  ## Parasitic Probability (Suggested: 0.3)
    p.kmax          = 100000  ## Max iterations
    p.nc, p.nr       = 10,1  ## Graph columns x rows
    p.arity         = 2  # Arity
    p.seed          = 43

    return myproblem1, p


def test1():
    """Test search_formulae_dcgpy_v1
    """
    myproblem       = myProblem2()

    p               = Box({})
    p.log_file      = 'trace.log'
    p.print_after   = 5
    p.print_best    = True


    p.nvars_in      = 2  ### nb of variables
    p.nvars_out     = 1
    p.operators     = ["sum", "mul", "div", "diff"]
    p.symbols       = ["x0","x1"]
    p.max_iter      = 10
    p.nexp          = 100
    p.offsprings    = 10
    p.stop          = 2000

    #### Run Search
    search_formulae_dcgpy_v1(myproblem, pars_dict=p, verbose=True)



def test2():
    """Test search_formulae_dcgpy_v1
    """
    myproblem       = myProblem1()

    p               = Box({})
    p.log_file      = 'trace.log'
    p.print_after   = 5
    p.print_best    = True


    p.nvars_in      = 2  ### nb of variables
    p.nvars_out     = 1
    p.operators     = ["sum", "mul", "div", "diff","sin","cos"]
    p.symbols       = ["x0","x1"]
    p.max_iter      = 10
    p.nexp          = 100
    p.offsprings    = 10
    p.stop          = 2000

    #### Run Search
    search_formulae_dcgpy_v1(myproblem, pars_dict=p, verbose=True)


def test6():
    """Test the myProblem4 class, parrallel version

    """
    myproblem       = myProblem4()

    p               = Box({})
    p.log_file      = 'trace.log'
    p.print_after   = 5
    p.print_best    = True


    p.nvars_in      = 3  ### nb of variables
    p.nvars_out     = 1
    p.operators     = ["sum", "mul", "div", "diff"]
    p.symbols       = ["x","v","k"]
    p.max_iter      = 10
    p.nexp          = 100
    p.offsprings    = 10
    p.stop          = 2000
    search_formulae_dcgpy_v1(problem = myproblem, pars_dict=p, verbose=False, )


def test7():
    """Test the myProblem3 class, parrallel version

    """
    myproblem       = myProblem3()

    p               = Box({})
    p.log_file      = 'trace.log'
    p.print_after   = 5
    p.print_best    = True


    p.nvars_in      = 3  ### nb of variables
    p.nvars_out     = 1
    p.operators     = ["sum", "mul", "div", "diff","sin","cos"]
    p.symbols       = ["theta","omega","c"]
    p.max_iter      = 10
    p.nexp          = 100
    p.offsprings    = 10
    p.stop          = 2000
    search_formulae_dcgpy_v1(problem = myproblem, pars_dict=p, verbose=False, )


def test1_parallel():
    """Test of search_formulae_dcgpy_v1_parallel
    """
    myproblem1,p = test_pars_values()

    search_formulae_dcgpy_v1_parallel(myproblem=myproblem1, pars_dict=p, verbose=False, npool=3 )


def test1_parallel2():
    """Test parralel run of search_formulae_dcgpy_v1, in customize parallle version.
    """
    from utilmy.parallel import multiproc_run

    myproblem1,p = test_pars_values()

    npool= 3
    input_list = []
    for i in range(npool):
        p2 = copy.deepcopy(p)
        p2['log_file'] = f'trace_{i}.log'
        input_list.append(p2)

    ### parallel Runs
    multiproc_run(_search_formulae_dcgpy_v1_wrapper,
                  input_fixed={"myproblem": myproblem1, 'verbose':False},
                  input_list=input_list,
                  npool=npool)



def test4_island():
    """Test search_formulae_dcgpy_v1_parallel_island
    """
    myproblem1,p = test_pars_values()

    #### Run Search
    search_formulae_dcgpy_v1_parallel_island(myproblem1, ddict_ref=p
                       ,hyper_par_list  = ['pa',  ]    ### X[0],  X[1]
                       ,hyper_par_bounds = [ [0], [ 0.6 ] ]
                       ,pop_size=6
                       ,n_island=2
                       ,dir_log="./logs/"
                      )



###################################################################################################
class myProblem1:
    def __init__(self,n_sample = 5,kk = 1.0,nsize = 100,):
        """  Define the problem and cost calculation using formulae_str
        Docs::


            myProblem.get_cost(   )

            ---- My Problem
            2)  list with scores (ie randomly generated)
            We use 1 formulae to merge  2 list --> merge_list with score
               Ojective to maximize  correlation(merge_list,  True_ordered_list)

        """
        import numpy as np
        self.n_sample  = 1
        self.kk        = kk
        self.nsize     = nsize

        self.x0 = np.random.random(50)*10 - 5.0
        self.x1 = np.random.random(50)*10 - 5.0

    def get_cost(self, expr, symbols):
        """ Cost Calculation, Objective to minimize Cost
        Docs::

            expr            : Expression whose cost has to be maximized
            symbols         : Symbols

        """
        #yt is the true expression
        yt = np.sin(self.x1)/self.x1 + self.x0*self.x1 + self.x1*np.cos(self.x1) 
        x0 = self.x0  
        x1 = self.x1
        y = eval(expr(symbols)[0])
        err = yt-y
        check = 3
        return sum(err*err), check


class myProblem2:
    def __init__(self,n_sample = 5,kk = 1.0,nsize = 100,):
        """  Define the problem and cost calculation using formulae_str
        Docs::


            myProblem.get_cost(   )

            ---- My Problem
            2)  list with scores (ie randomly generated)
            We use 1 formulae to merge  2 list --> merge_list with score
               Ojective to maximize  correlation(merge_list,  True_ordered_list)

        """
        import numpy as np
        self.n_sample  = 1
        self.kk        = kk
        self.nsize     = nsize

        self.x0 = np.random.random(50)*10 - 5.0
        self.x1 = np.random.random(50)*10 - 5.0


    def get_cost(self, expr, symbols):
        """ Cost Calculation, Objective to minimize Cost
        Docs::

            expr            : Expression whose cost has to be maximized
            symbols         : Symbols

        """

        yt = np.sin(self.x1) + self.x0 + self.x1*self.x1 #This is the true expression
        x0 = self.x0  
        x1 = self.x1
        y = eval(expr(symbols)[0])
        err = yt-y
        check = 3
        return sum(err*err), check


class myProblem3:
    def __init__(self):
        pass

    def get_cost(self, dCGP, symbols):
        """ Cost Calculation, Objective to minimize Cost
        Docs::

            expr            : Expression whose cost has to be maximized
            symbols         : Symbols

        """
        from random import random
        from dcgpy import kernel_set_gdual_vdouble as kernel_set
        from dcgpy import expression_gdual_vdouble as expression
        from pyaudi import gdual_vdouble as gdual
        n_points = 50
        omega = []
        theta = []
        c = []
        for i in range(n_points):
            omega.append(random()*10 - 5)
            theta.append(random()*10 - 5)
            c.append(random()*10)

        theta = gdual(theta,symbols[0],1)
        omega = gdual(omega,symbols[1],1)
        c = gdual(c)
        res = dCGP([theta,omega,c])[0]
        derivative_symbols = ['d'+item for item in symbols]
        dPdtheta = np.array(res.get_derivative({derivative_symbols[0]: 1}))
        dPdomega = np.array(res.get_derivative({derivative_symbols[1]: 1}))
        thetacoeff = np.array(theta.constant_cf)
        omegacoeff = np.array(omega.constant_cf)
        ccoeff = np.array(c.constant_cf)
        err = dPdtheta/dPdomega + (-ccoeff * np.sin(thetacoeff)) / omegacoeff
        check = sum(dPdtheta*dPdtheta + dPdomega*dPdomega)
        return sum(err * err ), check


class myProblem4:
    def __init__(self):
        pass

    def get_cost(self, dCGP, symbols):
        """ Cost Calculation, Objective to minimize Cost
        Docs::

            DCGP            : Formulae Expression Object
            symbols         : Symbols  [ 'x1', 'x2', 'x3' ]

        """
        import random
        from dcgpy import kernel_set_gdual_vdouble as kernel_set
        from dcgpy import expression_gdual_vdouble as expression
        from pyaudi import gdual_vdouble as gdual

        n_points = 50

        ###### Variable numerical  ################################
        x = np.random.random(n_points)*2 +2
        v = np.random.random(n_points)*2 +2
        k = np.random.random(n_points)*2 +2
        #for i in range(n_points):
        #    x.append(random.random()*2 + 2)
        #    v.append(random.random()*2 + 2)
        #    k.append(random.random()*2 + 2)
        x = gdual(x,symbols[0], 1)
        v = gdual(v,symbols[1], 1)
        k = gdual(k)
        xcoeff = np.array(x.constant_cf)
        vcoeff = np.array(v.constant_cf)
        kcoeff = np.array(k.constant_cf)


        #### Derivatives numerical  ##############################
        derivative_symbols = ['d'+item for item in symbols]

        formul = dCGP([x,v,k])[0]

        ### formul_str = dCGP.simplify(symbols)
        ### formul_val = eval( formul_str )    ### numerical values

        dPdx = np.array(formul.get_derivative({derivative_symbols[0]: 1}))
        dPdv = np.array(formul.get_derivative({derivative_symbols[1]: 1}))


        ### Cost numerical
        err  = dPdx/dPdv - kcoeff * xcoeff / vcoeff
        cost = sum(err * err)
        return cost, 3



###################################################################################################
def search_formulae_dcgpy_v1(problem=None, pars_dict:dict=None, verbose=1, ):
    """ Search Optimal Formulae
    Docs::

        conda install  dcgpy

        nvars_in      = p.nvars_in  ### nb of variables
        nvars_out     = p.nvars_out
        operator_list = kernel_set(p.operators, ["sum", "diff", "div", "mul"] )

        ### Log
        print_after   = p.get('print_after', 20)
        print_best    = p.get('print_best', True)
        pop_size      = p.get("pop_size", 5) #20  ## Population (Suggested: 10~20)
        max_iter      = p.get('max_iter', 2) #100000  ## Max iterations
        seed          = p.get('seed', 43)
        log_file      = p.get('log_file', 'log.log') # 'trace.py'

        -- Add constraints in the functional space

        https://darioizzo.github.io/dcgp/notebooks/phenotype_correction_ex.html
        https://darioizzo.github.io/dcgp/notebooks/finding_prime_integrals.html


    """
    from lib2to3.pygram import Symbols
    from dcgpy import expression_gdual_vdouble as expression
    from dcgpy import kernel_set_gdual_vdouble as kernel_set
    from pyaudi import gdual_vdouble as gdual
    import random
    from box import Box
    ######### Problem definition and Cost calculation


    #### Formulae GP Search params   #################
    p = Box(pars_dict)

    ### Problem
    nvars_in      = p.nvars_in  ### nb of variables
    nvars_out     = p.nvars_out
    operator_list = p.get('operators', ["sum", "mul", "div", "diff","sin","cos"])

    ### Log
    print_after   = p.get('print_after', 20)
    print_best    = p.get('print_best', True)
    pop_size      = p.get("pop_size", 5) #20  ## Population (Suggested: 10~20)
    max_iter      = p.get('max_iter', 2) #100000  ## Max iterations
    seed          = p.get('seed', 43)
    log_file      = p.get('log_file', 'log.log') # 'trace.py'

    ### search
    nexp            = p.get('nexp', 100) 
    offsprings      = p.get('offsprings',10)
    max_step        = p.get('stop', 2000)
    symbols         = p.get('symbols',['x0','x1','x2'])
    seed            = p.get('seed', 23)



    from utilmy import os_makedirs
    os_makedirs(log_file)
    def print_file(*s,):
        ss = " ".join([str(x) for x in  s])
        if verbose>0 : print(ss, flush=True)
        with open(log_file, mode='a') as fp :
            fp.write(ss +"\n")



    def run_experiment(max_step, offsprings, dCGP, symbols, verbose=False):
        """Run the Experiment in max_step
        Docs::
            max_step        : Maximum Generations
            offsprings      : Number of offsprings
            dCGP            : dCGP object : hold the formulae
            symbols   : list of variable as string


        """
        chromosome      = [1] * offsprings
        fitness         = [1] * offsprings
        best_chromosome = dCGP.get()
        best_fitness    = 1e10


        for kstep in range(max_step):
            for i in range(offsprings):
                check = 0
                while(check < 1e-3):
                    dCGP.set(best_chromosome)
                    dCGP.mutate_active(i+1) #  we mutate a number of increasingly higher active genes
                    fitness[i], check = problem.get_cost(dCGP, symbols)
                chromosome[i] = dCGP.get()
            #print(fitness)
            for i in range(offsprings):
                if fitness[i] <= best_fitness:
                    if (fitness[i] != best_fitness) and verbose:
                        dCGP.set(chromosome[i])
                        print("New best found: gen: ", kstep, " value: ", fitness[i], " ", dCGP.simplify(symbols))
                    best_chromosome = chromosome[i]
                    best_fitness = fitness[i]
            if best_fitness < 1e-3:
                break

        dCGP.set(best_chromosome)
        return kstep, dCGP


    def search():
        # Search for best possible solution using Genetic Algorithm

        kernels_new = kernel_set(operator_list)()

        #  nexp experiments to accumulate statistic
        result = []
        print("restart: \t gen: \t expr1: \t expr2")
        for i in range(nexp):
            dCGP = expression(inputs=nvars_in, outputs=nvars_out, rows=1, cols=15, levels_back=16, arity=2, kernels=kernels_new, seed = random.randint(0,234213213))
            kstep, dCGP = run_experiment(max_step=max_step, offsprings=10, dCGP=dCGP, symbols=symbols, verbose=False)

            if kstep < (max_step-1):
                form1 = dCGP(symbols)
                form2 = dCGP.simplify(symbols)
                print_file(i, "\t\t", kstep, "\t", form1, "   \t ", form2)

                result.append(form2)

        return result

    res = search()
    return res




###############################################################################################
############ Parallel version #################################################################
def search_formulae_dcgpy_v1_parallel(myproblem=None, pars_dict:dict=None, verbose=False, npool=2 ):
    """Parallel run of search_formulae_dcgpy_v1
    Docs::

        from utilmy.optim import gp_searchformulae as gp
        myproblem1,p = gp.test_pars_values()
        gp.search_formulae_dcgpy_v1_parallel(myproblem=myproblem1, pars_dict=p, verbose=False, npool=3 )


        npool: 2 : Number of parallel runs
    """
    from utilmy.parallel import multiproc_run

    input_list = []
    for i in range(npool):
        p2 = copy.deepcopy(pars_dict)

        fsplit = p2['log_file'].split("/")
        fsplit[-1] = f'trace_{i}.log'
        fi         = "/".join(fsplit)
        p2['log_file'] = fi
        input_list.append(p2)


    ### parallel Run
    multiproc_run(_search_formulae_dcgpy_v1_wrapper,
                  input_fixed={"myproblem": myproblem, 'verbose':False},
                  input_list=input_list,
                  npool=npool)



def _search_formulae_dcgpy_v1_wrapper( pars_dict:dict=None, myproblem=None, verbose=False, ):
    """ Wrapper for parallel version, :
    Docs::

        1st argument should the list of parameters: inverse order
        pars_dict is a list --> pars_dict[0]: actual dict
    """
    search_formulae_dcgpy_v1(myproblem=myproblem, pars_dict=pars_dict[0], verbose=verbose, )




def search_formulae_dcgpy_v1_parallel_island(myproblem, ddict_ref
             , hyper_par_list   = ['pa',  ]  ### X[0],  X[1]
             , hyper_par_bounds = [ [0], [1.0 ] ]
             , pop_size=2
             , n_island=2
             , max_step=1
             , max_time_sec=100
             , dir_log="./logs/"
             ):
    """ Use PYGMO Island model + DCGPY for mutiple parallel Search of formulae
    Docs::

      from utilmy.optim import gp_searchformulae as gp
      myproblem1,p = gp.test_pars_values()
      # p ={}

      #### Run Search
      gp.search_formulae_dcgpy_v1_parallel_island(myproblem1, ddict_ref=p
                       ,hyper_par_list   = [ 'pa',  ]    ### X[0],  X[1]
                       ,hyper_par_bounds = [ [0], [ 0.6 ] ]
                       ,pop_size=6
                       ,n_island=2
                       ,dir_log="./logs/"
                      )

       https://esa.github.io/pygmo2/archipelago.html
       https://esa.github.io/pygmo2/tutorials/coding_udi.html


    """
    os.makedirs(dir_log, exist_ok=True)

    class meta_problem(object):
        def fitness(self,X):
            # ddict = {  'pa': X[0] }
            ddict = {  hyper_par_list[i]:  X[i] for i in range( len(X)) }

            ddict = {**ddict_ref, **ddict}
            (cost, expr) =  search_formulae_dcgpy_v1(myproblem, pars_dict=ddict, verbose=True)   ### Cost

            ss = str(cost) + "," + str(expr)
            #try :
            #  with open(dir_log + "/log.txt", mode='a') as fp:
            #    fp.write(ss)
            #except :
            #    print(ss)

            return [cost]   #### Put it as a list

        def get_bounds(self):
            return hyper_par_bounds
            #return ([0.0]*len(X),[1.0]*len(X))

    import pygmo as pg, time

    prob  = pg.problem( meta_problem() )
    algo  = pg.de(10)  ### Differentail DE
    archi = pg.archipelago(algo = algo, prob =prob , pop_size = pop_size, n= n_island)

    archi.evolve(max_step)

    t0 = time.time()
    isok= True
    while isok :
        # https://esa.github.io/pygmo2/archipelago.html#pygmo.archipelago.status
        #status = archi.status()
        #isok   = True if status not in 'idle' else False
        status = archi.status
        isok   = True if status != pg.evolve_status.idle else False
        if time.time()-t0 > max_time_sec :  isok=False
        time.sleep(30)
    # archi.wait_check()


    ##### Let us inspect the results
    fs = archi.get_champions_f()
    xs = archi.get_champions_x()
    print(fs, xs)

    with open(dir_log +"/result.txt", mode='a') as fp:
        fp.write( "cost_min," + str(fs))
        fp.write( "xmin," + str(xs))
    return fs, xs










###################################################################################################
if __name__ == "__main__":
    import fire
    fire.Fire()

