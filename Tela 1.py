#tela1.py
import tkinter as tk

#criar uma janela
janela = tk.Tk()

janela.title('Bem Vindo ao Tkinter')

label = tk.Label(janela, text='Este é um Label', font=('Arial Bold', 70))
label.grid (column=0, row=0)

janela.mainloop ()

