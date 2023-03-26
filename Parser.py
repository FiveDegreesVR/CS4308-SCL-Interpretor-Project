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
        self.middle = str()

    def PrintTree(self):
        if self.data is not str():
            if self.data is isinstance(self.data, TreeNode):
                self.data.PrintTree()
            else:
                print(self.data,"\n yo")
        if self.right is not str():
            if self.right is isinstance(self.right, TreeNode):
                self.right.PrintTree()
            else:
                print(self.right,"\n how")
        if self.middle is not str():
            if self.middle is isinstance(self.middle, TreeNode):
                self.middle.PrintTree()
            else:
                print(self.middle,"\n it")
        if self.left is not str():
            if self.left is isinstance(self.left, TreeNode):
                self.left.PrintTree()
            else:
                print(self.left,"\n is")

    def insert(self, data):
        if self.data is str():
            self.data = data
        # If current data is '('
        elif data == '(':
            self.left = TreeNode(data)

        # If current data is an operator
        elif data == '*' or data == '/' or data == '+' or data == '-' or data == '=':
            self.middle = TreeNode(data)

        # If current data is ')'
        elif data == ')':
            self.right = TreeNode(data)

        # If current data is a keyword or variable
        else:
            if self.left is str():
                self.left = TreeNode(data)
            elif self.right is str():
                self.right = TreeNode(data)
            else:
                self.middle = TreeNode(data)

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
    # token = GetNextToken(count, tokenList)

    # ---------------------------- Parser Code

    jsonFile = open('OutputTokens.json')
    jsonData = json.load(jsonFile)

    tempList = []
    count = 0
    root = TreeNode(str())

    for item in jsonData:
        tempList.append(jsonData[item]['value'])

    for item in jsonData:
        if not jsonData[item]['value'] == 'EOS':
            root.insert(tempList[count])
        count = count + 1

    root.PrintTree()

