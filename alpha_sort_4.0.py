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

# For each word, sort the letters in alphabetical order, store as dict of lists
d = dict()
import collections
for w in words:
    alpha = sorted(w.lower())
    in_alphabet = [l for l in alpha if l in alphabet] # filter out any character not in the alphabet, including spaces
    a = sorted(in_alphabet)
    c = dict(collections.Counter(a)) # provide the number of occurrences of each letter in each word and arrange alphabetically
    
    for k, v in c.items():
        if k not in d or d[k] < c[k]:
            d[k] = c[k]

s = ""
for k,v in sorted(d.items()):
    if d[k] != 1:
        s = s + str(k) + "(" + str(d[k]) + "), "
    else:
        s = s + str(k) + ", "

print(s[:-2]) # eliminates the comma and space after the last printed element