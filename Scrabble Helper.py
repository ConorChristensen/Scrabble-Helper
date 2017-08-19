#Conor Christensen
#Last edited 14/08/17

#Task 1:

from Anagram_Table import HashTable

file = open('Dictionary.txt')

lines = sum(1 for line in file)                             #Find the number of words in the dictionary, as to create appropriate sized Hash Table
file.close()
anagrams = HashTable(lines*1000)                
file = open('Dictionary.txt')                   
for line in file:
    word = line.rstrip()
    anagrams.add(word)
output_list = anagrams.largestGroup()

print('Task 1:\nHere is your Largest Group of anagrams: ')
for print_word in range(len(output_list)):
    print(str(output_list[print_word]))

#Task 2:

def getScrabbleWords(key):
    key = key.lower()
    task2_output = anagrams[key]
    print("Words without using wildcard: ")
    for t in range(len(task2_output)):
        print(str(task2_output[t]))

#Task 3

def getWildcardWords(key):
    key = key.lower()
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    task3_output = []
    for i in range(26):
        try:
            temp_key = key+letters[i]
            task3_output.append(anagrams[temp_key])
        except KeyError:
            pass
    print("words with using a wildcard: ")
    for t in range(len(task3_output)):
        for s in range(len(task3_output[t])):
            print(str(task3_output[t][s]))

#Run task 2 and 3 as functions.
            
finish = False
while not finish:
    key = input('Enter query string: ')
    if key != '***':
        getScrabbleWords(key)
        getWildcardWords(key)
    else:
        finish = True
