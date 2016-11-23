def ident(check_string):
	count = {} 
	for s in check_string: 
	    if s in count.keys(): 
	        count[s] += 1 
	    else: 
	        count[s] = 1 

	for key in count: 
	    if count[key] > 1: 
	        print(key, count[key])

ident(input("enter the string: "))
