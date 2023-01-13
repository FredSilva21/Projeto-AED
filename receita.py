from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkVideoPlayer import TkinterVideo 

def criar_janela_receita(window):
    JanCriarReceita = Toplevel(window)
    JanCriarReceita.title("Adicionar Receita")

    w = 800
    h = 400
    ws = JanCriarReceita.winfo_screenwidth()
    hs = JanCriarReceita.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    JanCriarReceita.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #Nome da Receita
    lblNomeReceita = Label(JanCriarReceita, text="Nome da Receita", width=20, height=2)
    lblNomeReceita.place(x=70, y=50)

    #Caixa de texto para o nome da receita
    txtNomeReceita = Entry(JanCriarReceita, width=20)
    txtNomeReceita.place(x=70, y=100)

    #Botão de adicionar
    btnAdicionar = Button(JanCriarReceita, text="Adicionar", width=10, height=2)
    btnAdicionar.place(x=70, y=150)

    #Botão de cancelar
    btnCancelar = Button(JanCriarReceita, text="Cancelar", width=10, height=2)
    btnCancelar.place(x=250, y=150)

    #Botão de adicionar
    btnAdicionar = Button(JanCriarReceita, text="Adicionar", width=10, height=2)
    btnAdicionar.place(x=70, y=150)

    #Botão de cancelar
    btnCancelar = Button(JanCriarReceita, text="Cancelar", width=10, height=2)
    btnCancelar.place(x=250, y=150)

    #Botão de adicionar
    btnAdicionar = Button(JanCriarReceita, text="Adicionar", width=10, height=2)
    btnAdicionar.place(x=70, y=150)

    #Botão de cancelar
    btnCancelar = Button(JanCriarReceita, text="Cancelar", width=10, height=2)
    btnCancelar.place(x=250, y=150)