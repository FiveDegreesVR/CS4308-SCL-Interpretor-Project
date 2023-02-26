# Tokens
import json


# class keywords:
#     keywords = ['import', 'implementations', 'function', 'main', 'return',
#                 'type', 'integer', 'double', 'char', 'num', 'is', 'variables',
#                 'define', 'of', 'begin', 'display', 'set', 'exit', 'endfun',
#                 'symbol', 'end', 'input', 'structures', 'pointer', 'head',
#                 'last', 'NULL', 'ChNode', 'using', 'reverse', 'while',
#                 'endwhile',
#                 'call']  # KEYWORDS from token document (many one off tokens (such as main) from the document have been consolidated under keywords)
#     keywordsID = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
#                   17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
#                   32]  # 33
#
#
# class identifiers:
#     identifiers = ['x', 'r', 'area', 'cir', 'pchar', 'j']  # CONST from the token document
#     identifiersID = [200, 201, 202, 203, 204, 205]
#
#
# class operators:
#     operators = ['+', '-', '*', '/', '^', '>', '<', '"',
#                  '=']  # OPERATORS from token document (= was made into an operator as opposed
#     operatorsID = [400, 401, 402, 403, 404, 405, 406, 407, 408, ]
#
#
# class literals:
#     literals = []  # STATEMENTS from the token document
#     # string literals occur after the tokens 'input' or 'display
#     # header (and .c) literals occur after the token 'import'
#     # '49.95' occurs after 'set' 'x' '='
#     literalsID = [600]
#
#
# class specialSymbols:
#     specialSymbols = [',', '.', 'PI', 'M_PI']  # PI is a statement, M_PI is the value of PI? (leave as is for now...)
#     specialSymbolsID = [800, 801, 802, 803, 804]


# for each x in lineList
# for each i in keywords
# if lineList[x] == keywords[i]
# print('Next token is:' + keywordsID[i] + 'Next lexeme is ' + lineList[i]
# for each i in identifiers
# if lineList[x] == identifiers[i]
# print('Next token is:' + identifiersID[i] + 'Next lexeme is ' + lineList[i]
# for each i in operators
# if lineList[x] == operators[i]
# print('Next token is:' + operatorsID[i] + 'Next lexeme is ' + lineList[i]
# for each i in literals
# if lineList[x] == literals[i]
# print('Next token is:' + literalsID[0] + 'Next lexeme is ' + lineList[i]
# for each i in specialSymbols
# if lineList[x] == specialSymbols[i]
# print('Next token is:' + specialSymbolsID[i] + 'Next lexeme is ' + lineList[i]


# writing token list to json: https://pythonexamples.org/python-write-json-to-file/
# import json
# aDict = {tokensHere} #?
# jsonString
# if __name__ == '__main__':
#  Area_cir = filter_file("areacir.scl")


# ?Create a dynamic array that records tokens as they are encountered in the given file, Then
# jsonString = json.dumps(keywords.keywords)
# jsonString = json.dumps(keywords.keywords, identifiers.identifiers, operators.operators, literals.literals, specialSymbols.specialSymbols)
# jsonString = json.dumps(keywords, identifiers, operators, literals, specialSymbols)
# jsonFile = open ("tokenList", "w")
# jsonFile.write(jsonString)
# jsonString = json.dumps(identifiers.identifiers)
# jsonFile.write(jsonString)
# jsonString = json.dumps(operators.operators)
# jsonFile.write(jsonString)
# jsonString = json.dumps(literals.literals)
# jsonFile.write(jsonString)
# jsonString = json.dumps(specialSymbols.specialSymbols) #Find a better way
# jsonFile.close()

tokenList = {
    "keywords": {
        'import': 0,
        'implementations': 1,
        'function': 2,
        'main': 3,
        'return': 4,
        'type': 5,
        'integer': 6,
        'double': 7,
        'char': 8,
        'num': 9,
        'is': 10,
        'variables': 11,
        'define': 12,
        'of': 13,
        'begin': 14,
        'display': 15,
        'set': 16,
        'exit': 17,
        'endfun': 18,
        'symbol': 19,
        'end': 20,
        'input': 21,
        'structures': 22,
        'pointer': 23,
        'head': 24,
        'last': 25,
        'NULL': 26,
        'ChNode': 27,
        'using': 28,
        'reverse': 29,
        'while': 30,
        'endwhile': 31,
        'call': 32
    },

    "identifiers": {
        'x': 200,
        'r': 201,
        'area': 202,
        'cir': 203,
        'pchar': 204,
        'j': 205
    },

    "operators": {
        '+': 400,
        '-': 401,
        '*': 402,
        '/': 403,
        '^': 404,
        '>': 405,
        '<': 406,
        '"': 407,
        '=': 408
    },

    "specialSymbols": {
        ',': 800,
        '.': 801,
        'PI': 802,
        'M_PI': 803
    }
}


class Token:
    def __init__(self, type, id, value):
        self.type = type
        self.id = id
        self.value = value

    def getData(self):
        return [self.type, self.id, self.value]
