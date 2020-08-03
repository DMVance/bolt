#!/usr/bin/env python3
# This program allows the user to input a set of words, breaks each word into individual
# letters, counts occurrences of each letter, sorts alphabetically and prints only highest number of occurrences
# of each letter in any single word.

alphabet = list("abcdefghijklmnopqrstuvwxyz")
#print(alphabet)

# Get the word(s) from the user
print("Please enter the words you would like to sort alphabetically. Press Enter when finished: ")
wrd = input("--> ")
#print(wrd)

# split the string of words into individual words (eliminates spaces and obviates the need for c.pop(" ")?)
words = wrd.split()
#print(words)

# Sort the letters in the list in alphabetical order
#alpha = sorted(wrd.lower())
#print(alpha)
# For each word, sort the letters in alphabetical order, store as dict of lists
d = dict()
import collections
for w in words:
    alpha = sorted(w.lower())
    #print(alpha)
    in_alphabet = [l for l in alpha if l in alphabet] # filter out any character not in the alphabet, including spaces
    
    # this would be the filter for alphabet characters if not using list comprehension above:
    #def is_letter(letter):
    #    return letter in alphabet
    #in_alphabet = list(filter(is_letter, alpha))
    #print(in_alphabet)
    
    # provide the number of occurrences of each letter in each word and arrange alphabetically
    c = dict(collections.Counter(in_alphabet))
    #print(c)

    #s = ""
    #for k,v in c.items():
    #    if c[k] != 1:
    #        #print("{}({}) ".format(k, c[k]), end="")
    #        s = s + str(k) + "(" + str(c[k]) + "), "
    #    else:
    #        #print("{} ".format(k), end="")
    #        s = s + str(k) + ", "
    
    #def result(value, total):
    for k, v in c.items():
        if k not in d or d[k] < c[k]:
            d[k] = c[k]
    #print(d)

    #print(s[:-2]) # eliminates the comma and space after the last printed element

s = ""
for k,v in c.items():
    if d[k] != 1:
        #print("{}({}) ".format(k, c[k]), end="")
        s = s + str(k) + "(" + str(d[k]) + "), "
    else:
        #print("{} ".format(k), end="")
        s = s + str(k) + ", "
print(s[:-2]) # eliminates the comma and space after the last printed element
#print(d)

# Output to a usable format, such as PowerPoint, PDF, even Word or Text file

# if __name__ == '__main__': main()