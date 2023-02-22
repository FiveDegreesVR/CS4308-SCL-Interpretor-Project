#Tokens
keywords = ['import', 'implementations', 'function', 'main', 'return',
            'type', 'integer', 'double', 'char', 'num', 'is', 'variables',
            'define', 'of', 'begin', 'display', 'set', 'exit', 'endfun',
            'symbol', 'end', 'input', 'structures', 'pointer', 'head',
            'last', 'NULL', 'ChNode', 'using', 'reverse', 'while',
            'endwhile', 'call'] #KEYWORDS from token document (many one off tokens (such as main) from the document have been consolidated under keywords)
identifiers = ['x', 'r',  'area', 'cir', 'pchar', 'j']#CONST from the token document
operators = ['+', '-', '*', '/', '^', '>', '<', '"', '='] #OPERATORS from token document (= was made into an operator as opposed
literals = [ '45.95', 'Welcome to the world of SCL', 'Value of x:', 'Enter value of radius:',
            'Value of radius:', 'Value of area:', 'Value of circumference:',
            'scl.h', 'stdio.h', 'stdlib.h', 'string.h', 'recrevlisth.c'] #STATEMENTS from the token document
specialSymbols = [',', '.', 'PI', 'M_PI'] #PI is a statement, M_PI is the value of PI? (leave as is for now...)