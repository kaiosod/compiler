from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import webbrowser
from Lexer import Lexer

root = Tk()
style = ttk.Style()
style.theme_use('clam')

style.configure("Treeview",
    background = "#D3D3D3",
    foreground = "black",
    rowheight =25,
    fieldbackground = "#D3D3D3"
)

style.map('Treeview',background=[('selected','blue')])

root.geometry("900x500") 
root.configure(background="#a0a0a0")
root.title('Mali')
root.resizable(width=False, height=False)


# Commands
def getInput(): 
    inp = inputText.get(1.0, "end-1c")
    analyzer = Lexer(inp) 
    dict_return = analyzer.identifier_tokens() 

    table.delete(*table.get_children())
    
    for dict_key in dict_return:
        table.insert('', END,values = [f'{dict_key}',dict_return[dict_key]],tag='')
        


def clearInput():  
    for i in table.get_children():
        table.delete(i)

def showInfo():
    messagebox.showinfo(title='About', message='This is an IDE for Mali Language')


    
# root_label = Label(root, text="Analisador Lexico", font=15) 
# root_label.place(x=390,y=300)

#Box Text
inputText = Text(root,height = 30, width = 60,font=("Cascade Mono",10))
inputText.place(x=5,y=6)
# inp = inputText.get(1.0, "end-1c") 

# Menu Bar
barMenu = Menu(root)

# Menu Bar - Files
menuFile = Menu(barMenu,tearoff=0)
menuFile.add_command(label='Add File',command=getInput)

# Menu Bar - Run
menuRun = Menu(barMenu,tearoff=0)
menuRun.add_command(label='Run Code',command=getInput)

# Menu Bar - Help
menuHelp = Menu(barMenu,tearoff=0)
menuHelp.add_command(label='GitHub',
                     command=lambda: webbrowser.open('https://github.com/kaiosod/compiler'))
menuHelp.add_command(label='Issues',
                     command=lambda: webbrowser.open('https://github.com/kaiosod/compiler/issues'))
menuHelp.add_command(label='Documentarion',
                     command=lambda: webbrowser.open('https://github.com/kaiosod/compiler/wiki'))
menuHelp.add_command(label='About',
                     command=showInfo)


# menuFile.add_separator()
barMenu.add_cascade(label='Files',menu=menuFile)
barMenu.add_cascade(label='Run',menu=menuRun)
barMenu.add_cascade(label='Help',menu=menuHelp)



root.config(menu=barMenu)

# Buttons
button = ttk.Button(root, text = 'Start',command = getInput)  
button.place(x=435,y=290)  

button = ttk.Button(root, text = 'Clear',command = clearInput)  
button.place(x=435,y=325)  

#Table
table = ttk.Treeview(root,column = ['column1','column2'],show = 'headings')

table.column('column1',width=120)
table.heading('#1',text = 'Token')

table.column('column2',width=335)
table.heading('#2',text = 'Lexema')

table.grid(row = 0, column=0)
table.place(x=435,y=5)

 
mainloop() 

