class DataHandler:
	
	def __init__(self, dir):
		self.dir = dir
		try:
			self.fp = open(self.dir, 'r')
		except IOError:
			print('cannot open')
			
		self.line = 0
		
	def get_dir(self):
		return self.dir

	def close(self):
		self.fp.close()
		
	def read_line(self):
		self.line = self.fp.readline().rstrip().split(",")
		
	def line_input(self):
		return self.line[:13]
	
	def line_output(self):
		return self.line[14:]
