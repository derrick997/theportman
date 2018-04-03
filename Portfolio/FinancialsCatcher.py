from Time import timestamp
import Web_Access
from Read_Num_Str import catchStatementNum
from Stock import Stock
import datetime


def catchIncomeStatementFromYahooFinance(stockStruct, market=None, shortName=None):

    symbol = stockStruct.getSymbol()

    direccion = "https://finance.yahoo.com/quote/" + symbol + "/financials?p=" + symbol + "&annual"
    currentPage = Web_Access.accessWithBs(direccion)

    #print(currentPage)

    quarterlyIncomeStatementStartIndex = currentPage.find("incomeStatementHistory")
    quarterlyIncomeStatementStartIndex = currentPage.find("incomeStatementHistory", quarterlyIncomeStatementStartIndex+1)
    #^income statement quarterly data lives here


    annualIncomeStatementStartIndex = currentPage.find("incomeStatementHistory", quarterlyIncomeStatementStartIndex+1)
    annualIncomeStatementEndIndex = currentPage.find("]", annualIncomeStatementStartIndex)
    #print(annualIncomeStatementStartIndex)
    #print(annualIncomeStatementEndIndex)

    incomeStatement = currentPage[annualIncomeStatementStartIndex:annualIncomeStatementEndIndex]
    #print(incomeStatement) #annual income statement

    IS_numYearsAvailable = incomeStatement.count("endDate") #The number of years for which income statements are available

    IS_endDate_list = []
    IS_totalRevenue_list = []
    IS_costOfRevenue_list = []
    IS_grossProfit_list = []
    IS_researchDevelopment_list = []
    IS_sellingGeneralAdministrative_list = []
    IS_nonRecurring_list = []
    IS_otherOperatingExpenses_list = []
    IS_totalOperatingExpenses_list = []
    IS_operatingIncome_list = []
    IS_totalOtherIncomeExpenseNet_list = []
    IS_ebit_list = []
    IS_interestExpense_list = []
    IS_incomeBeforeTax_list = []
    IS_incomeTaxExpense_list = []
    IS_minorityInterest_list = []
    IS_netIncomeFromContinuingOps_list = []
    IS_discontinuedOperations_list = []
    IS_extraordinaryItems_list = []
    IS_effectOfAccountingCharges_list = []
    IS_otherItems_list = []
    IS_netIncome_list = []

    for i in range(IS_numYearsAvailable):

        IS_endDate_list.append(datetime.datetime.fromtimestamp(catchStatementNum(incomeStatement, "endDate")).date())
        IS_totalRevenue_list.append(catchStatementNum(incomeStatement, "totalRevenue"))
        IS_costOfRevenue_list.append(catchStatementNum(incomeStatement, "costOfRevenue"))
        IS_grossProfit_list.append(catchStatementNum(incomeStatement, "grossProfit"))
        IS_researchDevelopment_list.append(catchStatementNum(incomeStatement, "researchDevelopment"))
        IS_sellingGeneralAdministrative_list.append(catchStatementNum(incomeStatement, "sellingGeneralAdministrative"))
        IS_nonRecurring_list.append(catchStatementNum(incomeStatement, "nonRecurring"))
        IS_otherOperatingExpenses_list.append(catchStatementNum(incomeStatement, "otherOperatingExpenses"))
        IS_totalOperatingExpenses_list.append(catchStatementNum(incomeStatement, "totalOperatingExpenses"))
        IS_operatingIncome_list.append(catchStatementNum(incomeStatement, "operatingIncome"))
        IS_totalOtherIncomeExpenseNet_list.append(catchStatementNum(incomeStatement, "totalOtherIncomeExpenseNet"))
        IS_ebit_list.append(catchStatementNum(incomeStatement, "ebit"))
        IS_interestExpense_list.append(catchStatementNum(incomeStatement, "interestExpense"))
        IS_incomeBeforeTax_list.append(catchStatementNum(incomeStatement, "incomeBeforeTax"))
        IS_incomeTaxExpense_list.append(catchStatementNum(incomeStatement, "incomeTaxExpense"))
        IS_minorityInterest_list.append(catchStatementNum(incomeStatement, "minorityInterest"))
        IS_netIncomeFromContinuingOps_list.append(catchStatementNum(incomeStatement, "netIncomeFromContinuingOps"))
        IS_discontinuedOperations_list.append(catchStatementNum(incomeStatement, "discontinuedOperations"))
        IS_extraordinaryItems_list.append(catchStatementNum(incomeStatement, "extraordinaryItems"))
        IS_effectOfAccountingCharges_list.append(catchStatementNum(incomeStatement, "effectOfAccountingCharges"))
        IS_otherItems_list.append(catchStatementNum(incomeStatement, "otherItems"))
        IS_netIncome_list.append(catchStatementNum(incomeStatement, "netIncome"))

        currentYearStartIndex = incomeStatement.find("},{")+1
        incomeStatement = incomeStatement[currentYearStartIndex:]


    stockStruct.setIS_numYearsAvailable(IS_numYearsAvailable)
    stockStruct.setIS_endDateIS_list(IS_endDate_list)
    stockStruct.setIS_totalRevenue_list(IS_totalRevenue_list)
    stockStruct.setIS_costOfRevenue_list(IS_costOfRevenue_list)
    stockStruct.setIS_grossProfit_list(IS_grossProfit_list)
    stockStruct.setIS_researchDevelopment_list(IS_researchDevelopment_list)
    stockStruct.setIS_sellingGeneralAdministrative_list(IS_sellingGeneralAdministrative_list)
    stockStruct.setIS_nonRecurring_list(IS_nonRecurring_list)
    stockStruct.setIS_otherOperatingExpenses_list(IS_otherOperatingExpenses_list)
    stockStruct.setIS_totalOperatingExpenses_list(IS_totalOperatingExpenses_list)
    stockStruct.setIS_operatingIncome_list(IS_operatingIncome_list)
    stockStruct.setIS_totalOtherIncomeExpenseNet_list(IS_totalOtherIncomeExpenseNet_list)
    stockStruct.setIS_ebit_list(IS_ebit_list)
    stockStruct.setIS_interestExpense_list(IS_interestExpense_list)
    stockStruct.setIS_incomeBeforeTax_list(IS_incomeBeforeTax_list)
    stockStruct.setIS_incomeTaxExpense_list(IS_incomeTaxExpense_list)
    stockStruct.setIS_minorityInterest_list(IS_minorityInterest_list)
    stockStruct.setIS_netIncomeFromContinuingOps_list(IS_netIncomeFromContinuingOps_list)
    stockStruct.setIS_discontinuedOperations_list(IS_discontinuedOperations_list)
    stockStruct.setIS_extraordinaryItems_list(IS_extraordinaryItems_list)
    stockStruct.setIS_effectOfAccountingCharges_list(IS_effectOfAccountingCharges_list)
    stockStruct.setIS_otherItems_list(IS_otherItems_list)
    stockStruct.setIS_netIncome_list(IS_netIncome_list)

    return stockStruct

