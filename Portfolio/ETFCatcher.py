from Time import timestamp
from Web_Access import access, accessWithJavascript, accessWithBs
from Read_Num_Str import getNextNum, readCharsUntil, catchStatementNum
from Stock import Stock

def catchETFFromYahooFinance(stockStruct, market=None, shortName=None):

    direccion = "https://finance.yahoo.com/quote/" + stockStruct.getSymbol() + "?p=" + stockStruct.getSymbol()
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
