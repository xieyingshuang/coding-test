def countMoney(amount):

    bills = [10000, 5000, 1000]

    coins = [500, 100, 50, 10, 5, 1]

    n_bills = [0, 0, 0]

    n_coins = [0, 0, 0, 0, 0, 0]

    print ("Requested withdraw amount: $ " + str(amount))
    print ("Bills/coins distribution:")

    for bill, n_bill in zip(bills, n_bills):
        if amount >= bill:
            n_bill = amount // bill
            amount = amount - bill * n_bill
            if n_bill > 1:
               print (str(n_bill)+" bills of $"+str(bill))
            else:
               print (str(n_bill)+" bill of $"+str(bill))

    for coin, n_coin in zip(coins, n_coins):
        if amount >= coin:
            n_coin = amount // coin
            amount = amount - coin * n_coin
            if n_coin > 1:
               print (str(n_coin)+" coins of $"+str(coin))
            else:
               print (str(n_coin)+" coin of $"+str(coin))

# Insert the Money
print("please insert the desired money:")
amount = int(input())
countMoney(amount)
