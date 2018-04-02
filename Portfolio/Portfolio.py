import InputPortfolio
import StockCatcher
import FinancialsCatcher
import OutputPortfolio
import BondsCatcher
from TBond import TBond
from Stock import Stock

#Prompt for user input
portfolio_in_list = InputPortfolio.portfolioManualInput()
portfolio_main = []
print()

#Merge input info with current data, and create main list
if InputPortfolio.throwPromptFor("Quote Analysis Summary"):
    portfolio_main_quote = []
    for stock in portfolio_in_list:
        stock = StockCatcher.getStockFromYahooFinance(stock.name, stock.symbol, stock, stock.market)
        print(stock.quoteToString())
        portfolio_main_quote.append(stock)
    portfolio_main = portfolio_main_quote

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

if InputPortfolio.throwPromptFor("Treasury Bond Rates"):
    tbonds = BondsCatcher.catchBondFromYahooFinance(TBond())
    print(tbonds.tBondToString())

#OutputPortfolio.savePortfolioAsCsv(portfolio_main)
OutputPortfolio.savePortfolioAsXlsx(portfolio_main)

#OutputPortfolio.printPortfolioSummary(portfolio_main)


