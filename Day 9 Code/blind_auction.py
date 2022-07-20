import os
from auction_art import logo

#Function to clear terminal
def clear():
    os.system('cls')

print(logo)

bids = {}
bidding_finished = False

def find_winner(bidding_record):
    highest_bid = 0
    winner = ''
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f'The winner is {winner} with a bid of ${highest_bid}')

while not bidding_finished:
    name = input('What\'s your name bruh?: ')
    price = int(input('Enter your bid amount: $'))
    bids[name] = price
    should_continue = input('Are there any bidders? Type \'yes\' or \'no\': ')
    if should_continue == 'no':
        bidding_finished = True
        find_winner(bids)
    elif should_continue == 'yes':
        clear()