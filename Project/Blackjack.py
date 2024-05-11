## Black Jack Project\
import random
import os


def Check():
    Start = input("Do you want to play a game of BlackJack? Type 'y' or 'n' : ").lower()
    if(Start == "y"):
        return(True)
    else:
        return(False)
    pass

def Card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return(card)
    pass

if Check(): 
    while True:
        os.system('cls')
        My_Card = []
        PC_Card = []
        My_Score = 0
        PC_Score = 0
        index = 0    
        for i in range(0,2):

            My_Card.append(Card())
            PC_Card.append(Card())
            My_Score +=  My_Card[i]
            PC_Score += PC_Card[i]
        

        while True:
            print(f"    Your Cards : {My_Card}, current score : {My_Score}")
            print(f"    Computer's first card : {PC_Card[0]}")
        

            Pass = input("Type 'y' to get another card, type 'n' to pass : ").lower()
            
            if Pass ==  "y":
                if PC_Score < 15:
                    PC_Card.append(Card())
                    PC_Score+= PC_Card[2+index]
                    
                if My_Score < 21:

                    My_Card.append(Card())
                    My_Score+= My_Card[2+ index]

                if My_Score > 21:
                    print(f"    Your final hand : {My_Card},final score : {My_Score}")
                    print(f"    Computer's final hand :{PC_Card}, final score : {PC_Score}")     
                    if My_Score < 21 or My_Score >= PC_Score :
            
                        if PC_Score == My_Score :
                         print("Draw")
                         break
                        if My_Score > 21 or My_Score <= PC_Score:
                            print("Lose")
                            break

                        if PC_Score > 21 or My_Score >= PC_Score:
                            print("Win")
                    break
                        
                
                  

            if Pass == "n":
                  print(f"    Your final hand : {My_Card},final score : {My_Score}")
                  print(f"    Computer's final hand :{PC_Card}, final score : {PC_Score}")
                  
                  if My_Score < 21 or My_Score >= PC_Score :

                    if PC_Score == My_Score :
                         print("Draw")
                         break
    
                    if PC_Score > 21 or My_Score >= PC_Score:
                            print("Win")
                            break
                    if My_Score > 21 or My_Score <= PC_Score:
                            print("Lose")
                            break
                    
                  
                  break
            index+=1
        Agian  = input("Do you want to play agian type 'y' or 'n' : ").lower(   )
        if Agian == "n":    
             break

    

else : print("No") 