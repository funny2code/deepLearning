HELP= """ Utils for easy batching




"""
import os, sys, socket, platform, time, gc,logging, random, datetime, logging

from utilmy.utilmy_base import date_now

################################################################################################
verbose = 3   ### Global setting
from utilmy import log, log2




################################################################################################
def test_all():
    """function test_all
    """
    test1()

    test_os_process_find_name()
    test_index()



def test_functions():
    """Check that list function is working.
    os_lock_releaseLock, os_lock_releaseLock, os_lock_run
    Basic test on only 1 thread
    """
    # test function
    def running(fun_args):
        log(f'Function running with arg: {fun_args}')

    # test that os_lock_run is working
    os_lock_acquireLock(running, 'Test_args', plock='tmp/plock.lock')
    os_lock_acquireLock(running, [1, 2, 3], plock='tmp/plock.lock')



def test_funtions_thread():
    """Check that list function is working.
    Docs::

        os_lock_releaseLock, os_lock_releaseLock, os_lock_run
        Multi threads
        How the test work.
        - Create and run 5 threads. These threads try to access and use 1 function `running`
        with os_lock_run. So in one 1, only 1 thread can access and use this function.
    """
    import threading

    # define test function
    def running(fun_args):
        log(f'Function running in thread: {fun_args} START')
        time.sleep(fun_args* 0.2)
        log(f'Function running in thread: {fun_args} END')

    # define test thread
    def thread_running(number):
        log(f'Thread {number} START')
        os_lock_acquireLock(running, number, plock='tmp/plock2.lock')
        log(f'Thread {number} sleeping in {number*3}s')
        time.sleep(number* 0.5)
        log(f'Thread {number} END')

    # Create thread
    for i in range(3):
        t = threading.Thread(target=thread_running, args=(i+1, ))
        t.start()


def test_index():
    """Check that class IndexLock is working
    Multi threads
    How the test work.
    - The test will create the INDEX with the file using plock
    - Create 100 threads that try to write data to this INDEX file lock
    - This test will make sure with this INDEX file log
        only 1 thread can access and put data to this file.
        Others will waiting to acquire key after thread release it.
    """
    import threading
    import os

    file_name = "./test.txt"
    #file_lock = "tmp/plock3.lock"

    def remove_file(file_name):
        if os.path.exists(file_name):
            os.remove(file_name)

    remove_file(file_name)
    INDEX = IndexLock(file_name, file_lock=None)

    # 1. Normal put get string
    log("------------------------ Test put string ------------------------")
    str_test = "The quick brown fox jumps over the lazy dog"
    log(INDEX.put(str_test))
    log(INDEX.get())
    assert str_test in INDEX.get(), "[FAILED] Put string"

    #. 2 Normal put get array of string
    log("------------------------ Test put array ------------------------")
    data_test = (
        "The earliest known appearance of the phrase is from",
        "favorite copy set by writing teachers for their pupils",
        "Computer usage",
        "Cultural references",
    )
    log(INDEX.put(data_test))
    log(INDEX.get())
    for string in data_test:
        assert string in INDEX.get(), "[FAILED] Put list array"

    # 3. Test the comment tring will be ignore when get data
    log("------------------------ Test put comments ------------------------")
    str_test = "# References"
    INDEX.put(str_test)
    log(INDEX.get())
    assert str_test not in INDEX.get(), "[FAILED] Comment string should be ignored"

    # 4. min size
    log("------------------------ Test put small size ------------------------")
    str_test = "zxcv"
    INDEX.put(str_test)
    log(INDEX.get())
    assert str_test not in INDEX.get(), "[FAILED] small siZe should be ignored"

    # 5. Try to put same data.
    log("------------------------ Test put duplicated string ------------------------")
    str_test = "Numerous references to the phrase have occurred in movies"
    put1 = INDEX.put(str_test)
    assert put1 == [str_test], "[FAILED] Put string"
    put2 = INDEX.put(str_test)
    assert put2 == []
    log(INDEX.get())
    assert str_test in INDEX.get(), "[FAILED] Put duplicated string"


    log("------------------------ Test threads ------------------------")
    # 6. Multi threads with IndexLock
    # define test thread
    def thread_running(number):
        log(f'Thread {number} START')
        INDEX.put(f'Thread {number}')
        INDEX.save_filter(f'Thread {number}')
        log( INDEX.get() )
        assert f'Thread {number}' in INDEX.get(), "[FAILED] Put string"
        log(f'Thread {number} END')

    # Create thread
    for i in range(5):
        t = threading.Thread(target=thread_running, args=(i+1, ))
        t.start()


