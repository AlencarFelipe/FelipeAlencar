import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

#Função dos botões
def funcao_clicar():
    print("Você clicou no botão")

def funcao_abrir():
    pass

#Caixas de Diálogo:
"""def mensagem():
    messagebox.showinfo("Titulo", "Estou aprendendo Python!")"""

#Cria uma janela
janela = tk.Tk()

#Criar um menu
menu_bar = tk.Menu()
janela.config(menu=menu_bar)
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Arquivo", menu=file_menu)
file_menu.add_command(label="abrir", command=funcao_abrir)

#Cria um Label
label = tk.Label(janela, text = "Usuario")
label.pack()

#Criar uma area para inserir texto
entrada_txt = tk.Entry(janela, width= 10)
entrada_txt.pack()

#Cria outro label
lbl_senha = tk.Label(janela, width=10, text = "Senha")
lbl_senha.pack()

#Cria uma entrada para digitar a senha
txt_senha = tk.Entry(janela, width=10,)
txt_senha.pack()

#Button: Botão:
botao = tk.Button(janela, text ="Login", command = funcao_abrir())
botao.pack()

"""#CSS do TKinter
estilo = ttk.Style("botao", foreground ="green", padding =(10,10))
estilo.pack()
estilo.configure("TButton", font =("Arial", 12, "Bold"))"""

#Aplica estilo ao label
estilo = ttk.Style()
estilo.configure("TLabel", foreground="green", padding=(10,10), font=("Arial", 12, "Bold"))

janela.mainloop()


