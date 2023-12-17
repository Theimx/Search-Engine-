#A programme to fill a Txt file with an index make with a Txt file that you give and a Hash table 

#importing the hashing function of the project
from Hashing_function import hash

#The function to write in your indexing word and is index, with a line break
def writeavar(a):
    a = str(a)
    b = "\n" + a
    fichier = open("Index.txt", "a")
    fichier.write(b)
    fichier.close()

#The function to make a string of your word, his index by the hashing function, return
#Your word in this form : int(index) = str(word)
#Example : 100 = Hello
def indexing(a):
    a = str(a)
    c = a 
    b = " = "
    a = str(hash(c))
    d = a + b + c
    return str(d)

#piece of code to return the number of line of the Txt files that you want to index
with open(r"YourTxtFile.txt", 'r') as fp:
    for count, line in enumerate(fp):
        pass
#number of lines:
nb_line = count + 1


#Function to write and indexing a word : writeavar(indexing("Yourword"))

#The piece of code who analyse,indexing
file  = open("YourTxtFile.txt","r",encoding="utf8")
lines = file.readlines()
for n, line in enumerate(lines) :
    writeavar(indexing(line))
file.close()