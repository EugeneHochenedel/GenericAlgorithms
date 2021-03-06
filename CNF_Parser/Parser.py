def Main():
	#Opens and reads the file
	inFile = open("Expressions.txt", 'r')
	
	#Does the following for every expression in the opened file
	for expression in (inFile):
		
		#Boolean to determine if the clause is open or closed
		openClause = False;
		#Recieves data after each time the string is evaluated
		expressionEval = "";
		
		#An empty list that will hold all of the literals in the string
		literals = [];
		#An empty list that will hold all of the clauses within the string
		eachClause = [];
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
			if (char in listOPEN):
				expressionEval += char
				#Sets open clause to true
				openClause = True;
			
			#Checks if the char is a NOT and if the char is inside or outside of a clause
			elif (char in listNOT):
				if(openClause == True):
					#Adds the char to the string for the expression evaluation
					expressionEval += char;
			
			#Checks if the char is an AND and if the char is inside or outside of a clause
			elif (char in listAND):
				if(openClause == True):
					#Adds the char to the string for the expression evaluation
					expressionEval += char;
			
			#Checks if the char is an OR and if the char is inside or outside of a clause
			elif (char in listOR):
				if(openClause == True):
					#Adds the char to the string for the expression evaluation
					expressionEval += char;
			
			#Checks if the character is to be ignored
			elif (char in listNULL):
				#if the character is in the list, it's ignored
				continue;
			
			#Checks if the character closes a clause
			elif (char in listEND and openClause == True):
				expressionEval += char
				#Sets open clause to false, closing it
				openClause = False;
				#Adds the informaiton in the expression evaluation string to the list of clauses
				eachClause.append(expressionEval);
				#Resets the string
				expressionEval = "";

			elif (openClause == True or openClause == False):
				#Adds the characters that weren't counted to the expression evaluation string
				expressionEval += char;
				#Checks if char is in the list of literals
				if (char in literals):
					#If the char is already in the list, it gets ignored
					continue;
				#If the char is not in a list, add it to the list of literals
				literals.append(char);
		
		literals.sort();
		print expression;
		print "Literals:", len(literals);
		print "Each literal:", literals;
		print "Clauses:", len(eachClause);
		
		print "\n";
	
	inFile.close();

Main()