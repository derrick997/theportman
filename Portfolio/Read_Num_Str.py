import datetime

# FORMATO

# lee el numero desde un indice inicial, y convierte ',' a '.'
def getNum(page, start_index=0):
    if (page == "<COULDN'T ACCESS WEBSITE>" or page == "<OCR COULDN'T READ PROPERLY>"):
        return page
    pageLength = len(page)
    index = start_index
    result = str()

    while (index < pageLength):
        if (page[index] == ' ' or page[index] == "\t" or page[index] == ">"):
            index += 1
        elif ((page[index] == '-') or (page[index] == '+')):
            result = result + page[index]
            index += 1
        else:
            break

    while (index<pageLength):
        if (page[index].isdigit()):
            result = result + page[index]
            index += 1
        else:
            break

    while (index<pageLength):
        if (page[index] == ',') or (page[index] == '.'):
            result = result + '.'
            index += 1
        else:
            break

    while (index<pageLength):
        if (page[index].isdigit()):
            result = result + page[index]
            index += 1
        elif (page[index] == ","):
            index += 1
        else:
            break

    # return "no num found" if no number found
    if (result == "" or result == "," or result == "." or result == "+" or result == "-"):
        return "<NO NUM FOUND>"

    # return number in appropriate type
    if (len(result) > 1) and (result.find(".") != -1 or result.find(",") != -1):
        return float(result)
    else:
        return int(result)

# lee el numero desde un indice inicial, borra '.', y convierte ',' a '.'
def getNumAlt(page, start_index):
    if (page == "<COULDN'T ACCESS WEBSITE>" or page == "<OCR COULDN'T READ PROPERLY>"):
        return page

    pageLength = len(page)
    index = start_index
    result = str()

    while (index < pageLength):
        if (page[index] == ' ' or page[index] == "\t" or page[index] == ">"):
            index += 1
        elif ((page[index] == '-') or (page[index] == '+')):
            result = result + page[index]
            index += 1
        else:
            break

    while (index < pageLength):
        if (page[index].isdigit()):
            result = result + page[index]
            index += 1
        elif (page[index] == "."):
            index += 1
        else:
            break

    while (index < pageLength):
        if (page[index] == ','):
            result = result + '.'
            index += 1
        else:
            break

    while (index < pageLength):
        if (page[index].isdigit()):
            result = result + page[index]
            index += 1
        elif (page[index] == ","):
            index += 1
        else:
            break

    # return "no num found" if no number found
    if (result == "" or result == "," or result == "." or result == "+" or result == "-"):
        return "<NO NUM FOUND>"

    # return number in appropriate type
    if (len(result) > 1) and (result.find(".") != -1 or result.find(",") != -1):
        return float(result)
    else:
        return int(result)

# ignore the following characters until a digit is found. then, return the number.  hasta el limite desde punto de inicio
def getNextNum(page, start_index, limit=500):
    if (page == "<COULDN'T ACCESS WEBSITE>" or page == "<OCR COULDN'T READ PROPERLY>"):
        return page
    pageLength = len(page)
    index = start_index
    limit = start_index+limit

    while (index < pageLength and index < limit):
        if (page[index] == "+" or page[index] == "-") and (page[index+1].isdigit()):
            break
        elif not (page[index].isdigit()):
            index += 1
        else:
            break
    result = getNum(page, index)
    return result

# ignore the following characters until a digit is found. then, return date for mm/dd/yyyy in date type. hasta el limite desde punto de inicio
def getNextDate(page, start_index, limit=500):
    if (page == "<COULDN'T ACCESS WEBSITE>" or page == "<OCR COULDN'T READ PROPERLY>"):
        return page
    pageLength = len(page)
    index = start_index
    limit = start_index+limit

    while (index < pageLength and index < limit):
        if (page[index] == "+" or page[index] == "-") and (page[index+1].isdigit()):
            break
        elif not (page[index].isdigit()):
            index += 1
        else:
            break
    month = getNum(page, index)
    index += 2

    while (index < pageLength and index < limit):
        if (page[index] == "+" or page[index] == "-") and (page[index+1].isdigit()):
            break
        elif not (page[index].isdigit()):
            index += 1
        else:
            break

    date = getNum(page, index)
    index += 2

    while (index < pageLength and index < limit):
        if (page[index] == "+" or page[index] == "-") and (page[index+1].isdigit()):
            break
        elif not (page[index].isdigit()):
            index += 1
        else:
            break

    year = getNum(page, index)

    result = datetime.date(year, month, date)

    return result

