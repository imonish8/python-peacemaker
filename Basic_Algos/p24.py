# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())

while(T>0): 

 numberA = int(input())
 input_str = input()
 A = set(input_str.split())
 numberB = int(input())
 input_str2 = input()
 B = set(input_str2.split())

 if A.issubset(B):
    print("True")

 else:
    print("False")
 T -= 1


'''
You are given two sets,  and .
Your job is to find whether set  is a subset of set .

If set  is subset of set , print True.
If set  is not a subset of set , print False.

link : https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true 


'''