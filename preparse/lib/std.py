import preparse.lib.ext as ext
import importlib
from preparse.vars import prepvars as prepvars

class stop(Exception):
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
	

def setup():
	ext.def_ext(py_exec, "py_exec")
	ext.def_ext(stop_e, "stop")
	ext.def_ext(get_attr, "get")
