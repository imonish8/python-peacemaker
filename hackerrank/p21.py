'''
May 18 

link : https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true

'''

def average(array):
    new_set = set()
    
    
    for item in arr:
        new_set.add(item)
  
    sumValue = sum(new_set)
    lengthSet = len(new_set)
    averageSum = sumValue/lengthSet 
   
    return averageSum

'''
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
'''
