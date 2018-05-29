from Formatting import listItemToString, addLabelAndAppend, nonlistItemToString, nonlistAddLabelAndAppend

class Stock():
    def __init__(self):
        self.symbol = ""
        self.company = ""
        self.dateTime = None
        self.price = 0
        self.bid = 0
        self.ask = 0
        self.name = ""
        self.beta = 0
        self.dividends = 0
        self.marketcap = 0
        self.enterprisevalue = 0
        self.numberbought = 0
        self.pricebought = 0
        self.market = ""

        #Holding Analysis
        self.holdingAnalysisList = []

        #Income Statement
        self.IS_numYearsAvailable = 0
        self.IS_endDate_list = []
        self.IS_totalRevenue_list = []
        self.IS_costOfRevenue_list = []
        self.IS_grossProfit_list = []

        self.IS_researchDevelopment_list = []
        self.IS_sellingGeneralAdministrative_list = []
        self.IS_nonRecurring_list = []
        self.IS_otherOperatingExpenses_list = []
        self.IS_totalOperatingExpenses_list = []
        self.IS_operatingIncome_list = []

        self.IS_totalOtherIncomeExpenseNet_list = []
        self.IS_ebit_list = []
        self.IS_interestExpense_list = []
        self.IS_incomeBeforeTax_list = []
        self.IS_incomeTaxExpense_list = []
        self.IS_minorityInterest_list = []
        self.IS_netIncomeFromContinuingOps_list = []
        self.IS_discontinuedOperations_list = []
        self.IS_extraordinaryItems_list = []
        self.IS_effectOfAccountingCharges_list = []
        self.IS_otherItems_list = []
        self.IS_netIncome_list = []

        #Balance Sheet
        self.BS_numYearsAvailable = 0

        self.BS_endDate_list = []
        self.BS_cash_list = []
        self.BS_shortTermInvestments_list = []
        self.BS_netReceivables_list = []
        self.BS_inventory_list = []
        self.BS_otherCurrentAssets_list = []
        self.BS_totalCurrentAssets_list = []
        self.BS_longTermInvestments_list = []
        self.BS_propertyPlantEquipment_list = []
        self.BS_goodWill_list = []
        self.BS_intangibleAssets_list = []
        self.BS_otherAssets_list = []
        self.BS_deferredLongTermAssetCharges_list = []
        self.BS_totalAssets_list = []

        self.BS_accountsPayable_list = []
        self.BS_shortLongTermDebt_list = []
        self.BS_otherCurrentLiab_list = []
        self.BS_totalCurrentLiabilities_list = []
        self.BS_longTermDebt_list = []
        self.BS_otherLiab_list = []
        self.BS_deferredLongTermLiab_list = []
        self.BS_minorityInterest_list = []
        self.BS_totalLiab_list = []

        self.BS_stockOptionWarrants_list = []
        self.BS_commonStock_list = []
        self.BS_retainedEarnings_list = []
        self.BS_treasuryStock_list = []
        self.BS_capitalSurplus_list = []
        self.BS_otherStockholderEquity_list = []
        self.BS_totalStockholderEquity_list = []
        self.BS_netTangibleAssets_list = []


        # Cashflow Statement

        self.CF_numYearsAvailable = 0

        self.CF_endDate_list = []
        self.CF_netIncome_list = []
        self.CF_depreciation_list = []
        self.CF_changeToNetincome_list = []
        self.CF_changeToAccountReceivables_list = []
        self.CF_changeToLiabilities_list = []
        self.CF_changeToInventory_list = []
        self.CF_changeToOperatingActivities_list = []
        self.CF_totalCashFromOperatingActivities_list = []

        self.CF_capitalExpenditures_list = []
        self.CF_investments_list = []
        self.CF_otherCashflowsFromInvestingActivities_list = []
        self.CF_totalCashflowsFromInvestingActivities_list = []

        self.CF_dividendsPaid_list = []
        self.CF_salePurchaseOfStock_list = []
        self.CF_netBorrowings_list = []
        self.CF_otherCashflowsFromFinancingActivities_list = []
        self.CF_totalCashFromFinancingActivities_list = []

        self.CF_effectOfExchangeRate_list = []
        self.CF_changeInCash_list = []

        #Valuation factors
        self.wacc = 0


    def quoteToString(self):

        string = "\n"

        if (self.getCompany() != None):
            string = string + "-----QUOTE SUMMARY FOR " + self.getCompany().upper() + "-----\n"

        string = nonlistItemToString(string, self.getName(), "Stock Name")
        string = nonlistItemToString(string, self.getCompany(), "Company")
        string = nonlistItemToString(string, self.getSymbol(), "Ticker Symbol")
        string = nonlistItemToString(string, self.getMarket(), "Stock Market")
        string = nonlistItemToString(string, self.getDateTime(), "Last Updated")
        string = nonlistItemToString(string, self.getPrice(), "Stock Price$")
        string = nonlistItemToString(string, self.getBid(), "Bid Price$")
        string = nonlistItemToString(string, self.getAsk(), "Ask Price$")
        string = nonlistItemToString(string, self.getBeta(), "Equity Beta")
        string = nonlistItemToString(string, self.getDividends(), "Dividends")
        string = nonlistItemToString(string, self.getMarketcap(), "Market cap")
        string = nonlistItemToString(string, self.getEnterprisevalue(), "Enterprise Value")
        string = nonlistItemToString(string, self.getPricebought(), "Price Bought")
        string = nonlistItemToString(string, self.getNumberbought(), "Shares Bought")

        string = string + "\n\n-----END OF QUOTE SUMMARY-----"

        '''print("-----Start of summary-----")

        total_paid = 0.00
        total_current = 0.00
        total_gain = 0.00

        for stock in stock_list:
            print(stock.quoteToString())

            total_paid += (stock.numberbought * stock.pricebought)
            total_current += (stock.numberbought * stock.price)

            gainloss = stock.price - stock.pricebought
            total_gain += gainloss

            if gainloss < 0:
                gainloss *= -1
                print(colored("Loss per share so far: $(" + str(gainloss) + ")", "red"))
                print(colored("Total loss so far: $(" + str(gainloss * stock.numberbought) + ")", "red") + "\n")
            else:
                print(colored("Gain per share so far: $" + str(gainloss), "green"))
                print(colored("Total gain so far: $" + str(gainloss * stock.numberbought), "green") + "\n")

        print("Total portfolio cost: $" + str(total_paid))
        print("Total portfolio value: $" + str(total_current))
        if total_gain < 0:
            print(colored("Total current loss: $(" + str(total_gain * -1) + ")", "red") + "\n")
        else:
            print(colored("Total current gain: $" + str(total_gain), "green") + "\n")'''

        return string


    def incomeStatementToString(self):

        string = "\n"
        
        if (self.getCompany() != None):
            string = string + "-----INCOME STATEMENT FOR " + self.getCompany().upper() + "-----\n"

        string = listItemToString(string, self.IS_endDate_list, "Year Ended")
        string = listItemToString(string, self.IS_totalRevenue_list, "Total Revenue")
        string = listItemToString(string, self.IS_costOfRevenue_list, "-Cost of Revenue")
        string = listItemToString(string, self.IS_grossProfit_list, "=Gross Profit")
        string = listItemToString(string, self.IS_researchDevelopment_list, "-R&D Costs")
        string = listItemToString(string, self.IS_sellingGeneralAdministrative_list, "-SG&A Cost")
        string = listItemToString(string, self.IS_nonRecurring_list, "-Non Recurring")
        string = listItemToString(string, self.IS_otherOperatingExpenses_list, "-Other Operating Exp")
        string = listItemToString(string, self.IS_totalOperatingExpenses_list, "-Total Operating Exp")
        string = listItemToString(string, self.IS_operatingIncome_list, "=Operating Income")
        string = listItemToString(string, self.IS_totalOtherIncomeExpenseNet_list, "-Other Income Exp, Net")
        string = listItemToString(string, self.IS_ebit_list, "=EBIT")
        string = listItemToString(string, self.IS_interestExpense_list, "-Interest Exp")
        string = listItemToString(string, self.IS_incomeBeforeTax_list, "=EBT")
        string = listItemToString(string, self.IS_incomeTaxExpense_list, "-Income Tax Exp")
        string = listItemToString(string, self.IS_minorityInterest_list, "-Minority Interest")
        string = listItemToString(string, self.IS_netIncomeFromContinuingOps_list, "=Net Income from Cont. Operationsnet")
        string = listItemToString(string, self.IS_discontinuedOperations_list, "+Disc. Operations")
        string = listItemToString(string, self.IS_extraordinaryItems_list, "-Extraordinary Items")
        string = listItemToString(string, self.IS_effectOfAccountingCharges_list, "-Effect of Accounting Changes")
        string = listItemToString(string, self.IS_otherItems_list, "-Other Items")
        string = listItemToString(string, self.IS_netIncome_list, "=Net Incomene")

        string = string + "\n\n-----END OF INCOME STATEMENT-----"

        return string

    def balanceSheetToString(self):

        string = "\n"

        if (self.getCompany() != None):
            string = string + "-----BALANCE SHEET FOR " + self.getCompany().upper() + "-----\n"

        string = listItemToString(string, self.BS_endDate_list, "As of")

        string = string + "\n\nASSETS\n"
        
        string = listItemToString(string, self.BS_cash_list, "Cash And Cash Equivalents")
        string = listItemToString(string, self.BS_shortTermInvestments_list, "Short Term Investments")
        string = listItemToString(string, self.BS_netReceivables_list, "Net Receivables")
        string = listItemToString(string, self.BS_inventory_list, "Inventory")
        string = listItemToString(string, self.BS_otherCurrentAssets_list, "Other Current Assets")
        string = listItemToString(string, self.BS_totalCurrentAssets_list, "Total Current Assets")
        string = listItemToString(string, self.BS_longTermInvestments_list, "Long Term Investments")
        string = listItemToString(string, self.BS_propertyPlantEquipment_list, "Property Plant and Equipment")
        string = listItemToString(string, self.BS_goodWill_list, "Goodwill")
        string = listItemToString(string, self.BS_intangibleAssets_list, "Intangible Assets")
        string = listItemToString(string, self.BS_otherAssets_list, "Other Assets")
        string = listItemToString(string, self.BS_deferredLongTermAssetCharges_list, "Deferred Long Term Asset Charges")
        string = listItemToString(string, self.BS_totalAssets_list, "Total Assets")

        string = string + "\n\nLIABILITIES \n"

        string = listItemToString(string, self.BS_accountsPayable_list, "Accounts Payable")
        string = listItemToString(string, self.BS_shortLongTermDebt_list, "Short/Current Long Term Debt")
        string = listItemToString(string, self.BS_otherCurrentLiab_list, "Other Current Liabilities")
        string = listItemToString(string, self.BS_totalCurrentLiabilities_list, "Total Current Liabilities")
        string = listItemToString(string, self.BS_longTermDebt_list, "Long Term Debt")
        string = listItemToString(string, self.BS_otherLiab_list, "Other Liabilities")
        string = listItemToString(string, self.BS_deferredLongTermLiab_list, "Deferred Long Term Liability Charges")
        string = listItemToString(string, self.BS_minorityInterest_list, "Minority Interest")
        string = listItemToString(string, self.BS_totalLiab_list, "Total Liabilities")

        string = string + "\n\nSHAREHOLDERS' EQUITY\n"

        string = listItemToString(string, self.BS_stockOptionWarrants_list, "Misc. Stocks Options Warrants")
        string = listItemToString(string, self.BS_commonStock_list, "Common Stock")
        string = listItemToString(string, self.BS_retainedEarnings_list, "Retained Earnings")
        string = listItemToString(string, self.BS_treasuryStock_list, "Treasury Stock")
        string = listItemToString(string, self.BS_capitalSurplus_list, "Additional Paid-in Capital")
        string = listItemToString(string, self.BS_otherStockholderEquity_list, "Other Stockholder Equity")
        string = listItemToString(string, self.BS_totalStockholderEquity_list, "Total Stockholder Equity")
        string = listItemToString(string, self.BS_netTangibleAssets_list, "Net Tangible Assets")

        string = string + "\n\n-----END OF BALANCE SHEET-----"

        return string

    def cashFlowStatementToString(self):

        string = "\n"

        if (self.getCompany() != None):
            string = string + "-----CASH FLOW STATEMENT FOR " + self.getCompany().upper() + "-----\n"

        string = listItemToString(string, self.CF_endDate_list, "Year Ended")

        string = string + "\n\nCASH FLOWS FROM OPERATING ACTIVITIES\n"

        string = listItemToString(string, self.CF_endDate_list, "Year Ended")
        string = listItemToString(string, self.CF_netIncome_list, "Net Income")
        string = listItemToString(string, self.CF_depreciation_list, "Depreciation")
        string = listItemToString(string, self.CF_changeToNetincome_list, "Adjustments To Net Income")
        string = listItemToString(string, self.CF_changeToAccountReceivables_list, "Changes In Accounts Receivables")
        string = listItemToString(string, self.CF_changeToLiabilities_list, "Changes In Liabilities")
        string = listItemToString(string, self.CF_changeToInventory_list, "Changes In Inventories")
        string = listItemToString(string, self.CF_changeToOperatingActivities_list, "Changes In Other Operating Activities")
        string = listItemToString(string, self.CF_totalCashFromOperatingActivities_list, "Total Cash Flow From Operating Activities")

        string = string + "\n\nCASH FLOWS FROM INVESTING ACTIVITIES\n"

        string = listItemToString(string, self.CF_capitalExpenditures_list, "Capital Expenditures")
        string = listItemToString(string, self.CF_investments_list, "Investments")
        string = listItemToString(string, self.CF_otherCashflowsFromInvestingActivities_list, "Other Cash flows from Investing Activities")
        string = listItemToString(string, self.CF_totalCashflowsFromInvestingActivities_list, "Total Cash Flows From Investing Activities")

        string = string + "\n\nCASH FLOWS FROM FINANCING ACTIVITIES\n"

        string = listItemToString(string, self.CF_dividendsPaid_list, "Dividends Paid")
        string = listItemToString(string, self.CF_salePurchaseOfStock_list, "Sale Purchase of Stock")
        string = listItemToString(string, self.CF_netBorrowings_list, "Net Borrowings")
        string = listItemToString(string, self.CF_otherCashflowsFromFinancingActivities_list, "Other Cash Flows from Financing Activities")
        string = listItemToString(string, self.CF_totalCashFromFinancingActivities_list, "Total Cash Flows From Financing Activities")

        string = listItemToString(string, self.CF_effectOfExchangeRate_list, "Effect Of Exchange Rate Changes")
        string = listItemToString(string, self.CF_changeInCash_list, "Change In Cash and Cash Equivalents")

        string = string + "\n\n-----END OF CASH FLOW STATEMENT-----"

        return string

    def quoteToListOfLists(self):

        title = "QUOTE SUMMARY FOR " + self.getCompany().upper()

        listOfLists = [[title], []]


        listOfLists = nonlistAddLabelAndAppend(listOfLists, self.getName(), "Stock Name")
        listOfLists = nonlistAddLabelAndAppend(listOfLists, self.getCompany(), "Company")
        listOfLists = nonlistAddLabelAndAppend(listOfLists, self.getSymbol(), "Ticker Symbol")
        listOfLists = nonlistAddLabelAndAppend(listOfLists, self.getMarket(), "Stock Market")

        listOfLists.append([])

        listOfLists = nonlistAddLabelAndAppend(listOfLists, self.getDateTime(), "Last Updated")
        listOfLists = nonlistAddLabelAndAppend(listOfLists, self.getPrice(), "Stock Price")
        listOfLists = nonlistAddLabelAndAppend(listOfLists, self.getBid(), "Bid Price")
        listOfLists = nonlistAddLabelAndAppend(listOfLists, self.getAsk(), "Ask Price")
        listOfLists = nonlistAddLabelAndAppend(listOfLists, self.getBeta(), "Equity Beta")
        listOfLists = nonlistAddLabelAndAppend(listOfLists, self.getDividends(), "Dividends")
        listOfLists = nonlistAddLabelAndAppend(listOfLists, self.getMarketcap(), "Market cap")
        listOfLists = nonlistAddLabelAndAppend(listOfLists, self.getEnterprisevalue(), "Enterprise Value")

        listOfLists.append([])

        listOfLists = nonlistAddLabelAndAppend(listOfLists, self.getPricebought(), "Price Bought")
        listOfLists = nonlistAddLabelAndAppend(listOfLists, self.getNumberbought(), "Shares Bought")

        #print(listOfLists)

        return listOfLists

    def incomeStatementToListOfLists(self):

        title = "INCOME STATEMENT FOR " + self.getCompany().upper()

        listOfLists = [[title], []]

        listOfLists = addLabelAndAppend(listOfLists, self.getIS_endDate_list(), "Year Ended")

        listOfLists = addLabelAndAppend(listOfLists, self.getIS_totalRevenue_list(), "Total Revenue")
        listOfLists = addLabelAndAppend(listOfLists, self.getIS_costOfRevenue_list(), "Cost of Revenue")
        listOfLists = addLabelAndAppend(listOfLists, self.getIS_grossProfit_list(), "Gross Profit")

        listOfLists.append([])
        listOfLists.append(["OPERATING EXPENSES"])
        listOfLists.append([])

        listOfLists = addLabelAndAppend(listOfLists, self.getIS_researchDevelopment_list(), "Research & Development Expense")
        listOfLists = addLabelAndAppend(listOfLists, self.getIS_sellingGeneralAdministrative_list(), "Selling, General & Administrative Expense")
        listOfLists = addLabelAndAppend(listOfLists, self.getIS_nonRecurring_list(), "Non-Recurring Expenses")
        listOfLists = addLabelAndAppend(listOfLists, self.getIS_otherOperatingExpenses_list(), "Other Operating Expenses")
        listOfLists = addLabelAndAppend(listOfLists, self.getIS_totalOperatingExpenses_list(), "Total Operating Expenses")
        listOfLists = addLabelAndAppend(listOfLists, self.getIS_operatingIncome_list(), "Operating Income")

        listOfLists.append([])
        listOfLists.append(["INCOME FROM CONTINUING OPERATIONS"])
        listOfLists.append([])

        listOfLists = addLabelAndAppend(listOfLists, self.getIS_totalOtherIncomeExpenseNet_list(), "Total Other Income Expense, Net")
        listOfLists = addLabelAndAppend(listOfLists, self.getIS_ebit_list(), "Earnings Before Interest and Taxes")
        listOfLists = addLabelAndAppend(listOfLists, self.getIS_interestExpense_list(), "Interest Expense")
        listOfLists = addLabelAndAppend(listOfLists, self.getIS_incomeBeforeTax_list(), "Earnings Before Taxes")
        listOfLists = addLabelAndAppend(listOfLists, self.getIS_incomeTaxExpense_list(), "Income Tax Expense")
        listOfLists = addLabelAndAppend(listOfLists, self.getIS_minorityInterest_list(), "Minority Interest")
        listOfLists = addLabelAndAppend(listOfLists, self.getIS_netIncomeFromContinuingOps_list(), "Net Income From Continuing Operations")

        listOfLists.append([])
        listOfLists.append(["NON-RECURRING EVENTS"])
        listOfLists.append([])

        listOfLists = addLabelAndAppend(listOfLists, self.getIS_discontinuedOperations_list(), "Discontinued Operations")
        listOfLists = addLabelAndAppend(listOfLists, self.getIS_extraordinaryItems_list(), "Extraordinary Items")
        listOfLists = addLabelAndAppend(listOfLists, self.getIS_effectOfAccountingCharges_list(), "Effect of Accounting Changes")
        listOfLists = addLabelAndAppend(listOfLists, self.getIS_otherItems_list(), "Other Items")

        listOfLists.append([])
        listOfLists.append(["NET INCOME"])
        listOfLists.append([])

        listOfLists = addLabelAndAppend(listOfLists, self.getIS_netIncome_list(), "Net Income")

        listOfLists.append([])
        listOfLists.append([])

        return listOfLists

    def balanceSheetToListOfLists(self):

        title = "BALANCE SHEET FOR " + self.getCompany().upper()

        listOfLists = [[title]]

        listOfLists.append([])
        listOfLists.append(["ASSETS"])
        listOfLists.append([])

        listOfLists = addLabelAndAppend(listOfLists, self.getBS_endDate_list(), "As Of")
        listOfLists = addLabelAndAppend(listOfLists, self.getBS_cash_list(), "Cash And Cash Equivalents")
        listOfLists = addLabelAndAppend(listOfLists, self.getBS_shortTermInvestments_list(), "Short Term Investments")
        listOfLists = addLabelAndAppend(listOfLists, self.getBS_netReceivables_list(), "Net Receivables")
        listOfLists = addLabelAndAppend(listOfLists, self.getBS_inventory_list(), "Inventory")
        listOfLists = addLabelAndAppend(listOfLists, self.getBS_otherCurrentAssets_list(), "Other Current Assets")
        listOfLists = addLabelAndAppend(listOfLists, self.getBS_totalCurrentAssets_list(), "Total Current Assets")
        listOfLists = addLabelAndAppend(listOfLists, self.getBS_longTermInvestments_list(), "Long Term Investments")
        listOfLists = addLabelAndAppend(listOfLists, self.getBS_propertyPlantEquipment_list(), "Property Plant and Equipment")
        listOfLists = addLabelAndAppend(listOfLists, self.getBS_goodWill_list(), "Goodwill")
        listOfLists = addLabelAndAppend(listOfLists, self.getBS_intangibleAssets_list(), "Intangible Assets")
        listOfLists = addLabelAndAppend(listOfLists, self.getBS_otherAssets_list(), "Other Assets")
        listOfLists = addLabelAndAppend(listOfLists, self.getBS_deferredLongTermAssetCharges_list(), "Deferred Long Term Asset Charges")
        listOfLists = addLabelAndAppend(listOfLists, self.getBS_totalAssets_list(), "Total Assets")

        listOfLists.append([])
        listOfLists.append(["LIABILITIES"])
        listOfLists.append([])

        listOfLists = addLabelAndAppend(listOfLists, self.getBS_accountsPayable_list(), "Accounts Payable")
        listOfLists = addLabelAndAppend(listOfLists, self.getBS_shortLongTermDebt_list(), "Short/Current Long Term Debt")
        listOfLists = addLabelAndAppend(listOfLists, self.getBS_otherCurrentLiab_list(), "Other Current Liabilities")
        listOfLists = addLabelAndAppend(listOfLists, self.getBS_totalCurrentLiabilities_list(), "Total Current Liabilities")
        listOfLists = addLabelAndAppend(listOfLists, self.getBS_longTermDebt_list(), "Long Term Debt")
        listOfLists = addLabelAndAppend(listOfLists, self.getBS_otherLiab_list(), "Other Liabilities")
        listOfLists = addLabelAndAppend(listOfLists, self.getBS_deferredLongTermLiab_list(), "Deferred Long Term Liability Charges")
        listOfLists = addLabelAndAppend(listOfLists, self.getBS_minorityInterest_list(), "Minority Interest")
        listOfLists = addLabelAndAppend(listOfLists, self.getBS_totalLiab_list(), "Total Liabilities")

        listOfLists.append([])
        listOfLists.append(["SHAREHOLDERS' EQUITY"])
        listOfLists.append([])

        listOfLists = addLabelAndAppend(listOfLists, self.getBS_stockOptionWarrants_list(), "Misc. Stocks Options Warrants")
        listOfLists = addLabelAndAppend(listOfLists, self.getBS_commonStock_list(), "Common Stock")
        listOfLists = addLabelAndAppend(listOfLists, self.getBS_retainedEarnings_list(), "Retained Earnings")
        listOfLists = addLabelAndAppend(listOfLists, self.getBS_treasuryStock_list(), "Treasury Stock")
        listOfLists = addLabelAndAppend(listOfLists, self.getBS_capitalSurplus_list(), "Additional Paid-in Capital")
        listOfLists = addLabelAndAppend(listOfLists, self.getBS_otherStockholderEquity_list(), "Other Stockholder Equity")
        listOfLists = addLabelAndAppend(listOfLists, self.getBS_totalStockholderEquity_list(), "Total Stockholder Equity")
        listOfLists = addLabelAndAppend(listOfLists, self.getBS_netTangibleAssets_list(), "Net Tangible Assets")

        listOfLists.append([])
        listOfLists.append([])

        return listOfLists


    def cashFlowStatementToListOfLists(self):

        title = "CASH FLOW STATEMENT FOR " + self.getCompany().upper()

        listOfLists = [[title], []]

        listOfLists = addLabelAndAppend(listOfLists, self.getCF_endDate_list(), "Year Ended")


        listOfLists.append([])
        listOfLists.append(["CASH FLOWS FROM OPERATING ACTIVITIES"])
        listOfLists.append([])

        listOfLists = addLabelAndAppend(listOfLists, self.getCF_netIncome_list(), "Net Income")
        listOfLists = addLabelAndAppend(listOfLists, self.getCF_depreciation_list(), "Depreciation")
        listOfLists = addLabelAndAppend(listOfLists, self.getCF_changeToNetincome_list(), "Adjustments To Net Income")
        listOfLists = addLabelAndAppend(listOfLists, self.getCF_changeToAccountReceivables_list(), "Changes In Accounts Receivables")
        listOfLists = addLabelAndAppend(listOfLists, self.getCF_changeToLiabilities_list(), "Changes In Liabilities")
        listOfLists = addLabelAndAppend(listOfLists, self.getCF_changeToInventory_list(), "Changes In Inventories")
        listOfLists = addLabelAndAppend(listOfLists, self.getCF_changeToOperatingActivities_list(), "Changes In Other Operating Activities")
        listOfLists = addLabelAndAppend(listOfLists, self.getCF_totalCashFromOperatingActivities_list(), "Total Cash Flow From Operating Activities")

        listOfLists.append([])
        listOfLists.append(["CASH FLOWS FROM INVESTING ACTIVITIES"])
        listOfLists.append([])

        listOfLists = addLabelAndAppend(listOfLists, self.getCF_capitalExpenditures_list(), "Capital Expenditures")
        listOfLists = addLabelAndAppend(listOfLists, self.getCF_investments_list(), "Investments")
        listOfLists = addLabelAndAppend(listOfLists, self.getCF_otherCashflowsFromInvestingActivities_list(), "Other Cash flows from Investing Activities")
        listOfLists = addLabelAndAppend(listOfLists, self.getCF_totalCashflowsFromInvestingActivities_list(), "Total Cash Flows From Investing Activities")

        listOfLists.append([])
        listOfLists.append(["CASH FLOWS FROM FINANCING ACTIVITIES"])
        listOfLists.append([])

        listOfLists = addLabelAndAppend(listOfLists, self.getCF_dividendsPaid_list(), "Dividends Paid")
        listOfLists = addLabelAndAppend(listOfLists, self.getCF_salePurchaseOfStock_list(), "Sale Purchase of Stock")
        listOfLists = addLabelAndAppend(listOfLists, self.getCF_netBorrowings_list(), "Net Borrowings")
        listOfLists = addLabelAndAppend(listOfLists, self.getCF_otherCashflowsFromFinancingActivities_list(), "Other Cash Flows from Financing Activities")
        listOfLists = addLabelAndAppend(listOfLists, self.getCF_totalCashFromFinancingActivities_list(), "Total Cash Flows From Financing Activities")

        listOfLists = addLabelAndAppend(listOfLists, self.getCF_effectOfExchangeRate_list(), "Effect Of Exchange Rate Changes")
        listOfLists = addLabelAndAppend(listOfLists, self.getCF_changeInCash_list(), "Change In Cash and Cash Equivalents")

        listOfLists.append([])
        listOfLists.append([])

        return listOfLists



