""" Command Line for utilmy.
Doc::

        utilmy   gpu_usage
        utilmy   gpu_available




"""
HELP1 ="""
utilmy  init

utilmy  help

$utilmy/images/util_image.py image_remove_background 


"""
import fire, argparse, os, sys


#############################################################################################
def log(*s):
    """function log"""
    print(*s, flush=True)


#############################################################################################
try :
   import utilmy 
   dir_utilmy =  utilmy.__path__[0].replace("\\","/")  + "/"
except:   
   dir_utilmy = os.path.dirname(os.path.abspath(__file__)).replace("\\","/") 



#############################################################################################
def run_cli():
    """ utilmy command line
    Doc::

        utilmy   gpu_usage
        utilmy   gpu

        utilmy   show   myfile.parquet




    """
    import argparse
    from utilmy.utilmy import os_system    
    p   = argparse.ArgumentParser()
    add = p.add_argument

    add('task',  metavar='task',  type=str,  nargs="?", help='gpu,gpu_usage')
    add('arg2', metavar='arg2', type=str, nargs="?", help='')
    add('arg3', metavar='arg3', type=str, nargs="?", help='')


    add("--dirin",    type=str, default='gpu',     help = "repo_url")
    add("--repo_dir",    type=str, default="./",     help = "repo_dir")
    add("--dirout",     type=str, default="docs/",  help = "doc_dir")
    add("--out_file",     type=str, default="",      help = "out_file")
    add("--exclude_dir", type=str, default="",       help = "path1,path2")
    add("--prefix",      type=str, default=None,     help = "hdops://github.com/user/repo/tree/a")
    add("--verbose",      type=int, default=0,     help = "hdops://github.com/user/repo/tree/a")
  
    args = p.parse_args()
    do = args.task

    if args.verbose > 0 : log(dir_utilmy)

    if do == 'gpu_usage': 
        ss=  os_system( f"python {dir_utilmy}/deeplearning/util_dl.py   gpu_usage", doprint=True)

    if do == 'gpu': 
        ss = os_system( f"python {dir_utilmy}/deeplearning/util_dl.py   gpu_available",doprint=True)
        # log(ss[0])

    if do == 'show':
        ss = os_system( f"{dir_utilmy}/ppandas.py  pd_check_file  --dirin '{args.arg2}'  ",doprint=True)
        log(ss)

    if do == 'find': 
        os_system( f"{dir_utilmy}/oos.py  os_find_infile   --pattern  '{args.arg2}' --dirin '{args.arg3}'  ")


    if do == 'help':
        print(HELP1)

    if do == 'init':
        pass

    if do == 'colab':
        from utilmy import util_colab as mm
        mm.help()


    if "utilmy." in do or "utilmy/" in do :
        from utilmy.utilmy import load_function_uri
        uri = do.replace(".", "/")  ### "utilmy.ppandas::test"
        dirfile  = "utilmy/" + do if 'utilmy/' not in do else do
        fun_name = args.task

        cmd = f"{dir_utilmy}/{dirfile}  {fun_name}  "
        os.system(cmd)






#############################################################################################



###################################################################################################
if __name__ == "__main__":
    run_cli()
    # fire.Fire()


