import datetime


class Inflation():
    def __init__(self):
        self.inflation = {} #key=year, value=rate
        self.timestamp = None

    def InflationToString(self):

        current_year = int(datetime.date.year)

        string = "\n"

        string = string + "-----START OF PROJECTED INFLATION-----\n"

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

        string = string + "\n\n-----END OF PROJECTED INFLATION-----"

        return string

    def InflationToListOfLists(self):

        title = "PROJECTED INFLATION"

        listOfLists = [[title], []]

        listOfLists.append(["Retrieved on", self.timestamp])

        listOfLists.append([])
        listOfLists.append([])

        return listOfLists




