import re
import subprocess as sp
import tkinter


# python -m black teste.py
class Interpreter:
    def __init__(self):
        pass
              
    def compiler_code(self,line):
        
        newText = ""
        Nline = line.split('\n')

        for line in Nline:

            if re.findall('//',line) != None:
                
                try: 
                    line_pos = re.search('//',line)
                    line_comment = line[line_pos.span()[0]:]
                    line = line.replace(line_comment,'')
                except:
                    line = line
                    pass

            newText = f"{newText}\n{line}"

        code = newText

        code = code.replace('numb ','')
        # code = code.replace(' ','')
        code = code.replace('liter ','')
        code = code.replace('boole ','')
        code = code.replace('show','print')
        code = code.replace('true','True')
        code = code.replace('false','False')
        code = code.replace('doit','for')
        code = code.replace('loop','while')
        code = code.replace('orcase','elif')
        code = code.replace('case','if')
        code = code.replace('other','else')

        print(code)

        #write code in python file
        
        pythonFile = open(R"code\temp\temp.py", "a")
        pythonFile.write(code)
        pythonFile.close()
 
        # Run code and get output
        output = sp.getoutput(f'python {pythonFile.name}')
        
        if "IndentationError:" in output:
            tkinter.messagebox.showwarning(title = 'IndentationError',message = f'Seu código apresenta erro de indentação !')

        elif "SyntaxError:" in output:
            tkinter.messagebox.showwarning(title = 'SyntaxError:',message = f'Seu código apresenta erro de sintaxe !')

        
        return output



