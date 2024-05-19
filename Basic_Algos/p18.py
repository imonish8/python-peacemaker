'''
16 may 

Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of .
Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

link : https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true
'''

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
integer_tuple = tuple(integer_list)

result = hash(integer_tuple)

print(result)
