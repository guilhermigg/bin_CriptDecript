from tkinter import *
import tkinter.messagebox as msgbox
import cdbin as binário

color = 'green'
color2 = 'lightgreen'
color3 = 'white'

class Janela:
    def __init__(self,janela):
        
        # Definições da janela
        janela.title('Decodificação/Codificação em Binário')
        janela.geometry('400x400')
        janela.resizable(False,False)
        janela.configure(bg=color)
        janela.wm_iconbitmap('imagens/ico.ico')

        # Imagem
        img = PhotoImage(file='imagens/bg.png')
        self.imagem = Label()
        self.imagem.image = img
        self.imagem['image'] = img
        self.imagem['bg'] = 'black'
        self.imagem.place(x=0,y=0)

        # Campos 
        self.entrada = Text(width=35,height=7,font=('Arial','10'),bg=color2)
        self.entrada.place(x=85,y=70)

        self.saida = Text(width=35,height=7,font=('Arial','10'),bg=color2)
        self.saida.place(x=85,y=230)

        # Botões
        self.b_decript = Button(text='Descriptografar',command=self.decript,bg=color2)
        self.b_decript.place(x=205,y=195)

        self.b_cript = Button(text='Criptografar',command=self.cript,bg=color2)
        self.b_cript.place(x=115, y=195)

        self.b_credits = Button(text='Créditos',command=self.credits,bg=color2)
        self.b_credits.place(x=340,y=373)

    def decript(self):
        value = self.entrada.get(0.0,END)
        descriptografado = binário.decript(value)
        self.saida.delete(0.0,END)
        self.saida.insert(END,descriptografado)

    def cript(self):
        value = self.entrada.get(0.0,END)
        criptografado = binário.cript(value)
        self.saida.delete(0.0,END)
        self.saida.insert(END,criptografado)

    def credits(self):
        msgbox.showinfo('Créditos','Desenvolvido por: Guilherme Evaristo')

root = Tk()
Janela(root)
root.mainloop()