def test_os_process_find_name():
    """function test_os_process_find_name
    Args:
    Returns:
        
    """
    # check name with re
    print(os_process_find_name(name="*util_batch.py"))
    # check name without re
    print(os_process_find_name(name="util_batch", isregex=0))

    # test with fnmatch
    print(os_process_find_name(name='*bash*'))
    print(os_process_find_name(name='*.py'))
    print(os_process_find_name(name='python*'))


def test1():
    
    # TODO: This test has a bug
    log("#######   now_weekday_isin()...")
    # timezone = datetime.timezone.utc
    # now_weekday = (datetime.datetime.now(timezone).weekday() + 1) % 7
    # is_week_in = now_weekday_isin(day_week=[now_weekday], timezone="utc")
    # assert is_week_in == True, "This isn't correct weekday"

    # TODO: This test has a bug
    log("#######   now_hour_between()...")
    # UTC time now.
    # timezone = datetime.timezone.utc
    # now_hour = datetime.datetime.now(tz=timezone)
    # format_time = "%H:%M"
    # Hours with 1 hour more and 1 hour less difference.
    # first_hour = (now_hour + datetime.timedelta(hours=1)).time().strftime("%H:%M")
    # second_hour = (now_hour + datetime.timedelta(hours=-1)).strftime("%H:%M")
    # is_hour_between = now_hour_between(
    #     hour1=first_hour,
    #     hour2=second_hour,
    #     timezone="utc"
    # )
    # assert is_hour_between == True, "Now hour isn't between"

    # TODO: This test has a bug.
    log("#######   now_daymonth_isin()...")
    # timezone = datetime.timezone.utc
    # now_day_month = datetime.datetime.now(tz=timezone).day
    # is_daymonth_in = now_daymonth_isin(
    #     day_month=[now_day_month],
    #     timezone=timezone
    #     )
    # assert is_daymonth_in == True, "The day month isn't in"





########################################################################################
##### Date #############################################################################
def now_weekday_isin(day_week=None, timezone='jp'):
    """Check if today is in the list of weekday numbers.
    Docs::
    
        true if now() is in the list of weekday numbers, false if not

        Args:
            day_week          :  [1,2,3],  0 = Sunday, 1 = Monday, ...   6 = Saturday           
            timezone (string) :  Timezone :  'UTC', 'Asia/Tokyo'
            
    """
    # 0 is sunday, 1 is monday
    if not day_week:
        day_week = {0, 1, 2,4,5,6}

    # timezone = {'jp' : 'Asia/Tokyo', 'utc' : 'utc'}.get(timezone, 'utc')
    
    now_weekday = (datetime.datetime.now(tz=tzone(timezone)).weekday() + 1) % 7
    if now_weekday in day_week:
        return True
    return False


def now_hour_between(hour1="12:45", hour2="13:45", timezone="jp"):
    """Check if the time is between   hour1 <  current_hour_time_zone < hour2
    Docs::

        Args:
            hour1 (string):     start format "%H:%M",  "12:45".
            hour2 (string):     end,  format "%H:%M",  Default to "13:45".
            timezone (string):  'Asia/Tokyo', 'utc' 
                
        Returns:  true if the time is between two hours, false otherwise.
            
    """
    # Daily Batch time is between 2 time.
    # timezone = {'jp' : 'Asia/Tokyo', 'utc' : 'utc'}.get(timezone, 'utc')
    format_time = "%H:%M"
    hour1 = datetime.datetime.strptime(hour1, format_time).time()
    hour2 = datetime.datetime.strptime(hour2, format_time).time()
    now_weekday = datetime.datetime.now(tz=tzone(timezone)).time()
    if hour1 <= now_weekday <= hour2:
        return True
    return False


def now_daymonth_isin(day_month, timezone="jp"):
    """function now_daymonth_isin

    Check if today is in a List of days of the month in numbers 
    
    Docs::

        Args:
            day_month (:obj:`list` of :obj:'int'): List of days of the month in numbers to check if today is in this list.
            timezone (string): Timezone of time now.
                Default to "jp".  
        
        Returns:
            Boolean, true if today is in the list "day_month", false otherwise.

    """
    # 1th day of month
    timezone = {'jp' : 'Asia/Tokyo', 'utc' : 'utc'}.get(timezone, 'utc')

    if not day_month:
        day_month = [1]

    now_day_month = datetime.datetime.now(tz=tzone(timezone)).day

    if now_day_month in day_month:
        return True
    return False


