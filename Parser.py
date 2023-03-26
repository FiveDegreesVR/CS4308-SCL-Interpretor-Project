# # from Scl_Scanner import *

# # #funtionality of getNextToken was fulfilled in deliverable 1
# # #Read in tokens and parse out left to right, top from bottom

# # json_file = open('OutputTokens.json')
# # json_data = json.load(json_file)

# # class ParseTree(object):
# #     def __init__(self):
# #         self.left = None
# #         self.right = None
# #         self.root = None

# # for item in json_data:
# #     #print(json_data[item]['value'])
# #     #print(json_data[item]['Type'])
# #     if not json_data[item]['value'] == 'EOS':
# #         print(json_data[item]['value'])
# #     else:
# #         print('\n')

# from Scl_Scanner import *
# import json
# from itertools import islice
# # funtionality of getNextToken was fulfilled in deliverable 1
# # Read in tokens and parse out left to right, top from bottom
# jsonFile = open('OutputTokens.json')
# jsonData = json.load(jsonFile)
# jsonFileTree = open("ParseTree.json", "w")

# #Might not be needed, overcomplicated


# # What this seems to be trying to accomplish is he is using templist as like a lookahead, but you can't use value b/c that is a string and is not comparable to numbers
# # Need to make a function that looks ahead and returns the amount of tokens after the root
# # Length is fine, just need to use range to iterate it

# def LookAhead(jsonFile,x):
#     counter = 0
#     for i in islice(jsonFile,x,None):
#         if(jsonFile[i]['value'] == "EOS"):
#             print(counter,"end of loop")
#             return counter
#         else:
#             print(counter)
#             counter = counter+1

# # Above def is done, returns the amount of elements after root
# # LookAhead looks at the next tokens until it finds a EOS token and then stops and returns the number
# #def Node_allocation()


# #   For the if statements in PTree, I was planning on making them into their own function so that I could call it recursively in the child_nodes > 3 portion but I suppose you also could just call PTree recursively
# #   You would need to change it a bit tho, so I recommend creating a different function for it
# #   The counter number is set the way it is for testing, not anything else, should normally start at 0, as PTree will be used to create all the parse trees
# #   Not sure how we want to store the parse tree, I personally was thinking textfile but we can do it however
# #   Need a way to dynamically change counter based on what if statement it was pulled into, so that it skips over what was just done
# #   Also if you create a function for this if statements, you will likely have to implement the saving there as well as printing, and have it return counter so the PTree can call it again.

# def PTree(jsonFile,tempList):
#     counter = 47
#     # counter is to show where the program currently is in the json file
#     # Look ahead will always be 1 more than counter due to it messing up the if statements otherwise
#     child_nodes = LookAhead(jsonFile,48)
#     if(child_nodes > 3):
#         print("more than 3")
#         print("\n")
#     elif(child_nodes==3):
#         print("equal to 3")
#         print("\n")
#     elif(child_nodes==2):
#         print("        ",tempList[counter])
#         print("    /   ","        ","    \\   ")
#         print("  ",tempList[counter+1],"             ", tempList[counter+2])
#         print("equal to 2")
#         print("\n")
#     elif(child_nodes==1):
#         print("        ",tempList[counter])
#         print("        ","   |     ")
#         print("        ",tempList[counter+1])
#         print("equal to 1")
#         print("\n")
#     else:
#         print("        ",tempList[counter])
#         print("leafnode")
#         print("\n")

# tempList = []

# for item in jsonData:
#     tempList.append(jsonData[item]['value'])



# # This was just for testing
# LookAhead(jsonData,3)
# PTree(jsonData,tempList)



from Scl_Scanner import *
import json
from itertools import islice
from Scl_Scanner import *
from Token import *
import json

# funtionality of getNextToken was fulfilled in deliverable 1
# Read in tokens and parse out left to right, top from bottom

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = str()
        self.right = str()
        self.count = 0
        self.lineCount = 0
        self.last_data = str()

    # dont ask
    def UpdateCounts(self, lineCount):
        self.data = "Line: " + str(lineCount)
        lineCount += 1
        if self.left is not str():
            self.left.UpdateCounts(lineCount)

    def PrintTree(self):
        print(self.data)
        if self.right is not str():
            self.right.PrintTree()
        if self.left is not str():
            self.left.PrintTree()

    def iterate(self, num):
        if self.count != 0:
            if self.left is not str():
                self.left.iterate(num)
            num = num + 1
        return num

    def insert(self, data):
        iterations = self.iterate(0)
        if iterations > 0:
            self.left.insert(data)
        else:
            if data == "EOS":
                if self.left is not str():
                    self.left.insert(self.count + 1)
                else:
                    self.left = TreeNode(self.count + 1)
                self.count += 1
            elif self.right is not str():
                self.right.insert(data)
            elif self.right is str():
                self.right = TreeNode(data)
        # if self.data is isinstance(self.data, int):
        #     self.right = TreeNode(data)
        #     self.right = TreeNode(data)


#funtionality of getNextToken was fulfilled in deliverable 1
#Read in tokens and parse out left to right, top from bottom

countTk = -1

def GetNextToken(countTk, tokenList):
    countTk += 1
    return tokenList[countTk]

if __name__ == '__main__':
    sysArgv = sys.argv  # scan file from sys argvs

    tokenList = GenerateTokenList(sysArgv[1])

    # example call
    # token = GetNextToken(countTk, tokenList)

    # ---------------------------- Parser Code

    root = TreeNode(0)
    countIterate = -1
    for item in tokenList:
        root.insert(GetNextToken(countIterate, tokenList).value)
        #print(GetNextToken(countIterate, tokenList).value)
        countIterate = countIterate+1

    root.UpdateCounts(0)
    root.PrintTree()