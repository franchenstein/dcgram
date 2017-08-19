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

'''
Name: calc_cond_probs
Input:
    *L: maximum sub-sequence length to be analyzed.
Output: 
    *conditional_probabilities: a list of dictionaries. Each dictionary 
     contains keys that are of the form:
     symbol|subsequence
     meaning the probability of "symbol" occuring after that subsequence.
     There is one dictionary for each length of subsequence.
Description:
    Calculates the probability of each symbol in alphabet occuring each
    subsequence in probabilities and create a similiar dictionary for those
    conditional probabilities.
'''     
def calc_cond_probs(probabilities, alphabet, L):
    #Output initialized as empty list:
    conditional_probabilities = []
    print("Calculating subsequence conditional probabilities")
    print("L = " + str(L))
    if probabilities:
        #The first element, i.e. the probabilities of each symbol given the
        #empty string is just the probabilities of the occurence of those
        #symbols, i.e. the first element of the probabilities list.
        conditional_probabilities = [probabilities[0]]
        #This loop calculates the conditional probabilities of subsquences of
        #length greater than 0 given each symbol in the alphabet:
        for l in range(0, L):
            print("Calculating conditional probabilities of subsequences of length: " + str(l))
            d = {}
            l1 = probabilities[l]
            l2 = probabilities[l+1]
            for s in l1:
                for a in alphabet:
                    cond = a + "|" + s
                    t = s + a
                    if t in l2.keys():
                        d[cond] = l2[t]/l1[s]
                    else:
                        d[cond] = 0.0
            conditional_probabilities.append(d)
    else:
        print("Probabilities not computed.")
        print("Run calc_probs function before this one.")
    print("*****************")
    print("Conditional probabilities calculated!")
    print("*****************")
    return conditional_probabilities
