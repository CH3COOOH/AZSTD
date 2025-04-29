import time

def localtime(style='%Y-%m-%d %H:%M:%S'):
	return time.strftime(style, time.localtime())

class Log:
	def __init__(self, show_level=1):
		self.show_level = show_level
		self.level_map = ['DEBUG', 'INFO', 'WARN', 'ERROR']

	def print(self, msg, level=1, write=False):
		if self.show_level > level:
			return None
		localtime = localtime()
		msg = '[%s][%s] %s' % (localtime, self.level_map[level], msg)
		print(msg)
		if write == True:
			with open('event.log', 'a') as o:
				o.write(msg + '\n')