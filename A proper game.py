import random
import time

#Dice function
def roll_dice():
    return random.randint(1,6)
#Single Player Mode
def single_player():
    score=0
    print("\n--- Single Player Mode ---")
    
    while True:
        input("Press Enter to roll 🎲 ")
        roll=roll_dice()
        print("You got:", roll)
        
        score+=roll
        print("Your total score:", score)
        
        choice=input("Roll again? (Yes/No): ").lower()
        print()
        
        if choice !="yes" and choice != "y":
            break
        
    print("final score:", score)
    print("Game over😎\n")
    
#👥 Multiplayer Mode
def multiplayer():
    p1_score=0
    p2_score=0
    rounds=5
    
    print("\n--- Multiplayer Mode ---")
    
    for i in range(rounds):
        print(f"\nround {i+1}")
        
        input("Player 1 press Enter 🎲")
        p1=roll_dice()
        print("Player 1 got:", p1)
        p1_score += p1
        
        input("Player 2 press Enter 🎲")
        p2=roll_dice()
        print("Player 2 got:", p2)
        p1_score  += p2
        
    print("n\--- Final Scores ---")
    print("player 1:", p1_score)
    print("player 2:", p2_score)
    
    if p1_score > p2_score:
        print("🏆 Player 1 wins!")
    elif p2_score > p1_score:
        print("🏆 Player 2 wins!")
    else:
        print("It's a Draw 😎")
        
    print()
    
#🎮 Main Menu
def main():
    while True:  
            print("==== DICE GAME MENU ====")
            print("1. Single Player")
            print("2. Multiplayer")
            print("3. Exit")
            
            choice = input("Enter your choice:")
            
            if  choice == "1":
                single_player()
            elif choice == "2":
                multiplayer()
            elif choice == "3":
                print("Exiting game... Bye 👋")
                break
            else:
                print("invalid choice! Try again.\n")
                
# Run the game
main()