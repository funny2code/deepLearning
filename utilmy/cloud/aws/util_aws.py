# -*- coding: utf-8 -*-
""" Utils for AWS
Docs::

    https://loige.co/aws-command-line-s3-content-from-stdin-or-to-stdout/


   ### Read from S3
   https://stackoverflow.com/questions/45082832/how-to-read-partitioned-parquet-files-from-s3-using-pyarrow-in-python
   
   
   https://pypi.org/project/smart-open/6.2.0/
   
   
   


"""
import os, sys, time, datetime,inspect,  yaml, gc, pandas as pd, numpy as np, glob
from typing import Union, IO
import boto3

try :
    ## https://anaconda.org/conda-forge/orjson
    ## conda install -c conda-forge orjson     #### pip install orjson
    import orjson as  json  
except :   
    import json


######################################################################################
from utilmy.utilmy_base import log, log2

def help():
    """function help"""
    from utilmy import help_create
    ss = help_create(__file__)
    print(ss)


####################################################################################
def test_all():
    """
    """
    test1()


def test1():
    """function test1

    """    
    data = glob_s3(bucket_name="", path="", recursive=True, max_items_per_api_call="1000", extra_params=[])
    print(json.dumps(data, indent=2))




    
####################################################################################
def s3_read_json(path_s3="", n_workers=1, verbose=True, suffix=".json",   **kw):
    """  Run Multi-processors load using smart_open
    Docs::

         pip install "smart_open[s3]==6.2.0"
         https://github.com/RaRe-Technologies/smart_open/blob/develop/howto.md#how-to-read-from-s3-efficiently 

         If run on Windows operating system, please move freeze_support to the main function
         As suggested here https://docs.python.org/3/library/multiprocessing.html#multiprocessing.freeze_support
    """
    from multiprocessing import freeze_support
    from smart_open import s3

    try :    
       freeze_support()
    except Exception as e : 
       log(e)   

    res_data = {}
    for key, content in s3.iter_bucket(path_s3, workers=n_workers, accept_key=lambda key: key.endswith(suffix)):
        res_data[key] =  json.loads(content)

    return res_data


def s3_get_filelist(path_s3_bucket="/mybucket1/mybucket2/", suffix=".json"):
    # Get all json files in a S3 bucket
    s3         = boto3.resource('s3')
    my_bucket  = s3.Bucket(path_s3_bucket)
    s3_objects = []
    for file in my_bucket.objects.all():
        # filter only json files
        if file.key.lower().find(suffix) != -1:
            s3_objects.append(file.key)
    return s3_objects


def s3_json_read2(path_s3, npool=5, start_delay=0.1, verbose=True, input_fixed:dict=None, suffix=".json",  **kw):
    """  Run Multi-thread json reader for S3 json files, using smart_open in Mutlti Thread
    Doc::

         Return list of tuple  : (S3_path, ddict )

        https://github.com/RaRe-Technologies/smart_open/blob/develop/howto.md#how-to-read-from-s3-efficiently 

        https://github.com/RaRe-Technologies/smart_open
        
        ### stream content *into* S3 (write mode) using a custom session
        import os, boto3
        session = boto3.Session(
            aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
        )
        url = 's3://smart-open-py37-benchmark-results/test.txt'
        with open(url, 'wb', transport_params={'client': session.client('s3')}) as fout:
            bytes_written = fout.write(b'hello world!')
            print(bytes_written)

        ### Buffer writing
        tp = {'min_part_size': 5 * 1024**2}
        with open('s3://bucket/key', 'w', transport_params=tp) as fout:
            fout.write(lots_of_data)            

    """
    import time, functools, json
    from smart_open import open

    ### Global Session, Shared across Threads
    session = boto3.Session()   
    client  = session.client('s3')

    def json_load(s3_path, verbose=True):
        ### Thread Safe function to parallelize
        with open(s3_path, mode='r', transport_params={'client': client} ) as f:
            ddict = json.loads(f)
        return (s3_path, ddict)


    if input_fixed is not None:
        fun_async = functools.partial(json_load, **input_fixed)
    else :
        fun_async= json_load    

    input_list = s3_get_filelist(path_s3, suffix= suffix)


    #### Input xi #######################################
    xi_list = [[] for t in range(npool)]
    for i, xi in enumerate(input_list):
        jj = i % npool
        xi_list[jj].append( xi )  ### xi is already a tuple

    if verbose:
        for j in range(len(xi_list)):
            log('thread ', j, len(xi_list[j]))
        # time.sleep(6)

    #### Pool execute ###################################
    import multiprocessing as mp
    # pool     = multiprocessing.Pool(processes=3)
    pool = mp.pool.ThreadPool(processes=npool)
    job_list = []
    for i in range(npool):
        time.sleep(start_delay)
        log('starts', i)
        job_list.append(pool.apply_async(fun_async, (xi_list[i],) ))
        if verbose: log(i, xi_list[i])

    res_list = []
    for i in range(len(job_list)):
        res_list.append(job_list[i].get())
        log(i, 'job finished')

    pool.close(); pool.join(); pool = None
    log('n_processed', len(res_list))
    return res_list



