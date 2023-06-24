from random import choice
import string
import tkinter as tk


#Codigo
def Gerar():
    global senha
    #PASSWORDSIZE
    valores = ""

    print(digitsSize)
    if letters1.get() == 1 and digits2.get() == 0 and digits3.get() == 0:
        valores = string.ascii_letters
    elif letters1.get() == 0 and digits2.get() == 1 and digits3.get() == 0:
        valores = string.digits
    elif letters1.get() == 0 and digits2.get() == 0 and digits3.get() == 1:
        valores = string.punctuation    
    elif letters1.get() == 1 and digits2.get() == 1 and digits3.get() == 0:
        valores = string.digits + string.ascii_letters
    elif letters1.get() == 1 and digits2.get() == 0 and digits3.get() == 1:
        valores = string.ascii_letters + string.punctuation
    elif letters1.get() == 0 and digits2.get() == 1 and digits3.get() == 1:
        valores = string.digits + string.punctuation
    elif letters1.get() == 0 and digits2.get() == 0 and digits3.get() == 0:
        valores = ""
    else:
        valores = string.ascii_letters + string.digits + string.punctuation

    tamanho = int(digitsSize.get())
  #letters1 = string.ascii_letters
  #digits2 = string.digits
  #valores = string.digits + string.ascii_letters
    senha = ''
    for _ in range(tamanho):
        senha += choice(valores)

#printar a senha na janela
    texto_senha["text"] = 'Senha Gerada', senha


def Copy():
  texto_senha.clipboard_clear()
  texto_senha.clipboard_append(senha)




#JANELA
janela = tk.Tk()
janela.title("Gerador")
janela.geometry("300x300")

#WHITE BOX DIGITS
text_sizeofdigits = tk.Label(janela, text="Size of Digits")
text_sizeofdigits.pack()

digitsSize = tk.Entry(janela, width= 10)
digitsSize.focus_set()
digitsSize.pack()

#CHECKBOX
letters1 = tk.IntVar()
digits2 = tk.IntVar()
digits3 = tk.IntVar()

c1 = tk.Checkbutton(janela, text='Letras',variable=letters1)
c1.pack()
c2 = tk.Checkbutton(janela, text='Numeros',variable=digits2)
c2.pack()
c3 = tk.Checkbutton(janela, text='Special',variable=digits3)
c3.pack()

#TEXT CLICK ON THE BUTTON
texto_orientacao = tk.Label(janela, text= "Click on the button to generate a password")
texto_orientacao.pack()

#Botao
botao = tk.Button(janela, text="Gerar",width=10, height=2, command=Gerar,  bg='green')
botao.pack()


botao2 = tk.Button(janela, text="Copy", width=10, height=2, command=Copy, bg='cyan')
botao2.pack()


#senha gerada
texto_senha = tk.Label(janela, text="{Senha Gerada}")
texto_senha.pack()



janela.mainloop()