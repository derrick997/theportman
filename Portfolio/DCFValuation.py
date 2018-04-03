from Stock import Stock
import FinancialsCatcher
import StockCatcher
import InputPortfolio
from Formatting import nonlistItemToString

#Calculate WACC

def calculateDCF(stockStruct):

    stockStruct, waccListOfLists, waccToString = calculateWacc(stockStruct)
    print(waccToString)

    newWacc = None
    if InputPortfolio.throwPromptForDifferentInput("WACC"):
        newWacc = float(input("Enter a wacc: "))
        waccListOfLists.append(["Inputted WACC", newWacc])


    #calculate terminal value
    #...

    return stockStruct, waccListOfLists

def calculateWacc(stockStruct):

    print()

    riskFreeRate = float(input("Enter a Risk Free Rate: ").strip())/100.00
    marketRiskPremium = float(input("Enter a Market Risk Premium: ").strip())/100.00

    """Cost of Debt calculated based on most recent year's interest expense and LT debt"""
    costOfDebt = (stockStruct.getIS_interestExpense_list()[-1])/(stockStruct.getBS_longTermDebt_list()[-1])

    costOfEquity = riskFreeRate + stockStruct.getBeta() * marketRiskPremium

    """Weights calculated using current market cap and most recent LT debt"""
    totalCapital = stockStruct.getBS_longTermDebt_list()[-1] + stockStruct.getMarketcap()
    weightOfDebt = stockStruct.getBS_longTermDebt_list()[-1] / totalCapital
    weightOfEquity = stockStruct.getMarketcap()/ totalCapital

    """Tax rate calculated using most recent year's tax expense"""
    taxRate = (stockStruct.getIS_incomeTaxExpense_list()[-1])/(stockStruct.getIS_incomeBeforeTax_list()[-1])

    wacc = (costOfEquity * weightOfEquity) + (costOfDebt * weightOfDebt * (1-taxRate))

    stockStruct.setWacc(wacc)

    title = "WACC CALCULATION FOR " + stockStruct.getCompany()

    listOfLists = [[title], [], ["Risk Free Rate", riskFreeRate], ["Beta", stockStruct.getBeta()],
                   ["Market Risk Premium", marketRiskPremium], ["Cost of Equity", costOfEquity], [],
                   ["Cost of Debt", costOfDebt], ["Tax Rate", taxRate], [], ["Weight of Equity", weightOfEquity],
                   ["Weight of Debt", weightOfDebt], [], ["WACC", wacc]]

    string = "\n-----START OF WACC OF CALCULATION-----\n"

    string = nonlistItemToString(string, riskFreeRate, "Risk Free Rate")
    string = nonlistItemToString(string, stockStruct.getBeta(), "Beta")
    string = nonlistItemToString(string, marketRiskPremium, "Market Risk Premium""Beta")
    string = nonlistItemToString(string, costOfEquity, "Cost of Equity")

    string = string + "\n"

    string = nonlistItemToString(string, costOfDebt, "Cost of Debt")
    string = nonlistItemToString(string, taxRate, "Tax Rate")

    string = string + "\n"

    string = nonlistItemToString(string, weightOfEquity, "Weight of Equity")
    string = nonlistItemToString(string, weightOfDebt, "Weight of Debt")
    string = nonlistItemToString(string, wacc, "WACC")

    string = string + "\n\n-----END WACC CALCULATION-----"

    return stockStruct, listOfLists, string

'''stock = Stock()
stock.setSymbol("DPZ")
stock = StockCatcher.catchStockFromYahooFinance(stock)
stock = FinancialsCatcher.catchBalanceSheetFromYahooFinance(stock)
stock = FinancialsCatcher.catchIncomeStatementFromYahooFinance(stock)
stock = FinancialsCatcher.catchCashFlowStatementFromYahooFinance(stock)
calculateDCF(stock)'''


'''
#yearly values
ebit = 0
taxes = 0


year = 0

#constant value
perpetual_growth = 0


#yearly calc

taxrate = #derive
nopat = ebit*(1-taxrate)


#single calc
terminal_value = 0


input("Calculated WACC is " + str(wacc) + ". Use a different WACC? (Y/N): ")'''