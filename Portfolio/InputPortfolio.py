from Stock import Stock
from Read_Num_Str import getNum
import csv

def portfolioManualInput():

    stock_list = []

    s_num = 1
    while (1):
        print("Stock number " + str(s_num))
        s_name = input("Stock name: ").strip()
        s_symbol = input("Ticker symbol: ").strip()
        s_price_bought = input("Price at buy: ").strip()
        s_price_bought_float = getNum(s_price_bought)
        s_shares_bought = input("Number of shares bought: ").strip()
        s_shares_bought_float = getNum(s_shares_bought)
        s_market = input("Stock market (optional): ").strip()

        s_stock = Stock()
        s_stock.setName(s_name)
        s_stock.setSymbol(s_symbol)
        s_stock.setPricebought(s_price_bought_float)
        s_stock.setNumberbought(s_shares_bought_float)
        if (s_market != ""):
            s_stock.market = s_market

        correct = None
        while (correct != "Y" and correct != "y" and correct != "N" and correct != "n"):
            correct = input("Is the inputted information correct (Y/N): ")
            correct = correct.strip()
        if (correct == "N" or correct == "n"):
            print("This stock won't be added.\n")
        else:
            stock_list.append(s_stock)
            s_num += 1

        another = None
        while (another != "Y" and another != "y" and another != "N" and another != "n"):
            another = input("Add another stock? (Y/N): ")
            another = another.strip()
        if(another == "N" or another == "n"):
            break
        else:
            print()

    return stock_list



def savePortfolio(stock_list):

    save = None
    while (save != "Y" and save != "y" and save != "N" and save != "n"):
        save = input("Save this portfolio? (Y/N): ")
        save = save.strip()
    if (save == "N" or save == "n"):
        print("This portfolio will not be saved.")
    else:
        name_confirmation = None
        first_try = True

        while (name_confirmation != "Y" and name_confirmation != "y"):

            if first_try:
                name = input("Enter portfolio name: ")
                first_try = False
            else:
                name = input("Please re-enter portfolio name: ")
            name = name.strip()
            print(name)

            second_confirmation = None
            while (second_confirmation != "Y" and second_confirmation != "y" and second_confirmation != "N" and second_confirmation != "n"):
                second_confirmation = input('Is "' + name + '" correct? (Y/N): ')
                second_confirmation = second_confirmation.strip()
            if (second_confirmation == "N" or second_confirmation == "n"):
                pass
            else:

                # Add code to save as file here

def portfolioInputFromFile():

    stock_list = []

    name_confirmation = None
    first_try = True

    while (name_confirmation != "Y" and name_confirmation != "y"):

        if first_try:
            name = input("Enter portfolio source file name: ")
            first_try = False
        else:
            name = input("Please re-enter portfolio source file name: ")
        name = name.strip()
        print(name)

        second_confirmation = None
        while (second_confirmation != "Y" and second_confirmation != "y" and second_confirmation != "N" and second_confirmation != "n"):
            second_confirmation = input('Is "' + name + '" correct? (Y/N): ')
            second_confirmation = second_confirmation.strip()
        if (second_confirmation == "N" or second_confirmation == "n"):
            pass
        else:
            with open('names.csv') as csvfile:
                ...
                reader = csv.DictReader(csvfile)
            ...
            for row in reader:
                ...
                print(row['first_name'], row['last_name'])



'''
list = portfolioInput()
for stock in list:
    print(stock.toString())
    '''