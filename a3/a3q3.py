##
## ===========================================================================
##  Azoacha Forcheh (20558994)
##  CS 234 Fall 2017
##  Assignment 03, Problem 3
## ===========================================================================
##
##
import check

# DONE: Need to account for numbers >= 10
# Idea: after finding first number, keep going w/out check until first "{"
# Do same to get the compressed string, but go until first "}"

# Need to account for nesting
def decompressFile(txt):
    f = open(txt, 'r')
    text = f.read()
    n =  len(text)

    # the decompressed string
    decomp = ""

    i = 0
    while i < n:
        chr = text[i]

        if chr.isalpha():
            decomp += chr

        if chr.isdigit():
            rep = ""
            pattern = ""

            while chr != "{":
                rep += chr
                i += 1
                chr = text[i]
            rep = int(rep)

            # chr is now at "{" - move to pattern
            while text[i+1] != "}":
                i += 1
                chr = text[i]
                pattern += chr

            decomp += pattern * rep

        i += 1

    return decomp

# Test 1: Basic case
check.expect("Question 3, Test 1", decompressFile("a3q3_test1.txt"),
             "aabcbcbc")

# Test 2: Nested strings
#check.expect("Question 3, Test 2", decompressFile("a3q3_test2.txt"),
#             "acccaccc")

# Test 3: Some parts of file are decompressed already
check.expect("Question 3, Test 3", decompressFile("a3q3_test3.txt"),
             "abcabcabccdcdef")

# Test 4: an empty file
check.expect("Question 3, Test 4", decompressFile("a3q3_test4.txt"), "")