def varMapping(list, translate):
	int = 0;
	for items in (list):
		if (items == translate):
			return int;
		else:
			int += 1;
		
def Main():
	#Opens and reads the file
	inFile = open("Expression.txt", 'r');
	
	#Does the following for every expression in the opened file
	for expression in (inFile):
		
		#Boolean to determine if the clause is open or closed
		openClause = False;
		#Recieves data after each time the string is evaluated
		expressionEval = "";
		#An empty string to hold the converted clauses
		convertedExpression = "";
		
		#An empty list that will hold all of the literals in the string
		literals = [];
		#An empty list that will hold all of the clauses within the string
		eachClause = [];
		values = [0, 1, 0, 1, 0];
		indexValue = 0;
		test1 = "01010";
		temp = [];
		
		#List of characters that open a clause in the string
		listOPEN = ['(', '[', '<'];
		#List of characters in the string that represent a NOT
		listNOT = ['?','!',"#"];
		#List of characters in the string that represent an OR
		listOR = ['V','|', ','];
		#List of characters in the string that represent an AND
		listAND = ['&','*',':'];
		#List of characters that close a clause in the string
		listEND = [')', ']', '>'];
		#List of characters in the string that are to be ignored
		listNULL = [' ', '\n'];
		
		#For each char in expression check what they are
		for char in (expression):
			#Checks if the char opens a clause
			if (char in listOPEN and openClause == False):
				#Sets open clause to true
				openClause = True;
			
			#Checks if the char is a NOT and if the char is inside or outside of a clause
			elif (char in listNOT and openClause == True):
				#Adds the char to the string for the expression evaluation
				expressionEval += char;
			
			#Checks if the char is an AND and if the char is inside or outside of a clause
			elif (char in listAND):
				#Adds the char to the string for the expression evaluation
				expressionEval += char;
			
			#Checks if the char is an OR and if the char is inside or outside of a clause
			elif (char in listOR and openClause == True):
				#Adds the char to the string for the expression evaluation
				expressionEval += char;
			
			#Checks if the character is the list of characters to be ignored
			elif (char in listNULL):
				#If the character is in the list, it's ignored
				continue;
			
			#Checks if the character closes a clause
			elif (char in listEND and openClause == True):
				#Sets open clause to false, closing it
				openClause = False;
				#Adds the informaiton in the expression evaluation string to the list of clauses
				eachClause.append(expressionEval);
				#Resets the string
				expressionEval = "";

			elif (openClause == True):
				#Adds the characters that weren't counted to the expression evaluation string
				expressionEval += char;
				#Checks if char is in the list of literals
				if (char in literals):
					#If the char is already in the list, it gets ignored
					continue;
				#If the char is not in a list, add it to the list of literals
				literals.append(char);
		
		literals.sort();
		
		#Loops through each clause and converts the literals to values
		for string in (eachClause):
			inverseValue = 0;
			#An empty string to hold the clauses after the values preceded by a NOT are changed
			inverseExpression = "";
			
			for char in (string):
				if (char in listNOT):
					convertedExpression += '~';
				elif (char in listAND):
					convertedExpression += '&';
				elif (char in listOR):
					convertedExpression += '|';
				else:
					index = varMapping(literals, char);
					convertedExpression += str(values[index])

			for char in (convertedExpression):
				if (inverseValue == 1):
					if (char == '1'):
						inverseExpression += str(0);
					
					elif (char == '0'):
						inverseExpression += str(1);
					inverseValue = 0;
					
				elif (char == '~' and inverseValue == 0):
					inverseValue = 1;
				else:
					inverseExpression += char;
		
		print "Expression:", expression;
		print "Literals:", len(literals);
		print "Each literal:", literals;
		print "Clauses:", len(eachClause);
		print "Conversion:", convertedExpression;
		print "Inverse:", inverseExpression;
		print '\n';
	
	inFile.close();

Main()
