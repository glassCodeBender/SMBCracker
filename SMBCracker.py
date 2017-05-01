# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# -*- coding: utf-8 -*-
"""
@Author: Alex Moorman

usage: ~$ SMBCracker.py passwordfile.txt usernamefile.txt

Program Purpose:
Program cracks passwords and then gathers data by connecting to the SMB of a server.
"""
import os
import sys

class SMBCracker:

    def __init__(self):
       pass
    
 
    def import_pfile(self):        
        # use argv to pass commandline arguments to the variables
        if os.path.exists(argv[2]):
            try:
                fpasswd = open(argv[2])
            except IOError:
                print("Could not read file " + argv[2])
                
        for f in fpasswd:
            try:
                pass_list = f.readlines()
            except IOError:
                print("Could not read file " + argv[2])
        fpasswd.close()
        return pass_list
    

    def import_ufile(self):
        if os.path.exists(argv[1]):
            try:
                fusers = open(argv[1])
            except IOError:
                print("Could not read file " + argv[1])                

        for f in fusers:
            try:
                user_list = f.readlines()
            except IOError:
                print("Could not read file " + argv[1])
        fusers.close()
        return user_list
    
# read a combination of each username and password in to see if one matches


# need a command to close files and exit programs if we have success


# read the next 50 lines (this assumes we only read first 50 lines)

"""
 create a if __name__ = __main__ command at the end that will determine what happens
 if the program is run from another program. 

"""
"""
with open(pfile_string) as f:
    for i in range(50):
        f.next()
    for line in f:
        pass_list2 = f.readlines()
"""     
