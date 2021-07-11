from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import scrolledtext
from analisisLexico import lexer
from analisisLexico import getTokens

window = Tk()
window.title("LIVESCRIPT")
window.geometry("650x560")
window.config(bg="gold")

lbl = Label(window, text="LIVESCRIPT", font=("Arial Bold", 30))
lbl.grid(row=0 , column=10)
lbl.config(bg="gold")
imagen =ImageTk.PhotoImage(Image.open("image/javaScript.pmg").resize((100,100)))

image=Label(window, image=imagen).grid(row=0 , column=1)

ingresarLb= Label(window, text="Ingrese su codigo: ", font=("Arial Bold", 10))
ingresarLb.grid(row=3 , column=0)
ingresarLb.config(bg="gold")

entry = tk.Entry(window,  justify=tk.LEFT)
entry.place(x=5,y=130, width=400, height=300)

botonAnalizar= tk.Button(text= "Analizar")
botonAnalizar.place(x=180,y=450, width=80, height=60)

def createWindowLexico():
    newWindowLx = Tk()
    newWindowLx.geometry("380x260")
    labelLexico = tk.Label(newWindowLx, text = "Analisis lexico")
    labelLexico.pack()
    text_area = tk.Text(newWindowLx, wrap=tk.WORD, width=30, height=10, font=("Times New Roman", 15))
    lexer.input(entry.get())
    tok = lexer.token()
    linea = str(tok) + "\n"
    text_area.insert(INSERT, linea)
    text_area.pack()
    pass



def createWindowSintatico():
    newWindowLx = Tk()
    newWindowLx.geometry("350x205")
    labelLexico = tk.Label(newWindowLx, text = "Analisis Sintactico")
    labelLexico.pack()

    pass
def createWindowSemantico():
    newWindowLx = Tk()
    newWindowLx.geometry("350x205")
    labelLexico = tk.Label(newWindowLx, text = "Analisis Semantico")
    labelLexico.pack()

    pass

botonLexico= tk.Button(text= "Analizar Lexico", command= createWindowLexico)
botonLexico.place(x=450,y=150, width=120, height=80)

botonSintaxis= tk.Button(text= "Analizar Sintaxis", command = createWindowSintatico)
botonSintaxis.place(x=450,y=250, width=120, height=80)

botonSemantico= tk.Button(text= "Analizar Semantica", command= createWindowSemantico)
botonSemantico.place(x=450,y=350, width=120, height=80)


window.mainloop()

