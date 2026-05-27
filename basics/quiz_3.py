def new_game():
    guesses = []
    correct_guesses = 0

    for question_num, (question, options) in enumerate(questions.items(), start=1):
        print("\n" + question)
        for option in options:
            print(option)

        guess = input("Enter (A, B, C, or D): ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(options, guess)

    display_score(correct_guesses)

def check_answer(options, guess):
    if guess in ['A', 'B', 'C', 'D']:
        correct_option = options[0]
        return guess == correct_option
    else:
        print("Invalid input! Skipping question.")
        return False

def display_score(correct_guesses):
    score = (correct_guesses / len(questions)) * 100
    print(f"\nYou got {int(score)}%")

def play_again():
    response = input("Do you want to play again? (Yes or no): ").lower()
    return response == "yes"

# Dictionary to hold all the questions and options
questions = {
    "Q1: Who created Python?": ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
    "Q2: Which collection is ordered, changeable, and allows duplicate members?": ["A. Tuple", "B. List", "C. Dictionary", "D. Set"],
    "Q3: How do you insert COMMENTS in Python code?": ["A. //this is a comment", "B. /*This is a comment", "C. #This is a comment", "D. *This is a comment"],
    "Q4: Python is attributed to which comedy group?": ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
    "Q5: Which Method can be used to remove any whitespace from both the beginning and the end of a string?": ["A. ptrim()", "B. trim()", "C. len()", "D. strip()"],
    "Q6: Which Operator has higher precedence in the following list?": ["A. %", "B. &", "C. **", "D. >"],
    "Q7: What year was Python created?": ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
    "Q8: Which one is not a legal variable name?": ["A. _myvar", "B. my_var", "C. Myvar", "D. my-var"],
    "Q9: What is the correct file extension for Python?": ["A. .pt", "B. .py", "C. .pyth", "D. .py"],
    "Q10: Which method can be used to replace parts of a string?": ["A. replace()", "B. switch()", "C. repl()", "D. replaceString()"]
}

if __name__ == "__main__":
    play = True
    while play:
        new_game()
        play = play_again()

    print("\nThank you for playing! Goodbye!")
