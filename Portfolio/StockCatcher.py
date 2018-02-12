from Time import timestamp
from Web_Access import access, accessWithJavascript, accessWithBs
from Read_Num_Str import getNextNum
from Stock import Stock

def getFromYahooFinance(stockName, symbol, market=None, shortName=None):
    direccion = "https://finance.yahoo.com/quote/" + symbol + "?p=" + symbol
    currentPage = accessWithBs(direccion)
    #print(currentPage)

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

    return currentStock


'''nike = getFromYahooFinance("NIKE, Inc.", "NKE")
print("symbol: " + str(nike.symbol))
print("name: " + str(nike.name))
print("price: " + str(nike.price))
print("bid: " + str(nike.bid))
print("ask: " + str(nike.ask))
print("beta: " + str(nike.beta))
print("market cap: " + str(nike.marketcap))
print("trailing dividends: " + str(nike.dividends))
print("enterprise value: " + str(nike.enterprisevalue))'''



def getFromiHub(stockName, symbol, market, shortName):
    direccion = "https://ih.advfn.com/stock-market/" + market + "/" + shortName + "-" + symbol + "/financials"
    #print(direccion)
    #currentPage = access(direccion)#.decode("UTF-8")
    #currentPage = accessWithJavascript(direccion)#.decode("UTF-8")
    currentPage = accessWithBs(direccion)
    #print(currentPage)

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

    return currentStock

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

