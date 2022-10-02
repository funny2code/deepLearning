# -*- coding: utf-8 -*-
import glob
import json
import os
import pathlib
import shutil
import sys
import tarfile
import zipfile
from typing import Optional, Union
import yaml
from loguru import logger





#####################################################################
def load_function(package="mlmodels.util", name="path_norm"):
  """function load_function.
  Get the function of a package.

  Docs::
          
        Args:
            package (string): Package's name. Defaults to "mlmodels.util".
            name (string): Name of the function that belongs to the package.  

        Returns:
            Returns the function of the package.

        Example:
            from utilmy import utils

            function = utils.load_function(
                package="datetime",
                name="timedelta")

            print(function())#0:00:00
    
  """
  import importlib
  return  getattr(importlib.import_module(package), name)



def load_function_uri(uri_name="path_norm"):
    """ Load dynamically function from URI.
    Docs::

        ###### Pandas CSV case : Custom MLMODELS One
        #"dataset"        : "mlmodels.preprocess.generic:pandasDataset"
    
        ###### External File processor :
        #"dataset"        : "MyFolder/preprocess/myfile.py:pandasDataset"

        Args:
            uri_name (string): URI of the function to get.
        
        Returns:
            Returns the function with the given URI.

        Example:
            from utilmy import utils

            function = utils.load_function_uri(uri_name="datetime:timedelta")

            print(function()) #0:00:00


    """
    
    import importlib, sys
    from pathlib import Path
    pkg = uri_name.split(":")

    assert len(pkg) > 1, "  Missing :   in  uri_name module_name:function_or_class "
    package, name = pkg[0], pkg[1]
    
    try:
        #### Import from package mlmodels sub-folder
        return  getattr(importlib.import_module(package), name)

    except Exception as e1:
        try:
            ### Add Folder to Path and Load absoluate path module
            path_parent = str(Path(package).parent.parent.absolute())
            sys.path.append(path_parent)
            #log(path_parent)

            #### import Absolute Path model_tf.1_lstm
            model_name   = Path(package).stem  # remove .py
            package_name = str(Path(package).parts[-2]) + "." + str(model_name)
            #log(package_name, model_name)
            return  getattr(importlib.import_module(package_name), name)

        except Exception as e2:
            raise NameError(f"Module {pkg} notfound, {e1}, {e2}")


def load_callable_from_uri(uri):
    """function load_callable_from_uri.
    Doc::
            
            Args:
                uri:   
            Returns:
                
    """
    assert(len(uri)>0 and ('::' in uri or '.' in uri))
    if '::' in uri:
        module_path, callable_name = uri.split('::')
    else:
        module_path, callable_name = uri.rsplit('.',1)
    if os.path.isfile(module_path):
        module_name = '.'.join(module_path.split('.')[:-1])
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    else:
        module = importlib.import_module(module_path)
    return dict(getmembers(module))[callable_name]
        

def load_callable_from_dict(function_dict, return_other_keys=False):
    """function load_callable_from_dict.
    Doc::
            
            Args:
                function_dict:   
                return_other_keys:   
            Returns:
                
    """
    function_dict = function_dict.copy()
    uri = function_dict.pop('uri')
    func = load_callable_from_uri(uri)
    try:
        assert(callable(func))
    except:
        raise TypeError(f'{func} is not callable')
    arg = function_dict.pop('arg', {})
    if not return_other_keys:
        return func, arg
    else:
        return func, arg, function_dict
    



#####################################################################
def test_all():
    """.
    Doc::
            
            #### python test.py   test_utils
    """
    def test_logs(): 
        from utilmy.utils import log,log2, logw, loge, logger_setup
        print("testing logs utils........")
        logger_setup()
        log("simple log ")
        log2("debug log")
        logw("warning log")
        loge("error log")
    
    def config_load_test():
        from utilmy.utils import config_load
        config_load()
    
    def dataset_download_test():
        from utilmy.utils import dataset_donwload
        dataset_donwload("https://github.com/arita37/mnist_png/raw/master/mnist_png.tar.gz", './testdata/tmp/test/dataset/')
    
    def os_extract_archive_test():
        from utilmy.utils import os_extract_archive
        os_extract_archive("./testdata/tmp/test/dataset/mnist_png.tar.gz","./testdata/tmp/test/dataset/archive/", archive_format = "auto")
    
    def to_file_test():
        from utilmy.utils import to_file
        to_file("to_file_test_str", "./testdata/tmp/test/to_file.txt")

    test_logs()
    config_load_test()
    dataset_download_test()
    os_extract_archive_test()
    to_file_test()


