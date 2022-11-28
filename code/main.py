import webbrowser
from tkinter import *
from tkinter import messagebox, ttk
import tkinter.scrolledtext as st 
from Interpreter import Interpreter
from Lexer import Lexer
import os

root = Tk()
style = ttk.Style()
style.theme_use('clam')

# colors
# #c2d6d6
backgroundColor = "#E6E6E6"
foregroundColor = "#FFFFFF"

style.configure("Treeview",
    background = foregroundColor,
    foreground = "black",
    rowheight =25,
    fieldbackground = foregroundColor
)

style.map('Treeview',background=[('selected','blue')])

root.geometry("900x500") 
root.configure(background=backgroundColor)
root.title('Mali')
root.resizable(width=False, height=False)

#Box Text (INPUT)

inputText = st.ScrolledText(root, 
                            width = 57, 
                            height = 30,
                            font = ("Cascade Mono",10),
                            bg = foregroundColor,
                            fg= "black") 
inputText.grid(column = 0, pady = 7, padx = 7) 

# Console (OUTPUT)

outputText = st.ScrolledText(root, 
                            width = 62, 
                            height = 8,
                            font = ("Cascade Mono",10),
                            bg = foregroundColor,
                            fg = "black",) 
outputText.grid(column = 0, pady = 7, padx = 7) 
outputText.place(x = 435, y= 360)

# outputText.insert(END,conteudo)
 
# Commands
def getInput(): 

    clearInput()
    
    try:
        os.remove(f"code/temp/temp.py")
    except:
        pass

    inp = inputText.get(1.0, "end-1c")
    analyzer = Lexer(inp)
    convert = Interpreter()
    dict_return = analyzer.identifier_tokens() 

    counter = 0
    inpList = inp.split("\n")

    for i in inpList:
        if i:
            counter +=1 

    outputText.insert(END,convert.compiler_code(inp))

    table.delete(*table.get_children())
    length = 0
    for dict_key in dict_return:
        table.insert('', END,values = [f'{dict_key}',dict_return[dict_key]],tag='')
        length = length + len(dict_return[dict_key])
    print(length)

    var1.set(length)
    var2.set(counter)

    
def clearInput():  
    for i in table.get_children():
        table.delete(i)

    outputText.delete("1.0", "end") 

def showInfo():
    messagebox.showinfo(title='About', message='This is an IDE for Mali Language')


# Menu Bar
barMenu = Menu(root,background=foregroundColor,fg=foregroundColor)

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
button = ttk.Button(root, text = 'Run',command = getInput)  
button.place(x=435,y=290)  

button = ttk.Button(root, text = 'Clear',command = clearInput)  
button.place(x=435,y=325)  

#Table
table = ttk.Treeview(root,
                    column = ['column1','column2'],
                    show = 'headings')

table.column('column1',width=120)
table.heading('#1',text = 'Token')

table.column('column2',width=335)
table.heading('#2',text = 'Lexema')

table.grid(row = 0, column=0)
table.place(x=435,y=5)

# Labels
# root_label = Label(root, text=f"Nº de Tokens: ", background=backgroundColor) 
# root_label.place(x=530,y=290)

root_label = Label(root, text=f"Mali 1.0", background=backgroundColor,font = ("Cascade Mono",9,"bold")) 
root_label.place(x=530,y=290)

root_label = Label(root, text=f"Nº de Tokens: ", background=backgroundColor) 
root_label.place(x=530,y=310)

root_label = Label(root, text=f"Nº de Linhas: ", background=backgroundColor) 
root_label.place(x=530,y=330)

var1 = StringVar()
var2 = StringVar()
var3 = StringVar()


# root_label = Label(root,textvariable = var1, background=backgroundColor)
# root_label.place(x=670,y=290)

root_label = Label(root,textvariable = var1, background=backgroundColor)
root_label.place(x=610,y=310)

root_label = Label(root,textvariable = var2, background=backgroundColor)
root_label.place(x=610,y=330)

 
mainloop() 

