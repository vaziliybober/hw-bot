
class Logger:
	def __init__(self, filename):
		self._filename = filename

	def log(self, text):
		file = open(self._filename, 'a')
		file.write(text + '\n')