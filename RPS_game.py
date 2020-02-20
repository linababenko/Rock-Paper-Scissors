# Rock Paper Scissors'
import random
from colorama import Fore, Style

# print(Fore.BLUE + "Hello World")
# print(Style.RESET_ALL) #сбросить настройки цвета


stats_count = {'user': 0, 'bot': 0, 'draw': 0}

WIN_LIST = [('R', 'S'),
            ('S', 'P'),
            ('P', 'R')]

SELECTIONS_LIST = ['R', 'P', 'S']


def GAME():
    while True:
        start = input(Style.BRIGHT + Fore.LIGHTBLUE_EX +
                      "***************************************************"
                      "\n*              Rock-Paper-Scissors                *"
                      "\n***************************************************"
                      "\n*                                                 *"
                      "\n***************************************************"
                      "\n          Do you want to play? [Y], [n]")

        if start == 'n' or start == 'N':
            exit()
        elif start == 'Y' or start == 'y':
            while True:
                your_choice = str(input(Style.NORMAL + Fore.LIGHTBLUE_EX + "\n      <<<<< Choose {} >>>>> : ".format(
                    SELECTIONS_LIST)))  # user can..
                # choose in list
                your_choice = your_choice.upper()  # conversion to uppercase

                bot_choice = random.choice(['R', 'P', 'S'])

                if your_choice in SELECTIONS_LIST:
                    bot_choice = random.choice(SELECTIONS_LIST)

                    print("You: {}".format(your_choice))  # string formatting. Insert {your_choice}
                    print("Bot: {}".format(bot_choice))

                    match = your_choice, bot_choice

                if your_choice == bot_choice:
                    stats_count['draw'] += 1
                    print(Fore.YELLOW + "\nResult: Both are {}! So that's a draw!".format(your_choice))

                elif match in WIN_LIST:
                    stats_count['user'] += 1
                    print(Fore.LIGHTGREEN_EX + "\nResult: The power of {} beats {}! You won!".format(your_choice,
                                                                                                     bot_choice))

                else:
                    stats_count['bot'] += 1
                    print(Fore.RED + "\nResult: The power of {} is stronger than {}! You lost!".format(your_choice,
                                                                                                       bot_choice))

                print("\n_______  STATS  _______"
                      "\n  YOU  |  BOT  |  DRAW"
                      "\n   {user}       {bot}       {draw}"
                      "\n_______________________".format(**stats_count))

                if stats_count['user'] == 3:  # if player gets 5 points, he wins
                    print("The game is DONE! You won! Cool!")
                    exit()

                elif stats_count['bot'] == 3:  # if bot gets 5 points, he wins
                    print(
                        "The game is DONE! You lost! Try again")
                    exit()


# start the program
GAME()
