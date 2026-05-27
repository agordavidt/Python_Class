"""
A program to grade the results of students in their semester coursesbased on their score

100 - 80 = A
79 - 60 = B
59 - 40 = C
39 - 30 = D
29 - 0 = F
"""

score = int(input("Enter score: "))
if score >= 80 and score <= 100:
    print("A")
elif score >= 60 and score <= 79:
    print("B")
elif score >= 40 and score <= 59:
    print("C")
elif score >= 30 and score <= 39:
    print("D")
else:
    print("F")
