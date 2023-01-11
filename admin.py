from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkVideoPlayer import TkinterVideo 


def adicionarUtilizador(window):
    JanCriarAdmin = Toplevel(window)
    JanCriarAdmin.title("Adicionar Utilizadores")

    w = 450
    h = 230
    ws = JanCriarAdmin.winfo_screenwidth()
    hs = JanCriarAdmin.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    JanCriarAdmin.geometry('%dx%d+%d+%d' % (w, h, x, y))

    

    #CHECKBUTTON USER OU ADMIN
    cb1 = IntVar()
    cb1.set(1)
    cb2 = IntVar()

    cb1_utilizador = Checkbutton(JanCriarAdmin, text="Utilizador", variable = cb1)
    cb2_utilizador = Checkbutton(JanCriarAdmin,text="Administrador",variable=cb2)
        
    cb1_utilizador.place(x=70, y=150)
    cb2_utilizador.place(x=70, y=180)
