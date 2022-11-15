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

            line = self.remove_comments(line)
            line = self.remove_garbage(line)
            
                        
            # Does not consider space
            for i in line:
                if re.match('[+|\-|\/|*|=]',i) != None:
                    self.list_operator.append(i)
                    line = line.replace(i,'')

                elif re.match('[,|.||(|)]',i) != None:
                    self.list_delimiter.append(i)

            # Remove Args of functions
            line = self.remove_args(line)

            list_lexemas = re.split("\s", line)

            # Drop duplicates
            list_lexemas = list(filter(None, list_lexemas))

            
            # Consider space
            for i in list_lexemas:
                c = 0

                if re.match('[A-Z]+|[a-z]+',i) != None:
                    for j in ['numb','liter','boole','if','else','true','false','null','show','doit','loop','case','orcase','other','range','in']:
                        if i == j:
                            c = 1
                            self.list_keyWord.append(i)
                            break
                    if c != 1:  
                        self.list_identifier.append(i)
                            
   
        self.list_keyWord = list(set(self.list_keyWord))
        self.list_identifier = list(set(self.list_identifier))
        self.list_operator = list(set(self.list_operator))
        self.list_delimiter = list(set(self.list_delimiter))

        self.dict_lex = {'Identificador':self.list_identifier,
                        'Operador':self.list_operator,
                        'Palavra Chave':self.list_keyWord,
                        'Delimitador':self.list_delimiter}


        return self.dict_lex

    def remove_comments(self,line):
        if re.findall('//',line) != None:
            
            try:
                line_pos = re.search('//',line)
                line_comment = line[line_pos.span()[0]:]
                out = line.replace(line_comment,'')
            except:
                out = line
                pass
            
        return out

    def remove_args(self,line):
        pos1 = line.find('(')
        pos2 = line.find(')')
        out = line.replace(line[pos1:pos2+1],'')
        return out

    def remove_garbage(self,line):
        try:
            out = line.replace(':','')
        except:
            pass
        return out


