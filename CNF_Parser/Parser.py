def Main():
	inFile = open("CNF_Parser\Expressions.txt", 'r')
	
	for expression in (inFile):
		
		eachClause = 0;
		literals = [];
		openClause = 0;
		eachNOT = 0;
		eachAND = 0;
		eachOR = 0;
		
		listNOT = ['?','!',"#"];
		listOR = ['V','/', ','];
		listAND = ['&','*',':'];
		listOPEN = ['(', '[', '<'];
		listEND = [')', ']', '>'];
		
		listNULL = [' ', '\n'];
		
		for char in (expression):
			if (char in listNOT):
				eachNOT += 1;
			
			elif (char in listAND):
				eachAND += 1;
			
			elif (char in listOR):
				eachOR += 1;
			
			elif (char in listOPEN):
				openClause += 1;
			
			elif (char in listEND):
				eachClause += 1;
			
			elif (char in listNULL):
				continue;
			
			else:
				if (char in literals):
					continue;
				literals.append(char);
		
		
		literals.sort();
		print expression;
		print "Literals:", len(literals);
		print "Each literal:", literals;
		print "Clauses:", eachClause;
		print "AND:", eachAND;
		print "OR:", eachOR;
		print "NEGATION:", eachNOT;
		
		print "\n";
	
	inFile.close();

Main()