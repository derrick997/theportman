from Stock import Stock


def stockHoldingAnalysis(stock):

    analysisListOfLists = None
    analysisString = None

    string = "\n"

    if (stock.getCompany() != None):

        string = string + "-----HOLDING ANALYSIS FOR " + stock.getCompany().upper() + "-----\n\n"

        total_paid = (stock.getNumberbought() * stock.getPricebought())
        string = string + "Price of stocks at buy: $" + str(stock.getPricebought()) + "\n"
        string = string + "Total paid for stocks: $" + str(total_paid) + "\n"

        gainloss = stock.price - stock.pricebought
        total_gainloss = gainloss * stock.numberbought

        title = "HOLDING ANALYSIS FOR " + stock.getCompany().upper()
        analysisListOfLists = [[title], [], ["Price at buy", stock.getPricebought()],
                               ["Total paid for stocks", total_paid]]

        if gainloss < 0:
            gainloss *= -1
            string = string + "Loss per share so far: $(" + str(gainloss) + ")\n"
            string = string + "Total loss so far: $(" + str(total_gainloss) + ")\n"

            analysisListOfLists.append(["Loss per share so far", gainloss])
            analysisListOfLists.append(["Total loss so far", total_gainloss])

        else:
            string = string + "Gain per share so far: $" + str(gainloss) + "\n"
            string = string + "Total gain so far: $" + str(total_gainloss) + "\n"

            analysisListOfLists.append(["Gain per share so far", gainloss])
            analysisListOfLists.append(["Total gain so far", total_gainloss])

        analysisString = string + "\n-----END OF HOLDING ANALYSIS-----"

        stock.setHoldingAnalysisList(analysisListOfLists)

        return stock, analysisString
