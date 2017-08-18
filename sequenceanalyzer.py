import numpy as np
import pandas as pd

'''
Name: calc_probs
Input:
    *X: sequence to be analyzed
    *L: maximum sub-sequence length to be analyzed.
Output: 
    *probabilities: a list of dictionaries. Each dictionary contains keys
     that are sequences of the same length. The value associated to a key
     is a probability of that subsequence appearing in the original sequence
    *alphabet: the unique symbols that appear in the sequence.
Description:
    Checks the number of occurances of subsequences of lengths from 1 to L.
    Divides the number of occurances by the sequence's length in order to
    obtain relative frequencies. Creates a dictionary for subsequences of 
    each length. When checking for subsequences of length 1, the method 
    records each individual symbol that appears and stores it as the
    sequence's alphabet.
'''             
def calc_probs(X, L):
    #Output lists, initialized as empty lists:
    probabilities = []
    alphabet = []
    print("Calculating subsequence probabilities")
    print("L = " + str(L))
    #This first loop iterates the subsequence length to be analyzed:
    for l in range(1, L + 1):
        print("Calculating probabilities of subsequences of length: " + str(l))
        current_probs = {} #Dictionary storing the probabilities of current l
        #This loop traverses the string counting occurences of subsequences:
        for i in range(0, len(X) - (l - 1)):
            #current_value stores a string with the subsequence from position
            #i to position i+l
            current_value = ''.join(str(e) for e in X[i:i+l])
            #When l is 1, the unique symbols are stored in alphabet:
            if l == 1:
                if not (current_value in alphabet):
                    alphabet.append(current_value)
            #If the key for current_value has not appeared yet, it is created
            #and its count starts at 1.
            if not current_value in current_probs.keys():
                current_probs[current_value] = 1
            #If the key has already shown up, its count is incremented.
            else:
                current_probs[current_value] += 1
        #After the sequence is analyzed, the counts for each key are divided by
        #the sequence's length in order to get probabilities:
        for key in current_probs.keys():
            current_probs[key] /= float(len(X))
        probabilities.append(current_probs)
    print("*****************")
    print("Probabilities calculated!")
    print("*****************")
    return [probabilities, alphabet]
