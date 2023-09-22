from art import logo
import os
print(logo)

print("Welcome to the secret auction program.")

def highest(bid_data):
    highest_bid = 0
    winner = ""
    for bidder_key in bid_data:
        bid_amount = bid_data[bidder_key]
        if bid_amount > highest_bid:
           highest_bid = bid_amount
           winner = bidder_key
    print(f"The winner is {winner} with a bid of €{highest_bid}")

bid = {}
should_end = False
while not should_end:
    name = input("What's your name? \n").capitalize()
    price = int(input("What's your bid? \n€"))
    bid[name] = price
    restart = input("are there other users who want to bid? yes(type y) or no(type n? \n")
    if restart == "n":
        should_end = True
        highest(bid)
    elif restart == "y":
        os.system("cls")
    else:
        print("Invalid data!")
        break


