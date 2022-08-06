def multi_glob(paths, n_pool=3):
    """ Get list of files for multiple folders using multiprocessing
    Docs::
        takes a list of strings which contain the paths of the folders to scan
        returns a list of lists which contain the paths of discovered files
    """
    from multiprocessing import Pool
    from utilmy.multiglobHelper import helper #needs to be contained in a seperate file
    
    print(n_pool)
    with Pool(n_pool) as p:
        out = p.map(helper, paths)
    return(out)