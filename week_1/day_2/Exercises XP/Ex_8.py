data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

def questions ():
    correct_ans = 0
    wrong_answers = []
    for q in data:
        answer = input(q["question"] + " " )
        if answer.strip().lower()== q["answer"]:
            correct_ans += 1
        else :
            wrong_answers.append((q["question"], answer, q["answer"]))

    print(f"Correct answers: {correct_ans}")
    print(f"Wrong answers: {len(wrong_answers)}")

    if wrong_answers:
        print("Details of wrong answers:")
        for question, user_ans, correct_ans in wrong_answers:
            print(f"Q: {question}\nYour answer: {user_ans}\nCorrect answer: {correct_ans}\n")
        if len(wrong_answers) > 3:
            print("You had more than 3 wrong answers. Try again!")

questions ()
