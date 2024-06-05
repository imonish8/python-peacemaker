'''
Given an integer, , print the following values for each integer  from  to :
Decimal
Octal
Hexadecimal (capitalized)
Binary

link : https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true
'''

def print_formatted(number):
    # your code goes here
    width = len(bin(n)) - 2
    for i in range(1,n+1):
        val_i = str(i)
        val_oct= str(oct(i)[2:])
        val_hex= str(hex(i)[2:].upper())
        val_bi =  str(bin(i)[2:])
        print(val_i.rjust(width),val_oct.rjust(width), val_hex.rjust(width), val_bi.rjust(width) )
     

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)