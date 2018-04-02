import Web_Access
from Read_Num_Str import catchStatementNum
import datetime
from TBond import TBond
from Time import timestamp


def catchBondFromYahooFinance(tbondStruct):

    #13WK
    direccion = "https://finance.yahoo.com/quote/^IRX?p=^IRX"
    currentPage = Web_Access.accessWithBs(direccion)
    bondRate13wk = catchStatementNum(currentPage, "regularMarketPrice")
    tbondStruct.setbill13Wk(bondRate13wk)

    # 5YR
    direccion = "https://finance.yahoo.com/quote/^FVX?p=^FVX"
    currentPage = Web_Access.accessWithBs(direccion)
    bondRate5yr = catchStatementNum(currentPage, "regularMarketPrice")
    tbondStruct.setbond5Yr(bondRate5yr)

    # 10YR
    direccion = "https://finance.yahoo.com/quote/^TNX?p=^TNX"
    currentPage = Web_Access.accessWithBs(direccion)
    bondRate10yr = catchStatementNum(currentPage, "regularMarketPrice")
    tbondStruct.setbond10Yr(bondRate10yr)

    # 30YR
    direccion = "https://finance.yahoo.com/quote/^TYX?p=^TYX"
    currentPage = Web_Access.accessWithBs(direccion)
    bondRate30yr = catchStatementNum(currentPage, "regularMarketPrice")
    tbondStruct.setbond30Yr(bondRate30yr)

    #Timestamp
    tbondStruct.dateTime = timestamp()

    return tbondStruct

#Test
'''usbonds = TBond()
usbonds = catchBondFromYahooFinance(usbonds)
print(usbonds.tBondToString())
print(usbonds.tBondToListOfLists())'''