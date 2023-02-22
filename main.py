def remove_items(test_list, item):
    # using list comprehension to perform the task
    res = [i for i in test_list if i != item]

    return res


# group 6 (Allen Smith, Nikita Smith, Josh Poore, Cole Young)
if __name__ == '__main__':
    file = open('areacir.scl', 'r')

    # filtering off:
    # Block Comments
    # Empty Lines
    # Empty Spaces
    # Line Comments

    Comment = False
    lineList = []

    for line in file:

        lineTokens = line.split(' ')

        # Filters Block Comments (Proof of Concept, need to implement temp for changes)
        commentStart = "/*"
        commentEnd = "*/"

        if commentStart in line:
            Comment = True

        if not Comment:
            lineList.append(lineTokens)

        if commentEnd in line:
            Comment = False
        # End of Block comment filter

        # Need to do \n thing here

    # Empty space token filter
    loopCount = 0
    for line in lineList:
        lineList[loopCount] = remove_items(line, '')
        loopCount += 1

    # \n filter
    loopCount = 0
    for line in lineList:
        modifiedStr = line[len(line) - 1]
        modifiedStr = modifiedStr[:-1]
        line[len(line) - 1] = modifiedStr
        lineList[loopCount] = line
        loopCount += 1

    # line comment filter
    loopCount = 0
    for line in lineList:
        if '//' in line:
            line = line[:line.index('//')]
            lineList[loopCount] = line
        loopCount += 1

    # Empty Line filter
    for line in lineList:
        if line[0] == '':
            lineList.remove(line)

    lineList = list(filter(None, lineList))

    # Split '"' into separate tokens
    loopCount = 0
    for line in lineList:
        newLine = []

        for token in line:
            # covers if " is at the beginning of the token
            if '"' in token[0] and len(token) > 1:
                idx = token.index('"')
                newLine.append('"')
                newLine.append(token[1:])
            else:
                newLine.append(token)

            # covers if " is at the end of the token
            if '"' in newLine[len(newLine) - 1]:
                newLine[len(newLine) - 1] = newLine[len(newLine) - 1].removesuffix('"')
                newLine.append('"')

        lineList[loopCount] = newLine
        loopCount += 1

    # print final filtered list
    for line in lineList:
        print(line)
