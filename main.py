def get_stock_purchase_info():
    symbol = input("What stock did you purchase?: ")
    shares = input("How many shares did you purchase?: ")
    purchase_price = input("What price did you get filled at?: ")
    total = int(shares) * float(purchase_price)
    total = "${:,.2f}".format(total)
    print('You purchased: ' + shares +
          ' shares of ' + symbol +
          ' for $' + purchase_price + ' per share for a total of ' + str(total))
    return [symbol, int(shares), float(purchase_price)]


print(get_stock_purchase_info())


# Get updated current price of stock purchased
# Get contracts sold info (strike, expiration date, contract price, total contracts)
