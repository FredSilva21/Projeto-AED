from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkVideoPlayer import TkinterVideo 

def criar_janela_receita(window):
  # Cria a janela principal
  # Cria os rótulos
  titulo_receita =Label(window, text="Título da Receita")
  titulo_receita.pack()

  ingredientes =Label(window, text="Ingredientes:")
  ingredientes.pack()

  ingrediente_1 =Label(window, text="Ingrediente 1")
  ingrediente_1.pack()

  ingrediente_2 =Label(window, text="Ingrediente 2")
  ingrediente_2.pack()

  # etc.

  instrucoes =Label(window, text="Instruções de Preparo:")
  instrucoes.pack()

  # Cria a área de texto para as instruções de preparo
  instrucoes_texto =Text(window)
  instrucoes_texto.pack()

  # Adiciona os dados da receita aos componentes
  titulo_receita["text"] = "Bolo de Chocolate"
  ingrediente_1["text"] = "2 xícaras de açúcar"
  ingrediente_2["text"] = "1 xícara de farinha de trigo"
  # etc.

  instrucoes_texto.insert(END, "1. Pré-aqueça o forno a 180°C.\n")
  instrucoes_texto.insert(
    END, "2. Em uma tigela, misture o açúcar, a farinha de trigo, o cacau em pó e o fermento.\n")
  instrucoes_texto.insert(
    END, "3. Adicione os ovos, o óleo e o leite e misture até formar uma massa homogênea.\n")
  # etc.