ques = [
    ["Q1. Which language was used to create Facebook ?", "1. Python", "2. Java", "3. PHP", "4.None", 3],
    ["Q2. Which data structure is needed to convert infix notation to postfix notation ?", "1. Tree", "2. Branch", "3. Stack", "4. Queue", 3],
    ["Q3. Which of the following refers to the rectangular area for displaying information and running programs ?", "1. Desktop ", "2. Dialog box", "3. Menu ", "4. Windows", 4],
    ["Q4. The information you put into the computer is called ?", "1. facts ", "2. data ", "3. files ", "4. directory ", 2],
    ["Q5. What is 1+1", "1. 2", "2. 3", "3. 1", "4. 9", 1]
        ]

money = 0
price = [1000, 2000, 5000, 10000, 50000]

for i in range(0, len(ques)):
    q = ques[i]
    print(f"Question for RS {price[i]}")
    print("\n", q[0])
    print(f"{q[1]}       {q[2]}")          
    print(f"{q[3]}       {q[4]}")
    
    ans = int(input("Enter the answer (1-4): "))
    
    if(ans == q[-1]):
        print(f"Correct Answer! You won {price[i]} \n\n")
        
        if(i==2):
            money = 5000
        elif(i == 4):
            money = 50000
    else:
        print("Wrong Answer")
        break
    
print(f"You won {money} in total")