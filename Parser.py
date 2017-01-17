def Main():
	inFile = open("Expressions.txt", 'r')
	
	for expression in (inFile):
		
		eachClause = 0;
		literals = [];
		openClause = 0;
		eachNegation = 0;
		eachAND = 0;
		eachOR = 0;
		
		for char in (expression):
			if (char == "?"):
				eachNegation += 1;
			
			elif (char == "&"):
				eachAND += 1;
			
			elif (char == "V"):
				eachOR += 1;
			
			elif (char == "("):
				openClause += 1;
			
			elif (char == ")"):
				eachClause += 1;
			
			elif (char == " " or char == "\n"):
				continue;
			
			else:
				if (char in literals):
					continue;
				literals.append(char);
		
		print expression;
		literals.sort();
		
		print "Literals:", len(literals);
		print "Each literal:", literals;
		print "Clauses:", eachClause;
		print "AND:", eachAND;
		print "OR:", eachOR;
		print "NEGATION:", eachNegation;
		
		print "\n";
	
	inFile.close();

Main()