import re 

class Lexer:
    def __init__(self,inp):
        self.list_identifier = []
        self.list_operator= []
        self.list_keyWord = []
        self.list_delimiter = []
        self.inp = inp

        self.dict_lex = {'Identificador':self.list_identifier,
                        'Operador':self.list_operator,
                        'Palavra Chave':self.list_keyWord,
                        'Delimitador':self.list_delimiter}

    def identifier_tokens(self):
        list_inp = self.inp.split('\n')

        for line in list_inp:
            
            # list_lexemas = line.split(' ')
            list_lexemas = re.split("\s", line)
            list_lexemas = list(filter(None, list_lexemas))
            print(list_lexemas)

            for i in list_lexemas:
                c = 0
                if re.match('[A-Z]+|[a-z]+',i) != None:
                    for j in ['numb','liter','boole','if','else','true','false','null','show','doit','loop','case','orcase','other']:
                        if i == j:
                            c = 1
                            self.list_keyWord.append(i)
                            break
                    if c != 1:  
                        self.list_identifier.append(i)
                            
                elif re.match('[+|\-|\/|*|=]',i) != None:
                    self.list_operator.append(i)

                elif re.match('[,|.||(|)]',i) != None:
                    self.list_delimiter.append(i)

        # list(set(lista))

        self.list_keyWord = list(set(self.list_keyWord))
        self.list_identifier = list(set(self.list_identifier))
        self.list_operator = list(set(self.list_operator))

        self.dict_lex = {'Identificador':self.list_identifier,
                        'Operador':self.list_operator,
                        'Palavra Chave':self.list_keyWord,
                        'Delimitador':self.list_delimiter}


        return self.dict_lex