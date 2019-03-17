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
    """
      The variable pregnum is a recode that indicates how many times each re- spondent has
      been pregnant. Print the value counts for this variable and compare them to the 
      published results in the NSFG codebook:
      https://www.icpsr.umich.edu/nsfg6/Controller?displayPage=labelDetails&fileCode=FEM&section=R&subSec=7869&srtLabel=606835
    """
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
    print("pregnums:")
    for i in range(0,len(preg_stat_nsfg)):
        print( preg_stat_nsfg[i][0]," ",preg_stat_nsfg[i][1])
    print("7-95 ",Npregs_7_95,"\nTotal = ",Npregs_tot)


    """
    cross-validate the respondent and pregnancy files by comparing pregnum for each respondent
    with the number of records in the pregnancy file.
    """
    pregdf=nsfg.ReadFemPreg()
    map_ResptoPreg=nsfg.MakePregMap(pregdf)
    fail=0
    for index, pregnum in respdf.pregnum.iteritems(): 
            #print("index",index,"pregnum",pregnum)
        caseid = respdf.caseid[index]
        indices = map_ResptoPreg[caseid]
        if pregnum!=len(indices):
            print("caseid in resp:",caseid,", pregnum=",pregnum," entries in preg= ",indices)
            fail+=1
    if fail==0:
        print('%s: All tests passed.' % script)
    

if __name__ == '__main__':
    main(*sys.argv)
