#---------------------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for q in questions_quiz:
        print("-------------------")
        print(q)
        for opts in options[question_num-1]:
            print(opts)
        guess = input("Enter (A, B, C or D): ").upper()
        guesses.append(guess)



        correct_guesses += check_answer(questions_quiz.get(q), guess)
        question_num += 1
    display_score(correct_guesses, guesses)
#---------------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("Answer correct!")
        return 1
    else:
        print("Answer Wrong!")
        return 0 
    
#---------------------------------
def display_score(correct_guesses, guesses):
    print("----------------------")
    print("RESULTS:")
    print("----------------------")

    print("Answers: ", end="")
    for a in questions_quiz:
        print(questions_quiz.get(a), end=" ")
    print()

    print("Guesses: ", end="")
    for g in guesses:
        print(g, end=" ")
    print()

    score = int ((correct_guesses/len(questions_quiz))*100)
    print("Your score is: "+str(score)+"%")

#---------------------------------
def play_again():
    response = input("Do you want to play again? (yes or no):")
    response = response.lower()

    if response == "yes":
        return True
    else:
        return False

questions_quiz = {
    "Who created Python?: ": "A",
    "What year was Pyhton created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the earth round?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smoth", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]]

new_game()
while play_again():
    new_game()
print("Thanks for playing!")
