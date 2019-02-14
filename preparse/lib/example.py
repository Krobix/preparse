import preparse.lib.ext as ext

def simple(text):
	print("This is simple")
	
def advanced(text):
	print("This is advanced")
	print(text[1])
	
def setup():
	ext.def_ext(simple, "simple_example")
	ext.def_ext(advanced, "advanced_example")
