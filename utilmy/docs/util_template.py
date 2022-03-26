##### BLOCK_HEADER ####################################################################################
# -*- coding: utf-8 -*-
MNAME = "utilmy."
HELP = """ utils for




"""

##### BLOCK_IMPORT ####################################################################################
import os, sys, glob, time,gc, datetime, numpy as np, pandas as pd
from typing import List, Optional, Tuple, Union
from numpy import ndarray
from box import Box






###### BLOCK LOG #######################################################################################
from utilmy import log, log2

def help():
    """function help"""
    from utilmy import help_create
    print( HELP + help_create(MNAME) )



###### BLOCK TEST  ######################################################################################
def test_all() -> None:
    """function test_all

    """
    log(MNAME)
    test1()
    test2()


def test1() -> None:
    """function test1
    Args:
    Returns:

    """
    pass




def test2() -> None:
    """function test2
    Args:
    Returns:

    """
    pass




########### CORE BLOCK ##################################################################################











































###### FOOTER BLOCK #############################################################################################
if __name__ == "__main__":
    import fire
    fire.Fire()