def s3_json_read3(path_s3, npool=5, start_delay=0.1, verbose=True, input_fixed:dict=None, suffix=".json",  **kw):
    """  Run Multi-thread json reader for S3 json files, using smart_open in Mutlti Thread
    Doc::

         Return list of tuple  : (S3_path, ddict )

        https://github.com/RaRe-Technologies/smart_open/blob/develop/howto.md#how-to-read-from-s3-efficiently 

        https://github.com/RaRe-Technologies/smart_open
        
        ### stream content *into* S3 (write mode) using a custom session
        import os, boto3
        session = boto3.Session(
            aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
        )
        url = 's3://smart-open-py37-benchmark-results/test.txt'
        with open(url, 'wb', transport_params={'client': session.client('s3')}) as fout:
            bytes_written = fout.write(b'hello world!')
            print(bytes_written)

        ### Buffer writing
        tp = {'min_part_size': 5 * 1024**2}
        with open('s3://bucket/key', 'w', transport_params=tp) as fout:
            fout.write(lots_of_data)            

    """
    import json
    from smart_open import open

    ### Global Session, Shared across Threads
    session = boto3.Session()   
    client  = session.client('s3')

    def json_load(s3_path, verbose=True):
        ### Thread Safe function to parallelize
        with open(s3_path, mode='r', transport_params={'client': client} ) as f:
            ddict = json.loads(f)
        return (s3_path, ddict)
  

    input_list  = s3_get_filelist(path_s3, suffix= suffix)

    input_fixed = {'verbose': True}  ### Fixed params


    #### Run Multihreading
    from utilmy import multithread_run
    list_tuple = multithread_run(fun_async= json_load, input_list= input_list,
                                 n_pool= npool, input_fixed= input_fixed)
    return list_tuple



def s3_donwload(path_s3="", n_pool=5, dir_error=None, start_delay=0.1, verbose=True,   **kw):
    """  Run Multi-thread fun_async on input_list.
    Doc::

        # Define where to store artifacts:
        # - temporarily downloaded file and
        # - list of failed to download file in csv file
    """

    # Required library
    from concurrent.futures import ThreadPoolExecutor, as_completed
    from functools import partial
    import os, json, csv
    import boto3
    from smart_open import open


    def load_json(raw_json_data):
        with open(raw_json_data, mode='r') as f:
            data = json.loads(f)
        return data

    def s3_get_filelist(BUCKET):
        """
            Get all json files in a S3 bucket
        """
        s3 = boto3.resource('s3')

        my_bucket = s3.Bucket(BUCKET)
        s3_objects = []
        for file in my_bucket.objects.all():
            # filter only json files
            if file.key.lower().find(".json") != -1:
                s3_objects.append(file.key)
        return s3_objects

    def download_one_file(res_data: dict, bucket: str, client: boto3.client, s3_file: str):
        """ Download a single file from S3
        Args:
            res_data (dict): Store result of our json s3 reading
            bucket (str): S3 bucket where images are hosted
            output (str): Dir to store the images
            client (boto3.client): S3 client
            s3_file (str): S3 object name
        """
        bytes_buffer = io.BytesIO()
        client.download_fileobj(Bucket=bucket, Key=s3_file, Fileobj=bytes_buffer)
        byte_value = bytes_buffer.getvalue()
        res_data[s3_file] = byte_value.decode()


    files_to_download = s3_get_filelist(path_s3)
    # Creating only one session and one client
    session = boto3.Session()
    client = session.client("s3")
    
    res_data = {}

    ## The client is shared between threads
    func = partial(download_one_file, res_data, path_s3, client)


    ## List for storing possible failed downloads to retry later
    failed_downloads = []

    with ThreadPoolExecutor(max_workers=n_pool) as executor:
        # Using a dict for preserving the downloaded file for each future, to store it as a failure if we need that
        futures = {
            executor.submit(func, file_to_download): file_to_download for file_to_download in files_to_download
        }
        for future in as_completed(futures):
            if future.exception():
                failed_downloads.append(futures[future])

    if len(failed_downloads) > 0  and dir_error is not None :
       log(failed_downloads)

    return res_data
 


####################################################################################
def s3_get_filelist_cmd(parent_cmd: list) -> list:
    """ AWS CLI S3 Call by subprocess and get list of  results:
        list of (name, date, size)

    """
    import json
    from subprocess import PIPE, Popen

    files_list = []
    # Run the cmd that we were passed and store the output
    proc = Popen(parent_cmd, stdout=PIPE, stderr=PIPE)
    out, err = proc.communicate()

    # If the cmd exited without error code, continue
    if proc.returncode == 0:

        # Load the output as JSON and add the response to files_list
        output = json.loads(out.decode("utf8"))
        files_list.extend(output["Contents"])

        # If there is a valid NextToken make recursive calls until there isn't
        if output["NextToken"]:

            # Create a copy of parent cmd
            recursive_cmd = parent_cmd[:]

            # If there was a starting token in previous request remove it
            if "--starting-token" in recursive_cmd:
                recursive_cmd.pop(-1)
                recursive_cmd.pop(-1)

            # Add NextToken as starting-token to next cli cmd
            recursive_cmd.extend(["--starting-token", output["NextToken"]])

            # Run the cmd and add the result to files list
            files_list.extend(s3_get_filelist_cmd(recursive_cmd))
    else:
        print("Oh No. An Error Occurred!")
        raise Exception(err.decode("utf8"))

    # Return files_list which contains all data for this
    return files_list



