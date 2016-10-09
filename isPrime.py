#!/usr/bin/python3

'''
Programmer: Kyle Kloberdanz
Date      : 9 Oct 2016
License   : GNU GPL v2

Description:
    give it an argument from cli to determine if it is prime or not,
    give no arguments to launch an interactive shell

    from the shell, type the number to check if it is prime. To find
    all numbers that make it composite, type "all" after the number,
        Example: 
	    > 4444 all
	    4444 =  2 * 2222
	    4444 =  4 * 1111
	    4444 =  11 * 404
	    4444 =  22 * 202
	    4444 =  44 * 101
	    4444 is NOT prime

'''

import math
import sys
import re

def isPrime(n, ALL=False):
    if n <= 1:
        return False

    s = int(math.sqrt(n) + 1)
    result = True
    # for i in range(2, s):
    s = int(math.sqrt(n) + 1)
    if ALL:

        for i in range(2, s):
            if n % i == 0:
                print(n, "= ", i, "*", int(n/i))
                result = False
        return result

    else:

        for i in range(2, s):
            if n % i == 0:
                print(n, "= ", i, "*", int(n/i))
                return False
        return True

def print_result(n, ALL=False):
    if isPrime(int(n), ALL):
        print(n, "is prime")
    else:
        print(n, "is NOT prime")

def execute(user_input):

    user_input_re = re.compile('^ *[0-9]+ *$|^ *[0-9]+ [a-zA-Z]+ *$')
    numbers_re    = re.compile('[0-9]+')

    if user_input == "":
        return

    if user_input == 'q' or user_input == 'exit':
        quit()

    m = user_input_re.search(user_input)
    num_match = numbers_re.search(user_input)
    if m and num_match:
        if "ALL" in user_input.upper():
            print_result(user_input[num_match.start() : num_match.end()], True)

        else: 
            print_result(int(user_input))
    else:
        print("error: not valid input")

if len(sys.argv) > 1:
    for term in sys.argv[1:]:
        execute(term)
else:
    while True:
        user_input = input("> ")
        execute(user_input)

