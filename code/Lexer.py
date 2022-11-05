import re 

class Lexer:
    def __init__(self,inp):
        self.list_identifier = []
        self.list_operator= []
        self.list_keyWord = []
        self.inp = inp

        self.dict_lex = {'Identifier':self.list_identifier,
                        'Operator':self.list_operator,
                        'Key World':self.list_keyWord}

    def identifier_tokens(self):
        list_inp = self.inp.split('\n')

        for line in list_inp:
            
            # list_lexemas = line.split(' ')
            list_lexemas = re.split("\s", line)
            list_lexemas = list(filter(None, list_lexemas))
            print(list_lexemas)
            
            for i in list_lexemas:
                if re.match('[A-Z]+|[a-z]+',i) != None:
                    self.list_identifier.append(i)
                elif re.match('[+|\-|\/|*|=]',i) != None:
                    self.list_operator.append(i)
                elif i == 'liter' or i == 'numb' or i == 'show':
                    self.list_keyWord.append(i)

        return self.dict_lex