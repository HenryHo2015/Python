#!/usr/bin/python
#Describe:Getting disk info. from the system.
#Usage:python disk_info_python.py

import psutil
print "The system partition info:%r"%psutil.disk_partitions()
print "Free space:%r"%psutil.disk_usage('/').free
print "Disk I/O info.:%r"%psutil.disk_io_counters(perdisk=True)

