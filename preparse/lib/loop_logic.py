from preparse.vars import prepvars as prepvars


def start_loop(typev):
	prepvars["__LOOP__"] = typev

def continue_loop(condition, executing, func):
	typev = prepvars["__LOOP__"]
	if typev == "ifdef":
		if condition[1] in prepvars.keys:
			func(executing)
		else:
			pass
	elif typev == "ifnotdef":
		if not condition[1] in prepvars.keys:
			func(executing)
		else:
			pass
	else:
		pass
	 
