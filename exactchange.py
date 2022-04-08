import math

cost = input("How much did the item cost?")
payingWith = input("How much money are you giving me?")

change = float(payingWith) - float(cost)

def exactchange(amount):

    numberOfEachCoin = {}

    if (amount / 50 > 1):
        numberOfEachCoin['$50'] = math.floor(amount/50)
        amount = amount - 50*math.floor(amount/50)
    else:
        numberOfEachCoin['$50'] = 0

    if (amount / 20 > 1):
        numberOfEachCoin['$20'] = math.floor(amount/20)
        amount = amount - 20*math.floor(amount/20)
    else:
        numberOfEachCoin['$20'] = 0    

    if (amount / 10 > 1):
        numberOfEachCoin['$10'] = math.floor(amount/10)
        amount = amount - 10*math.floor(amount/10)
    else:
        numberOfEachCoin['$10'] = 0

    if (amount / 5 > 1):
        numberOfEachCoin['$5'] = math.floor(amount/5)
        amount = amount - 5*math.floor(amount/5)
    else:
        numberOfEachCoin['$5'] = 0

    if (amount / 1 > 1):
        numberOfEachCoin['$1'] = math.floor(amount/1)
        amount = amount - 1*math.floor(amount/1)
    else:
        numberOfEachCoin['$1'] = 0

    if (amount / 0.25 > 1):
        numberOfEachCoin['$0.25'] = math.floor(amount/0.25)
        amount = amount - 0.25*math.floor(amount/0.25)
    else:
        numberOfEachCoin['$0.25'] = 0

    if (amount / 0.10 > 1):
        numberOfEachCoin['$0.10'] = math.floor(amount/0.10)
        amount = amount - 0.10*math.floor(amount/0.10)
    else:
        numberOfEachCoin['$0.10'] = 0

    if (amount / 0.05 > 1):
        numberOfEachCoin['$0.05'] = math.floor(amount/0.05)
        amount = amount - 0.05*math.floor(amount/0.05)
    else:
        numberOfEachCoin['$0.05'] = 0

    if (amount / 0.01 > 1):
        numberOfEachCoin['$0.01'] = math.floor(amount/0.01)
        amount = amount - 0.01*math.floor(amount/0.01)
    else:
        numberOfEachCoin['$0.01'] = 0

    return numberOfEachCoin

print(exactchange(change))
