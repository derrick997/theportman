

class TBond():
    def __init__(self):
        self.bill13Wk = 0
        self.bond5Yr = 0
        self.bond10Yr = 0
        self.bond30Yr = 0
        self.dateTime = None

    def tBondToString(self):

        string = "\n"

        string = string + "-----TREASURY BOND YIELDS-----\n"

        string = string + "\nRetrieved on " + str(self.dateTime)
        string = string + "\n13 Wk Treasury Bill: " + str(self.getbill13Wk())
        string = string + "\n5 Yr Treasury Bond: " + str(self.getbond5Yr())
        string = string + "\n10 Yr Treasury Bond: " + str(self.getbond10Yr())
        string = string + "\n30 Yr Treasury Bond: " + str(self.getbond30Yr())

        string = string + "\n\n-----END TREASURY BOND YIELDS-----"

        return string

    def tBondToListOfLists(self):

        title = "TREASURY BOND YIELDS"

        listOfLists = [[title], []]

        listOfLists.append(["Retrieved on", self.dateTime])
        listOfLists.append(["13 Wk Treasury Bill", self.getbill13Wk()])
        listOfLists.append(["5 Yr Treasury Bond", self.getbond5Yr()])
        listOfLists.append(["10 Yr Treasury Bond", self.getbond10Yr()])
        listOfLists.append(["30 Yr Treasury Bond", self.getbond30Yr()])

        listOfLists.append([])
        listOfLists.append([])

        return listOfLists

    
    def setbill13Wk(self, bill13Wk):
        self.bill13Wk = bill13Wk

    def getbill13Wk(self):
        return self.bill13Wk
    
    def setbond5Yr(self, bond5Yr):
        self.bond5Yr = bond5Yr

    def getbond5Yr(self):
        return self.bond5Yr
    
    def setbond10Yr(self, bond10Yr):
        self.bond10Yr = bond10Yr

    def getbond10Yr(self):
        return self.bond10Yr
    
    def setbond30Yr(self, bond30Yr):
        self.bond30Yr = bond30Yr

    def getbond30Yr(self):
        return self.bond30Yr
    

