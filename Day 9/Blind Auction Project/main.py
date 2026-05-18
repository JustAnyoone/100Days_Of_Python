# TODO-1: Ask the user for input
import art

programming_dictionary = {
}



continue_bind = True
while continue_bind :
    print(art.logo)
    name = input(f"What's your name ? :")
    bid = int(input(f"Whats your bind ? :"))
# TODO-2: Save data into dictionary {name: price}
    programming_dictionary[name] = bid
    print(programming_dictionary)
# TODO-3: Whether if new bids need to be added
    again = input("Add another user bid [yes],[no]??").lower()
    if again == "yes" :
        print(f"\n" * 20)
    elif again == "no" :
        winner = ""
        highest_bid = 0
        for bidder in programming_dictionary:
            bid_amount = programming_dictionary[bidder]
            if bid_amount > highest_bid:
                highest_bid = bid_amount
                winner = bidder

        print(f"The winner is: {winner} with a bid of ${highest_bid}")

# TODO-4: Compare bids in dictionary


