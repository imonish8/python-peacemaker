# Enter your code here. Read input from STDIN. Print output to STDOUT

input_str = input()
A = set(input_str.split())

N = int(input())
flag = True

while(N>0):
    N -= 1
    input_str = input()
    others = set(input_str.split())
    
    if not A.issuperset(others):
        flag = False
      

if flag == True:
    print("True")
else:
    print("False")
    

'''
You are given a set  and  other sets.
Your job is to find whether set  is a strict superset of each of the  sets.
Print True, if  is a strict superset of each of the  sets. Otherwise, print False.
A strict superset has at least one element that does not exist in its subset.

link : https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true

'''