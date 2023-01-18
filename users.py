
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkVideoPlayer import TkinterVideo 


#region Criar Conta
def guardarConta(resultado,janelaLogin):
    fBaseDados = open("./ficheiros/basedados.txt", "a", encoding="utf-8")
    fBaseDados.write(resultado)
    fBaseDados.close()
    janelaLogin()


def verificarConta(nome, email, passe, cpasse, resultado,janelaLogin):
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
                guardarConta(resultado,janelaLogin)
            else:
                messagebox.showerror(
                    "Erro", "As duas passwords não coincidem.")


def criarConta(nome,email,passe,cpasse,janelaLogin):
    
    resultado = "\n" + nome + ";" + email + ";" + passe + ";" + "user"

    verificarConta(nome, email, passe, cpasse, resultado,janelaLogin)

# endregion

# region Login

def login(nome,passe,janelaAppAdmin,janelaApp):
   # ABRE O FICHEIRO basedados.txt E PARA LEITURA
    fBaseDados = open("ficheiros/basedados.txt", "r", encoding="utf-8")
    linhas = fBaseDados.readlines()
    campos = []

    for lin in linhas:
        campos = lin.split(";")
        campos1 = campos[3].split("\n")
        if campos[0]==nome:
            break

   

    # CASO OS CAMPOS "UTILIZADOR" OU "PALAVRA-PASSE" ESTEJAM VAZIOS, RETORNA UM ERRO
    if nome == "" or passe == "":
        messagebox.showerror(
            "Erro", "Por favor forneça os seus dados de acesso.")
    
    
    # CASO OS DADOS DE ACESSO ESTEJAM CORRETOS, EFETUA LOGIN
    if nome != "" and passe != "":
        if campos[0] == nome and campos[2] == passe and campos1[0] == "admin":
            messagebox.showinfo("Bem vindo ADMINISTRADOR",
                                f"Olá {nome}! Está autenticado como ADMIN")
            nome=""
            passe=""
            janelaAppAdmin()
            return campos[0]

        elif campos[0] == nome and campos[2] == passe and campos[3] == "user":
            messagebox.showinfo(
                "Bem vindo", f"Olá {nome}, o seu login foi efetuado com sucesso!")
            nome=""
            passe=""
            janelaApp()
            return campos[0]

        # SE OS DADOS ESTIVEREM ERRADOS, RETORNA UM ERRO
        else:
            messagebox.showerror("Tentativa de Login sem sucesso",
                                 "Utilizador ou palavra-passe incorreta. Por favor tente novamente ou crie conta.")
            passe=""
# endregion

#region Convidado
def convidado(janelaAppConvidado):
    messagebox.showinfo(
            "Bem vindo", f"Olá convidado, o seu login foi efetuado com sucesso!")
    janelaAppConvidado()

def mensageConv():
    messagebox.showinfo("Sem Acesso!","Convidados não tem acesso a esta parte da aplicação,por favor crie uma conta!") 
#endregion