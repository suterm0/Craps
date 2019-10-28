# Michael Suter
# Craps assignment
# 10/21/19
from random import randint


def create():
    print("How much is your bankroll.")
    bank = int(input(">> "))
    if bank <= 0:
        print("Invalid input. The game will now exit")
        exit()
    return bank


def roll_dice():
    minimum = 2
    maximum = 12
    roll = randint(minimum, maximum)
    input("Press enter to roll your die >>")
    print(f"You rolled a {roll}")
    return roll


def play_game():
    bank = create()
    # Added a while loop to make gameplay continue
    choice = 1
    while choice == 1:
        print(f"You have ${bank} available to gamble")
        print("How much would you like to bet?")
        bet = int(input(">> "))
        while bet > bank or bet <= 0:
            print(f'Invalid amount, you have ${bank}')
            print("How much would you like to bet?")
            bet = int(input(">> "))
        point = roll_dice()
        if point == 7 or point == 11:
            print("You Won congratulations")
            bank = bank + bet
            print(f"Your new bankroll is ${bank}")
        elif point == 2 or point == 3 or point == 12:
            print("You lost!")
            bank = int(bank - bet)
            print(f"Your new bankroll is ${bank}")
        else:
            print(f"Your point is now {point} you must roll this again to win.")
            print("If you roll a 7 then you lose.")
            total = roll_dice()
            print(total)
            while total != point and total != 7:
                print("Keep rolling!")
                #missing the total =
                total = roll_dice()
                print(total)
            if total == point:
                print("You have won!")
                bank = int(bank + bet)
                print(f"You now have ${bank}")
            elif total == 7:
                print("You lost!")
                bank = int(bank - bet)
                print(f"You now have ${bank}")
                # Not needed : return bank, total, point, bet
    print("Would you like to play again? 1 for yes, 2 for no:")
    choice = int(input())

# Not sure you need this function????
def after_play_game(bank, total, point, bet):
    while total != point or 7:
        print("Keep rolling!")
        roll_dice()
    if total == point:
        print("You have won!")
        bank = int(bank + bet)
        print(f"You now have ${bank}")
    elif total == point:
        print("You lost!")
        bank = int(bank - bet)
        print(f"You now have ${bank}")


#after_play_game()

print("""
Welcome to the dice game!
Rules:
1. If you roll a initial combined 7 or 11 you win!
2. If you roll a initial combined 2, 3 or 12 you lose!
3. If you roll none of the initial values then your first roll will be your point for the rest of the game.
4. If you roll your point then you win but if you roll a 7 after the first roll you lose
""")
play_game()


print("Would you like to keep playing? Type Y to start a new game or press N to exit.")
play_again = input("(Y/N)? >>")
while play_again == 'y' or 'Y':
    play_game()


print("Thanks for playing!")
print("Bye")
