from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog
from tkVideoPlayer import TkinterVideo
from tkinter import ttk
import os


#region adicionar utilizador
def janelaAddUtilizador(window):
    janCriarAdmin = Toplevel(window)
    janCriarAdmin.title("Adicionar Utilizadores")
    janCriarAdmin.resizable(False, False)
    janCriarAdmin.focus_force()

    w = 550
    h = 330
    ws = janCriarAdmin.winfo_screenwidth()
    hs = janCriarAdmin.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janCriarAdmin.geometry('%dx%d+%d+%d' % (w, h, x, y))

    lblUtilizador = Label(janCriarAdmin, text="       Nome de Utilizador:",
                         fg="black", relief="raised", font="Playfair", bd=-2)
    lblUtilizador.place(x=60, y=20)

    # Entry Utilizador
    entUtilizador = Entry(janCriarAdmin, fg="black", width=25)
    entUtilizador.place(x=280, y=24)
    
    # Label Utilizador
    lblEmail = Label(janCriarAdmin, text="\t            Email:", fg="black",
                    relief="raised", font="Playfair", bd=-2)
    lblEmail.place(x=60, y=50)
    
    # Entry Utilizador
    entEmail = Entry(janCriarAdmin, fg="black", width=25)
    entEmail.place(x=280, y=54)
    
    # Label Utilizador
    lblPass = Label(janCriarAdmin, text="\tPalavra-Passe:", fg="black",
                    relief="raised", font="Playfair", bd=-2)
    lblPass.place(x=50, y=80)
    
    # Entry Utilizador
    entPass = Entry(janCriarAdmin, fg="black", width=25, show="*")
    entPass.place(x=280, y=84)
    
    # Label Utilizador
    lblCpass = Label(janCriarAdmin, text="Confirmar Palavra-Passe:", fg="black",
                    relief="raised", font="Playfair", bd=-2)
    lblCpass.place(x=50, y=110)
    
    # Entry Utilizador
    entCpass = Entry(janCriarAdmin, fg="black", width=25, show="*")
    entCpass.place(x=280, y=114)
     
    # RADIOBUTTON USER OU ADMIN
    radioBtn = StringVar()
    radioBtn.set("Utilizador")
    rb1_utilizador = Radiobutton(janCriarAdmin, text="Utilizador",value="Utilizador",variable=radioBtn)
    rb2_administrador = Radiobutton(janCriarAdmin, text="Administrador",value="Administrador",variable=radioBtn)

    rb1_utilizador.place(x=70, y=150)
    rb2_administrador.place(x=70, y=180)

    # Botão de adicionar
    btnAdicionar = Button(janCriarAdmin, text="Adicionar Conta", width=15, height=2,command=lambda:adicionarUtilizador(entUtilizador.get(),entEmail.get(),entPass.get(),entCpass.get(),radioBtn))
    btnAdicionar.place(x=200, y=220)

    # Botão de cancelar
    btnCancelar = Button(janCriarAdmin, text="Cancelar", width=15, height=2,command=lambda:janCriarAdmin.destroy())
    btnCancelar.place(x=350, y=220)


def verificarConta(nome, email, passe, cpasse, resultado):
    fBaseDados = open("./ficheiros/basedados.txt", "r", encoding="utf-8")
    campos = []
    
    if nome == "" or email == "" or passe == "" or cpasse == "":
        messagebox.showerror(
            "Erro", "Por favor forneça todos os dados corretamente.")
        

    if nome != "" and passe != "":

        linhas = fBaseDados.readlines()
        for lin in linhas:
            campos = lin.split(";")
        #SE JA EXISTIR UMA CONTA COM O MESMO NOME
        if nome == campos[0]:
            messagebox.showerror(
                "Erro", "Já existe uma conta com esse nome, por favor use outro nome.")
                
        #SE JA EXISTIR UMA CONTA COM O MESMO EMAIL
        elif email==campos[2]:
            messagebox.showerror(
                "Erro", "Já existe uma conta com esse email, por favor use outro email.")

        #SE JA EXISTIR UMA CONTA COM O MESMO NOME E EMAIL
        elif nome==campos[0] and email==campos[2]:
            messagebox.showerror(
                "Erro", "Já existe uma conta com esses dados, por favor efetue login.")
        # SE A PALAVRA-PASSE FOR CONFIRMADA CORRETAMENTE CRIA A CONTA
        else:
            if passe == cpasse:
                guardarConta(resultado)
                nome=""
                email=""
                passe=""
                cpasse=""
            else:
                messagebox.showerror(
                    "Erro", "As duas passwords não coincidem.")



