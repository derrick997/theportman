import InputPortfolio
import StockCatcher
import OutputPortfolio

#Prompt for user input
portfolio_in_list = InputPortfolio.portfolioManualInput()
portfolio_main = []
print()

#Merge input info with current data, and create main list
for stock in portfolio_in_list:
    current = StockCatcher.getFromYahooFinance(stock.name, stock.symbol, stock.market)
    current.setPricebought(stock.pricebought)
    current.setNumberbought(stock.numberbought)
    portfolio_main.append(current)

#Print summary of portfolio
OutputPortfolio.printPortfolioSummary(portfolio_main)




