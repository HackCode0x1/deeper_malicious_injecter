#!/usr/bin/env python

import glob

from setuptools import setup
from os import mkdir
import os.path
from os import system as cmd

Dir = 'bin'
if not os.path.exists(Dir):
	mkdir(Dir)
cmd('cp deeperinjecter.py bin/deeperinjecter')
cmd('cp Moduls/* bin')
scripts = glob.glob('bin/*')


version="4.1.0"


setup(name="DeeperMalicious",
    version=version,
    license="GPL",
    author='N@RAMInA$_AKB',
    url="https://github.com/NoOAYe/deeper_malicious_injecter",
    install_requires=['halo==0.0.30 ','colorama==0.4.3 ','yaspin',
     ],
    scripts = scripts
)



if os.path.exists(Dir):
	cmd('rm -rf bin >/dev/null')
  
   
   
  
    
    
