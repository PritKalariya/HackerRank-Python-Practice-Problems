if __name__ == '__main__':
    students = []
    marks = []
    names = []

    for _ in range(int(input("Enter the number of students: "))):
        name = input("Enter the name: ")
        score = float(input("Enter the score: "))
        students.append([name, score])
        marks.append(score)    

    marks = sorted(set(marks))
    second_higgest = marks[1]

    for student in students:
        if second_higgest == student[1]:
            names.append(student[0])

    names.sort()

    for name in names:
        print(name)