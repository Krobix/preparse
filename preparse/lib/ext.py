extensions = {}

def def_ext(func, name):
	'''
	Allows you to define external commands. func parameter represents the actual function (Do not include the parenthesis), and name represents how it will be called.
	'''
	extensions[name] = func
	
