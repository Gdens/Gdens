from random import shuffle as shuf
import os

def clear():
    os.system("cls" if os.name == 'nt' else 'clear')

score = 0

question_list = ["Baseball", "Basketball", "Football", "Hockey"]
other_list = ["A", "B", "C", "D"]

clear()
answer = ""
correct = "Baseball"
print("Which sport is my favorite?\n")
shuf(question_list)
for letter, sport in zip(other_list, question_list):
    print(f"  {letter}. {sport}")
while answer not in other_list:
    answer = input().upper()
if other_list.index(answer) == question_list.index(correct):
    print("Correct")
    score = score + 1
else:
    print("Wrong!")


question_list = ["365", "52", "450", "10"]
other_list = ["A", "B", "C", "D"]

clear()
answer = ""
correct = "365"
print("How many days are in a year?\n")
shuf(question_list)
for letter, sport in zip(other_list, question_list):
    print(f"  {letter}. {sport}")
while answer not in other_list:
    answer = input().upper()
if other_list.index(answer) == question_list.index(correct):
    print("Correct")
    score = score + 1
else:
    print("Wrong!")

question_list = ["Blue", "Green", "Yellow", "Grey"]
other_list = ["A", "B", "C", "D"]

clear()
answer = ""
correct = "Blue"
print("What color is the sky?\n")
shuf(question_list)
for letter, sport in zip(other_list, question_list):
    print(f"  {letter}. {sport}")
while answer not in other_list:
    answer = input().upper()
if other_list.index(answer) == question_list.index(correct):
    print("Correct")
    score = score + 1
else:
    print("Wrong!")


question_list = ["Purple", "Green", "Red", "Water"]
other_list = ["A", "B", "C", "D"]


clear()
answer = ""
correct = "Purple"
print("What color is the rain?\n")
shuf(question_list)
for letter, sport in zip(other_list, question_list):
    print(f"  {letter}. {sport}")
while answer not in other_list:
    answer = input().upper()
if other_list.index(answer) == question_list.index(correct):
    print("Correct")
    score = score + 1
else:
    print("Wrong!")

question_list = ["25", "65", "83", "52"]
other_list = ["A", "B", "C", "D"]

clear()
answer = ""
correct = "52"
print("How many weeks are in a year?\n")
shuf(question_list)
for letter, sport in zip(other_list, question_list):
    print(f"  {letter}. {sport}")
while answer not in other_list:
    answer = input().upper()
if other_list.index(answer) == question_list.index(correct):
    print("Correct")
    score = score + 1
else:
    print("Wrong!")


question_list = ["Sun", "British", "Mailman", "Rain"]
other_list = ["A", "B", "C", "D"]

clear()
answer = ""
correct = "Sun"
print("Here comes the _____?\n")
shuf(question_list)
for letter, sport in zip(other_list, question_list):
    print(f"  {letter}. {sport}")
while answer not in other_list:
    answer = input().upper()
if other_list.index(answer) == question_list.index(correct):
    print("Correct")
    score = score + 1
else:
    print("Wrong!")

question_list = ["Red", "Pink", "Purple", "Perriwinkle"]
other_list = ["A", "B", "C", "D"]

clear()
answer = ""
correct = "Pink"
print("What is my favorite color?\n")
shuf(question_list)
for letter, sport in zip(other_list, question_list):
    print(f"  {letter}. {sport}")
while answer not in other_list:
    answer = input().upper()
if other_list.index(answer) == question_list.index(correct):
    print("Correct")
    score = score + 1
else:
    print("Wrong!")

question_list = ["Thunder", "Sun", "Rain", "Storm"]
other_list = ["A", "B", "C", "D"]

clear()
answer = ""
correct = "Rain"
print("Have you ever seen the ______?\n")
shuf(question_list)
for letter, sport in zip(other_list, question_list):
    print(f"  {letter}. {sport}")
while answer not in other_list:
    answer = input().upper()
if other_list.index(answer) == question_list.index(correct):
    print("Correct")
    score = score + 1
else:
    print("Wrong!")

question_list = ["Thunderstruck", "Bad", "Gone", "Dancing"]
other_list = ["A", "B", "C", "D"]

clear()
answer = ""
correct = "Thunderstruck"
print("You've been _______?\n")
shuf(question_list)
for letter, sport in zip(other_list, question_list):
    print(f"  {letter}. {sport}")
while answer not in other_list:
    answer = input().upper()
if other_list.index(answer) == question_list.index(correct):
    print("Correct")
    score = score + 1
else:
    print("Wrong!")



question_list = ["Apple", "Bannana", "Cherry", "Date", "Elderberry", "Fig", "Gundam"]
other_list = ["A", "B", "C", "D", "E", "F", "G"]

clear()
answer = ""
correct = "Gundam"
print("Which one does not fit?")
shuf(question_list)
for letter, fruit in zip(other_list, question_list):
    print(f"  {letter}. {fruit}")
while answer not in other_list:
    answer = input().upper()
if other_list.index(answer) == question_list.index(correct):
    print("Correct")
    score = score + 1
else:
    print("Wrong!")

print("Score: " + str(score))
grade = score / 10

print("Grade: " + str(grade * 100) + "%")

if score >= 0.9:
    print("A")
if score == 0.8:
    print("B")
if score == 0.7:
    print("C")
if score == 0.6:
    print("D")
if score < 0.6:
    print("F")