def s3_split_path(s3_path):
    """ path -->  bucket, key
    """
    path_parts=s3_path.replace("s3://","").split("/")
    bucket=path_parts.pop(0)
    key="/".join(path_parts)
    return bucket, key



def glob_s3(path: str, recursive: bool = True,
            max_items_per_api_call: str = 1000,
            fields = "name,date,size",
            return_format='tuple',
            extra_params: list = None) -> list:
    """  Glob files on S3 using AWS CLI

    Docs::

        path: str, recursive: bool = True,
        max_items_per_api_call: str = 1000,
        fields = "name,date,size"
        return_format='tuple'
        extra_params: list = None

        https://bobbyhadz.com/blog/aws-cli-list-all-files-in-bucket



    """        
    bucket_name, path = s3_split_path(path)

    #### {Name: Key, LastModified: LastModified, Size: Size}
    sfield= ""
    if 'name' in fields : sfield += "{Name: Key,"
    if 'date' in fields : sfield += "LastModified: LastModified,"
    if 'size' in fields : sfield += "Size: Size,"   
    sfield += sfield[:-1] + "}"


    # Create cmd to list all objects with default pagination
    cmd = ["aws", "s3api", "list-objects-v2", "--bucket", bucket_name, "--output", "json",
            "--query", "{Contents: Contents[]." + sfield + "  ,NextToken: "
                          "NextToken}"]

    # If pagination is not required, add flag
    if not recursive:
        cmd.append("--no-paginate")
    else:
        # Note : max_items_per_api_call * 1000 is the limit of files that this function can process
        cmd.extend(["--max-items", str(max_items_per_api_call)])

    # If only specific path is needed to be listed, add it
    if path:   cmd.extend(["--prefix", path])

    # If any extra params were passed, add them here
    if extra_params:   cmd.extend(extra_params)

    # run cmd and return files data
    files_data = s3_get_filelist_cmd(cmd)

    if 'tuple' in return_format:
      flist = []
      for xi in files_data :
        xlist = tuple()
        if xi.get("Name", None):          xlist += (xi['Name'],) 
        if xi.get("LastModified", None):  xlist += (xi['LastModified'],)
        if xi.get("Output", None):        xlist += (xi['Output'],)
        flist.append(xlist)
      print(flist)
    else :  
      return files_data



def s3_load_file(s3_path: str, 
                 extra_params: list = None, 
                 return_stream: bool = False, 
                 is_binary: bool = False) -> Union[str, IO, bytes]:
    """ Load file in memory using AWS CLI  --> subprocess --> stdout --> python
    Docs::

          file_data = get_data(s3_path="", extra_params=[])
          
          extra params:
          return_stream:  return as stream data
          is_binary :     return as binary string


          Infos:
             cmd = ["aws", "s3", "cp", s3_path, "-"]

             https://loige.co/aws-command-line-s3-content-from-stdin-or-to-stdout/

             https://aws.amazon.com/blogs/media/processing-user-generated-content-using-aws-lambda-and-ffmpeg/

             https://stackoverflow.com/questions/48725405/how-to-read-binary-data-over-a-pipe-from-another-process-in-python


    """             
    from subprocess import PIPE, Popen

    cmd = ["aws", "s3", "cp", s3_path, "-"]

    # If any extra params were passed, add them here
    if extra_params:   cmd.extend(extra_params)

    # Run cmd
    proc = Popen(cmd, stdout=PIPE, stderr=PIPE)

    # If we need a stream
    if return_stream: return proc.stdout


    # If we need to return the data only
    file_data = ""
    if not is_binary:
        for this_line in iter(proc.stdout.readline, b''):

            # Poll for return code
            proc.poll()
            # If return code exists exit from loop
            if proc.returncode is not None:
                break

            # Decode the binary stream
            this_line_decoded = this_line.decode("utf8")
            if this_line_decoded:
                # In case you want to have stdout as well
                # If removed there will be no indication that we are still receiving the data
                print(this_line_decoded)
                file_data = file_data + "\n" + this_line_decoded
    else:
        for this_bit in iter(proc.stdout.read, b''):
            file_data = bytes()
            print(this_bit, sep="", end="")
            file_data = file_data + this_bit

    # If the process returncode is None and we reach here, start polling for returncode until it exists
    while proc.returncode is None:
        proc.poll()

    # raise exception if error occurred, else return file_data
    if proc.returncode != 0 and proc.returncode is not None:
        _, err = proc.communicate()
        raise Exception(f"Error occurred with exit code {proc.returncode}\n{str(err.decode('utf8'))}")
    elif proc.returncode == 0:
        return file_data








############################################################################################################
if __name__ == '__main__':
    import fire
    fire.Fire()




