#!/usr/bin/env python3
# This program allows the user to input a set of words, breaks each word into individual
# letters, counts occurrences of each letter, sorts alphabetically and prints only highest number of occurrences
# of each letter in any single word. Sample input: apple banana orange  Sample output: a(3), b, e, g, l, n(2), o, p(2), r

# TO DO: 
# Use functions for blocks of code
# Add assert statements to check validity of code

import collections, string # modules in the standard python library 

def letter_sort():
    # iterate over each word's letters and count letter occurrences, then add highest number of occurrences of each letter to new dictionary
    final_dict = dict()
    for w in words:
        alpha = [l for l in w if l in alphabet] # uses list comprehension to filter out any character not in the alphabet, including spaces https://realpython.com/list-comprehension-python/
        count_dict = dict(collections.Counter(alpha)) # provide the number of occurrences of each letter in each word and arrange alphabetically

        for k, v in sorted(count_dict.items()): # send highest letter count for each letter into new dictionary, d
            if k not in final_dict or final_dict[k] < count_dict[k]:
                final_dict[k] = count_dict[k]
    #assert
    return final_dict
    
def final_form():
    # Print with this format: a(3), b, c, d(2),...
    strung_out = ""
    for k,v in sorted(final_dict.items()):
        if final_dict[k] != 1:
            strung_out = strung_out + str(k) + "(" + str(final_dict[k]) + "), "
        else:
            strung_out = strung_out + str(k) + ", "
    #assert
    return 

def main():
    # Declare global variables
    alphabet = string.ascii_lowercase
    
    # Get the word(s) from the user
    print("Please enter the words and press [Enter]: ")
    wrdset = input("--> ").lower()
    
    # split the string of words into individual words and eliiminate unnecessary characters
    words = wrdset.replace("-", " ").replace(",", " ").replace("*", " ").split(" ") # delimiter = any character in wrdset that isn't in alphabet

    print(strung_out[:-2])

main()
