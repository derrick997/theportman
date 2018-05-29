

# financial statement items to string
def listItemToString(string, listItem, label):
    if (listItem != None):
        itemStr = '\t'.join(str(e) for e in listItem)
        string = string + "\n" + label + ": \t" + itemStr
    return string

def addLabelAndAppend(listOfLists, listGetter, label):
    listGetter.insert(0, label)
    listOfLists.append(listGetter)
    return listOfLists

def nonlistItemToString(string, nonlistItem, label):
    if (nonlistItem != None):
        string = string + "\n" + label + ": \t" + str(nonlistItem)
    else:
        string = string + "\n" + label + ": \t Unavailable"
    return string

def nonlistAddLabelAndAppend(listOfLists, nonlistGetter, label):
    listOfLists.append([label, nonlistGetter])
    return listOfLists