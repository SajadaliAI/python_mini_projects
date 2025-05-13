print("************")
print("WELLCOME TO MY QUIZ GAME")
question_bank = [
    {"text"  : "the ability of one class to acquired methods and attributes of an other class is called ____.",
     "answer":"A"},
     {"text" :  "which of the following is a type of inheritance?","answer":"D"},
     {"text" : "What type of inheritance has multiple subclasses to a single superclass?","answer":"C"},
     {"text" :"Whta is depth of multilevel inheritance in python?","answer":"C"},
     {"text" :"What does MRD stand for?","answer":"B"}

]
options = [["A. Inheritance","B. Abstraction","C.Multiple","D. objects"],
           ["A.single","B.double","C.Multiple","D.both A and B"],
           ["A. Multiple inheritance","B.Multilevel Inheritance","C.Hirarchical Inheritance","D. both A and C"],
           ["A. Two level","B.Three level","C. Any Level","D None of these"],
           ["A. Method recursive object","B. Method resolution Order","C. Main resolution order","D.Method resolution Object"], 
]
score=0
def check_answer(user_guess,correct_answer):
    if user_guess==correct_answer:
        return True
    else:
        False
for question_num in range(len(question_bank)):
    print("*************")
    print(question_bank[question_num]["text"])
    for i in options[question_num]:
        print(i)

    guess = input("Enter your answer(A/B/C/D): ").upper()    
    is_correct=check_answer(guess,question_bank[question_num]["answer"])
    if is_correct:
        print("Correct Answer")
        score +=1
    else:
        print("Not_correct Answer")
        print(f"the correct answer is {question_bank[question_num]["answer"]}")
    print(f"your correct score is{score}/{question_num+1}")    
print(f"you have given {score} coreect answer ")    
print(f"your score is{(score/len(question_bank))*100}%")    
   
