#!/usr/bin/python
#Describe:Getting memory info. form the system.
#Usage:python mem_info_python.py

import psutil
print "Available memory:%r"%psutil.virtual_memory().available
print "Used memory:%r"%psutil.virtual_memory().used
print "Free memory:%r"%psutil.virtual_memory().free
print "Used swap:%r"%psutil.swap_memory().used
print "Free swap:%r"%psutil.swap_memory().free