def time_sleep(nmax=5, israndom=True):
    """function time_sleep_random

    Time sleep function with random feature.
    
    Docs::

        Args:
            nmax (int): Number of seconds for the time sleep.
                Default to 5.   
            israndom (boolean): True if the argument "nmax" is the max number of second to be chosen randomly.
                Default to True.

        Returns: None.
        
        Example:
            from utilmy import util_batch
            import datetime

            timezone = datetime.timezone.utc
            now_day_month = datetime.datetime.now(tz=timezone).day

            util_batch.time_sleep(nmax = 10, israndom=False)
    """
    import random, time
    if israndom:
       time.sleep( random.randrange(nmax) )
    else :
       time.sleep( nmax )


        

####################################################################################################
####################################################################################################
def batchLog(object):    
    """function batchLog
    Args:
        object:   
    Returns:
        
    """
    def __init__(self,dirlog="log/batch_log", use_date=True, tag="", timezone="jp"):
        """  Log on file when task is done and Check if a task is done.
           Log file format:
           dt\t prog_name\t name \t tag \t info
        
        """
        today = date_now(fmt="%Y%m%d")
        self.dirlog = dirlog + f"/batchlog_{tag}_{today}.log"
        
    
    def save(self, msg,   **kw):    
        """  Log on file , termination of file
             Thread Safe writing.    
            dt\t prog_name\t name \t tag \t info
            
            One file per day

        """
        ### Thread Safe logging on disk
        pass


    def isdone(self, name="*" ):
        """  Find if a task was done or not.
        """
        flist = self.getall( date="*" )
        for fi in flist :
            if name in fi : #### use regex
                return True
        return False             

    
    def getall(self, date="*" ):
        """  get the log
        """
        with open(self.dirlog, mode='r') as fp:
            flist = fp.readlines()
            
        flist2 = []    
        for  fi in flist :
            if fi[0] == "#" or len(fi) < 5 : continue
            flist2.append(fi)            
        return flist2



#########################################################################################
def os_wait_filexist(flist, sleep=300):
    """function os_wait_filexist
    Args:
        flist:   
        sleep:   
    Returns:
        
    """
    import glob, time
    nfile = len(flist)
    ii = -1
    while True:
       ii += 1
       kk = 0
       if ii % 10 == 0 :  log("Waiting files", flist)        
       for fi in flist :
            fj = glob.glob(fi) #### wait
            if len(fj)> 0:
                kk = kk + 1
       if kk == nfile: break
       else : time.sleep(sleep)



def os_wait_fileexist2(dirin, ntry_max=100, sleep_time=300): 
    """function os_wait_fileexist2
    Args:
        dirin:   
        ntry_max:   
        sleep_time:   
    Returns:
        
    """
    import glob, time
    log('####### Check if file ready', "\n", dirin,)
    ntry=0
    while ntry < ntry_max :
       fi = glob.glob(dirin )
       if len(fi) >= 1: break
       ntry += 1
       time.sleep(sleep_time)    
       if ntry % 10 == 0 : log('waiting file') 
    log('File is ready:', dirin)    




def os_wait_cpu_ram_lower(cpu_min=30, sleep=10, interval=5, msg= "", name_proc=None, verbose=True):
    """function os_wait_cpu_ram_lower
    Args:
        cpu_min:   
        sleep:   
        interval:   
        msg:   
        name_proc:   
        verbose:   
    Returns:
        
    """
    #### Wait until Server CPU and ram are lower than threshold.    
    #### Sleep until CPU becomes normal usage
    import psutil, time

    if name_proc is not None :   ### If process not in running ones
        flag = True
        while flag :
            flag = False
            for proc in psutil.process_iter():
               ss = " ".join(proc.cmdline())
               if name_proc in ss :
                    flag = True
            if flag : time.sleep(sleep)

    aux = psutil.cpu_percent(interval=interval)  ### Need to call 2 times
    while aux > cpu_min:
        ui = psutil.cpu_percent(interval=interval)
        aux = 0.5 * (aux +  ui)
        if verbose : log( 'Sleep sec', sleep, ' Usage %', aux, ui, msg )
        time.sleep(sleep)
    return aux



