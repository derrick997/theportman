
class MRP():
    def __init__(self):

        #current month
        self.MRP1 = 0
        self.MRP1datetime = None

        #previous month
        self.MRP0 = 0
        self.MRP0datetime = None

        self.timestamp = None

    def MRPToString(self):

        string = "\n"

        string = string + "-----START OF MARKET RISK PREMIUM-----\n"

        string = string + "\nRetrieved on " + str(self.timestamp)
        string = string + "\nCurrent Market Risk Premium: " + str(self.MRP1) + "% for the month of " + str(self.MRP1datetime)[:10]
        string = string + "\nPrevious Market Risk Premium: " + str(self.MRP0) + "% for the month of " + str(self.MRP0datetime)[:10]
        string = string + "\n*These are trailing 12 month, with adjusted payout"

        string = string + "\n\n-----END OF MARKET RISK PREMIUM-----"

        return string

    def MRPToListOfLists(self):

        title = "MARKET RISK PREMIUM"

        listOfLists = [[title], []]

        listOfLists.append(["Retrieved on", self.timestamp])
        listOfLists.append(["Current Market Risk Premium", self.MRP1, "for the month of", self.MRP1datetime])
        listOfLists.append(["Previous Market Risk Premium", self.MRP0, "for the month of", self.MRP0datetime])
        listOfLists.append(["*These are trailing 12 month, with adjusted payout"])

        listOfLists.append([])
        listOfLists.append([])

        return listOfLists




