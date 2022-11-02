from tkinter import *
from tkinter import ttk
import compiler.analyzer as analyzer

root = Tk()
style = ttk.Style()
style.theme_use('clam')

root.geometry("700x400") 
root.configure(background="#a0a0a0")
root.title('Lexical Analyzer')
root.resizable(width=False, height=False)

def getInput(): 
    inp = inputText.get(1.0, "end-1c")
    dict_return = analyzer.analisador(inp) 

    table.delete(*table.get_children())
    
    for dict_key in dict_return:
        table.insert('', END,values = [f'{dict_key}',dict_return[dict_key]],tag='')
        


def clearInput():  
    for i in table.get_children():
        table.delete(i)

    
# root_label = Label(root, text="Analisador Lexico", font=15) 
# root_label.place(x=390,y=300)

#Box Text
inputText = Text(root,height = 24, width = 53,font=("Cascade Mono",10))
inputText.place(x=5,y=5)
# inp = inputText.get(1.0, "end-1c") 

# Buttons
button = ttk.Button(root, text = ' Start ',command = getInput)  
button.place(x=430,y=350)  

button = ttk.Button(root, text = ' Clear ',command = clearInput)  
button.place(x=520,y=350)  

#Table
table = ttk.Treeview(root,column = ['column1','column2'],show = 'headings')

table.column('column1',width=150)
table.heading('#1',text = 'Token')

table.column('column2',width=150)
table.heading('#2',text = 'Lexema')

table.grid(row = 0, column=0)
table.place(x=390,y=5)

 
mainloop() 