def test0(): 
    """function test0.
    Doc::
            
            Args:
            Returns:
                
    """
    logger_setup()
    log("simple log ")
    log2("debug log")
    logw("warning log")
    loge("error log")
    
def test1():
    """function test1.
    Doc::
            
            Args:
            Returns:
                
    """
    import utilmy as uu
    drepo, dirtmp = uu.dir_testinfo()

    config_load()

    
    log("####### config_load() ..")
    # TODO: This test has a bug
    # Testing config_load with a custom yaml file.
    # test_path = drepo + "testdata/tmp/test/"
    # test_file_path = test_path + "config.yaml"
    # test_text = '{"testing": "testing",}'
    # expected_response = dict(testing="testing")
    # uu.to_file(test_text, test_file_path)
    # config_load_response = config_load()
    # assert config_load_response == expected_response, "The config isn't the expected"
    # Error's output: Cannot read yaml file /home/necromancer/Documents/programming/Jobs/Freelancer/pythontests/myutil/testdata/tmp/test/config.yaml,'str' object has no attribute 'read_text'
    # Error's reason: The string that has the path of the existing yaml file, is expected to have the method named "read_text".
    # This method exists in the objects "pathlib.PosixPath", When we give a value to the parameter "config_path", it won't have the value of the variable "config_path_default",
    # Which it is an object "pathlib.PosixPath", therefore, "config_path" won't be an object "pathlib.PosixPath", but will be an string.


    dataset_donwload("https://github.com/arita37/mnist_png/raw/master/mnist_png.tar.gz", './testdata/tmp/test/dataset/')
    os_extract_archive("./testdata/tmp/test/dataset/mnist_png.tar.gz","./testdata/tmp/test/dataset/archive/", archive_format = "auto")
    to_file("to_file_test_str", "./testdata/tmp/test/to_file.txt")

##########################################################################################
################### Logs Wrapper #########################################################
def log(*s):
    """function log.
    Doc::
            
            Args:
                *s:   
            Returns:
                
    """
    logger.info(",".join([str(t) for t in s]))


def log2(*s):
    """function log2.
    Doc::
            
            Args:
                *s:   
            Returns:
                
    """
    logger.debug(",".join([str(t) for t in s]))


def logw(*s):
    """function logw.
    Doc::
            
            Args:
                *s:   
            Returns:
                
    """
    logger.warning(",".join([str(t) for t in s]))


def loge(*s):
    """function loge.
    Doc::
            
            Args:
                *s:   
            Returns:
                
    """
    logger.error(",".join([str(t) for t in s]))


def logger_setup():
    """function logger_setup.
    Doc::
            
            Args:
            Returns:
                
    """
    config = {
        "handlers": [
            {
                "sink": sys.stdout,
                "format": "<level>{level: <8}</level>| <level>{message}</level>",
            }
        ]
    }
    logger.configure(**config)


logger_setup()


