from preparse.vars import prepvars as prepvars
from preparse.lib.std import InvalidPreparseError


def continue_loop(condition, func):
	ex = condition
	if prepvars["__DEBUG__"]:
		print(str(condition))
	try:
		temp = list(condition[0])
		temp.remove("#")
		condition[0] = "".join(temp)
	except:
		return None
	if condition[0] == "ifdef":
		if condition[1] in prepvars:
			ex.remove(ex[0])
			ex.remove(ex[0])
			func("#" + " ".join(ex))
		else:
			pass
	elif condition[0] == "ifnotdef":
		if condition[1] not in prepvars:
			ex.remove(ex[0])
			ex.remove(ex[0])
			func("#" + " ".join(ex))
		else:
			pass
	elif condition[0] == "try":
		try:
			ex.remove(ex[0])
			ex.remove(ex[0])
			func("#" + " ".join(ex))
		except:
			print(" ".join(ex) + " statement failed")
	else:
		func("#" + " ".join(condition))
		
		
def setup():
	raise InvalidPreparseError("Do not #use loop_logic")