#Test
'''nike = Stock()
nike = catchIncomeStatementFromYahooFinance(nike)
print(nike.financialToString())'''


'''starbucks = Stock()
starbucks = catchIncomeStatementFromYahooFinance(starbucks)
print(starbucks.financialToString())'''

def catchBalanceSheetFromYahooFinance(stockStruct, market=None, shortName=None):

    symbol = stockStruct.getSymbol()

    direccion = "https://finance.yahoo.com/quote/" + symbol + "/balance-sheet?p=" + symbol + "&annual"
    currentPage = Web_Access.accessWithBs(direccion)

    #print(currentPage)

    quarterlyBalanceSheetStartIndex = currentPage.find("balanceSheetHistoryQuarterly")
    quarterlyBalanceSheetStartIndex = currentPage.find("balanceSheetStatements", quarterlyBalanceSheetStartIndex+1)
    #^balance sheet quarterly data lives here


    annualBalanceSheetStartIndex = currentPage.find("balanceSheetStatements", quarterlyBalanceSheetStartIndex+1)
    annualBalanceSheetEndIndex = currentPage.find("]", annualBalanceSheetStartIndex)
    #print(annualIncomeStatementStartIndex)
    #print(annualIncomeStatementEndIndex)

    balanceSheet = currentPage[annualBalanceSheetStartIndex:annualBalanceSheetEndIndex]
    #print(balanceSheet) #annual balance sheet

    BS_numYearsAvailable = balanceSheet.count("endDate") #The number of years for which balance sheet are available

    BS_endDate_list = []
    BS_cash_list = []
    BS_shortTermInvestments_list = []
    BS_netReceivables_list = []
    BS_inventory_list = []
    BS_otherCurrentAssets_list = []
    BS_totalCurrentAssets_list = []
    BS_longTermInvestments_list = []
    BS_propertyPlantEquipment_list = []
    BS_goodWill_list = []
    BS_intangibleAssets_list = []
    BS_otherAssets_list = []
    BS_deferredLongTermAssetCharges_list = []
    BS_totalAssets_list = []
    BS_accountsPayable_list = []
    BS_shortLongTermDebt_list = []
    BS_otherCurrentLiab_list = []
    BS_totalCurrentLiabilities_list = []
    BS_longTermDebt_list = []
    BS_otherLiab_list = []
    BS_deferredLongTermLiab_list = []
    BS_minorityInterest_list = []
    BS_totalLiab_list = []
    BS_stockOptionWarrants_list = []
    BS_commonStock_list = []
    BS_retainedEarnings_list = []
    BS_treasuryStock_list = []
    BS_capitalSurplus_list = []
    BS_otherStockholderEquity_list = []
    BS_totalStockholderEquity_list = []
    BS_netTangibleAssets_list = []

    for i in range(BS_numYearsAvailable):

        BS_endDate_list.append(datetime.datetime.fromtimestamp(catchStatementNum(balanceSheet, "endDate")).date())
        BS_cash_list.append(catchStatementNum(balanceSheet, "cash"))
        BS_shortTermInvestments_list.append(catchStatementNum(balanceSheet, "shortTermInvestments"))
        BS_netReceivables_list.append(catchStatementNum(balanceSheet, "netReceivables"))
        BS_inventory_list.append(catchStatementNum(balanceSheet, "inventory"))
        BS_otherCurrentAssets_list.append(catchStatementNum(balanceSheet, "otherCurrentAssets"))
        BS_totalCurrentAssets_list.append(catchStatementNum(balanceSheet, "totalCurrentAssets"))
        BS_longTermInvestments_list.append(catchStatementNum(balanceSheet, "longTermInvestments"))
        BS_propertyPlantEquipment_list.append(catchStatementNum(balanceSheet, "propertyPlantEquipment"))
        BS_goodWill_list.append(catchStatementNum(balanceSheet, "goodWill"))
        BS_intangibleAssets_list.append(catchStatementNum(balanceSheet, "intangibleAssets"))
        BS_otherAssets_list.append(catchStatementNum(balanceSheet, "otherAssets"))
        BS_deferredLongTermAssetCharges_list.append(catchStatementNum(balanceSheet, "deferredLongTermAssetCharges"))
        BS_totalAssets_list.append(catchStatementNum(balanceSheet, "totalAssets"))
        BS_accountsPayable_list.append(catchStatementNum(balanceSheet, "accountsPayable"))
        BS_shortLongTermDebt_list.append(catchStatementNum(balanceSheet, "shortLongTermDebt"))
        BS_otherCurrentLiab_list.append(catchStatementNum(balanceSheet, "otherCurrentLiab"))
        BS_totalCurrentLiabilities_list.append(catchStatementNum(balanceSheet, "totalCurrentLiabilities"))
        BS_longTermDebt_list.append(catchStatementNum(balanceSheet, "longTermDebt"))
        BS_otherLiab_list.append(catchStatementNum(balanceSheet, "otherLiab"))
        BS_deferredLongTermLiab_list.append(catchStatementNum(balanceSheet, "deferredLongTermLiab"))
        BS_minorityInterest_list.append(catchStatementNum(balanceSheet, "minorityInterest"))
        BS_totalLiab_list.append(catchStatementNum(balanceSheet, "totalLiab"))
        BS_stockOptionWarrants_list.append(catchStatementNum(balanceSheet, "stockOptionWarrants"))
        BS_commonStock_list.append(catchStatementNum(balanceSheet, "commonStock"))
        BS_retainedEarnings_list.append(catchStatementNum(balanceSheet, "retainedEarnings"))
        BS_treasuryStock_list.append(catchStatementNum(balanceSheet, "treasuryStock"))
        BS_capitalSurplus_list.append(catchStatementNum(balanceSheet, "capitalSurplus"))
        BS_otherStockholderEquity_list.append(catchStatementNum(balanceSheet, "otherStockholderEquity"))
        BS_totalStockholderEquity_list.append(catchStatementNum(balanceSheet, "totalStockholderEquity"))
        BS_netTangibleAssets_list.append(catchStatementNum(balanceSheet, "netTangibleAssets"))
        
        currentYearStartIndex = balanceSheet.find("},{")+1
        balanceSheet = balanceSheet[currentYearStartIndex:]


    stockStruct.setBS_numYearsAvailable(BS_numYearsAvailable)
    stockStruct.setBS_endDate_list(BS_endDate_list)
    stockStruct.setBS_cash_list(BS_cash_list)
    stockStruct.setBS_shortTermInvestments_list(BS_shortTermInvestments_list)
    stockStruct.setBS_netReceivables_list(BS_netReceivables_list)
    stockStruct.setBS_inventory_list(BS_inventory_list)
    stockStruct.setBS_otherCurrentAssets_list(BS_otherCurrentAssets_list)
    stockStruct.setBS_totalCurrentAssets_list(BS_totalCurrentAssets_list)
    stockStruct.setBS_longTermInvestments_list(BS_longTermInvestments_list)
    stockStruct.setBS_propertyPlantEquipment_list(BS_propertyPlantEquipment_list)
    stockStruct.setBS_goodWill_list(BS_goodWill_list)
    stockStruct.setBS_intangibleAssets_list(BS_intangibleAssets_list)
    stockStruct.setBS_otherAssets_list(BS_otherAssets_list)
    stockStruct.setBS_deferredLongTermAssetCharges_list(BS_deferredLongTermAssetCharges_list)
    stockStruct.setBS_totalAssets_list(BS_totalAssets_list)
    stockStruct.setBS_accountsPayable_list(BS_accountsPayable_list)
    stockStruct.setBS_shortLongTermDebt_list(BS_shortLongTermDebt_list)
    stockStruct.setBS_otherCurrentLiab_list(BS_otherCurrentLiab_list)
    stockStruct.setBS_totalCurrentLiabilities_list(BS_totalCurrentLiabilities_list)
    stockStruct.setBS_longTermDebt_list(BS_longTermDebt_list)
    stockStruct.setBS_otherLiab_list(BS_otherLiab_list)
    stockStruct.setBS_deferredLongTermLiab_list(BS_deferredLongTermLiab_list)
    stockStruct.setBS_minorityInterest_list(BS_minorityInterest_list)
    stockStruct.setBS_totalLiab_list(BS_totalLiab_list)
    stockStruct.setBS_stockOptionWarrants_list(BS_stockOptionWarrants_list)
    stockStruct.setBS_commonStock_list(BS_commonStock_list)
    stockStruct.setBS_retainedEarnings_list(BS_retainedEarnings_list)
    stockStruct.setBS_treasuryStock_list(BS_treasuryStock_list)
    stockStruct.setBS_capitalSurplus_list(BS_capitalSurplus_list)
    stockStruct.setBS_otherStockholderEquity_list(BS_otherStockholderEquity_list)
    stockStruct.setBS_totalStockholderEquity_list(BS_totalStockholderEquity_list)
    stockStruct.setBS_netTangibleAssets_list(BS_netTangibleAssets_list)

    return stockStruct

