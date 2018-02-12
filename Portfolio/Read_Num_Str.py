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
