import datetime


class Inflation():
    def __init__(self):
        self.inflation = {} #key=year, value=rate
        self.timestamp = None

    def inflationToString(self):

        current_year = int(datetime.datetime.now().year)

        string = "\n"

        string = string + "-----START OF HISTORICAL AND PROJECTED INFLATION-----\n"

        string = string + "\nRetrieved on " + str(self.timestamp)
        string = string + "\nInflation for " + str(current_year-5) + ": " + self.inflation[current_year-5]
        string = string + "\nInflation for " + str(current_year-4) + ": " + self.inflation[current_year-4]
        string = string + "\nInflation for " + str(current_year-3) + ": " + self.inflation[current_year-3]
        string = string + "\nInflation for " + str(current_year-2) + ": " + self.inflation[current_year-2]
        string = string + "\nInflation for " + str(current_year-1) + ": " + self.inflation[current_year-1]
        string = string + "\nInflation for " + str(current_year) + ": " + self.inflation[current_year]
        string = string + "\nInflation for " + str(current_year+1) + ": " + self.inflation[current_year+1]
        string = string + "\nInflation for " + str(current_year+2) + ": " + self.inflation[current_year+2]
        string = string + "\nInflation for " + str(current_year+3) + ": " + self.inflation[current_year+3]
        string = string + "\nInflation for " + str(current_year + 4) + ": " + self.inflation[current_year+4]
        string = string + "\nInflation for " + str(current_year + 5) + ": " + self.inflation[current_year+5]
        string = string + "\n*Annual percent changes based on average consumer prices"

        string = string + "\n\n-----END OF HISTORICAL AND PROJECTED INFLATION-----"

        return string

    def inflationToListOfLists(self):

        current_year = int(datetime.datetime.now().year)

        title = "PROJECTED INFLATION"

        listOfLists = [[title], []]

        listOfLists.append(["Retrieved on", self.timestamp])
        listOfLists.append(["Inflation for", current_year - 5, self.inflation[current_year - 5]])
        listOfLists.append(["Inflation for", current_year - 4, self.inflation[current_year - 4]])
        listOfLists.append(["Inflation for", current_year - 3, self.inflation[current_year - 3]])
        listOfLists.append(["Inflation for", current_year - 2, self.inflation[current_year - 2]])
        listOfLists.append(["Inflation for", current_year - 1, self.inflation[current_year - 1]])
        listOfLists.append(["Inflation for", current_year, self.inflation[current_year]])
        listOfLists.append(["Inflation for", current_year + 1, self.inflation[current_year + 1]])
        listOfLists.append(["Inflation for", current_year + 2, self.inflation[current_year + 2]])
        listOfLists.append(["Inflation for", current_year + 3, self.inflation[current_year + 3]])
        listOfLists.append(["Inflation for", current_year + 4, self.inflation[current_year + 4]])
        listOfLists.append(["Inflation for", current_year + 5, self.inflation[current_year + 5]])
        listOfLists.append(["","","*Annual percent changes based on average consumer prices"])

        listOfLists.append([])
        listOfLists.append([])

        return listOfLists




