import sys

try:
    from msvcrt import getch
except ImportError:
	import tty
	import termios
	def getch():
		"""
		Gets a single character from STDIO.
		"""
		import sys
		import tty
		import termios
		fd = sys.stdin.fileno()
		old = termios.tcgetattr(fd)
		try:
			tty.setraw(fd)
			return sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old)

def pause(message='Press any key to continue . . . '):
	"""
	Prints the specified message if it's not None and waits for a keypress.
	"""
	if message is not None:
		print(message, end='')
		sys.stdout.flush()
	getch()
	print()

def pause_exit(status=None, message='Press any key to exit'):
	"""
	Prints the specified message if it is not None, waits for a keypress, then
	exits the interpreter by raising SystemExit(status).
	If the status is omitted or None, it defaults to zero (i.e., success).
	If the status is numeric, it will be used as the system exit status.
	If it is another kind of object, it will be printed and the system
	exit status will be 1 (i.e., failure).
	"""
	pause(message)
	sys.exit(status)
