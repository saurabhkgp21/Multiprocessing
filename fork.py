import os
import source
import time

def child(argument):
	print "PID {}, got argument {},Initial a = {}".format(os.getpid(), argument,source.a)
	source.a = 2*argument
	os._exit(0)  

def parent():
	print "Pid  before forking {}".format(os.getpid())
	process = 1
	while process < 3:
		process += 1
		newpid = os.fork()
		print "Fork Return Value {}, PID {}".format(newpid, os.getpid())
		if newpid == 0:
			child(process)
		else:
			pass

parent()