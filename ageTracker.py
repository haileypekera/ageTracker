counter= 1
database = {}

while (counter<=5):
	friend= input("The name of friend " + str(counter) + " is " )
	age= input("The age of friend " + str(counter) + " is " )
	database[friend]=age
	counter= counter + 1
	
print (database)
