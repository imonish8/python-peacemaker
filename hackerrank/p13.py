'''
You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
 For example, alison heck should be capitalised correctly as Alison Heck.
'''


# Complete the solve function below.
def solve(s):
    words = s.split()
    
    capitalized_words = ' '.join(word.capitalize() for word in words)
    
    
    return capitalized_words

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
