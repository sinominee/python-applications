import os

bids = {}
bidding_finished = False

def find_highest_bid(bidding_record):
    highest_bid = 0 
    for bidder in bidding_record:
        bid_amount = bidder_amount


while not bidding_finished:
    name = input("Enter your name? \n")
    price = int(input("Enter your Bid? \n $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.")
    if should_continue == "no":
        bidding_finished = True
    elif should_continue == "yes":
        os.system("cls")


