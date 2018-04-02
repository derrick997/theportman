from Time import timestamp
from Web_Access import access, accessWithJavascript, accessWithBs
from Read_Num_Str import getNextNum, readCharsUntil, catchStatementNum
from Stock import Stock

def getStockFromYahooFinance(stockName, symbol, stockStruct, market=None, shortName=None):
    direccion = "https://finance.yahoo.com/quote/" + symbol + "?p=" + symbol
    currentPage = accessWithBs(direccion)
    #print(currentPage)

    quoteSummary = currentPage[0:] ####

    companyVal = "<REFERENCE INDEX NOT FOUND>"
    companyIndex = currentPage.find('Summary for ')+12
    if companyIndex != -1:
        companyVal = readCharsUntil(currentPage, companyIndex, "-").strip()

    priceVal = catchStatementNum(quoteSummary, 'regularMarketPrice')
    bidVal = catchStatementNum(quoteSummary, 'bid":{')
    askVal = catchStatementNum(quoteSummary, 'ask":{')
    betaVal = catchStatementNum(quoteSummary, 'beta":{')
    marketcapVal = catchStatementNum(quoteSummary, 'marketCap":{')
    dividendsVal = catchStatementNum(quoteSummary, "trailingAnnualDividendRate")
    enterprisevalueVal = catchStatementNum(quoteSummary, "enterpriseValue")

    stockStruct.setCompany(companyVal)
    stockStruct.setSymbol(symbol)
    stockStruct.setName(stockName)
    stockStruct.setPrice(priceVal)
    stockStruct.setDateTime(timestamp())
    stockStruct.setBid(bidVal)
    stockStruct.setAsk(askVal)
    stockStruct.setMarketcap(marketcapVal)
    stockStruct.setDividends(dividendsVal)
    stockStruct.setBeta(betaVal)
    stockStruct.setEnterprisevalue(enterprisevalueVal)
    stockStruct.setMarket(market)

    return stockStruct

'''google = Stock()
google.setSymbol("GOOG")
google = catchStatementNum(google)
print(google.quote)'''

'''def getFromiHub(stockName, symbol, market, shortName):
    direccion = "https://ih.advfn.com/stock-market/" + market + "/" + shortName + "-" + symbol + "/financials"
    #print(direccion)
    #currentPage = access(direccion)#.decode("UTF-8")
    #currentPage = accessWithJavascript(direccion)#.decode("UTF-8")
    currentPage = accessWithBs(direccion)
    print(currentPage)

    priceVal = "<REFERENCE INDEX NOT FOUND>"
    priceIndex = currentPage.find('regularMarketPrice')
    if priceIndex != -1:
        priceVal = getNextNum(currentPage, priceIndex, 50)

    bidVal = "<REFERENCE INDEX NOT FOUND>"
    bidIndex = currentPage.find('bid":{')
    if bidIndex != -1:
        bidVal = getNextNum(currentPage, bidIndex, 30)

    askVal = "<REFERENCE INDEX NOT FOUND>"
    askIndex = currentPage.find('ask":{')
    if askIndex != -1:
        askVal = getNextNum(currentPage, askIndex, 30)

    betaVal = "<REFERENCE INDEX NOT FOUND>"
    betaIndex = currentPage.find('beta":{')
    if betaIndex != -1:
        betaVal = getNextNum(currentPage, betaIndex, 50)

    marketcapVal = "<REFERENCE INDEX NOT FOUND>"
    marketcapIndex = currentPage.find('marketCap":{')
    if marketcapIndex != -1:
        marketcapVal = getNextNum(currentPage, marketcapIndex, 30)

    dividendsVal = "<REFERENCE INDEX NOT FOUND>"
    dividendsIndex = currentPage.find("trailingAnnualDividendRate")
    if dividendsIndex != -1:
        dividendsVal = getNextNum(currentPage, dividendsIndex, 50)

    enterprisevalueVal = "<REFERENCE INDEX NOT FOUND>"
    enterprisevalueIndex = currentPage.find("enterpriseValue")
    if enterprisevalueIndex != -1:
        enterprisevalueVal = getNextNum(currentPage, enterprisevalueIndex, 50)


    currentStock = Stock()
    currentStock.setSymbol(symbol)
    currentStock.setName(stockName)
    currentStock.setPrice(priceVal)
    currentStock.setDateTime(timestamp())
    currentStock.setBid(bidVal)
    currentStock.setAsk(askVal)
    currentStock.setMarketcap(marketcapVal)
    currentStock.setDividends(dividendsVal)
    currentStock.setBeta(betaVal)
    currentStock.setEnterprisevalue(enterprisevalueVal)
    currentStock.setMarket(market)

    direccion_historicals = "https://ih.advfn.com/stock-market/" + market + "/" + shortName + "-" + symbol + "/financialsfinancials?btn=annual_reports&istart_date=90&mode=quarterly_reports"
    # print(direccion)
    # currentPage = access(direccion)#.decode("UTF-8")
    # currentPage = accessWithJavascript(direccion)#.decode("UTF-8")
    currentPage = accessWithBs(direccion_historicals)
    # print(currentPage)

    """ebitdaVal = "<REFERENCE INDEX NOT FOUND>"
    ebitdaValIndex = currentPage.find("EBITDA")
    if ebitdaValIndex != -1:
        ebitdaVal = getNextNum(currentPage, ebitdaValIndex, 50)

    return ebitdaVal"""

    return currentStock'''


# PENDING:
# create BS attributes for data structure
# method to get a series of x numbers, to get a series of historicals


'''nike = getFromiHub("NIKE, Inc.", "NKE", "NYSE", "nike",)
print("symbol: " + str(nike.symbol))
print("name: " + str(nike.name))
print("price: " + str(nike.price))
print("bid: " + str(nike.bid))
print("ask: " + str(nike.ask))
print("beta: " + str(nike.beta))
print("market cap: " + str(nike.marketcap))
print("trailing dividends: " + str(nike.dividends))
print("enterprise value: " + str(nike.enterprisevalue))'''

