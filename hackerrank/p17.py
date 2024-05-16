'''
16 may
We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).
Let's try to understand this with an example.
You are given an immutable string, and you want to make changes to it.

link :https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true

'''


def mutate_string(string, position, character):
    list_string = list(string)
    list_string.pop(position) #removed first poped out
    list_string.insert(position, character) # inserted then...
    string = ''.join(list_string) # joined it again to make it look like original
    
   
    return string # printing/ returning to function

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
