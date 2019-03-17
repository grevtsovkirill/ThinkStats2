"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    respdf=nsfg.ReadFemResp()
    #respdf.head()
    pregnum=respdf['pregnum']
    preg_stat=pregnum.value_counts().sort_index()
    list_of_Npregs=pregnum.unique()
    list_of_Npregs.sort()
    preg_stat_nsfg=[]
    print("list_of_Npregs",list_of_Npregs)
    Npregs_7_95=0
    Npregs_tot=0
    for i in list_of_Npregs:
        Npregs_tot+=preg_stat[i]
        if i<7:
            preg_stat_nsfg.append((i,preg_stat[i]))
        if i>6:
            Npregs_7_95+=preg_stat[i]
    print("pregnums:\n","\n".join([str(x) for x in preg_stat_nsfg]),"\n7-95 ",Npregs_7_95,"\nTotal = ",Npregs_tot)
    dict_toPreg=nsfg.MakePregMap(respdf)
    #print("dict_toPreg",dict_toPreg)
    
    #print('%s: All tests passed.' % script)
    

if __name__ == '__main__':
    main(*sys.argv)