##########################################################################################
################### donwload  ############################################################
def config_load(config_path: Optional[Union[str, pathlib.Path]] = None):
    """Load Config file into a dict.
    Doc::
            
            1) load config_path
            2) If not, load in HOME USER
            3) If not, create default one
            # config_default = yaml.load(os.path.join(os.path.dirname(__file__), 'config', 'config.yaml'))
        
            Args:
                config_path: path of config or 'default' tag value
            Returns: dict config
    """
    path_default = pathlib.Path.home() / ".mygenerator"
    config_path_default = path_default / "config.yaml"
    config_default = {
        "current_dataset": "mnist",
        "datasets": {
            "mnist": {
                "url": "https://github.com/arita37/mnist_png/raw/master/mnist_png.tar.gz",
                "path": str(path_default / "mnist_png" / "training"),
            }
        },
    }

    ##################################################################
    if config_path is None or config_path == "default":
        logw(f"Using config: {config_path_default}")
        config_path = config_path_default

    try:
        log2("loading config", config_path)
        return yaml.load(config_path.read_text(), Loader=yaml.Loader)
    except Exception as e:
        logw(f"Cannot read yaml file {config_path}", e)

    logw("#### Using default configuration")
    log2(config_default)
    log(f"Creating default config file in {config_path}")
    os.makedirs(path_default, exist_ok=True)
    with open(config_path, mode="w") as fp:
        json.dump(config_default, fp)
    return config_default





##########################################################################################
################### donwload  ############################################################
def dataset_donwload(url, path_target):
    """Donwload on disk the tar.gz file.
    Docs::
            
        Args:
            url (string): File's URL to download.
            path_target (string): Folder's path to save the file.

        Returns:
            string: Full path of the saved file.

        Example:
            from utilmy import utils

            url = "{url of the file}"
            path_target = "/home/username/Desktop/example"

            full_path = utils.dataset_donwload(
                url=url, 
                path_target=path_target)

            print(full_path)

    """
    import wget
    log(f"Donwloading mnist dataset in {path_target}")
    os.makedirs(path_target, exist_ok=True)
    wget.download(url, path_target)
    tar_name = url.split("/")[-1]
    os_extract_archive(path_target + "/" + tar_name, path_target)
    log2(path_target)
    return path_target + tar_name

  

def os_extract_archive(file_path, path=".", archive_format="auto"):
    """Extracts an archive if it matches tar, tar.gz, tar.bz, or zip formats..
    
    Docs::
                
        Args:
            file_path (string): path to the archive file
            path (string): path to extract the archive file
            archive_format (string): Archive format to try for extracting the file.
                Options are 'auto', 'tar', 'zip', and None.
                'tar' includes tar, tar.gz, and tar.bz files.
                The default 'auto' is ['tar', 'zip'].
                None or an empty list will return no matches found.
        Returns:
            True if a match was found and an archive extraction was completed,
            False otherwise.

        Example:
        from utilmy import utils

        is_extracted = utils.os_extract_archive(
            file_path="/home/necromancer/Desktop/example.zip",
            path="/home/necromancer/Desktop/testingfolder")

        print(is_extracted)#Displays true if the match was found

    """
    if archive_format is None:
        return False
    if archive_format == "auto":
        archive_format = ["tar", "zip"]
    if isinstance(archive_format, str):
        archive_format = [archive_format]

    file_path = os.path.abspath(file_path)
    path = os.path.abspath(path)

    for archive_type in archive_format:
        if archive_type == "tar":
            open_fn = tarfile.open
            is_match_fn = tarfile.is_tarfile
        if archive_type == "zip":
            open_fn = zipfile.ZipFile
            is_match_fn = zipfile.is_zipfile

        if is_match_fn(file_path):
            with open_fn(file_path) as archive:
                try:
                    archive.extractall(path)
                except (tarfile.TarError, RuntimeError, KeyboardInterrupt):
                    if os.path.exists(path):
                        if os.path.isfile(path):
                            os.remove(path)
                        else:
                            shutil.rmtree(path)
                    raise
            return True
    return False


def to_file(s, filep):
    """function to_file.
    
    Write the argument "s" in a file.

    Docs::
            
        Args:
            s (string): string to write in the file.    
            filep (string): Path of the file to write.
        
        Returns:
            None.

        Example:
            from utilmy import utils

            filep = "/home/username/Desktop/example/test"

            string = "Test string"

            result = utils.to_file(s=string, filep=filep)

            print(result)#It prints "None", but the file has the text.

    """
    with open(filep, mode="a") as fp:
        fp.write(str(s) + "\n")
