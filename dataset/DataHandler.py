class DataHandler:
	
	def __init__(self, dir):
		self.dir = dir
		self.fp =[]
		self.line = []
	def get_dir(self):
		return self.dir
	
	def read(self):
		try:
			self.fp = open(self.dir, 'r')
		except IOError:
			print('cannot open')
	
	def close(self):
		self.fp.close()
		
	def read_line(self):
		self.line = self.fp.readline()
		
	def line_input(self):
		return self.line[:14]
	
	def line_output(self):
		return self.line[14:]