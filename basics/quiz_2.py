"""
Date: 15/08/2022
Program: Multi-Choice Exammination program
Author: David

"""
marks = 0
print("INSTRUCTION: \nAttempt All Questions \n**********************")
print("1. Which of the following is an IDE. ")
ans = ["a. Ms Word", "b. CorelDRAW", "c. VS Code", "d. Google Sheets"]
for i in ans:
    print(i)
qus = input("Choose the correct answer: ")
if qus == "c":
    print("correct answer")
    marks += 2
else:
    print("wrong answer")
print("2. What year was python created ")
ans = ["a. 2005", "b. 1991", "c. 2017", "d. 1998"]
for i in ans:
    print(i)
qus = input("Choose the correct answer: ")
if qus == "b":
    print("correct answer")
    marks += 20
else:
    print("wrong answer")
print("3. The following are OS except ")
ans = ["a. linux", "b. windows", "c. firefox", "d. Mac"]
for i in ans:
    print(i)
qus = input("Choose the correct answer: ")
if qus == "b":
    print("correct answer")
    marks += 20
else:
    print("wrong answer")
print("4. Which is a correct way to write comment in python ")
ans = ["a. /*Comment*/", "b. <!--comment-->", "c. //comment", "d. #comment"]
for i in ans:
    print(i)
qus = input("Choose the correct answer: ")
if qus == "d":
    print("correct answer")
    marks += 20
else:
    print("wrong answer")
print("5. python is a lower level programming language:  ")
ans = ["a. yes", "b. no", "c. a and b", "d. sometimes"]
for i in ans:
    print(i)
qus = input("Choose the correct answer: ")
if qus == "b":
    print("correct answer")
    marks += 20
else:
    print("wrong answer")

if marks >= 60:
    print(f"{marks}% \nCongratulations! You are qualified")
else:
    print(f"{marks}% \nyou can try again next time")



