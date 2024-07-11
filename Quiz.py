"""
A quiz program that randomizes the order of 10 questions and gives you a percentage score. It also tracks the highest score you have gotten.
"""

import random

#All Questions
quiz = {
    "question1": {
        "question": "Which planet is closest to the sun?",
        "answer": "mercury"
    },
    "question2": {
        "question": "What is 2x32? (Answer with an integer)",
        "answer": "64"
    },
    "question3": {
        "question": "In which ocean does Hawaii reside?",
        "answer": ["pacific ocean", "pacific"]
    },
    "question4": {
        "question": "How many sides does a dodecagon have?",
        "answer": "12"
    },
    "question5": {
        "question": "Who was the first president of the United States? (Answer with full name)",
        "answer": "george washington"
    },
    "question6": {
        "question": "How many atoms are in one H2O molecule? (Answer with an integer)",
        "answer": "3"
    },
    "question7": {
        "question": "Which country is the Leaning Tower of Pisa in?",
        "answer": "italy"
    },
    "question8": {
        "question": "In football, how many yards are in a typical down? (Answer with an integer)",
        "answer": "10"
    },
    "question9": {
        "question": "Name one of the four major brain lobes.",
        "answer": ["frontal", "frontal lobe", "parietal", "parietal lobe", "temporal",\
                    "temporal lobe", "occipital", "occipital lobe"]
    },
    "question10": {
        "question": "What is 7595 rounded to the nearest tenth? (Answer with an integer)",
        "answer": "7600"
    }
}

high_score = 0

percent = lambda a,b: int(a*100/b) 

def start_quiz():
    """
    Starts a single quiz round where the order of questions is randomized
    """
    number_list = []
    global length
    length = len(quiz)
    for i in range(length):
        number_list.append(i+1)
    score_counter = 0
    global high_score

    random.shuffle(number_list)

    for i in range(length):
        choice = number_list.pop()
        question = f"question{(choice)}"
        answer = input(f"{quiz[question]["question"]}\n").lower().strip()


        if type(quiz[question]["answer"]) == list:
            if answer in quiz[question]["answer"]:
                score_counter += 1
                print(f"Correct!\nScore: {score_counter}\n")
            else:
                temp_list = enumerate(quiz[question]["answer"])
                print_statement = ""
                for item in temp_list:
                    if item[0] == 0:
                        print_statement += item[1]
                    else:
                        print_statement += f" or {item[1]}"
                print(f"Incorrect\nThe accepted answers were {print_statement}.\nScore: {score_counter}\n")
        else:
            if answer == quiz[question]["answer"]:
                score_counter += 1
                print(f"Correct!\nScore: {score_counter}\n")
            else:
                print(f"Incorrect\nThe correct answer is {quiz[question]["answer"]}\nScore: {score_counter}\n")
    
    print(f"\nYou answered {score_counter} out of {length} questions correctly")
    print(f"Your percentage of correct answers is {percent(score_counter, length)}%\n")

    if score_counter > high_score:
        high_score = score_counter
        print(f"You got a new high score! Your new high score is {percent(high_score, length)}%")



accepted = ["y", "yes", "n", "no"]
accepted_yes = ["y", "yes"]
keep_playing = True

#Allows for repeated play and tracking of high score
while keep_playing:
    next_step = False
    start_quiz()

    answer = input("\nWould you like to keep playing (Y/N)?\n").lower().strip()
    while next_step == False:
        if answer in accepted:
            next_step = True
            if answer in accepted_yes:
                continue
            else:
                print(f"\nThank you for playing! Your high score was {percent(high_score, length)}%.")
                keep_playing = False
        else:
            print("That is not an accepted answer. Please try again.")