def os_process_find_name(name=r"((.*/)?tasks.*/t.*/main\.(py|sh))", ishow=1, isregex=1):
    """ Return a list of processes matching 'name'.
        Regex (./tasks./t./main.(py|sh)|tasks./t.*/main.(py|sh))
        Condensed Regex to:
        ((.*/)?tasks.*/t.*/main\.(py|sh)) - make the characters before 'tasks' optional group.
    """
    import psutil, re, fnmatch
    ls = []

    re_name = fnmatch.translate(name)
    for p in psutil.process_iter(["pid", "name", "exe", "cmdline"]):
        cmdline = " ".join(p.info["cmdline"]) if p.info["cmdline"] else ""
        if isregex:
            flag = re.match(re_name, cmdline, re.I)
        else:
            flag = name and name.lower() in cmdline.lower()

        if flag:
            ls.append({"pid": p.info["pid"], "cmdline": cmdline})

            if ishow > 0:
                log("Monitor", p.pid, cmdline)
    return ls



def os_wait_program_end(cpu_min=30, sleep=60, interval=5, msg= "", program_name=None, verbose=True):
    """function os_wait_program_end
    Args:
        cpu_min:   
        sleep:   
        interval:   
        msg:   
        program_name:   
        verbose:   
    Returns:
        
    """
    #### Sleep until CPU becomes normal usage
    import psutil, time

    if program_name is not None :   ### If process not in running ones
        flag = True
        while flag :
            flag = False
            for proc in psutil.process_iter():
               ss = " ".join(proc.cmdline())
               if program_name in ss :
                    flag = True
            if flag : time.sleep(sleep)

    aux = psutil.cpu_percent(interval=interval)  ### Need to call 2 times
    while aux > cpu_min:
        ui = psutil.cpu_percent(interval=interval)
        aux = 0.5 * (aux +  ui)
        if verbose : log( 'Sleep sec', sleep, ' Usage %', aux, ui, msg )
        time.sleep(sleep)
    return aux





#########################################################################################################
####### Atomic File writing ##############################################################################
class toFile(object):
   def __init__(self,fpath):
      """
       Thread Safe file writer
      """
      logger = logging.getLogger('log')
      logger.setLevel(logging.INFO)
      ch = logging.FileHandler(fpath)
      ch.setFormatter(logging.Formatter('%(message)s'))
      logger.addHandler(ch)
      self.logger = logger

   def write(self, msg):
        """ toFile:write
        Args:
            msg:     
        Returns:
           
        """
        self.logger.info( msg)


def to_file_safe(msg:str, fpath:str):
   """function to_file_safe
   Args:
       msg ( str ) :   
       fpath ( str ) :   
   Returns:
       
   """
   ss = str(msg)
   logger = logging.getLogger('log')
   logger.setLevel(logging.INFO)
   ch = logging.FileHandler(fpath)
   ch.setFormatter(logging.Formatter('%(message)s'))
   logger.addHandler(ch)

   logger.info( ss)



#########################################################################################################
####### Atomic File Index  read/writing #################################################################
class IndexLock(object):
    """Keep a Global Index of processed files.
      INDEX = IndexLock(findex)
      flist = index.save_isok(flist)  ## Filter out files in index and return available files
      ### only process correct files
      
    """
    ### Manage Invemtory Index with Atomic Write/Read
    def __init__(self, findex, file_lock=None, min_size=5, skip_comment=True, ntry=20):
        """ IndexLock:__init__
        Args:
            findex:     
            file_lock:     
            min_size:     
            skip_comment:     
            ntry:     
        Returns:
           
        """
        self.findex= findex
        os.makedirs(os.path.dirname( os.path.abspath(self.findex)), exist_ok=True)

        if file_lock is None:
            file_lock = os.path.dirname(findex) +"/"+ findex.split("/")[-1].replace(".", "_lock.")
        self.plock = file_lock

        ### Initiate the file
        if not os.path.isfile(self.findex):
            with open(self.findex, mode='a') as fp:
                fp.write("")

        self.min_size=min_size
        self.skip_comment=True
        self.ntry =ntry


    def read(self,): ### alias
        """ IndexLock:read
        Args:
            :     
        Returns:
           
        """
        """ IndexLock:save_isok
        Args:
            flist (function["arg_type"][i]) :     
        Returns:
           
        """
    def save_filter(self, val:list=None):
        """ IndexLock:save_filter
        Args:
            val (function["arg_type"][i]) :     
        Returns:
           
        """
        return self.put(val)


    ######################################################################
    def get(self, **kw):
        """ IndexLock:get
        Args:
            **kw:     
        Returns:
           
        """
        ## return the list of files
        with open(self.findex, mode='r') as fp:
            flist = fp.readlines()

        if len(flist) < 1 : return []

        flist2 = []
        for t  in flist :
            if len(t.strip()) < self.min_size: continue
            if self.skip_comment and t[0] == "#"  : continue
            flist2.append( t.strip() )
        return flist2


    def put(self, val:list=None):
        """ Read, check if the insert values are there, and save the files
          flist = index.check_filter(flist)   ### Remove already processed files
          if  len(flist) < 1 : continue   ### Dont process flist
          ### Need locking mechanism Common File to check for Check + Write locking.
        """
        import random, time
        if val is None : return True

        if isinstance(val, str):
            val = [val]

        i = 1
        while i < self.ntry :
            try :
                lock_fd = os_lock_acquireLock(self.plock)

                ### Check if files exist  #####################
                fall =  self.read()
                val2 = [] ; isok= True
                for fi in val:
                    if fi in fall :
                        log('exist in Index, skipping', fi)
                        isok =False
                    else :
                        val2.append(fi)

                if len(val2) < 1 : return []

                #### Write the list of files on Index: Wont be able to use by other processes
                ss = ""
                for fi in val2 :
                  x  = str(fi)
                  ss = ss + x.strip() + "\n"

                with open(self.findex, mode='a') as fp:
                    fp.write( ss )

                os_lock_releaseLock(lock_fd)
                return val2

            except Exception as e:
                log2(e)
                log2(f"file lock waiting {i}s")
                time.sleep( random.random() * i )
                i += 1



