from Scl_Scanner import *
from Token import *
import json

#funtionality of getNextToken was fulfilled in deliverable 1 
#Read in tokens and parse out left to right, top from bottom

count = -1

def GetNextToken(count, tokenList):
    count += 1
    return tokenList[count]

if __name__ == '__main__':
    sysArgv = sys.argv  # scan file from sys argvs

    tokenList = GenerateTokenList(sysArgv[1])

    # example call
    token = GetNextToken(count, tokenList)