# ignore the following characters until a digit is found, using getNumAlt. then, return the number. hasta el limite desde punto de inicio
def getNextNumAlt(page, start_index, limit=500):
    if (page == "<COULDN'T ACCESS WEBSITE>" or page == "<OCR COULDN'T READ PROPERLY>"):
        return page
    pageLength = len(page)
    index = start_index
    limit = start_index + limit

    while (index < pageLength and index < limit):
        if (page[index] == "+" or page[index] == "-") and (page[index+1].isdigit()):
            break
        elif not (page[index].isdigit()):
            index += 1
        else:
            break
    result = getNumAlt(page, index)
    return result

def getPrevNum(page, start_index, limit=500):
    if (page == "<COULDN'T ACCESS WEBSITE>" or page == "<OCR COULDN'T READ PROPERLY>"):
        return page
    index = start_index
    limit = start_index-limit

    while (index > -1 and index > limit):
        #print(page[index])
        if (page[index] == "+" or page[index] == "-") and (page[index+1].isdigit()):
            break
        elif not (page[index].isdigit()):
            index -= 1
        else:
            break

    while (index > -1 and index > limit):
        if (page[index] == "+" or page[index] == "-"):
            break
        elif (page[index] == "." or page[index] == ",") and (page[index-1].isdigit()):
            index -= 1
        elif not (page[index].isdigit()):
            index += 1
            break
        else:
            index -= 1

    result = getNum(page, index)
    return result



# lee la string (entre " ") desde un indice inicial, hasta el limite desde punto de inicio
def getNextStr(page, start_index, limit=500):
    if (page == "<COULDN'T ACCESS WEBSITE>" or page == "<OCR COULDN'T READ PROPERLY>"):
        return page

    index = start_index
    result = str()
    char = page[index]
    limit = start_index + limit

    while (char != '"' and index<limit):
        index += 1
        char = page[index]

    if (char == '"' and index<limit):
        index += 1
        char = page[index]

    while (char != '"'and index<limit):
        result = result + char
        index += 1
        char = page[index]

    if result == "":
        result = "-1"
    return result

# Given a text (e.g. html text), this function will print out every string (i.e. each string between " ")
def print_strings(text, endIndex=5000):
    currentIndex = 0
    previndex = -1
    while (currentIndex < endIndex - 3):
        if (previndex >= currentIndex):
            break
        previndex = currentIndex
        currentStr, currentIndex = readNextString(text, currentIndex)
        print(currentStr)
        print(currentIndex)

# iterator for print_strings
def readNextString(page, index):
    startIndex = page.find('"', index) +1
    endIndex = page.find('"', startIndex)
    theStr = page[startIndex:endIndex]
    #print(theStr)
    return theStr, endIndex+1

# returns the string from the index until the given char
def readCharsUntil(page, startIndex, endChar):
    currentIndex = startIndex
    string = ""
    while(1):
        currentChar = str(page[currentIndex])
        if currentChar == endChar:
            break
        string = string + str(page[currentIndex])
        currentIndex+=1
    return string

#returns true if the next subset of subsetLength length contains the given string
def nextIndicesContain(page, startIndex, subsetLength, string):
    substring = page[startIndex: startIndex+subsetLength]
    return (string in substring)


#Get the next num, or return 0 if "{}" in the next 35 chars
def catchStatementNum(statement, keyString):
    valueIndex = statement.find(keyString)
    if valueIndex != -1:
        if nextIndicesContain(statement, valueIndex, 35, ":{},"):
            return 0
        else:
            value = getNextNum(statement, valueIndex)
            return value
    else:
        return 0 #placeholder value if index not found