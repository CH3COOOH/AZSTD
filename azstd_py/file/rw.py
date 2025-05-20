## Last update: 2025.04.30

def gracefulRead(fname, method='r'):
	with open(fname, method) as o:
		buf = o.read()
	return buf

def gracefulWrite(fname, buff, method='w', encoding='utf-8'):
	try:
		if method == 'w':
			o = open(fname, method, encoding=encoding)
		elif method == 'wb':
			o = open(fname, method)
		o.write(buff)
		o.close()
		return 0
	except Exception as e:
		print(e)
		return -1

def readstream(fname, n_byte=1024):
	with open(fname, 'rb') as o:
		while True:
			data = o.read(n_byte)
			if not data:
				return None
			yield data
