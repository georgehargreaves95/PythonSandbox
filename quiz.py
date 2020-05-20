def question1():
    question_answered = False
    answer = None
    while not question_answered:
        answer = int(input("What is 4 + 5?"))
        print(answer, type(answer))
        if type(answer) is int:
            question_answered = True
        else:
            print("Please enter a whole integer!")
        continue
    answers['Answer 1'] = str(answer)


def question2():
    question_answered = False
    answer = None
    while not question_answered:
        answer = input("What is the name of the Potions Professor in Harry Potter?")
        if type(answer) is not str:
            print("Please enter a name!")
        else:
            question_answered = True
        continue
    answers['Answer 2'] = answer


def question3():
    question_answered = False
    answer = None
    while not question_answered:
        answer = input(
            "Multiple Choice time! "
            "\n What is a Conker? "
            "\nA) A seed "
            "\nB) A type of Cheese "
            "\nC) A small automobile"
        )
        if answer == 'A' or answer == 'B' or answer == 'C':
            question_answered = True
        else:
            print("Please choose A, B, or C!")
        continue
    answers['Answer 3'] = answer


def calculate_correct_ansewrs():
    global correct_answers
    if answers['Answer 1'] == '9':
        correct_answers = correct_answers + 1
        print("Question 1 correct! Well done!")
    else:
        print("Question 1 incorrect, bad luck! Correct answer: 9")
    if answers['Answer 2'].lower().__contains__('snape'):
        correct_answers = correct_answers + 1
        print("Question 2 correct! Well done!")
    else:
        print("Question 2 incorrect, bad luck! Correct answer: Severus Snape")
    if answers['Answer 3'].lower() == 'a':
        correct_answers = correct_answers + 1
        print("Question 3 correct! Well done!")
    else:
        print("Question 3 incorrect, bad luck! Correct answer: A, a seed.")


def output_totals():
    if correct_answers == 3:
        print("Excellent! You got all answers correct!")
    elif correct_answers == 0:
        print("Oh no! You got no correct answers, better luck next time!")
    else:
        print("Not bad! You got %s out of %s questions correct, good work!" % (correct_answers, number_of_questions))


print("Welcome to the quiz!")
answers = {'Answer 1': "", 'Answer 2': "", 'Answer 3': ""}
correct_answers = 0
number_of_questions = 3
question1()
question2()
question3()
calculate_correct_ansewrs()
output_totals()