def guardarConta(resultado):
    fBaseDados = open("./ficheiros/basedados.txt", "a", encoding="utf-8")
    fBaseDados.write(resultado)
    fBaseDados.close()


# Adicionar Utilizador
def adicionarUtilizador(nome,email,passe,cpasse,radioBtn):
    if radioBtn.get() == "Administrador":
            resultado = "\n" + nome + ";" + email + ";" + passe + ";" + "admin"
    else:
            resultado = "\n" + nome + ";" + email + ";" + passe + ";" + "user"
    
    verificarConta(nome, email, passe, cpasse, resultado)


def cancelar(janCriarAdmin,janelaAppAdmin):
    janCriarAdmin.destroy()
    janelaAppAdmin()

#endregion   
    
#region remover Utilizador


def janelaRemUtilizador(window):
    JanRemoverAdmin = Toplevel(window)
    JanRemoverAdmin.title("Remover Utilizadores")

    w = 600
    h = 400
    ws = JanRemoverAdmin.winfo_screenwidth()
    hs = JanRemoverAdmin.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    JanRemoverAdmin.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #Treeview
    tree=ttk.Treeview(JanRemoverAdmin,selectmode="browse",height=10,columns=("Nome","Email","Passe","Tipo"),show="headings")
    tree.column("Nome",width=100,anchor="center")
    tree.column("Email",width=150,anchor="center")
    tree.column("Passe",width=100,anchor="center")
    tree.column("Tipo",width=50,anchor="center")
    tree.heading("Nome",text="Nome")
    tree.heading("Email",text="Email")
    tree.heading("Passe",text="Passe")
    tree.heading("Tipo",text="Tipo")
    tree.place(x=100,y=20)
    
    #Botão de Ler Ficheiro
    btnLerFicheiro = Button(JanRemoverAdmin, text="Ler Ficheiro", width=15, height=2,command=lambda:inserirTree(tree))
    btnLerFicheiro.place(x=100, y=300)

    #Botão de Remover
    btnRemover = Button(JanRemoverAdmin, text="Remover", width=15, height=2,command=lambda:remover(tree))
    btnRemover.place(x=250, y=300)

    #Botão de Guardar Ficheiro
    btnGuardarFicheiro = Button(JanRemoverAdmin, text="Guardar Ficheiro", width=15, height=2,command=lambda:guardarFicheiro(tree))
    btnGuardarFicheiro.place(x=400, y=300)

#Inserir na treeview
def inserirTree(tree):
    fBaseDados = open("./ficheiros/basedados.txt", "r", encoding="utf-8")
    for linha in fBaseDados:
        dados = linha.split(";")
        tree.insert("", END, values=(dados[0],dados[1],dados[2],dados[3]))
    fBaseDados.close()

#Remover da treeview
def remover(tree):
    for selected_item in tree.selection():
        tree.delete(selected_item)

#Guardar Ficheiro
def guardarFicheiro(tree):
    fBaseDados = open("./ficheiros/basedados.txt", "w", encoding="utf-8")
    for child in tree.get_children():
        fBaseDados.write(str(tree.item(child)["values"][0])+";"+str(tree.item(child)["values"][1])+";"+str(tree.item(child)["values"][2])+";"+(tree.item(child)["values"][3])+"\n")
    fBaseDados.close()
    messagebox.showinfo("Sucesso", "Ficheiro guardado com sucesso.")

