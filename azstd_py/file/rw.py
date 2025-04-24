## Last update: 2023.02.04

def gracefulRead(fname, method='r'):
	with open(fname, method) as o:
		buf = o.read()
	return buf

def gracefulWrite(fname, buff, method='w'):
	try:
		with open(fname, method) as o:
			o.write(buff)
		return 0
	except:
		return -1


