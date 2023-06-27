bidders = {}
def auction(name, bid):
    bidders.update({name: bid})

isContinue = True
while isContinue:
    name = input("Whatis your name?: ")

    isZero = True
    while isZero:
        try:
            bid = int(input("What's your bid?: $"))
            if bid < 0:
                print("Your bid has to be greater than 0")
            else:
                isZero = False
        except Exception:
            print("Sorry something went wrong, please try again")

    auction(name, bid)
    
    isValid = True
    while isValid:
        anyBidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
        if anyBidders.lower() not in ['yes', 'no']:
            print("Please type 'yes' or 'no'.\n")
        else:
            isValid = False

    if(anyBidders.lower() == 'yes'):
        pass
    
    elif(anyBidders.lower() == 'no'):
        isContinue = False

        highest_bidder = 0
        highest_bidder_name = ""

        for name, bid in bidders.items():
            if bid > highest_bidder:
                highest_bidder_name = name
                highest_bidder = bid
        if bid == highest_bidder and len(bidders) > 1:
            equal = []
            for i in bidders:
                if bidders[i] == highest_bidder:
                    equal.append(i)
            if len(bidders) == 2:
                print("'s and ".join(equal) + "'s bid was the same, auction is over!")
            elif len(bidders) > 2:
                print("'s, ".join(equal[:-1]) + "'s, and " + equal[-1] + "'s bid was the same, auction is over!")
            break
        
        print(f"The highest bid was made by {highest_bidder_name} with a bid of {highest_bidder}")