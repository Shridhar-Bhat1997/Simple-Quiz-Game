def new_game(): # function for our game
    guesses=[]
    correct_guesses=0
    question_num=1  # to represent 1st question
    
# ---------------------------------------------------------------------------    

# display all the questions

    for key in Questions:
        print("--------------------------------------------") # line break
        print(key)
        
        for i in Options[question_num-1]: # to display 1st list for the 1st question
            print(i)
        
        guess=input("Enter (A,B,C or D): ")
        guess=guess.upper()
        guesses.append(guess) # compare guesses with correct answers
        
        correct_guesses += check_answer(Questions.get(key),guess) # Questions.get(key) ie actual answer
        question_num=question_num+1 # increment question number by 1
     
    display_score(correct_guesses,guesses)
    
# -------------------------------------------------------------------------------------
        
 
def check_answer(answer,guess): # function to check our answers
    
    if answer==guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0
    
# ----------------------------------------------------------------------------------------

def display_score(correct_guesses,guesses): # function to display our scores
    print("-------------------------------------")
    print("RESULTS")
    print("--------------------------------------")
    
    print("Answers: ",end="")
    for i in Questions:
        print(Questions.get(i), end=" ")
    print()
    
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()
    
    score= int((correct_guesses/len(Questions))*100)
    print("Your score is: "+str(score) + "%")

# -------------------------------------------------------------------------------------

def play_again(): # function to play again the game
    response=input("Do you want to play again? (yes or no): ")
    response=response.upper()
    
    if response == "YES":
        return True
    else:
        return False
    
# -------------------------------------------------------------------------------------- 

# Create a dictionary which hold all questions and answers ...(key:value) pairs..
# Each key is a question, that I would like to ask...
# Each question has a associated value...

Questions={
    "Which Union Ministry organised the EU-India Green Hydrogen Forum? :":"B",
    "What is the rank of India in the UNDP’s Human Development Index 2021? :":"D",
    "Which is the venue of the SCO Defence Ministers’ Meeting held in 2022? :":"B",
    "In which year Python was created? :":"A"
    }

# 2D list of different answers
Options=[["A.Ministry of Power","B.Ministry of New and Renewable Energy","C.Ministry of External Affairs","D.Ministry of Commerce and Industry"],
         ["A.121","B.125","C.129","D.132"],
         ["A.Beijing","B.Tashkent","C.Shanghai","D.Nursultan"],
         ["A.1991","B.1998","C.1994","D.1999"]]

new_game()

while play_again():
    new_game()
    
print("Good Bye!")




    