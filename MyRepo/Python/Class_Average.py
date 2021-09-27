total = 0
Student_names = []
students_grades = []
grade = {"A":4, "B":3, "C":2, "D":1, "F":0}
q = "y"
while q == "y":
    Student_names.append(input("list of name of students"))
    abc = input("enter student grades").upper()
    if abc in grade:
        students_grades.append(abc)
        if abc == "A":
            total = total + 4
        elif abc == "B":
            total = total + 3
        elif abc == "C":
            total = total + 2
        elif abc == "D":
            total = total + 1
        else:
            continue
    else:
        print("not a grade")
    while True:
        q = input("Do you want to continue")
        if q == "y" or q == "name":
            break
        else:
            print("Not valid")
for i, j in zip(Student_names, grade):
    print(f"  {i}. {j}")
GPA = total / len(Student_names)
print(GPA)

