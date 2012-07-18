import os, sys

class parser():

	def __init__(self, data=None):
		if data:
			self.args = data
		else:
			self.args = sys.argv[1:]
		self.options = {}


	def is_num(self, s):
		if s[0] in ('-', '+'):
			return s[1:].isdigit()
		return s.isdigit()



	def run(self):
		for opt in self.args:
			if opt.find("=") != -1:
				keypos = opt.find("=")
				if opt[keypos+1:] == "True":
					self.options[opt[:keypos]] = True
				elif opt[keypos+1:] == "False":
					self.options[opt[:keypos]] = False
				elif self.is_num(opt[keypos+1:]):
					self.options[opt[:keypos]] = int(opt[keypos+1:])
				else:
					self.options[opt[:keypos]] = opt[keypos+1:]
			else:
				self.options[opt] = True

		return self.options

if __name__ == "__main__":
	print "Import it in your scripts!"
