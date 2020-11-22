if __name__ == '__main__':
    n = int(input("Enter the number of records: "))
    student_marks = {}
    
    for _ in range(n):
        name, *line = input("Enter name & marks: ").split()
        scores = list(map(float, line))
        scores = sum(scores)/3
        student_marks[name] = scores
    
    query_name = input("Enter query name: ")
    
    print('%.2f' % student_marks[query_name])