def five_question_quiz():
    score = 0 # out of 5
    o = correct = "Well done!\n"
    x = incorrect = "Sorry, that's wrong\n"
    q1 = input("What is 1 + 1? ")
    feedback = ["You need to try harder", "Better luck next time", "Keep trying", "Not bad", "Nearly there!", "Nice work!"]
    if int(q1) == 2:
        score += 1
        print(o)
    else:
        print(x)
    q2 = input("What is 1 + 2? ")
    if int(q2) == 3:
        score += 1
        print(o)
    else:
        print(x)
    q3 = input("What is 1 + 3? ")
    if int(q3) == 4:
        score += 1
        print(o)
    else:
        print(x)
    q4 = input("What is 1 + 4? ")
    if int(q4) == 5:
        score += 1
        print(o)
    else:
        print(x)
    q5 = input("What is 1 + 5? ")
    if int(q5) == 6:
        score += 1
        print(o)
    else:
        print(x)
    percentage_score = "{}%".format(score / 5 * 100)

    print("You got {} out of 5 correct ({}). {}".format(score, percentage_score, feedback[score]))

five_question_quiz()

