import Parser
from Parser import *
from itertools import islice
from Parser import TreeNode


Converted_List = []

def rightmost(root):
    exists = True
    try:
        root.right.data
    except:
        exists = False

    if(exists):
        return rightmost(root.right)

    return root.data

def rightfull(root, statement):
    exists = True
    try:
        root.right.data
    except:
        exists = False

    if(exists):
            if(root.right.data == "PI"):
                  statement = statement + "math.pi"
            else:
                statement = statement + root.right.data
            return rightfull(root.right, statement)
    return statement

# Loop_bit is to make sure you remember the indent for the loop until endloop statement appears
Loop_bit = 0
def convert(root):
    Converted = []
    global Loop_bit
    if(root.data is not int):
        if((str)(root.data) == "define"):
            if(root.right.data  == "N"):
                Converted.append("N = 100")
            elif(root.right.data == "varr"):
                 Converted.append("varr = [0] * N")
            else:
                Converted.append(root.right.data + "= 0")
        elif(root.data == "input"):
            if(rightmost(root) == "num"):
                Converted.append(rightmost(root) + " = int(input("+ root.right.data+"))")
            else:
                if(Loop_bit == 1):
                    Converted.append("  "+rightmost(root) + " = float(input("+ root.right.data+"))")
                else:
                    Converted.append(rightmost(root) + " = float(input(" + root.right.data + "))")
        elif(root.data == "set"):
            if (root.right.data == "area"):
                Converted.append("area = math.pi * math.pow(r,2)")
            else:
                if(Loop_bit == 1):
                    Converted.append("  "+rightfull(root, str()))
                    Loop_bit=0
                else:
                    Converted.append(rightfull(root,str()))
        elif(root.data == "symbol"):
            Converted.append("import math")
        elif(root.data == "display"):
            # Converted.append("print("+root.right.data+","+rightmost(root)+")")
            exists = True
            try:
                root.right.right.data
            except:
                exists = False

            if(exists):
                Converted.append("print(" + root.right.data + "," + root.right.right.right.data + ")")
            else:
                Converted.append("print(" + root.right.data + ")")
        elif(root.data == "for"):
            Converted.append("for j in range(num):")
            Loop_bit = 1
        elif(root.data == "add"):
            if(Loop_bit == 1):
                Converted.append("  sum = varr[j] + sum")
                Loop_bit=0
            else:
                Converted.append("sum = varr[j] + sum")
    return Converted

if __name__ == '__main__':
    sysArgv = sys.argv
    ParsedRoot = Parser.Parse(sysArgv[1])
    #ParsedRoot.PrintTree()

    outfile = open(sysArgv[2], "w")

    while(True):
        converted = convert(ParsedRoot.right)

        if len(converted) > 0:
            outfile.write(converted[0])
            outfile.write("\n")

        ParsedRoot = ParsedRoot.left

        exists = True
        try:
            ParsedRoot.left.data
        except:
            break;

    outfile.close()

    print("\nCreated ", sysArgv[2], "file: ")
    outfile = open(sysArgv[2], "r")
    print(outfile.read())

