#A file for creating an index in a python file with a text file and an Hashing function : 
#Word ==>
#value = Hash(Word) ==>
#value = Word 

#importing the hashing function of the project
from Hashing_function import hash

#piece of code to return the number of line of the dictionnary 
with open(r"FrenchDictionary.txt", 'r') as fp:
    for count, line in enumerate(fp):
        pass
print('Total Number of lines:', count + 1)
