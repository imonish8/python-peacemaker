'''
16 may 
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, showing 2 places after the decimal.
16 May
'''

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
   # my code here down,,,

    marks = student_marks.get(query_name)
    
    
    average_Score = sum(marks)/ len(marks)
    
    print("{:.2f}".format(average_Score))
