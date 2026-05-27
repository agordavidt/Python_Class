"""
Date:15/08/2022
Program: A simple quiz program using logical statements (if, elif and else)
Author: David
"""

score = 0

print("Attempt the following questions: ")
print("**********************************")
question = input("What year did Nigeria become a republic: ")
if question == "1963":
    print("correct answer!")
    score += 2
else:
    print("wrong Answer")

question = input("what is name of Nigerian National Football Team: ")
if question == "super eagles":
    print("correct answer!")
    score += 2
else:
    print("wrong Answer")
question = input("What is the capital of Nigeria: ")
if question == "abuja" or question.casefold() == "fct" or question == "federal capital territory":
    print("correct answer!")
    score += 2
else:
    print("wrong Answer")
    score += 2
question = input("What year was Facebook founded: ")
if question == "2004":
    print("correct answer!")
    score += 2
else:
    print("wrong Answer")
question = input("Who is the president of Nigeria:")
if question == "Buhari":
    print("correct answer!")
    score += 2
else:
    print("wrong Answer")

total_score = int(score) * 10
print(f"You scored: {total_score}%")

