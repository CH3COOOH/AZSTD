## Last update: 2026.03.08

def read_t(fname: str):
	with open(fname, 'r') as o:
		buf = o.read()
	return buf

def read_t8(fname: str):
	with open(fname, 'rb') as o:
		buf = o.read().decode('utf-8')
	return buf

def write_t(fname: str, buf: str):
	with open(fname, 'w') as o:
		o.write(buf)
	return buf

def write_t8(fname: str, buf: str):
	with open(fname, 'wb') as o:
		o.write(buf.encode('utf-8'))
	return buf

def read_stream(fname, n_byte=1024):
	with open(fname, 'rb') as o:
		while True:
			data = o.read(n_byte)
			if not data:
				return None
			yield data

if __name__ == '__main__':
	write_t8('wt8.txt', '今が最高！')