
'''
may 18 

link : https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
'''


N = int(input())
lst = []
    
    for _ in range(N):
        command = input().strip().split()
        cmd = command[0]
        if cmd == "insert":
            lst.insert(int(command[1]), int(command[2]))
        elif cmd == "print":
            print(lst)
        elif cmd == "remove":
            lst.remove(int(command[1]))
        elif cmd == "append":
            lst.append(int(command[1]))
        elif cmd == "sort":
            lst.sort()
        elif cmd == "pop":
            lst.pop()
        elif cmd == "reverse":
            lst.reverse()
            #########################################
            # match case approach 
for _ in range(N):
    command = input().strip().split()
    match command[0]:
        case 'print':
            print(lst)
            break
        case 'insert':
            lst.insert(int(command[1]), int(command[2]))
        case 'remove':
            lst.remove(int(command[1]))
        case 'append':
            lst.append(int(command[1]))
        case 'sort':
            lst.sort()
        case 'pop':
            lst.pop()
        case 'reverse':
            lst.reverse()
        