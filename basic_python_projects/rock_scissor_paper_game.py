
import random
item_list = ["Rock","Scissor","Paper"]
user_choice = input("Enter your move = Rock, Scissor, Paper:= ")
comp_choice = random.choice(item_list)

print(f"User choice = {user_choice},computer choice = {comp_choice}")                                                                               

if user_choice == comp_choice:
    print("Both chooses same = MATCH Tie: ")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock: ,computer Win")
    else:
        print("Rock smashes scissor: You Win")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor Cuts Paper ,Computer Win")  
    else:
        print("paper covers rock ,Computer Win")

elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor Cuts paper: You Win ")
    else:
        print("Rock smashes Scissor,Computer Win ")    


