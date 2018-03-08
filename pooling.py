from multiprocessing.dummy import Pool as ThreadPool
import time
import source
n = 2

def test_function(name):
	print 'Starting thread: name {} at {}'.format(name, time.time())
	print 'Thread : name {}(In starting), common source {}'.format(name, source.a)
	t = time.time()
	if name == 'Saurabh':
		source.a = name[0]
	while time.time() - t < 2:
		pass

	print 'Thread : name {}(At End), common source {}'.format(name, source.a)
	print 'Completed thread: name {} at {}'.format(name, time.time())



name = ['Saurabh', 'Agarwal']


print 'Starting {} at {}'.format(n, time.time())
pool = ThreadPool(n)
pool.map(test_function, name)
pool.close() 
pool.join()