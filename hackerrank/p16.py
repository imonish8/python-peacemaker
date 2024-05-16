'''
16 may

You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

link : https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true
'''


def split_and_join(line):
    # write your code here
    split_string = line.split(" ")
    final_string = "-".join(split_string)
    
    return final_string 
    
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
