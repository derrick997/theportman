from Stock import Stock
import FinancialsCatcher
import StockCatcher
import BondsCatcher
import MRPCatcher
import InflationCatcher
from TBond import TBond
from MRP import MRP
from Inflation import Inflation
import InputPortfolio
from Formatting import nonlistItemToString

#Calculate WACC

def calculateDCF(stockStruct):

    waccListOfLists, waccInUse, economyListOfLists = calculateWacc(stockStruct)

    if InputPortfolio.throwPromptFor("use a different WACC"):
        newWacc = float(input("Enter a wacc: "))
        waccListOfLists.append(["Inputted WACC", newWacc])
        waccInUse = newWacc

    terminalValueListOfLists, economyListOfLists = calculateTerminalValue(stockStruct, waccInUse, economyListOfLists)

    #calculate terminal value
    #...

    return stockStruct, waccListOfLists, economyListOfLists

def calculateWacc(stockStruct):

    print("\nLet's start with calculating the WACC.")

    economy_list = []

    if InputPortfolio.throwPromptFor("get the Treasury Bond Yields"):
        tbonds = BondsCatcher.catchBondFromYahooFinance(TBond())
        print(tbonds.tBondToString())
        for bond_element in tbonds.tBondToListOfLists():
            economy_list.append(bond_element)

    riskFreeRate = float(input("Enter a Risk Free Rate (%): ").strip())/100.00

    print()
    if InputPortfolio.throwPromptFor("get the Market Risk Premium"):
        mrp = MRPCatcher.catchMarketRiskPremiumFromNYUAdamodaran(MRP())
        print(mrp.MRPToString())
        for mrp_element in mrp.MRPToListOfLists():
            economy_list.append(mrp_element)

    marketRiskPremium = float(input("Enter a Market Risk Premium (%): ").strip()) / 100.00

    """Cost of Debt calculated based on most recent year's interest expense and LT debt"""
    costOfDebt = (stockStruct.getIS_interestExpense_list()[-1])/(stockStruct.getBS_longTermDebt_list()[-1])

    costOfEquity = riskFreeRate + stockStruct.getBeta() * marketRiskPremium #levered beta

    """Weights calculated using current market cap and most recent LT debt"""
    totalCapital = stockStruct.getBS_longTermDebt_list()[-1] + stockStruct.getMarketcap()
    weightOfDebt = stockStruct.getBS_longTermDebt_list()[-1] / totalCapital
    weightOfEquity = stockStruct.getMarketcap()/ totalCapital

    """Tax rate calculated using most recent year's tax expense"""
    taxRate = (stockStruct.getIS_incomeTaxExpense_list()[-1])/(stockStruct.getIS_incomeBeforeTax_list()[-1])

    wacc = (costOfEquity * weightOfEquity) + (costOfDebt * weightOfDebt * (1-taxRate))

    title = "WACC CALCULATION FOR " + stockStruct.getCompany()

    listOfLists = [[title], [], ["Risk Free Rate", riskFreeRate], ["Levered Beta", stockStruct.getBeta()],
                   ["Market Risk Premium", marketRiskPremium], ["Cost of Equity", costOfEquity], [],
                   ["Cost of Debt", costOfDebt], ["Tax Rate", taxRate], [], ["Weight of Equity", weightOfEquity],
                   ["Weight of Debt", weightOfDebt], [], ["Calculated WACC", wacc]]

    waccToString = "\n-----START OF WACC CALCULATION-----\n"

    waccToString = nonlistItemToString(waccToString, riskFreeRate, "Risk Free Rate")
    waccToString = nonlistItemToString(waccToString, stockStruct.getBeta(), "Levered Beta")
    waccToString = nonlistItemToString(waccToString, marketRiskPremium, "Market Risk Premium")
    waccToString = nonlistItemToString(waccToString, costOfEquity, "Cost of Equity")

    waccToString = waccToString + "\n"

    waccToString = nonlistItemToString(waccToString, costOfDebt, "Cost of Debt")
    waccToString = nonlistItemToString(waccToString, taxRate, "Tax Rate")

    waccToString = waccToString + "\n"

    waccToString = nonlistItemToString(waccToString, weightOfEquity, "Weight of Equity")
    waccToString = nonlistItemToString(waccToString, weightOfDebt, "Weight of Debt")
    waccToString = nonlistItemToString(waccToString, wacc, "Calculated WACC")

    waccToString = waccToString + "\n\n-----END OF WACC CALCULATION-----\n"

    print(waccToString)

    return listOfLists, wacc, economy_list

#def calculateShortTermExpectedFCF(stockStruct, wacc, economyListOfLists):


def calculateTerminalValue(stockStruct, wacc, economyListOfLists):

    print("\nLastly, let's calculate terminal value.")
    print()

    if InputPortfolio.throwPromptFor("get the projected Inflation Rates"):
        inflation = InflationCatcher.catchInflationFrom_________(Inflation())
        print(inflation.inflationToString())
        for inflation_element in inflation.inflationToListOfLists():
            economyListOfLists.append(inflation_element)

    growthRate = float(input("Enter a Perpetual Growth Rate (%): ").strip()) / 100.00

    #FCF[N + 1](1 + g) / (WACC - g)

    lastProjectedFCF = 0 #Replace for last fcf

    terminalValue = lastProjectedFCF*(1 + growthRate)/(wacc - growthRate)

    discountedTerminalValue = 0 #update

    title = "TERMINAL VALUE CALCULATION FOR " + stockStruct.getCompany()

    listOfLists = [[]]

    waccToString = "\n-----START OF WACC CALCULATION-----\n"

    waccToString = nonlistItemToString(waccToString, riskFreeRate, "Risk Free Rate")
    waccToString = nonlistItemToString(waccToString, stockStruct.getBeta(), "Levered Beta")
    waccToString = nonlistItemToString(waccToString, marketRiskPremium, "Market Risk Premium")
    waccToString = nonlistItemToString(waccToString, costOfEquity, "Cost of Equity")

    waccToString = waccToString + "\n"

    waccToString = nonlistItemToString(waccToString, costOfDebt, "Cost of Debt")
    waccToString = nonlistItemToString(waccToString, taxRate, "Tax Rate")

    waccToString = waccToString + "\n"

    waccToString = nonlistItemToString(waccToString, weightOfEquity, "Weight of Equity")
    waccToString = nonlistItemToString(waccToString, weightOfDebt, "Weight of Debt")
    waccToString = nonlistItemToString(waccToString, wacc, "Calculated WACC")

    waccToString = waccToString + "\n\n-----END OF WACC CALCULATION-----\n"

    print(waccToString)

    return listOfLists, economyListOfLists


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