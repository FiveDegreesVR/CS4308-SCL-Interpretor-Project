from Parser import *
from itertools import islice
from Parser import TreeNode


Converted_List = []

def rightmost(TreeNode root):
        if(root.right.data is not str()):
             rightmost(root.right)
        
        return root.data

def rightfull(TreeNode root, String statement):
     if(root.right.data is not str()):
             if(root.right.data is "PI"):
                  statement = statement + "math.pi"
             else:
                statement = statement + root.right.data
             rightfull(root.right, statement)
        return statement
             

def convert(TreeNode root):
    Converted = []
    if(root.data is not int):
         if(root.data is "define"):
              if(root.right.data  is "N"):
                   Converted.append("N = 100")
              else:
                   Converted.append(root.right.data + "= 0")
            elif(root.data is "input"):
              Converted.append(rightmost(root) + "= int(input("+ root.right.data+"))")
            elif(root.data is "set"):
              Converted.append(rightfull(root,str()))
            elif(root.data is "symbol"):
              Converted.append("import math")
            elif(root.data is "display"):
              
