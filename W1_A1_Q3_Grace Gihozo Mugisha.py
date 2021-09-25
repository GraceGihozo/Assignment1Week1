print("Welcome to ALU hangman")
Q1 = "when was ALU founded ?"
Q2 = "Who is the CEO of ALU?"
Q3 = "Where are ALU campuses"
Q4 = "How many campuses does ALU have?"
Q5 = "What is the name of ALU Rwanda’s Dean?"
Q6 = "Who is in charge of Student Life?"
Q7 = "What is the name of our Lab?"
Q8 = "How many students do we have in Year 2 CS?"
Q9 = "How many degrees does ALU offer?"
Q10 = "Where are the headquarters of ALU?"

Answer = {Q1: "2015", Q2: "Fred Swanike", Q3: "Rwanda and Mauritius", Q4: "2", Q5: "Gaidi Faraj", Q6: "Sila Ogidi",
          Q7: "Egypt", Q8: "57", Q9: "8", Q10: "Mauritius"}
name= input("please enter your name")
print("It's simple", name,)
print(" Let go")
score = 0
solution=0
mistake= 0
for A in Answer:
    solution= input("Enter the answer:")
    if solution == Answer[A]:
        score =score+1
        print("your are in right way", score )

    else:
        mistake =mistake+1
        print("you are hanging the man",score)
        if mistake ==6:
            print("Oops man dies")
            break
if score == 10:
    print("congratulation!!!you get all questions right.your man lives")
elif score >= 6:
    print("your man live, you had only"+mistake+"mistake question", score)






