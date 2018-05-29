import Web_Access
from Read_Num_Str import catchDateString, addMonths, getNextNum
from MRP import MRP
from Time import timestamp


def catchMarketRiskPremiumFromNYUAdamodaran(MRPStruct):

    direccion = "http://pages.stern.nyu.edu/~adamodar/New_Home_Page/home.htm"
    currentPage = Web_Access.access(direccion).decode('UTF-8')
    #print(currentPage)

    currentMRPdate = catchDateString(currentPage, "Implied ERP on ", '%B %d, %Y', '<')  # is it possible to scrape time period?
    #print(currentMRPdate.date())
    MRPStruct.MRP1datetime = currentMRPdate
    MRPStruct.MRP0datetime = (addMonths(currentMRPdate, -1))

    currentmarketriskpremiumIndex = currentPage.find("Implied ERP")
    currentmarketriskpremium = getNextNum(currentPage, currentmarketriskpremiumIndex+40,150)
    #print(currentmarketriskpremium)
    MRPStruct.MRP1 = currentmarketriskpremium

    previousmarketriskpremiumIndex = currentPage.find("Implied ERP", currentmarketriskpremiumIndex+1)
    previousmarketriskpremium = getNextNum(currentPage, previousmarketriskpremiumIndex+40,150)
    #print(previousmarketriskpremium)
    MRPStruct.MRP0 = previousmarketriskpremium

    MRPStruct.timestamp = timestamp()

    return MRPStruct

'''mrp = catchMarketRiskPremiumFromNYUAdamodaran(MRP)
print(mrp.MRPToString(mrp))'''