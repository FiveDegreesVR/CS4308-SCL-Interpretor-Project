import Token
kw = Token.keywords()
id = Token.identifiers()
op = Token.operators()
lit = Token.literals()
spS = Token.specialSymbols()

def remove_items(test_list, item):
    # using list comprehension to perform the task
    res = [i for i in test_list if i != item]

    return res


def filter_file(File_name):
    file = open(File_name, 'r')
    # filtering off:
    # Block Comments
    # Empty Lines
    # Empty Spaces
    # Line Comments

    Comment = False
    lineList = []

    for line in file:
        lineTokens = []
        if '"' in line:
            splitLocation = line.find('"')
            beforeStr = line[:splitLocation]
            afterStr = line[splitLocation:]
            secondSplitLocation = splitLocation + afterStr[1:].find('"') + 1
            thirdSplitLocation = afterStr[1:].find('"')
            strStatement = line[splitLocation:secondSplitLocation + 1]
            afterStr = line[secondSplitLocation + 1:]

            beforeStatementTokens = beforeStr.split(' ')
            for token in beforeStatementTokens:
                lineTokens.append(token)

            lineTokens.append(strStatement)

            if afterStr != '\n':
                afterStatementTokens = afterStr.split(' ')
                for token in afterStatementTokens:
                    lineTokens.append(token)

            lineList.append(lineTokens)
            continue

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


    # for line in file:
    #
    #     lineTokens = line.split(' ')
    #
    #     # Filters Block Comments (Proof of Concept, need to implement temp for changes)
    #     commentStart = "/*"
    #     commentEnd = "*/"
    #
    #     if commentStart in line:
    #         Comment = True
    #
    #     if not Comment:
    #         lineList.append(lineTokens)
    #
    #     if commentEnd in line:
    #         Comment = False
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
        if '\n' in line[len(line) - 1]:
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
    # loopCount = 0
    # for line in lineList:
    #     newLine = []
    #
    #     for token in line:
    #         # covers if " is at the beginning of the token
    #         if '"' in token[0] and len(token) > 1:
    #             idx = token.index('"')
    #             newLine.append('"')
    #             newLine.append(token[1:])
    #         else:
    #             newLine.append(token)
    #
    #         # covers if " is at the end of the token
    #         if '"' in newLine[len(newLine) - 1]:
    #             newLine[len(newLine) - 1] = newLine[len(newLine) - 1].removesuffix('"')
    #             newLine.append('"')
    #
    #     lineList[loopCount] = newLine
    #     loopCount += 1

    # print final filtered list
    for line in lineList:
        print(line)

    return lineList

# def printToken(fileList, kw, id, op, lit, spS)
#     for each x in lineList
#         for each i in keywords
#                 if lineList[x] == keywords[i]
#                 print('Next token is:' + keywordsID[i] + 'Next lexeme is ' + lineList[i]
#         for each i in identifiers
#             if lineList[x] == identifiers[i]
#                 print('Next token is:' + identifiersID[i] + 'Next lexeme is ' + lineList[i]
#         for each i in operators
#             if lineList[x] == operators[i]
#                 print('Next token is:' + operatorsID[i] + 'Next lexeme is ' + lineList[i]
#         for each i in literals
#             if lineList[x] == literals[i]
#                 print('Next token is:' + literalsID[0] + 'Next lexeme is ' + lineList[i]
#         for each i in specialSymbols
#             if lineList[x] == specialSymbols[i]
#                 print('Next token is:' + specialSymbolsID[i] + 'Next lexeme is ' + lineList[i]



# group 6 (Allen Smith, Nikita Smith, Josh Poore, Cole Young)
# TODO: 1. turn output list into token obj with token type, token id, and value (whats stored in the token)
# TODO: 2. print tokens to JSON file + console at runtime
# TODO: 3. feed in .scl file through argument when calling "main" (ex: "python scl_scanner.py areacir.py" for scanning areacir.py)

if __name__ == '__main__':
    Area_cir = filter_file("areacir.scl")