#Test catch BS
'''google = Stock()
google.setSymbol("GOOG")
google = catchBalanceSheetFromYahooFinance(google)
'''

'''mu = Stock()
mu.setSymbol("MU")
mu = catchBalanceSheetFromYahooFinance(mu)'''

def catchCashFlowStatementFromYahooFinance(stockStruct, market=None, shortName=None):

    symbol = stockStruct.getSymbol()

    direccion = "https://finance.yahoo.com/quote/" + symbol + "/cash-flow?p=" + symbol + "&annual"
    currentPage = Web_Access.accessWithBs(direccion)

    #print(currentPage)

    annualCashFlowStatementStartIndex = currentPage.find("cashflowStatementHistory")
    annualCashFlowStatementEndIndex = currentPage.find("]", annualCashFlowStatementStartIndex)
    #print(annualCashFlowStatementStartIndex)
    #print(annualCashFlowStatementEndIndex)

    cashFlowStatement = currentPage[annualCashFlowStatementStartIndex:annualCashFlowStatementEndIndex]
    #print(cashFlowStatement) #annual cashflow statement

    CF_numYearsAvailable = cashFlowStatement.count("endDate") #The number of years for which cashflow statements are available

    CF_endDate_list = []
    CF_netIncome_list = []
    CF_depreciation_list = []
    CF_changeToNetincome_list = []
    CF_changeToAccountReceivables_list = []
    CF_changeToLiabilities_list = []
    CF_changeToInventory_list = []
    CF_changeToOperatingActivities_list = []
    CF_totalCashFromOperatingActivities_list = []

    CF_capitalExpenditures_list = []
    CF_investments_list = []
    CF_otherCashflowsFromInvestingActivities_list = []
    CF_totalCashflowsFromInvestingActivities_list = []

    CF_dividendsPaid_list = []
    CF_salePurchaseOfStock_list = []
    CF_netBorrowings_list = []
    CF_otherCashflowsFromFinancingActivities_list = []
    CF_totalCashFromFinancingActivities_list = []

    CF_effectOfExchangeRate_list = []
    CF_changeInCash_list = []

    for i in range(CF_numYearsAvailable):

        CF_endDate_list.append(datetime.datetime.fromtimestamp(catchStatementNum(cashFlowStatement, "endDate")).date())

        CF_netIncome_list.append(catchStatementNum(cashFlowStatement, "netIncome"))
        CF_depreciation_list.append(catchStatementNum(cashFlowStatement, "depreciation"))
        CF_changeToNetincome_list.append(catchStatementNum(cashFlowStatement, "changeToNetincome"))
        CF_changeToAccountReceivables_list.append(catchStatementNum(cashFlowStatement, "changeToAccountReceivables"))
        CF_changeToLiabilities_list.append(catchStatementNum(cashFlowStatement, "changeToLiabilities"))
        CF_changeToInventory_list.append(catchStatementNum(cashFlowStatement, "changeToInventory"))
        CF_changeToOperatingActivities_list.append(catchStatementNum(cashFlowStatement, "changeToOperatingActivities"))
        CF_totalCashFromOperatingActivities_list.append(catchStatementNum(cashFlowStatement, "totalCashFromOperatingActivities"))

        CF_capitalExpenditures_list.append(catchStatementNum(cashFlowStatement, "capitalExpenditures"))
        CF_investments_list.append(catchStatementNum(cashFlowStatement, "investments"))
        CF_otherCashflowsFromInvestingActivities_list.append(catchStatementNum(cashFlowStatement, "otherCashflowsFromInvestingActivities"))
        CF_totalCashflowsFromInvestingActivities_list.append(catchStatementNum(cashFlowStatement, "totalCashflowsFromInvestingActivities"))

        CF_dividendsPaid_list.append(catchStatementNum(cashFlowStatement, "dividendsPaid"))
        CF_salePurchaseOfStock_list.append(catchStatementNum(cashFlowStatement, "salePurchaseOfStock"))
        CF_netBorrowings_list.append(catchStatementNum(cashFlowStatement, "netBorrowings"))
        CF_otherCashflowsFromFinancingActivities_list.append(catchStatementNum(cashFlowStatement, "otherCashflowsFromFinancingActivities"))
        CF_totalCashFromFinancingActivities_list.append(catchStatementNum(cashFlowStatement, "totalCashFromFinancingActivities"))

        CF_effectOfExchangeRate_list.append(catchStatementNum(cashFlowStatement, "effectOfExchangeRate"))
        CF_changeInCash_list.append(catchStatementNum(cashFlowStatement, "changeInCash"))

        currentYearStartIndex = cashFlowStatement.find("},{")+1
        cashFlowStatement = cashFlowStatement[currentYearStartIndex:]


    stockStruct.setCF_numYearsAvailable(CF_numYearsAvailable)
    stockStruct.setCF_endDate_list(CF_endDate_list)

    stockStruct.setCF_netIncome_list(CF_netIncome_list)
    stockStruct.setCF_depreciation_list(CF_depreciation_list)
    stockStruct.setCF_changeToNetincome_list(CF_changeToNetincome_list)
    stockStruct.setCF_changeToAccountReceivables_list(CF_changeToAccountReceivables_list)
    stockStruct.setCF_changeToLiabilities_list(CF_changeToLiabilities_list)
    stockStruct.setCF_changeToInventory_list(CF_changeToInventory_list)
    stockStruct.setCF_changeToOperatingActivities_list(CF_changeToOperatingActivities_list)
    stockStruct.setCF_totalCashFromOperatingActivities_list(CF_totalCashFromOperatingActivities_list)

    stockStruct.setCF_capitalExpenditures_list(CF_capitalExpenditures_list)
    stockStruct.setCF_investments_list(CF_investments_list)
    stockStruct.setCF_otherCashflowsFromInvestingActivities_list(CF_otherCashflowsFromInvestingActivities_list)
    stockStruct.setCF_totalCashflowsFromInvestingActivities_list(CF_totalCashflowsFromInvestingActivities_list)

    stockStruct.setCF_dividendsPaid_list(CF_dividendsPaid_list)
    stockStruct.setCF_salePurchaseOfStock_list(CF_salePurchaseOfStock_list)
    stockStruct.setCF_netBorrowings_list(CF_netBorrowings_list)
    stockStruct.setCF_otherCashflowsFromFinancingActivities_list(CF_otherCashflowsFromFinancingActivities_list)
    stockStruct.setCF_totalCashFromFinancingActivities_list(CF_totalCashFromFinancingActivities_list)

    stockStruct.setCF_effectOfExchangeRate_list(CF_effectOfExchangeRate_list)
    stockStruct.setCF_changeInCash_list(CF_changeInCash_list)

    return stockStruct

#Test catch CFS
'''google = Stock()
google.setSymbol("GOOG")
google = catchCashFlowStatementFromYahooFinance(google)'''
#print(google.cashFlowStatementToListOfLists())
