import os


#initialize global variables
BIDS = {}
CONT = True


def highest_bidder(bidding_record):
    '''Determine the highest bidder based off of the BIDS dictionary'''
    #highest bid
    high = 0
    winner = ''
    for bidder in bidding_record:
        amount = bidding_record[bidder]
        #determine who has highest amount and declare said individual
        if int(amount) > int(high):
            high = amount
            winner = bidder

    print(f'The winner is {winner.title()} with a bid of ${high}!')


#introduction
print('Welcome to the blind auction program.')


#initiliaze bid loop
try:
    while CONT:
        name = input('Name of bidder:\n ~ ')
        #clear screen for readability
        os.system('clear')
        price = input('Bid:\n $ ')
        BIDS[name] = price
        #query for addtional bidders
        more = input('Are there any more bidders? Type "yes" or "no"\n ~ ')
        if more == 'no':
            CONT = False

    highest_bidder(BIDS)

except KeyboardInterrupt:
    print('\nSee you later.')