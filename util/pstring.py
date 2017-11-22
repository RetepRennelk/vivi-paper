class pstring:
	'''
	Utility class 'Peter's string'
	
	- It overwrites '+=' to add a newline character to each add string
	- It is used to construct the html body during parse_root
	'''
	def __init__(self):
		self._s = ''
	def __iadd__(self, other):
		self._s += other + "\n"
		return self
