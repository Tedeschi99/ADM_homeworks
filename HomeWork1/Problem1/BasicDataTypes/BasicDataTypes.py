#runner up
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    
    top  = arr[0]
    runner = 0
    arr.sort(reverse=True)
    for i in range(0,n):
        if top < arr[i]:
            top = arr[i]
        if arr[i] != top:
            runner = arr[i]
            break      
    print(runner)

#List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    result = [
        [i, j, k]
        for i in range(x + 1)
        for j in range(y + 1)
        for k in range(z + 1)
        if i + j + k != n
    ]

    print(result)

#Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks = student_marks[query_name]
    average = sum(marks) / len(marks)

    print(f"{average:.2f}")

#Lists
if __name__ == '__main__':
    N = int(input())
    arr = []

    for _ in range(N):
        command = input().split()
        operation = command[0]

        if operation == "insert":
            arr.insert(int(command[1]), int(command[2]))

        elif operation == "print":
            print(arr)

        elif operation == "remove":
            arr.remove(int(command[1]))

        elif operation == "append":
            arr.append(int(command[1]))

        elif operation == "sort":
            arr.sort()

        elif operation == "pop":
            arr.pop()

        elif operation == "reverse":
            arr.reverse()

#Nested Lists
if __name__ == '__main__':
    Students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        Students.append([name, score])

    scores = [student[1] for student in Students]
    scores = sorted(set(scores))

    names = []

    for x in Students:
        if x[1] == scores[1]:
            names.append(x[0])

    names.sort()

    for i in names:
        print(i)

 #Tuples
 if __name__ == '__main__':
    n = int(raw_input())
    t = tuple(map(int, raw_input().split()))
    print hash(t)