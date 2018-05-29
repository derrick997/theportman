import InputPortfolio
import StockCatcher
import FinancialsCatcher
import OutputPortfolio
import DCFValuation
from Stock import Stock
import StockHoldingAnalysis

#Prompt for user input
portfolio_in_list = InputPortfolio.portfolioManualInput()
portfolio_main = []
print()

#Merge input info with current data, and create main list
if InputPortfolio.throwPromptFor("get the Quote Analysis Summary"):
    portfolio_main_quote = []
    for stock in portfolio_in_list:
        stock = StockCatcher.catchStockFromYahooFinance(stock)
        print(stock.quoteToString())
        portfolio_main_quote.append(stock)
    portfolio_main = portfolio_main_quote

print()

if InputPortfolio.throwPromptFor("get the Analysis of Holding"):
    portfolio_main_Holding = []
    for stock in portfolio_in_list:
        stock, analysisString = StockHoldingAnalysis.stockHoldingAnalysis(stock)
        print(analysisString)
        portfolio_main_Holding.append(stock)
    portfolio_main = portfolio_main_Holding

print()

if InputPortfolio.throwPromptFor("get the Historical Income Statements"):
    portfolio_main_IS = []
    for stock in portfolio_main:
        stock = FinancialsCatcher.catchIncomeStatementFromYahooFinance(stock)
        print(stock.incomeStatementToString())
        portfolio_main_IS.append(stock)
    portfolio_main = portfolio_main_IS

print()

if InputPortfolio.throwPromptFor("get the Historical Balance Sheets"):
    portfolio_main_BS = []
    for stock in portfolio_main:
        stock = FinancialsCatcher.catchBalanceSheetFromYahooFinance(stock)
        print(stock.balanceSheetToString())
        portfolio_main_BS.append(stock)
    portfolio_main = portfolio_main_BS

print()

if InputPortfolio.throwPromptFor("get the Historical Cash Flow Statements"):
    portfolio_main_CF = []
    for stock in portfolio_main:
        stock = FinancialsCatcher.catchCashFlowStatementFromYahooFinance(stock)
        print(stock.cashFlowStatementToString())
        portfolio_main_CF.append(stock)
    portfolio_main = portfolio_main_CF

print()

tbonds_list = None
waccListOfLists = None

if InputPortfolio.throwPromptFor("perform a DCF Analysis"):

    portfolio_main_DCF = []
    for stock in portfolio_main:
        portfolio_main_DCF = []
        stock, waccListOfLists, economyListOfLists = DCFValuation.calculateDCF(stock)
        #print(stock.cashFlowStatementToString())
        portfolio_main_DCF.append(stock)
    portfolio_main = portfolio_main_DCF

OutputPortfolio.savePortfolioAsXlsx(portfolio_main, tbonds_list, waccListOfLists, economyListOfLists)

#OutputPortfolio.printPortfolioSummary(portfolio_main)