class Index0(object):
    """
    ### to maintain global index, flist = index.read()  index.save(flist)
    """
    def __init__(self, findex:str="ztmp_file.txt", ntry=10):
        """ Index0:__init__
        Args:
            findex (function["arg_type"][i]) :     
            ntry:     
        Returns:
           
        """
        self.findex = findex
        os.makedirs(os.path.dirname(self.findex), exist_ok=True)
        if not os.path.isfile(self.findex):
            with open(self.findex, mode='a') as fp:
                fp.write("")

        self.ntry= ntry

    def read(self,):
        """ Index0:read
        Args:
            :     
        Returns:
           
        """
        import time
        try :
           with open(self.findex, mode='r') as fp:
              flist = fp.readlines()
        except:
           time.sleep(5)
           with open(self.findex, mode='r') as fp:
              flist = fp.readlines()


        if len(flist) < 1 : return []
        flist2 = []
        for t  in flist :
            if len(t) > 5 and t[0] != "#"  :
              flist2.append( t.strip() )
        return flist2

    def save(self, flist:list):
        """ Index0:save
        Args:
            flist (function["arg_type"][i]) :     
        Returns:
           
        """
        if len(flist) < 1 : return True
        ss = ""
        for fi in flist :
          ss = ss + fi + "\n"
        with open(self.findex, mode='a') as fp:
            fp.write(ss )
        return True


    def save_filter(self, val:list=None):
        """
          isok = index.save_isok(flist)
          if not isok : continue   ### Dont process flist
          ### Need locking mechanism Common File to check for Check + Write locking.
        """
        import random, time
        if val is None : return True

        if isinstance(val, str):
            val = [val]

        i = 1
        while i < self.ntry :
            try :
                ### Check if files exist  #####################
                fall =  self.read()
                val2 = [] ; isok= True
                for fi in val:
                    if fi in fall :
                        log('exist in Index, skipping', fi)
                        isok =False
                    else :
                        val2.append(fi)

                if len(val2) < 1 : return []

                #### Write the list of files on disk
                ss = ""
                for fi in val2 :
                  x  = str(fi)
                  ss = ss + x + "\n"

                with open(self.findex, mode='a') as fp:
                    fp.write( ss )

                return val2

            except Exception as e:
                log(f"file lock waiting {i}s")
                time.sleep( random.random() * i )
                i += 1



#####################################################################################################
######  Atomic Execution ############################################################################
def os_lock_acquireLock(plock:str="tmp/plock.lock"):
    ''' acquire exclusive lock file access, return the locker
    '''
    import fcntl
    os.makedirs(os.path.dirname(os.path.abspath(plock)), exist_ok=True)
    locked_file_descriptor = open( plock, 'w+')
    fcntl.flock(locked_file_descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
    return locked_file_descriptor


def os_lock_releaseLock(locked_file_descriptor):
    ''' release exclusive lock file access '''
    import fcntl
    fcntl.flock(locked_file_descriptor, fcntl.LOCK_UN)
    # locked_file_descriptor.close()





#####################################################################################################
if __name__ == '__main__':
    import fire
    fire.Fire()

