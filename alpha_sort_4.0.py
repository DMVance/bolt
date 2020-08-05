#!/usr/bin/env python3
# This program allows the user to input a set of words, breaks each word into individual
# letters, counts occurrences of each letter, sorts alphabetically and prints only highest number of occurrences
# of each letter in any single word.

alphabet = list("abcdefghijklmnopqrstuvwxyz")

# Get the word(s) from the user
print("Please enter the words you would like to sort alphabetically. Press Enter when finished: ")
wrdset = input("--> ")

# split the string of words into individual words (eliminates spaces and obviates the need for c.pop(" ")?)
words = wrdset.split()

# For each word, sort the letters in alphabetical order, count number of occurrences of each letter in each word, send only highest number of occurrences of each
# letter into a new dictionary
d = dict()
import collections
for w in words:
    alpha = sorted(w.lower())
    in_alphabet = [l for l in alpha if l in alphabet] # filter out any character not in the alphabet, including spaces https://realpython.com/list-comprehension-python/
    a = sorted(in_alphabet)
    c = dict(collections.Counter(a)) # provide the number of occurrences of each letter in each word and arrange alphabetically
    
    for k, v in c.items(): #this for loop taken from StackOverflow: https://stackoverflow.com/questions/47082410/keep-highest-value-of-duplicate-keys-in-dicts
        if k not in d or d[k] < c[k]:
            d[k] = c[k]

# alphabetically sort the new dictionary of letters (keys) and corresponding counts (values), put into string format to be able to print in desired format
# Print with this format: a(2), b, c, d(3),...
s = ""
for k,v in sorted(d.items()): # https://stackoverflow.com/questions/16600174/return-output-of-dictionary-to-alphabetical-order
    if d[k] != 1:
        s = s + str(k) + "(" + str(d[k]) + "), "
    else:
        s = s + str(k) + ", "

print(s[:-2]) # print final output eliminates the comma and space after the last printed element
