# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def alphabetize():
    string = input("Enter a sentence to alphabetize.\n ")
    new_string = "".join(sorted(string)).strip()
    print(f'Alphabetized: {new_string}')

alphabetize()