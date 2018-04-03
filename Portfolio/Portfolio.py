import InputPortfolio
import StockCatcher
import FinancialsCatcher
import OutputPortfolio
import BondsCatcher
import DCFValuation
from TBond import TBond
from Stock import Stock
import StockHoldingAnalysis

#Prompt for user input
portfolio_in_list = InputPortfolio.portfolioManualInput()
portfolio_main = []
print()

#Merge input info with current data, and create main list
if InputPortfolio.throwPromptFor("Quote Analysis Summary"):
    portfolio_main_quote = []
    for stock in portfolio_in_list:
        stock = StockCatcher.catchStockFromYahooFinance(stock)
        print(stock.quoteToString())
        portfolio_main_quote.append(stock)
    portfolio_main = portfolio_main_quote

print()

if InputPortfolio.throwPromptFor("Analysis of Holding"):
    portfolio_main_Holding = []
    for stock in portfolio_in_list:
        stock, analysisString = StockHoldingAnalysis.stockHoldingAnalysis(stock)
        print(analysisString)
        portfolio_main_Holding.append(stock)
    portfolio_main = portfolio_main_Holding

print()

if InputPortfolio.throwPromptFor("Historical Income Statements"):
    portfolio_main_IS = []
    for stock in portfolio_main:
        stock = FinancialsCatcher.catchIncomeStatementFromYahooFinance(stock)
        print(stock.incomeStatementToString())
        portfolio_main_IS.append(stock)
    portfolio_main = portfolio_main_IS

print()

if InputPortfolio.throwPromptFor("Historical Balance Sheets"):
    portfolio_main_BS = []
    for stock in portfolio_main:
        stock = FinancialsCatcher.catchBalanceSheetFromYahooFinance(stock)
        print(stock.balanceSheetToString())
        portfolio_main_BS.append(stock)
    portfolio_main = portfolio_main_BS

print()

if InputPortfolio.throwPromptFor("Historical Cash Flow Statements"):
    portfolio_main_CF = []
    for stock in portfolio_main:
        stock = FinancialsCatcher.catchCashFlowStatementFromYahooFinance(stock)
        print(stock.cashFlowStatementToString())
        portfolio_main_CF.append(stock)
    portfolio_main = portfolio_main_CF

print()

tbonds_list = None
waccListOfLists = None

if InputPortfolio.throwPromptFor("DCF Analysis"):

    if InputPortfolio.throwPromptFor("Treasury Bond Yields"):
        tbonds = BondsCatcher.catchBondFromYahooFinance(TBond())
        print(tbonds.tBondToString())
        tbonds_list = tbonds.tBondToListOfLists()

    portfolio_main_DCF = []
    for stock in portfolio_main:
        portfolio_main_DCF = []
        stock, waccListOfLists = DCFValuation.calculateDCF(stock)
        #print(stock.cashFlowStatementToString())
        portfolio_main_DCF.append(stock)
    portfolio_main = portfolio_main_DCF

#OutputPortfolio.savePortfolioAsCsv(portfolio_main)
OutputPortfolio.savePortfolioAsXlsx(portfolio_main, tbonds_list, waccListOfLists)

#OutputPortfolio.printPortfolioSummary(portfolio_main)