#endregion

#region  Adicionar Categoria

#Inserir na listbox
def inserirLista(lstbox,categorias):
    for i in range(len(categorias)):
        lstbox.insert(END, categorias[i])
    

#selecionar imagem
def selecionarImagem(imagem):
    file=filedialog.askopenfilename(initialdir = "./img/categorias",title = "Select file",filetypes = (("png files","*.png"),("gif files","*.gif"),("all files","*.*")))
    imagem.set(file)
    

def adicionarCategoria(lstbox,categoria,img,cat):
    linha=cat + ";" + img 

    if cat== "":
        messagebox.showerror("Erro", "Preencha o campo categoria.")
    elif img == "":
        messagebox.showerror("Erro", "Selecione uma imagem.")
    else:
        lstbox.insert(END, linha)
        categoria.append([cat,img])
        messagebox.showinfo("Sucesso", "Categoria adicionada com sucesso.")
        cat=""
        img=""

def janelaAddCategoria(window,categorias):
    JanCriarCategoria = Toplevel(window)
    JanCriarCategoria.title("Adicionar Categoria")

    w = 550
    h = 330
    ws = JanCriarCategoria.winfo_screenwidth()
    hs = JanCriarCategoria.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    JanCriarCategoria.geometry('%dx%d+%d+%d' % (w, h, x, y))

    # Lista de categorias
    listbox = Listbox(JanCriarCategoria, width=30, height=10)
    listbox.place(x=350, y=50)

    #Label de categoria
    lblCategoria = Label(JanCriarCategoria, text="Categoria:")
    lblCategoria.place(x=10, y=80)

    cat=StringVar()
    # Entrada de texto
    txtCategoria = Entry(JanCriarCategoria, width=30, textvariable=cat)
    txtCategoria.place(x=70, y=80)

    #Label de imagem
    lblImagem = Label(JanCriarCategoria, text="Imagem:")
    lblImagem.place(x=10, y=120)

    imagem=StringVar()
    # Entrada de texto
    txtImagem = Entry(JanCriarCategoria, width=30, textvariable=imagem)
    txtImagem.place(x=70, y=120)

    #Botão de selecionar imagem
    btnSelecionarImagem = Button(JanCriarCategoria, text="Selecionar Imagem", width=15, height=2,command=lambda:selecionarImagem(imagem))
    btnSelecionarImagem.place(x=70, y=200)

    # Botão de adicionar
    btnAdicionar = Button(
        JanCriarCategoria, text="Adicionar Categoria", width=15, height=2,command=lambda:adicionarCategoria(listbox,categorias,imagem.get(),cat.get(),janelaAddCategoria))
    btnAdicionar.place(x=70, y=250)

    inserirLista(listbox,categorias)

#endregion

#region Remover Categoria
def removerCategoria(listbox,categorias):
    if listbox.curselection():
        categorias.pop(listbox.curselection()[0])
        listbox.delete(listbox.curselection()[0])
        messagebox.showinfo("Sucesso", "Categoria removida com sucesso.")
    else:
        messagebox.showinfo("Erro", "Selecione uma categoria.")


def janelaRemCategoria(window,categorias):
    JanRemoverCategoria = Toplevel(window)
    JanRemoverCategoria.title("Remover Categoria")

    w = 550
    h = 330
    ws = JanRemoverCategoria.winfo_screenwidth()
    hs = JanRemoverCategoria.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    JanRemoverCategoria.geometry('%dx%d+%d+%d' % (w, h, x, y))

    # Lista de categorias
    listbox = Listbox(JanRemoverCategoria, width=30, height=10)
    listbox.place(x=350, y=50)

    # Botão de remover
    btnRemover = Button(JanRemoverCategoria,
                        text="Remover Categoria", width=10, height=2,command=lambda:removerCategoria(listbox,categorias))
    btnRemover.place(x=70, y=150)

    inserirLista(listbox,categorias)

#endregion


#region Alterar Categoria



#endregion