#Getters and Setters

    def setCompany(self, company):
        self.company = company

    def getCompany(self):
        return self.company

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setSymbol(self, symbol):
        self.symbol = symbol

    def getSymbol(self):
        return self.symbol

    def setDateTime(self, dateTime):
        self.dateTime = dateTime

    def getDateTime(self):
        return self.dateTime

    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price

    def setAsk(self, ask):
        self.ask = ask

    def getAsk(self):
        return self.ask

    def setBid(self, bid):
        self.bid = bid

    def getBid(self):
        return self.bid

    def setDividends(self, dividends):
        self.dividends = dividends

    def getDividends(self):
        return self.dividends

    def setMarketcap(self, marketcap):
        self.marketcap = marketcap

    def getMarketcap(self):
        return self.marketcap

    def setBeta(self, beta):
        self.beta = beta

    def getBeta(self):
        return self.beta

    def setEnterprisevalue(self, enterprisevalue):
        self.enterprisevalue = enterprisevalue

    def getEnterprisevalue(self):
        return self.enterprisevalue

    def setNumberbought(self, numberbought):
        self.numberbought = numberbought

    def getNumberbought(self):
        return self.numberbought

    def setPricebought(self, pricebought):
        self.pricebought = pricebought

    def getPricebought(self):
        return self.pricebought

    def setMarket(self, market):
        self.market = market

    def getMarket(self):
        return self.market


    """INCOME STATEMENT"""

    def setIS_numYearsAvailable(self, IS_numYearsAvailable):
        self.IS_numYearsAvailable = IS_numYearsAvailable

    def getIS_numYearsAvailable(self):
        return self.IS_numYearsAvailable

    def setIS_endDateIS_list(self, IS_endDate_list):
        self.IS_endDate_list = IS_endDate_list

    def getIS_endDate_list(self):
        return self.IS_endDate_list

    def setIS_totalRevenue_list(self, IS_totalRevenue_list):
        self.IS_totalRevenue_list = IS_totalRevenue_list

    def getIS_totalRevenue_list(self):
        return self.IS_totalRevenue_list

    def setIS_costOfRevenue_list(self, IS_costOfRevenue_list):
        self.IS_costOfRevenue_list = IS_costOfRevenue_list

    def getIS_costOfRevenue_list(self):
        return self.IS_costOfRevenue_list

    def setIS_grossProfit_list(self, IS_grossProfit_list):
        self.IS_grossProfit_list = IS_grossProfit_list

    def getIS_grossProfit_list(self):
        return self.IS_grossProfit_list

    def setIS_researchDevelopment_list(self, IS_researchDevelopment_list):
        self.IS_researchDevelopment_list = IS_researchDevelopment_list

    def getIS_researchDevelopment_list(self):
        return self.IS_researchDevelopment_list

    def setIS_sellingGeneralAdministrative_list(self, IS_sellingGeneralAdministrative_list):
        self.IS_sellingGeneralAdministrative_list = IS_sellingGeneralAdministrative_list

    def getIS_sellingGeneralAdministrative_list(self):
        return self.IS_sellingGeneralAdministrative_list

    def setIS_nonRecurring_list(self, IS_nonRecurring_list):
        self.IS_nonRecurring_list = IS_nonRecurring_list

    def getIS_nonRecurring_list(self):
        return self.IS_nonRecurring_list

    def setIS_otherOperatingExpenses_list(self, IS_otherOperatingExpenses_list):
        self.IS_otherOperatingExpenses_list = IS_otherOperatingExpenses_list

    def getIS_otherOperatingExpenses_list(self):
        return self.IS_otherOperatingExpenses_list

    def setIS_totalOperatingExpenses_list(self, IS_totalOperatingExpenses_list):
        self.IS_totalOperatingExpenses_list = IS_totalOperatingExpenses_list

    def getIS_totalOperatingExpenses_list(self):
        return self.IS_totalOperatingExpenses_list

    def setIS_operatingIncome_list(self, IS_operatingIncome_list):
        self.IS_operatingIncome_list = IS_operatingIncome_list

    def getIS_operatingIncome_list(self):
        return self.IS_operatingIncome_list

    def setIS_totalOtherIncomeExpenseNet_list(self, IS_totalOtherIncomeExpenseNet_list):
        self.IS_totalOtherIncomeExpenseNet_list = IS_totalOtherIncomeExpenseNet_list

    def getIS_totalOtherIncomeExpenseNet_list(self):
        return self.IS_totalOtherIncomeExpenseNet_list

    def setIS_ebit_list(self, IS_ebit_list):
        self.IS_ebit_list = IS_ebit_list

    def getIS_ebit_list(self):
        return self.IS_ebit_list

    def setIS_interestExpense_list(self, IS_interestExpense_list):
        self.IS_interestExpense_list = IS_interestExpense_list

    def getIS_interestExpense_list(self):
        return self.IS_interestExpense_list

    def setIS_incomeBeforeTax_list(self, IS_incomeBeforeTax_list):
        self.IS_incomeBeforeTax_list = IS_incomeBeforeTax_list

    def getIS_incomeBeforeTax_list(self):
        return self.IS_incomeBeforeTax_list

    def setIS_incomeTaxExpense_list(self, IS_incomeTaxExpense_list):
        self.IS_incomeTaxExpense_list = IS_incomeTaxExpense_list

    def getIS_incomeTaxExpense_list(self):
        return self.IS_incomeTaxExpense_list

    def setIS_minorityInterest_list(self, IS_minorityInterest_list):
        self.IS_minorityInterest_list = IS_minorityInterest_list

    def getIS_minorityInterest_list(self):
        return self.IS_minorityInterest_list

    def setIS_netIncomeFromContinuingOps_list(self, IS_netIncomeFromContinuingOps_list):
        self.IS_netIncomeFromContinuingOps_list = IS_netIncomeFromContinuingOps_list

    def getIS_netIncomeFromContinuingOps_list(self):
        return self.IS_netIncomeFromContinuingOps_list

    def setIS_discontinuedOperations_list(self, IS_discontinuedOperations_list):
        self.IS_discontinuedOperations_list = IS_discontinuedOperations_list

    def getIS_discontinuedOperations_list(self):
        return self.IS_discontinuedOperations_list

    def setIS_extraordinaryItems_list(self, IS_extraordinaryItems_list):
        self.IS_extraordinaryItems_list = IS_extraordinaryItems_list

    def getIS_extraordinaryItems_list(self):
        return self.IS_extraordinaryItems_list

    def setIS_effectOfAccountingCharges_list(self, IS_effectOfAccountingChanges_list):
        self.IS_effectOfAccountingChanges_list = IS_effectOfAccountingChanges_list

    def getIS_effectOfAccountingCharges_list(self):
        return self.IS_effectOfAccountingChanges_list

    def setIS_otherItems_list(self, IS_otherItems_list):
        self.IS_otherItems_list = IS_otherItems_list

    def getIS_otherItems_list(self):
        return self.IS_otherItems_list

    def setIS_netIncome_list(self, IS_netIncome_list):
        self.IS_netIncome_list = IS_netIncome_list

    def getIS_netIncome_list(self):
        return self.IS_netIncome_list

    # Balance sheet

    def setBS_numYearsAvailable(self, BS_numYearsAvailable):
        self.BS_numYearsAvailable = BS_numYearsAvailable

    def getBS_numYearsAvailable(self):
        return self.BS_numYearsAvailable

    def setBS_endDate_list(self, BS_endDate_list):
        self.BS_endDate_list = BS_endDate_list

    def getBS_endDate_list(self):
        return self.BS_endDate_list

    def setBS_cash_list(self, BS_cash_list):
        self.BS_cash_list = BS_cash_list

    def getBS_cash_list(self):
        return self.BS_cash_list

    def setBS_shortTermInvestments_list(self, BS_shortTermInvestments_list):
        self.BS_shortTermInvestments_list = BS_shortTermInvestments_list

    def getBS_shortTermInvestments_list(self):
        return self.BS_shortTermInvestments_list

    def setBS_netReceivables_list(self, BS_netReceivables_list):
        self.BS_netReceivables_list = BS_netReceivables_list

    def getBS_netReceivables_list(self):
        return self.BS_netReceivables_list

    def setBS_inventory_list(self, BS_inventory_list):
        self.BS_inventory_list = BS_inventory_list

    def getBS_inventory_list(self):
        return self.BS_inventory_list

    def setBS_otherCurrentAssets_list(self, BS_otherCurrentAssets_list):
        self.BS_otherCurrentAssets_list = BS_otherCurrentAssets_list

    def getBS_otherCurrentAssets_list(self):
        return self.BS_otherCurrentAssets_list

    def setBS_totalCurrentAssets_list(self, BS_totalCurrentAssets_list):
        self.BS_totalCurrentAssets_list = BS_totalCurrentAssets_list

    def getBS_totalCurrentAssets_list(self):
        return self.BS_totalCurrentAssets_list

    def setBS_longTermInvestments_list(self, BS_longTermInvestments_list):
        self.BS_longTermInvestments_list = BS_longTermInvestments_list

    def getBS_longTermInvestments_list(self):
        return self.BS_longTermInvestments_list

    def setBS_propertyPlantEquipment_list(self, BS_propertyPlantEquipment_list):
        self.BS_propertyPlantEquipment_list = BS_propertyPlantEquipment_list

    def getBS_propertyPlantEquipment_list(self):
        return self.BS_propertyPlantEquipment_list

    def setBS_goodWill_list(self, BS_goodWill_list):
        self.BS_goodWill_list = BS_goodWill_list

    def getBS_goodWill_list(self):
        return self.BS_goodWill_list

    def setBS_intangibleAssets_list(self, BS_intangibleAssets_list):
        self.BS_intangibleAssets_list = BS_intangibleAssets_list

    def getBS_intangibleAssets_list(self):
        return self.BS_intangibleAssets_list

    def setBS_otherAssets_list(self, BS_otherAssets_list):
        self.BS_otherAssets_list = BS_otherAssets_list

    def getBS_otherAssets_list(self):
        return self.BS_otherAssets_list

    def setBS_deferredLongTermAssetCharges_list(self, BS_deferredLongTermAssetCharges_list):
        self.BS_deferredLongTermAssetCharges_list = BS_deferredLongTermAssetCharges_list

    def getBS_deferredLongTermAssetCharges_list(self):
        return self.BS_deferredLongTermAssetCharges_list

    def setBS_totalAssets_list(self, BS_totalAssets_list):
        self.BS_totalAssets_list = BS_totalAssets_list

    def getBS_totalAssets_list(self):
        return self.BS_totalAssets_list



    def setBS_accountsPayable_list(self, BS_accountsPayable_list):
        self.BS_accountsPayable_list = BS_accountsPayable_list

    def getBS_accountsPayable_list(self):
        return self.BS_accountsPayable_list

    def setBS_shortLongTermDebt_list(self, BS_shortLongTermDebt_list):
        self.BS_shortLongTermDebt_list = BS_shortLongTermDebt_list

    def getBS_shortLongTermDebt_list(self):
        return self.BS_shortLongTermDebt_list

    def setBS_otherCurrentLiab_list(self, BS_otherCurrentLiab_list):
        self.BS_otherCurrentLiab_list = BS_otherCurrentLiab_list

    def getBS_otherCurrentLiab_list(self):
        return self.BS_otherCurrentLiab_list

    def setBS_totalCurrentLiabilities_list(self, BS_totalCurrentLiabilities_list):
        self.BS_totalCurrentLiabilities_list = BS_totalCurrentLiabilities_list

    def getBS_totalCurrentLiabilities_list(self):
        return self.BS_totalCurrentLiabilities_list

    def setBS_longTermDebt_list(self, BS_longTermDebt_list):
        self.BS_longTermDebt_list = BS_longTermDebt_list

    def getBS_longTermDebt_list(self):
        return self.BS_longTermDebt_list

    def setBS_otherLiab_list(self, BS_otherLiab_list):
        self.BS_otherLiab_list = BS_otherLiab_list

    def getBS_otherLiab_list(self):
        return self.BS_otherLiab_list

    def setBS_deferredLongTermLiab_list(self, BS_deferredLongTermLiab_list):
        self.BS_deferredLongTermLiab_list = BS_deferredLongTermLiab_list

    def getBS_deferredLongTermLiab_list(self):
        return self.BS_deferredLongTermLiab_list

    def setBS_minorityInterest_list(self, BS_minorityInterest_list):
        self.BS_minorityInterest_list = BS_minorityInterest_list

    def getBS_minorityInterest_list(self):
        return self.BS_minorityInterest_list

    def setBS_totalLiab_list(self, BS_totalLiab_list):
        self.BS_totalLiab_list = BS_totalLiab_list

    def getBS_totalLiab_list(self):
        return self.BS_totalLiab_list



    def setBS_stockOptionWarrants_list(self, BS_stockOptionWarrants_list):
        self.BS_stockOptionWarrants_list = BS_stockOptionWarrants_list

    def getBS_stockOptionWarrants_list(self):
        return self.BS_stockOptionWarrants_list

    def setBS_commonStock_list(self, BS_commonStock_list):
        self.BS_commonStock_list = BS_commonStock_list

    def getBS_commonStock_list(self):
        return self.BS_commonStock_list

    def setBS_retainedEarnings_list(self, BS_retainedEarnings_list):
        self.BS_retainedEarnings_list = BS_retainedEarnings_list

    def getBS_retainedEarnings_list(self):
        return self.BS_retainedEarnings_list

    def setBS_treasuryStock_list(self, BS_treasuryStock_list):
        self.BS_treasuryStock_list = BS_treasuryStock_list

    def getBS_treasuryStock_list(self):
        return self.BS_treasuryStock_list

    def setBS_capitalSurplus_list(self, BS_capitalSurplus_list):
        self.BS_capitalSurplus_list = BS_capitalSurplus_list

    def getBS_capitalSurplus_list(self):
        return self.BS_capitalSurplus_list

    def setBS_otherStockholderEquity_list(self, BS_otherStockholderEquity_list):
        self.BS_otherStockholderEquity_list = BS_otherStockholderEquity_list

    def getBS_otherStockholderEquity_list(self):
        return self.BS_otherStockholderEquity_list

    def setBS_totalStockholderEquity_list(self, BS_totalStockholderEquity_list):
        self.BS_totalStockholderEquity_list = BS_totalStockholderEquity_list

    def getBS_totalStockholderEquity_list(self):
        return self.BS_totalStockholderEquity_list

    def setBS_netTangibleAssets_list(self, BS_netTangibleAssets_list):
        self.BS_netTangibleAssets_list = BS_netTangibleAssets_list

    def getBS_netTangibleAssets_list(self):
        return self.BS_netTangibleAssets_list

    """Cashflow statement"""

    def setCF_numYearsAvailable(self, CF_numYearsAvailable):
        self.CF_numYearsAvailable = CF_numYearsAvailable

    def getCF_numYearsAvailable(self):
        return self.CF_numYearsAvailable

    def setCF_endDate_list(self, CF_endDate_list):
        self.CF_endDate_list = CF_endDate_list

    def getCF_endDate_list(self):
        return self.CF_endDate_list

    def setCF_netIncome_list(self, CF_netIncome_list):
        self.CF_netIncome_list = CF_netIncome_list

    def getCF_netIncome_list(self):
        return self.CF_netIncome_list

    def setCF_depreciation_list(self, CF_depreciation_list):
        self.CF_depreciation_list = CF_depreciation_list

    def getCF_depreciation_list(self):
        return self.CF_depreciation_list

    def setCF_changeToNetincome_list(self, CF_changeToNetincome_list):
        self.CF_changeToNetincome_list = CF_changeToNetincome_list

    def getCF_changeToNetincome_list(self):
        return self.CF_changeToNetincome_list

    def setCF_changeToAccountReceivables_list(self, CF_changeToAccountReceivables_list):
        self.CF_changeToAccountReceivables_list = CF_changeToAccountReceivables_list

    def getCF_changeToAccountReceivables_list(self):
        return self.CF_changeToAccountReceivables_list

    def setCF_changeToLiabilities_list(self, CF_changeToLiabilities_list):
        self.CF_changeToLiabilities_list = CF_changeToLiabilities_list

    def getCF_changeToLiabilities_list(self):
        return self.CF_changeToLiabilities_list

    def setCF_changeToInventory_list(self, CF_changeToInventory_list):
        self.CF_changeToInventory_list = CF_changeToInventory_list

    def getCF_changeToInventory_list(self):
        return self.CF_changeToInventory_list

    def setCF_changeToOperatingActivities_list(self, CF_changeToOperatingActivities_list):
        self.CF_changeToOperatingActivities_list = CF_changeToOperatingActivities_list

    def getCF_changeToOperatingActivities_list(self):
        return self.CF_changeToOperatingActivities_list

    def setCF_totalCashFromOperatingActivities_list(self, CF_totalCashFromOperatingActivities_list):
        self.CF_totalCashFromOperatingActivities_list = CF_totalCashFromOperatingActivities_list

    def getCF_totalCashFromOperatingActivities_list(self):
        return self.CF_totalCashFromOperatingActivities_list



    def setCF_capitalExpenditures_list(self, CF_capitalExpenditures_list):
        self.CF_capitalExpenditures_list = CF_capitalExpenditures_list

    def getCF_capitalExpenditures_list(self):
        return self.CF_capitalExpenditures_list

    def setCF_investments_list(self, CF_investments_list):
        self.CF_investments_list = CF_investments_list

    def getCF_investments_list(self):
        return self.CF_investments_list

    def setCF_otherCashflowsFromInvestingActivities_list(self, CF_otherCashflowsFromInvestingActivities_list):
        self.CF_otherCashflowsFromInvestingActivities_list = CF_otherCashflowsFromInvestingActivities_list

    def getCF_otherCashflowsFromInvestingActivities_list(self):
        return self.CF_otherCashflowsFromInvestingActivities_list

    def setCF_totalCashflowsFromInvestingActivities_list(self, CF_totalCashflowsFromInvestingActivities_list):
        self.CF_totalCashflowsFromInvestingActivities_list = CF_totalCashflowsFromInvestingActivities_list

    def getCF_totalCashflowsFromInvestingActivities_list(self):
        return self.CF_totalCashflowsFromInvestingActivities_list

    def setCF_dividendsPaid_list(self, CF_dividendsPaid_list):
        self.CF_dividendsPaid_list = CF_dividendsPaid_list

    def getCF_dividendsPaid_list(self):
        return self.CF_dividendsPaid_list

    def setCF_salePurchaseOfStock_list(self, CF_salePurchaseOfStock_list):
        self.CF_salePurchaseOfStock_list = CF_salePurchaseOfStock_list

    def getCF_salePurchaseOfStock_list(self):
        return self.CF_salePurchaseOfStock_list

    def setCF_netBorrowings_list(self, CF_netBorrowings_list):
        self.CF_netBorrowings_list = CF_netBorrowings_list

    def getCF_netBorrowings_list(self):
        return self.CF_netBorrowings_list

    def setCF_otherCashflowsFromFinancingActivities_list(self, CF_otherCashflowsFromFinancingActivities_list):
        self.CF_otherCashflowsFromFinancingActivities_list = CF_otherCashflowsFromFinancingActivities_list

    def getCF_otherCashflowsFromFinancingActivities_list(self):
        return self.CF_otherCashflowsFromFinancingActivities_list

    def setCF_totalCashFromFinancingActivities_list(self, CF_totalCashFromFinancingActivities_list):
        self.CF_totalCashFromFinancingActivities_list = CF_totalCashFromFinancingActivities_list

    def getCF_totalCashFromFinancingActivities_list(self):
        return self.CF_totalCashFromFinancingActivities_list


    def setCF_effectOfExchangeRate_list(self, CF_effectOfExchangeRate_list):
        self.CF_effectOfExchangeRate_list = CF_effectOfExchangeRate_list

    def getCF_effectOfExchangeRate_list(self):
        return self.CF_effectOfExchangeRate_list

    def setCF_changeInCash_list(self, CF_changeInCash_list):
        self.CF_changeInCash_list = CF_changeInCash_list

    def getCF_changeInCash_list(self):
        return self.CF_changeInCash_list



    def setHoldingAnalysisList(self, holdingAnalysisList):
        self.holdingAnalysisList = holdingAnalysisList

    def getHoldingAnalysisList(self):
        return self.holdingAnalysisList
