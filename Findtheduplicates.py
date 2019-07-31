import math
n = int(input())
student_marks = {}
for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
query_name = input()
if query_name in student_marks:
        sum = sum(student_marks[query_name])
        print(sum)
        n = len(student_marks[query_name])
        output  = math.floor(sum/n)
        print(output)
else:
        print("The",query_name,"is not exists in dictionary")
