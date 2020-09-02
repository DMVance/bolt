#!/usr/bin/env python3
# This program allows the user to input a set of words, breaks each word into individual
# letters, counts occurrences of each letter, sorts alphabetically and prints only highest number of occurrences
# of each letter in any single word. Sample input: apple banana orange  Sample output: a(3), b, e, g, l, n(2), o, p(2), r

import collections, string # modules in the standard python library 

# Get the word(s) from the user
print("Please enter the words and press [Enter]: ")
wrdset = input("--> ").lower()

# split the string of words into individual words and eliiminate unnecessary characters
words = wrdset.replace("-", " ").replace(",", " ").replace("*", " ").split() # delimiter = any character in wrdset that isn't in alphabet

# iterate over each word's letters and count letter occurrences, then add highest number of occurrences of each letter to new dictionary
alphabet = string.ascii_lowercase # provides the lowercase alphabet
final_dict = dict()
for w in words:
    alpha = [l for l in w if l in alphabet] # uses list comprehension to filter out any character not in the alphabet, including spaces
    count_dict = dict(collections.Counter(alpha)) # provide the number of occurrences of each letter in each word
    
    for k, v in sorted(count_dict.items()): # send highest letter count for each letter into new dictionary, final_dict, and arrange alphabetically
        if k not in final_dict or final_dict[k] < count_dict[k]:
            final_dict[k] = count_dict[k]

# Format like this: a(3), b, c, d(2),...
strung_out = ""
for k,v in sorted(final_dict.items()):
    if final_dict[k] != 1:
        strung_out = f"{strung_out}{str(k)}({str(final_dict[k])}), "
    else:
        strung_out = f"{strung_out}{str(k)}, "

print(strung_out[:-2]) # print final output and eliminate the comma and space after the last element
