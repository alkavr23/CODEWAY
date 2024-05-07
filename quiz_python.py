print("Welcome to the Quiz Game!")
print("Rules: You will be asked a series of questions. Answer each question correctly to earn points.")

play_again = "yes"
while play_again.lower() == "yes":
    questions = ("When is International Women’s Day celebrated globally?",
                 "Who was the first woman to win a Nobel Prize ",
                 "Who is the first female Indian President to belong to the tribal community?",
                 " Who was the first woman to go into space? ",
                 "Which country first gave women the right to vote? ",
                 "------- was the first woman to fly solo across the Atlantic Ocean in 1932.")

    options = (("A. March 8", "B. April 12", "C. December 8", "D. August 10"),
                       ("A. Mother Theresa", "B. Marie Curie", "C. Indira Gandhi", "D. Malala Yousfzai"),
                       ("A. Dr Bharati Pravin Pawar", "B.  Pratibha Patil", "C. Sonia Gandhi", "D. Droupadi Murmu"),
                       ("A. Kalpana Chawla", "B. Sunita Williams", "C. Valentina Tereskova", "D. Sally Ride"),
                       ("A. New Zealand", "B. England", "C. America", "D. China"),
                       "")

    answers = ("A", "B", "D", "C", "A","AMELIA EARHART")
    guesses = []
    score = 0
    question_num = 0

    for question in questions:
        print("\n")
        print(question)
        for option in options[question_num]:
            print(option)

        guess = input("Enter the answer: ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            score += 1
            print("CORRECT!")
        else:
            print("INCORRECT!")
            print(f"{answers[question_num]} is the correct answer")
        question_num += 1
    print("\n")
    print("       RESULTS        ")
    print("\n")

    print("answers: ", end="")
    for answer in answers:
        print(answer, end=" ")
    print()

    print("guesses: ", end="")
    for guess in guesses:
        print(guess, end=" ")
    print()

    score = int(score / len(questions) * 100)
    print(f"Your score is: {score}%")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again=="no":
        print("Thanks for playing.")

