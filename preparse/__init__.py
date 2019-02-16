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
		
		
def compile_ppak(file):
	commands = []
	filesplit = file.split(".")
	filewrite = open(filesplit[0] + ".ppak", "wb")
	original = open(file, "r")
	original = original.read()
	original = original.split("\n")
	x = 0
	while x < len(original):
		try:
			commands.append(original[x])
		except:
			pass
		x = x + 1
	pickle.dump(commands, filewrite)
	filewrite.close()	
	
def run(file):
	file = open(file, "rb")
	commands = pickle.load(file)
	x = 0
	loop_words = [
		"ifdef",
		"ifnotdef",
		"try",
		"except",
		"endloop"]
	while x < len(commands):
		try:
			newcomm = list(commands[x])
			newcomm.remove("#")
			newcomm.remove("\n")
			commands[x] = "".join(newcomm)
		except ValueError:
			pass
		if commands[x].split(" ")[0] in loop_words:
			loop_logic.start_loop(commands[x].split(" ")[0])
		else:
			try:
				commands.remove("")
			except:
				pass
			loop_logic.continue_loop(prepvars["__LOOPTEXT__"], commands[x], exec_line)
		x = x + 1
	
		
	
		
