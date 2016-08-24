#!/usr/bin/python
#Describe:Getting CPU info. from system.
#Usage:cpu_info_python.py

import psutil
print "CPU user time:%r"%psutil.cpu_times().user
print "CPU count(Logical):%r"%psutil.cpu_count()
print "CPU count(Phyisical):%r"%psutil.cpu_count(logical=False)


