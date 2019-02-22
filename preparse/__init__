import pickle
import preparse.lib.ext as ext
import importlib
import preparse.lib as lib
from preparse.vars import prepvars as prepvars
from preparse.lib.std import InvalidPreparseError as InvalidPreparseError
import preparse.lib.loop_logic as loop_logic

compilelist = []

def exec_line(text):
	linetext = list(text)
	if linetext[0] == "#":
		linetext.remove("#")
	else:
		return None
	try:
		linetext.remove("\n")
	except:
		pass
	text = "".join(linetext)
	text = text.split(" ")
	if text[0] == "test":
		print("Preparse test successful\n")
	elif text[0] == "use":
		newmod = importlib.import_module("preparse.lib." + text[1])
		newmod.setup()
	elif text[0] in ext.extensions:
		try:
			ext.extensions[text[0]](text)
		except ValueError:
			raise InvalidPreparseError(text[0] + " is not structured properly. No proper function defined.")
	else:
		raise InvalidPreparseError(text[0] + " is an unknown command.")
	
def run(file):
	file = open(file, "rb")
	commands = pickle.load(file)
	x = 0
	while x < len(commands):
		prepvars["__LOOPTEXT__"] = commands[x].split(" ")
		ex = commands[x].split(" ")
		if prepvars["__DEBUG__"]:
			print(str(ex))
		loop_logic.continue_loop(ex, exec_line)
		x = x + 1
	
		
	
		
