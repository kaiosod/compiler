import re

# Identificador - nome da var, classe, função ou constante

# Atribuição - =
# Comparador - == =! > <
# Operador - + - / *
# Palavra Reservada - show, lite, numb

list_identifier = []
list_operator= []
list_keyWord = []

dict_lex = {'Identifier':list_identifier,
            'Operator':list_operator,
            'Key World':list_keyWord}

def analisador(inp):
    list_inp = inp.split('\n')
    
    for line in list_inp:
        #Splitar por espaço e por operador 
        # list_lexemas = line.split(' ')
        list_lexemas = re.split("[+|\-|\/|*|\s]", line)
        list_lexemas = list(filter(None, list_lexemas))
        
        for i in list_lexemas:
            if re.match('[A-Z]+|[a-z]+',i) != None:
                list_identifier.append(i)
            elif re.match('[+|\-|\/|*]',i) != None:
                list_operator.append(i)
            elif i == 'liter' or i == 'numb' or i == 'show':
                list_keyWord.append(i)

    return dict_lex
                

            
       
    

