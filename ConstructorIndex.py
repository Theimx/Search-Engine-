#A file for creating an index in a python file with a text file and an Hashing function : 
#Word ==>
#value = Hash(Word) ==>
#value = Word 

#importing the hashing function of the project
from Hashing_function import hash

def writeavar(a):
    a = str(a)
    b = "\n" + a
    fichier = open("Index.txt", "a")
    fichier.write(b)
    fichier.close()

def indexing(a):
    a = str(a)
    c = a 
    b = " = "
    a = str(hash(c))
    d = a + b + c
    return str(d)
#piece of code to return the number of line of the dictionnary 
with open(r"FrenchDictionary.txt", 'r') as fp:
    for count, line in enumerate(fp):
        pass
nb_line = count + 1


#writeavar(indexing())
#fichier = open("FrenchDictionary.txt", "r")
#print(writeavar(indexing(str(fichier.read()))))
#fichier.close()

file  = open("FrenchDictionary.txt","r",encoding="utf8")
lines = file.readlines()
for n, line in enumerate(lines) :
    writeavar(indexing(line))
file.close()