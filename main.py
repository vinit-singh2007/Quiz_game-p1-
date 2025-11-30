import random
from db import save_score_mysql
from question import questions

while True:
    score = 0
    ask = input("Do you want to start the quiz? yes/no: ")
    
    if ask.lower() == "yes":
        name = input("Enter your name: ")
        print("Welcome to the quiz game!!\n")

        random.shuffle(questions)

        for q in questions:
            print(q["question"])
            for opt in q["options"]:
                print(opt)
            
            ans = input("Enter the answer: ")
            if ans == q["answers"]:
                print("\nGreat!! You gave the right answer!\n")
                score += 1
            else:
                print("Wrong\n")

        print(f"Your score is: {score}/{len(questions)}\n")
        save_score_mysql(name, score)

    else:
        print("Thank you!!")
        break
