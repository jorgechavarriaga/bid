from colorama import Fore, Back, Style
from art import logo
from os import system, name
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

bidders = {}
more_bidders = True
while more_bidders:
    clear()
    print(f"{Fore.RED}{logo}{Style.RESET_ALL}")
    print("Welcome to the secret auction program\n")
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid
    question = input("Are theere any other bidders? Type 'yes' or 'no'\n").lower()
    if question == "no":
        more_bidders = False
        max_value = max(bidders.values())
        max_key = max(bidders, key=bidders.get)
        clear()
        print(f"The winner is {max_key} with a bid of ${max_value}")

max = 0
winner = ""
for name in bidders:
    if bidders[name] > max:
        max = bidders[name]
        winner = name
    
print(f"The winner is {winner} with a bid of ${max}")