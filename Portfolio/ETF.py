from Formatting import listItemToString, addLabelAndAppend, nonlistItemToString, nonlistAddLabelAndAppend


class ETF():
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

        # Holding Analysis
        self.holdingAnalysisList = []


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
        string = listItemToString(string, self.IS_netIncomeFromContinuingOps_list,
                                  "=Net Income from Cont. Operationsnet")
        string = listItemToString(string, self.IS_discontinuedOperations_list, "+Disc. Operations")
        string = listItemToString(string, self.IS_extraordinaryItems_list, "-Extraordinary Items")
        string = listItemToString(string, self.IS_effectOfAccountingCharges_list, "-Effect of Accounting Changes")
        string = listItemToString(string, self.IS_otherItems_list, "-Other Items")
        string = listItemToString(string, self.IS_netIncome_list, "=Net Incomene")

        string = string + "\n\n-----END OF INCOME STATEMENT-----"

        return string


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

        listOfLists = addLabelAndAppend(listOfLists, self.getIS_researchDevelopment_list(),
                                        "Research & Development Expense")
        listOfLists = addLabelAndAppend(listOfLists, self.getIS_sellingGeneralAdministrative_list(),
                                        "Selling, General & Administrative Expense")
        listOfLists = addLabelAndAppend(listOfLists, self.getIS_nonRecurring_list(), "Non-Recurring Expenses")
        listOfLists = addLabelAndAppend(listOfLists, self.getIS_otherOperatingExpenses_list(),
                                        "Other Operating Expenses")
        listOfLists = addLabelAndAppend(listOfLists, self.getIS_totalOperatingExpenses_list(),
                                        "Total Operating Expenses")
        listOfLists = addLabelAndAppend(listOfLists, self.getIS_operatingIncome_list(), "Operating Income")

        listOfLists.append([])
        listOfLists.append(["INCOME FROM CONTINUING OPERATIONS"])
        listOfLists.append([])

        listOfLists = addLabelAndAppend(listOfLists, self.getIS_totalOtherIncomeExpenseNet_list(),
                                        "Total Other Income Expense, Net")
        listOfLists = addLabelAndAppend(listOfLists, self.getIS_ebit_list(), "Earnings Before Interest and Taxes")
        listOfLists = addLabelAndAppend(listOfLists, self.getIS_interestExpense_list(), "Interest Expense")
        listOfLists = addLabelAndAppend(listOfLists, self.getIS_incomeBeforeTax_list(), "Earnings Before Taxes")
        listOfLists = addLabelAndAppend(listOfLists, self.getIS_incomeTaxExpense_list(), "Income Tax Expense")
        listOfLists = addLabelAndAppend(listOfLists, self.getIS_minorityInterest_list(), "Minority Interest")
        listOfLists = addLabelAndAppend(listOfLists, self.getIS_netIncomeFromContinuingOps_list(),
                                        "Net Income From Continuing Operations")

        listOfLists.append([])
        listOfLists.append(["NON-RECURRING EVENTS"])
        listOfLists.append([])

        listOfLists = addLabelAndAppend(listOfLists, self.getIS_discontinuedOperations_list(),
                                        "Discontinued Operations")
        listOfLists = addLabelAndAppend(listOfLists, self.getIS_extraordinaryItems_list(), "Extraordinary Items")
        listOfLists = addLabelAndAppend(listOfLists, self.getIS_effectOfAccountingCharges_list(),
                                        "Effect of Accounting Changes")
        listOfLists = addLabelAndAppend(listOfLists, self.getIS_otherItems_list(), "Other Items")

        listOfLists.append([])
        listOfLists.append(["NET INCOME"])
        listOfLists.append([])

        listOfLists = addLabelAndAppend(listOfLists, self.getIS_netIncome_list(), "Net Income")

        listOfLists.append([])
        listOfLists.append([])

        return listOfLists



    # Getters and Setters

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
