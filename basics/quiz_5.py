"""
A simple quiz game:
4 functions
Use case for functions 

"""

def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("                                ")
        print(key)
        for i in options[question_num - 1]:  #Using the list option index to interate one list after the other
            print(i)
        guess = input("Enter (A, B, C, or D): ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1
    display_score(correct_guesses)

def check_answer(answer, guess):
    if answer == guess:
        return 1
    else:
        return 0

def display_score(correct_guesses):
    score = (correct_guesses/len(questions)) * 100
    score = int(score)
    print(f"You got {score}%")

def play_again():
    response = input("Do you want to play again? (Yes or no): ").lower()
    if response == "yes":
        return True
    else:
        return False

#Dictionary to hold all the questions
questions = {
    "Q1: Who created Python?": "A",
    "Q2: Which collection is ordered, changeable, and allows duplicate members?": "B",
    "Q3: How do you insert COMMENTS in Python code? ": "C",
    "Q4: Python is attributed to which comedy group?": "C",
    "Q5: Which Method can be used to remove any whitespace from both the begining and the end of a string?": "D",
    "Q6: Which Operator has higher precedence in the following list": "C",
    "Q7: What year was python created": "B",
    "Q8: Which one is not a legal variable name?": "A",
    "Q9: What is the correct file extension for Python": "D",
    "Q10: Which method can be used to replace parts of a string?": "A"

}
#List of Lists (2D list to hold all the opitions)
options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
           ["A. Tuple", "B. List", "C. Dictionary", "D. Set"],
           ["A. //this is a comment", "B. /*This is a comment", "C. #This is a comment", "D. *This is a comment"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. ptrim()", "B. trim()", "C. len()", "D. strip()"],
           ["A. %", "B.&", "C. **", "D. >"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. _myvar", "B. my_var", "C. Myvar", "D. my-var"],
           ["A. .pt", "B. .py", "C. .pyth", "D. .py"], ["A. replace()", "B. switch()", "C. repl()", "D. replaceString()"]]

new_game()
# while play_again():
#     new_game()
#
# print("Bye!")
