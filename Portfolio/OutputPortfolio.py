from termcolor import colored

def printPortfolioSummary(stock_list):

    print("-----Start of summary-----")

    total_paid = 0.00
    total_current = 0.00
    total_gain = 0.00

    for stock in stock_list:
        stock_str = stock.toString()
        print(stock_str)

        total_paid += (stock.numberbought * stock.pricebought)
        total_current += (stock.numberbought * stock.price)

        gainloss = stock.price - stock.pricebought
        total_gain += gainloss

        if gainloss<0:
            gainloss *= -1
            print(colored("Loss per share so far: $(" + str(gainloss) + ")", "red") + "\n")
            print(colored("Total loss so far: $(" + str(gainloss*stock.numberbought) + ")", "red") + "\n")
        else:
            print(colored("Gain per share so far: $" + str(gainloss), "green") + "\n")
            print(colored("Total gain so far: $" + str(gainloss*stock.numberbought), "green") + "\n")


    print("Total portfolio cost: $" + str(total_paid))
    print("Total portfolio value: $" + str(total_current))
    if total_gain < 0:
        print(colored("Total current loss: $(" + str(total_gain*-1) + ")", "red") + "\n")
    else:
        print(colored("Total current gain: $" + str(total_gain), "green") + "\n")

    print("-----End of summary-----")