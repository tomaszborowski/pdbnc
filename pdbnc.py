#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A script to extract from a pdb file - result of native contact analysis
by cpptraj - residue numbers and names for residues with at least one
atom that makes contacts above a given threshold

argument # 1 - file name of the pdb file - result of native contact analysis by cpptraj
argument # 2 - threshold value from the range (0.0, 100.0)

Created on Fri Apr 27 19:05:39 2023
@author: borowski
Last update: 18.05.2023
"""
import sys, os
from collections import OrderedDict

def print_help():  
    help_text = """
A script to extract from a pdb file - result of native contact analysis
by cpptraj - residue numbers and names for residues with at least one
atom that makes contacts above a given threshold

argument # 1 - file name of the pdb file - result of native contact analysis by cpptraj
argument # 2 - threshold value from the range (0.0, 100.0)
    """
    
    print(help_text) 


### Seting the file names                                                  ###
sys_argv_len = len(sys.argv)
if sys_argv_len > 1:
    inp_f_name = sys.argv[1]
else:
    inp_f_name = None
if sys_argv_len > 2:
    threshold = eval(sys.argv[2])
else:
    threshold = None


### if -h - write help and exit                                            ###
if inp_f_name == "-h":
    print_help()
    sys.exit(1)

if inp_f_name == None:
    print("Name of input file (pdb) must be provided \n")
    sys.exit(1)    

if not os.path.isfile(inp_f_name):
    print("Input file (pdb) not found \n")
    sys.exit(1)

if not threshold:
    print("threshold value must be from the range (0.0, 100.0) \n")
    sys.exit(1) 


residues = OrderedDict()

### reading the pdb file ###
inp_f = open(inp_f_name, 'r')


for line in inp_f:
    s_line = line.split()
    if len(s_line) == 11:
        res_name = s_line[3]
        res_nr = s_line[4]
        beta = eval(s_line[9])
        if beta > threshold:
            if res_nr not in residues.keys():
                residues[res_nr] = res_name
             
inp_f.close()

res_numbers = []
### printing out results ###
for key, value in residues.items():
    print(key, value)
    res_numbers.append(eval(key))

print("\n")
print("### only residue numbers (1-based): ###")    
print(res_numbers)




 