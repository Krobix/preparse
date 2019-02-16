import preparse.lib.ext as ext
import importlib
from preparse.vars import prepvars as prepvars
import platform

class stop(Exception):
	pass
	
class InvalidPreparseError(Exception):
	pass

def py_exec(text):
	text.remove(text[0])
	exec(" ".join(text))
	
def stop_e(text):
	text.remove(text[0])
	text = " ".join(text)
	raise stop(text)

def get_attr(text):
	temp = importlib.import_module(text[1])
	prepvars[text[2]] = temp.__dict__[text[2]]
	
def echo(text):
	try:
		temp = prepvars[text[1]]
	except KeyError:
		raise InvalidPreparseError(text[1] + " is not an existing variable.")
	print(temp)
	
def vardef(text):
	prepvars[text[1]] = text[2]
	

def setup():
	ext.def_ext(py_exec, "py_exec")
	ext.def_ext(stop_e, "stop")
	ext.def_ext(get_attr, "get")
	ext.def_ext(echo, "echo")
	ext.def_ext(vardef, "define")
	if platform.python_version_tuple()[0] == "3":
		prepvars["__PY3__"] = 0
	else:
		prepvars["__PY2__"] = 0
	  
		
	
