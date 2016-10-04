import csv
dic = {}

# ================================================ read in csv
def readIn():
	with open('data/auth.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			#print(row['User'], row['Password'])
			dic[row['User']] = row['Password']

def availAlready(x,y): # in auth.csv or na
	readIn()
	if x in dic:
		return True
	if x not in dic:
		#makeAcc(x,y)
		return False

# ================================================ login
def checkAcc(x,y):
	readIn()
	if dic[x] != y: #not in auth.csv
		return False
	elif dic[x] == y: #it's right!!
		return True

# ================================================ register
def makeAcc(x,y):
	with open('data/auth.csv', 'ab') as csvfile: # APPEND
		fieldnames = ['User', 'Password']
		writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
		writer.writerow({'User': x, 'Password': y })











'''
FOR FUTURE REFERENCES:

# ================================================ read in csv
with open('data/auth.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		#print(row['User'], row['Password'])
		dic[row['User']] = row['Password']

# ================================================ append to csv
x = "" #parameters for writer.writerow
y = ""

with open('../data/auth.csv', 'ab') as csvfile:
    fieldnames = ['User', 'Password']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writerow({'User': x, 'Password': y })

#print dic['hello'] >> itsme
#print dic >> csv dictionary
'''