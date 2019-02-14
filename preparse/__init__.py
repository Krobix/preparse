import pickle
import preparse.lib.ext as ext
import importlib
import preparse.lib as lib
from preparse.vars import prepvars as prepvars

compilelist = []

class InvalidPreparseError(Exception):
	pass

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
	if text[0] == "compileadd":
		temp = open(text[1], "r")
		compilelist.append(temp.read())
	elif text[0] == "compilefinish":
		newfile = open(text[1], "w")
		x = 0
		tempstring = ""
		while x < len(text):
			tempstring = tempstring + text[x]
			x = x + 1
		newfile.write(tempstring)
	elif text[0] == "test":
		print("Preparse test successful\n")
	elif text[0] == "use":
		newmod = importlib.import_module("preparse.lib." + text[1])
		newmod.setup()
	elif text[0] in ext.extensions:
		try:
			ext.extensions[text[0]](text)
		except ValueError:
			raise InvalidPreparseError(text[0] + " is not structured properly. No proper function defined.")
	elif text[0] == "define":
		prepvars[text[1]] = text[2]
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
	
	
def run_loop(type):
	pass
	#Will finish later
	
def run(file):
	file = open(file, "rb")
	commands = pickle.load(file)
	x = 0
	loop_words = [
		"ifdef",
		"try",
		"else",
		"except"]
	while x < len(commands):
		try:
			newcomm = list(commands[x])
			newcomm.remove("#")
			newcomm.remove("\n")
			commands[x] = "".join(newcomm)
		except ValueError:
			pass
		if commands[x] in loop_words:
			run_loop(commands[x])
		else:
			try:
				commands.remove("")
			except:
				pass
			exec_line(commands[x])
		x = x + 1
	
		
	
		
