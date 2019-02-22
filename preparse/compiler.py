import pickle

def compile_single(file):
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
	
		
def compile_multi(*files):
	'''
	Compiles multiple files into one .ppak. The name of the first given file is used to create the new one. Like compile_single, give only a string containing the filename for each. (uses *args).
	'''
	
	amount = len(files) - 1
	alltext = []
	newfile = files[0]
	newfile = newfile.split(".")
	newfile = newfile[0]
	newfile = open(newfile + ".ppak", "wb")
	x = 0
	while x <= amount:
		currentfile = open(files[x], "r")
		text = currentfile.read()
		text = text.split("\n")
		alltext = alltext + text
		x = x + 1
	pickle.dump(alltext, newfile)
	newfile.close()
	
	
