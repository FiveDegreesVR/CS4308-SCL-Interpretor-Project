import Parser
from Parser import *
from itertools import islice
from Parser import TreeNode


Converted_List = []

def rightmost(root):
    if(root.right.data is not str()):
        rightmost(root.right)

    return root.data

def rightfull(root, statement):
    if(root.right.data is not str()):
            if(root.right.data is "PI"):
                  statement = statement + "math.pi"
            else:
                statement = statement + root.right.data
            rightfull(root.right, statement)
    return statement

# Loop_bit is to make sure you remember the indent for the loop until endloop statement appears
def convert(root):
    Converted = []
    Loop_bit = 0
    print(root.data)
    if(root.data is not int):
        if((str)(root.data) == "define"):
            if(root.right.data  is "N"):
                Converted.append("N = 100")
            elif(root.right.data is "varr"):
                 Converted.append("varr = [0] * N")
            else:
                Converted.append(root.right.data + "= 0")
        elif(root.data == "input"):
            if(rightmost(root) is "num"):
                Converted.append(rightmost(root) + "= int(input("+ root.right.data+"))")
            else:
                Converted.append(rightmost(root) + "= float(input("+ root.right.data+"))")
        elif(root.data == "set"):
            Converted.append(rightfull(root,str()))
        elif(root.data == "symbol"):
            Converted.append("import math")
        elif(root.data == "display"):
            Converted.append("print("+root.right.data+","+rightmost(root)+")")
        elif(root.data == "for"):
            Converted.append("for j in range(num):")
            Loop_bit = 1

    return Converted

if __name__ == '__main__':
    sysArgv = sys.argv
    ParsedRoot = Parser.Parse(sysArgv[1])
    ParsedRoot.PrintTree()
    while(ParsedRoot.left.data != None):
        print(convert(ParsedRoot.right))
        ParsedRoot = ParsedRoot.left
