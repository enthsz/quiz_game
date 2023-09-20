questions = ("What is the capital city of France?: ",
             "What is the largest mammal in the world?: ",
             "Which Disney movie features a young lion named Simba?: ",
             "What is the main ingredient in guacamole?: ",
             "In which sport do teams compete to score goals by hitting a puck into the opponent's net?: ")



options = (("A. London","B. Berlin","C. Madrid","D. Paris"),
           ("A. Elephant","B. Giraffe","C. Blue Whale","D. Cheetah"),
           ("A. Beauty and the Beast","B. Aladdin","C. The Lion King","D. Frozen"),
           ("A. Tomatoes","B. Avocado","C. Onions","D. Mangoes"),
           ("A. Tennis","B. Soccer","C. Ice Hockey","D. Basketball"))


answers = ("d","c","c","b","c")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (a,b,c,d): ").lower()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")
    
    
    question_num += 1


print("------------------------")
print("-------RESULTS-------")
print("------------------------")


score = int(score / len(answers) * 100)
print(f"Your score was {score}%")








    
   




        
        

  
