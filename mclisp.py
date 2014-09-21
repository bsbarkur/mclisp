envdict = {}

def evalq(exp):
	if len(exp) == 1:
		if isinstance(exp[0], list):
			exp1 = exp[0]
			res = "("
			ind = len(exp1)
			for i in range(ind-1):
				res += exp1[i] + " "
			res = res + exp1[len(exp1)-1] + ")"
			return res
	
		else:
			return "(" + exp[0] + ")"
	else:
		res = "("
		ind = len(exp)
		for i in range(ind-1):
			res += exp[i] + " "
		res = res + exp[len(exp)-1] + ")"
		return res

def evalcdr(exp):
	print "------- evaluating cdr ------"
	print exp
	if isinstance(exp[0], list):
		exp1 = exp[0]
		res = "("
		ind = len(exp1)
		for i in range(1, ind-1):
			res += exp1[i] + " "
		res = res + exp1[len(exp1)-1] + ")"
		return res
	else:
		print "in else"
		print exp
		if exp[0] == "QUOTE":
			(_, exp) = tokens
			return evalcdr(exp[1:])
		else:
			return exp[1]

def evalcons(e, e1):
	print "------- evaluating cons ----"
	first =""
	second =""
	rest = []
	if e[0] == "QUOTE":
		print e[1:]
		first = e[1:]	
	if e1[0] == "QUOTE":
		print e1[1:]
		second = e1[1:]

	rest.append(first)
	rest.append(second)
	

	res = "("
	res = res + rest[0][0] + " "

	if isinstance(rest[1][0], list):
		print rest[1][0]
		exp1 = rest[1][0]
		ind = len(exp1)
		for i in range(ind-1):
			res += exp1[i] + " "
		res = res + exp1[len(exp1)-1] + ")"
	return res

def evalcar(exp):
	print "------- evaluating car ------"
	print exp
	if isinstance(exp[0], list):
		exp1 = exp[0]
		res = "("
		ind = len(exp1)
		for i in range(ind-1):
			res += exp1[i] + " "
		res = res + exp1[len(exp1)-1] + ")"
		return res
	else:
		print "in else"
		if exp[0] == "QUOTE":
			(_, exp) = tokens
			return evalcar(exp[1])
		else:
			return exp[0]


def eval(tokens, env):
	if tokens[0] == "QUOTE":
		(_, exp) = tokens
		return evalq(exp)
	if tokens[0] == "CAR":
		(_, exp) = tokens
		print tokens
		print exp
		if isinstance(exp, list):
			return evalcar(exp)
		else:
			return error
	if tokens[0] == "CDR":
		(_, exp) = tokens
		print tokens
		print exp
		if isinstance(exp, list):
			return evalcdr(exp)
		else:
			return error
	if tokens[0] == "CONS":
		(_, exp, exp1) = tokens
		print exp
		print exp1
		return evalcons(exp, exp1)	

def parse(tokens):
    token = tokens.pop(0)
    if '(' == token:
        L = []
        while tokens[0] != ')':
            L.append(parse(tokens))
        tokens.pop(0) # pop off ')'
        return L
    elif ')' == token:
        print "error"
    else:
        return token
		

def tokenize(tokstr):
	newstr = tokstr.replace("(", "( ").replace(")", " )")
	return newstr.split(" ")
	
if __name__ == "__main__":
	print "------- tokenizing ------"
	tokens = tokenize("(CONS (QUOTE A) (QUOTE (B C)))")
	print tokens
	
	print "------- parsing ------"
	tokens = parse(tokens)
	print tokens

	print "------- parsing ------"
	tok = eval(tokens, envdict)
	print tok
