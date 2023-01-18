from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkVideoPlayer import TkinterVideo 
from tkinter import filedialog

from index import *


#region JANELAS RECEITAS
def janelaPao():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Receita")

    titulo_receita = tk.Label(janela, text="Título da Receita:")
    titulo_receita.pack()

    #Ingredientes
    ingredientes = tk.Label(janela, text="Ingredientes:", font=("Playfair Bold", 15))
    ingredientes.place(x=10, y=300)

    ingrediente_1 = tk.Label(janela, text="2 xícaras de farinha de trigo")
    ingrediente_1.place(x=10, y=330)

    ingrediente_2 = tk.Label(janela, text="1 xícara de água morna")
    ingrediente_2.place(x=10, y=350)

    ingrediente_3 = tk.Label(janela, text="200g de quejo ralado")
    ingrediente_3.place(x=10, y=370)

    ingrediente_4 = tk.Label(janela, text="200g de champignon fatiado")
    ingrediente_4.place(x=10, y=390)

    # Cria os rótulos
    titulo_receita = tk.Label(janela, text="Título da Receita")
    titulo_receita.pack()

    ingredientes = tk.Label(janela, text="Ingredientes:")
    ingredientes.pack()

    ingrediente_1 = tk.Label(janela, text="1 pão de forma")
    ingrediente_1.pack()

    ingrediente_2 = tk.Label(janela, text="200ml de leite")
    ingrediente_2.pack()

    ingrediente_3 = tk.Label(janela, text="3 ovos")
    ingrediente_3.pack()

    ingrediente_4 = tk.Label(janela, text="250g de presunto picado")
    ingrediente_4.pack()

    ingrediente_5 = tk.Label(janela, text="200g de queijo ralado")
    ingrediente_5.pack()

    ingrediente_6 = tk.Label(janela, text="Azeite")
    ingrediente_6.pack()

    # etc.

    instrucoes = tk.Label(janela, text="Instruções de Preparo:")
    instrucoes.pack()

    # Cria a área de texto para as instruções de preparo
    instrucoes_texto = tk.Text(janela)
    instrucoes_texto.pack()

    # Adiciona os dados da receita aos componentes
    titulo_receita["text"] = "Pão Recheado"

    instrucoes_texto.insert(tk.END, "1. Corte o pão de forma ao meio e retire a parte superior.\n")
    instrucoes_texto.insert(
        tk.END, "2. Em uma tigela, misture o leite, os ovos, o presunto e o queijo ralado.\n")
    instrucoes_texto.insert(
        tk.END, "3. Despeje a mistura no pão de forma e cubra com a parte superior.\n")
    instrucoes_texto.insert(
        tk.END, "4. Regue a superfície do pão com azeite e leve ao forno por aproximadamente 15 minutos ou até dourar.\n")
    instrucoes_texto.insert(
        tk.END, "5. Retire o pão recheado do forno e deixe esfriar antes de servir.\n")

    # Cria o botão para marcar a receita como favorita
    botao_favorito_pao = tk.Button(
        janela, text="Marcar como Favorita", width=20, height=2, bg="#ffff00", command=lambda: gosto_pao())
    botao_favorito_pao.place(x=10, y=500)
    
    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=20, height=2, bg="#1f77b4")
    botao_comentario.place(x=200, y=500)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(
        janela, text="Fechar", width=20, height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.place(x=390, y=500)

def janelaQuiche():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Receita")

    # Cria os rótulos
    titulo_receita = tk.Label(janela, text="Título da Receita:")
    titulo_receita.pack()

    ingredientes = tk.Label(janela, text="Ingredientes:")
    ingredientes.pack()

    ingrediente_1 = tk.Label(janela, text="1 massa de tarte pré-assada")
    ingrediente_1.pack()

    ingrediente_2 = tk.Label(janela, text="1 xícara de leite")
    ingrediente_2.pack()

    ingrediente_3 = tk.Label(janela, text="3 ovos")
    ingrediente_3.pack()

    ingrediente_4 = tk.Label(janela, text="200g de queijo ralado")
    ingrediente_4.pack()

    ingrediente_5 = tk.Label(janela, text="1 cebola pequena picada")
    ingrediente_5.pack()

    ingrediente_6 = tk.Label(janela, text="1 tomate picado")
    ingrediente_6.pack()

    # etc.

    instrucoes = tk.Label(janela, text="Instruções de Preparo:")
    instrucoes.pack()

    # Cria a área de texto para as instruções de preparo
    instrucoes_texto = tk.Text(janela)
    instrucoes_texto.pack()

    # Adiciona os dados da receita aos componentes
    titulo_receita["text"] = "Quiche"

    instrucoes_texto.insert(tk.END, "1. Pré-aqueça o forno a 180°C.\n")
    instrucoes_texto.insert(
        tk.END, "2. Em uma tigela, misture o leite, os ovos e o queijo ralado. Adicione a cebola e o tomate picados e misture novamente.\n")
    instrucoes_texto.insert(
        tk.END, "3. Despeje a mistura na massa de tarte pré-assada e leve ao forno por cerca de 40 minutos ou até dourar.\n")
    instrucoes_texto.insert(
        tk.END, "4. Retire a quiche do forno e deixe esfriar antes de servir.\n")
    
    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=20, height=2, bg="#ffff00")
    botao_favorito.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=20, height=2, bg="#1f77b4")
    botao_comentario.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(
        janela, text="Fechar", width=20, height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.pack(side=tk.LEFT, padx=10, pady=10)

def janelaPizza():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Receita")

    # Cria os rótulos
    titulo_receita = tk.Label(janela, text="Título da Receita")
    titulo_receita.pack()

    ingredientes = tk.Label(janela, text="Ingredientes:")
    ingredientes.pack()

    ingrediente_1 = tk.Label(janela, text="1 xícara de farinha de trigo")
    ingrediente_1.pack()

    ingrediente_2 = tk.Label(janela, text="1/2 xícara de água morna")
    ingrediente_2.pack()

    ingrediente_3 = tk.Label(janela, text="1/2 xícara de molho de tomate")
    ingrediente_3.pack()
    ingrediente_4 = tk.Label(janela, text="1/2 xícara de queijo ralado")
    ingrediente_4.pack()

    ingrediente_5 = tk.Label(
        janela, text="Ingredientes a gosto para rechear (ex.: presunto, pepperoni, cogumelos, etc.)")
    ingrediente_5.pack()

    # etc.

    instrucoes = tk.Label(janela, text="Instruções de Preparo:")
    instrucoes.pack()

    # Cria a área de texto para as instruções de preparo
    instrucoes_texto = tk.Text(janela)
    instrucoes_texto.pack()

    # Adiciona os dados da receita aos componentes
    titulo_receita["text"] = "Mini Pizzas"

    instrucoes_texto.insert(tk.END, "1. Pré-aqueça o forno a 220°C.\n")
    instrucoes_texto.insert(
        tk.END, "2. Em uma tigela, misture a farinha de trigo e a água morna até formar uma massa homogênea.\n")
    instrucoes_texto.insert(
        tk.END, "3. Abra a massa em um superfície lisa e enfarinhada e corte em círculos de aproximadamente 10 cm de diâmetro.\n")
    instrucoes_texto.insert(
        tk.END, "4. Disponha os círculos de massa em uma assadeira untada e leve ao forno por cerca de 5 minutos ou até dourar levemente.\n")
    instrucoes_texto.insert(
        tk.END, "5. Retire a assadeira do forno e espalhe o molho de tomate sobre os círculos de massa. Adicione o recheio de sua preferência e polvilhe o queijo ralado por cima.\n")
    instrucoes_texto.insert(
        tk.END, "6. Leve a assadeira de volta ao forno por mais 10 minutos ou até que as mini pizzas estejam douradas e o queijo derretido.\n")
    instrucoes_texto.insert(
        tk.END, "7. Retire a assadeira do forno e sirva as mini pizzas quentes.\n")

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=20, height=2, bg="#ffff00")
    botao_favorito.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=20, height=2, bg="#1f77b4")
    botao_comentario.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(janela, text="Fechar", width=20,
                             height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.pack(side=tk.LEFT, padx=10, pady=10)

def janelaSupremo():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Receita")

    # Cria os rótulos
    titulo_receita = tk.Label(janela, text="Título da Receita")
    titulo_receita.pack()

    ingredientes = tk.Label(janela, text="Ingredientes:")
    ingredientes.pack()

    ingrediente_1 = tk.Label(janela, text="1 camembert grande")
    ingrediente_1.pack()

    ingrediente_2 = tk.Label(janela, text="2 xícaras de farinha de rosca")
    ingrediente_2.pack()

    ingrediente_3 = tk.Label(janela, text="1 ovo batido")
    ingrediente_3.pack()

    ingrediente_4 = tk.Label(janela, text="1 xícara de azeite")
    ingrediente_4.pack()

    # etc.

    instrucoes = tk.Label(janela, text="Instruções de Preparo:")
    instrucoes.pack()

    # Cria a área de texto para as instruções de preparo
    instrucoes_texto = tk.Text(janela)
    instrucoes_texto.pack()

    # Adiciona os dados da receita aos componentes
    titulo_receita["text"] = "Suprême de Camembert"

    instrucoes_texto.insert(tk.END, "1. Pré-aqueça o forno a 180°C.\n")
    instrucoes_texto.insert(
        tk.END, "2. Em uma tigela, misture a farinha de rosca com o ovo batido até formar uma massa homogênea.\n")
    instrucoes_texto.insert(
        tk.END, "3. Corte o camembert em fatias de aproximadamente 1 cm de espessura.\n")
    instrucoes_texto.insert(
        tk.END, "4. Passe cada fatia de camembert na massa de farinha de rosca, cobrindo-a completamente.\n")
    instrucoes_texto.insert(
        tk.END, "5. Aqueça o azeite em uma panela e frite as fatias de camembert até dourar. Retire-as da panela e coloque-as em uma assadeira.\n")
    instrucoes_texto.insert(
        tk.END, "6. Leve a assadeira ao forno por cerca de 5 minutos ou até que o camembert esteja derretido por dentro.\n")
    instrucoes_texto.insert(
        tk.END, "7. Retire a assadeira do forno e sirva o suprême de camembert quente, acompanhado de pão ou batatas fritas.\n")

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=20, height=2, bg="#ffff00")
    botao_favorito.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=20, height=2, bg="#1f77b4")
    botao_comentario.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(janela, text="Fechar", width=20,
                             height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.pack(side=tk.LEFT, padx=10, pady=10)

def janelaRissois():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Receita")

    # Cria os rótulos
    titulo_receita = tk.Label(janela, text="Título da Receita")
    titulo_receita.pack()

    ingredientes = tk.Label(janela, text="Ingredientes:")
    ingredientes.pack()

    ingrediente_1 = tk.Label(janela, text="1 xícara de água")
    ingrediente_1.pack()

    ingrediente_2 = tk.Label(janela, text="1/2 xícara de farinha de trigo")
    ingrediente_2.pack()

    ingrediente_3 = tk.Label(janela, text="1/2 xícara de leite")
    ingrediente_3.pack()

    ingrediente_4 = tk.Label(janela, text="1/2 xícara de óleo")
    ingrediente_4.pack()

    ingrediente_5 = tk.Label(
        janela, text="1/2 xícara de recheio de sua preferência (ex.: frango desfiado, carne moída, queijo, etc.)")
    ingrediente_5.pack()

    instrucoes = tk.Label(janela, text="Instruções de Preparo:")
    instrucoes.pack()
    # Cria a área de texto para as instruções de preparo
    instrucoes_texto = tk.Text(janela)
    instrucoes_texto.pack()

    # Adiciona os dados da receita aos componentes
    titulo_receita["text"] = "Rissois"

    instrucoes_texto.insert(
        tk.END, "1. Em uma panela, misture a água, a farinha de trigo, o leite e o óleo até formar uma massa homogênea. Deixe esfriar.\n")
    instrucoes_texto.insert(
        tk.END, "2. Depois de fria, adicione o recheio de sua preferência à massa e misture bem.\n")
    instrucoes_texto.insert(
        tk.END, "3. Disponha uma folha de massa folhada sobre a superfície de trabalho e corte círculos de aproximadamente 10 cm de diâmetro.\n")
    instrucoes_texto.insert(
        tk.END, "4. Disponha uma porção de massa com o recheio no centro de cada círculo de massa folhada.\n")
    instrucoes_texto.insert(
        tk.END, "5. Pincele os bordos da massa folhada com água e dobre-a ao meio, formando um meio círculo. Pressione os bordos para fechar bem.\n")
    instrucoes_texto.insert(
        tk.END, "6. Aqueça o óleo em uma panela e frite os rissois até dourar. Retire-os da panela e coloque-os em uma assadeira para escorrer o excesso de óleo.\n")
    instrucoes_texto.insert(
        tk.END, "7. Sirva os rissois quentes, acompanhados de molho de sua preferência.\n")
    # etc.
    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=20, height=2, bg="#ffff00")
    botao_favorito.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=20, height=2, bg="#1f77b4")
    botao_comentario.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(janela, text="Fechar", width=20,
                             height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.pack(side=tk.LEFT, padx=10, pady=10)

def janelaTapas():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Receita")

    # Cria os rótulos
    titulo_receita = tk.Label(janela, text="Título da Receita")
    titulo_receita.pack()

    ingredientes = tk.Label(janela, text="Ingredientes:")
    ingredientes.pack()

    ingrediente_1 = tk.Label(janela, text="1 pão italiano")
    ingrediente_1.pack()

    ingrediente_2 = tk.Label(janela, text="100 g de queijo gorgonzola")
    ingrediente_2.pack()

    ingrediente_3 = tk.Label(janela, text="200 g de carne moída")
    ingrediente_3.pack()

    ingrediente_4 = tk.Label(janela, text="1 cebola pequena")
    ingrediente_4.pack()

    ingrediente_5 = tk.Label(janela, text="2 dentes de alho")
    ingrediente_5.pack()

    ingrediente_6 = tk.Label(janela, text="1 tomate pequeno")
    ingrediente_6.pack()

    ingrediente_7 = tk.Label(janela, text="Azeite de oliva")
    ingrediente_7.pack()

    ingrediente_8 = tk.Label(janela, text="Sal e pimenta-do-reino a gosto")
    ingrediente_8.pack()

    # etc.

    instrucoes = tk.Label(janela, text="Instruções de Preparo:")
    instrucoes.pack()

    # Cria a área de texto para as instruções de preparo
    instrucoes_texto = tk.Text(janela)
    instrucoes_texto.pack()
    # Adiciona os dados da receita aos componentes
    titulo_receita["text"] = "Tapas de Carne e Queijo Gorgonzola"

    instrucoes_texto.insert(tk.END, "1. Pré-aqueça o forno a 180°C.\n")
    instrucoes_texto.insert(
        tk.END, "2. Corte o pão italiano em fatias de aproximadamente 1 cm de espessura. Disponha as fatias em uma assadeira.\n")
    instrucoes_texto.insert(
        tk.END, "3. Em uma frigideira, aqueça um fio de azeite de oliva e refogue a cebola e o alho picados até ficarem macios. Adicione a carne moída e frite até dourar. Tempere com sal e pimenta-do-reino a gosto.\n")
    instrucoes_texto.insert(
        tk.END, "4. Disponha a carne refogada sobre as fatias de pão italiano e cubra com fatias finas de queijo gorgonzola. Corte o tomate em rodelas finas e coloque uma rodela sobre cada tapa.\n")
    instrucoes_texto.insert(
        tk.END, "5. Leve a assadeira ao forno por cerca de 10 minutos ou até que o queijo esteja derretido e gratinado.\n")
    instrucoes_texto.insert(
        tk.END, "6. Retire a assadeira do forno e sirva as tapas quentes.\n")
    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=20, height=2, bg="#ffff00")
    botao_favorito.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=20, height=2, bg="#1f77b4")
    botao_comentario.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(janela, text="Fechar", width=20,
                             height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.pack(side=tk.LEFT, padx=10, pady=10)

def janelaFrancesinha():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Receita")

    # Cria os rótulos
    titulo_receita = tk.Label(janela, text="Título da Receita")
    titulo_receita.pack()

    ingredientes = tk.Label(janela, text="Ingredientes:")
    ingredientes.pack()

    ingrediente_1 = tk.Label(janela, text="Pão de forma")
    ingrediente_1.pack()

    ingrediente_2 = tk.Label(janela, text="Linguiça")
    ingrediente_2.pack()

    ingrediente_3 = tk.Label(janela, text="Presunto")
    ingrediente_3.pack()

    ingrediente_4 = tk.Label(janela, text="Queijo")
    ingrediente_4.pack()

    ingrediente_5 = tk.Label(janela, text="Molho de tomate")
    ingrediente_5.pack()

    ingrediente_6 = tk.Label(janela, text="Ovo")
    ingrediente_6.pack()

    instrucoes = tk.Label(janela, text="Instruções de Preparo:")
    instrucoes.pack()

    # Cria a área de texto para as instruções de preparo
    instrucoes_texto = tk.Text(janela)
    instrucoes_texto.pack()

    # Adiciona os dados da receita aos componentes
    titulo_receita["text"] = "Francesinha"

    instrucoes_texto.insert(
        tk.END, "1. Corte o pão de forma ao meio e coloque a linguiça e o presunto fatiados.\n")
    instrucoes_texto.insert(
        tk.END, "2. Coloque o queijo por cima e leve ao forno até derreter.\n")
    instrucoes_texto.insert(
        tk.END, "3. Coloque o ovo por cima da mistura e regue com o molho de tomate.\n")
    instrucoes_texto.insert(
        tk.END, "4. Sirva quente.\n")
    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=20, height=2, bg="#ffff00")
    botao_favorito.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=20, height=2, bg="#1f77b4")
    botao_comentario.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(janela, text="Fechar", width=20,
                             height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.pack(side=tk.LEFT, padx=10, pady=10)

def janelaBifesPeru():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Receita")

    # Cria os rótulos
    titulo_receita = tk.Label(janela, text="Título da Receita")
    titulo_receita.pack()

    ingredientes = tk.Label(janela, text="Ingredientes:")
    ingredientes.pack()

    ingrediente_1 = tk.Label(janela, text="4 bifes de peru")
    ingrediente_1.pack()

    ingrediente_2 = tk.Label(janela, text="Sal e pimenta-do-reino a gosto")
    ingrediente_2.pack()

    ingrediente_3 = tk.Label(janela, text="1 colher de sopa de azeite")
    ingrediente_3.pack()

    ingrediente_4 = tk.Label(janela, text="2 dentes de alho picados")
    ingrediente_4.pack()

    ingrediente_5 = tk.Label(janela, text="1 xícara de caldo de frango")
    ingrediente_5.pack()

    ingrediente_6 = tk.Label(janela, text="2 colheres de sopa de catchup")
    ingrediente_6.pack()

    ingrediente_7 = tk.Label(janela, text="2 colheres de sopa de vinagre")
    ingrediente_7.pack()

    ingrediente_8 = tk.Label(janela, text="2 colheres de sopa de açúcar")
    ingrediente_8.pack()

    ingrediente_9 = tk.Label(janela, text="1 colher de chá de mostarda")
    ingrediente_9.pack()

    ingrediente_10 = tk.Label(janela, text="1 colher de chá de orégano")
    ingrediente_10.pack()

    instrucoes = tk.Label(janela, text="Instruções de Preparo:")
    instrucoes.pack()

    # Cria a área de texto para as instruções de preparo
    instrucoes_texto = tk.Text(janela)
    instrucoes_texto.pack()

    # Adiciona os dados da receita aos componentes
    titulo_receita["text"] = "Bifes de Peru ao Molho de Catchup"

    instrucoes_texto.insert(
        tk.END, "1. Tempere os bifes de peru com sal e pimenta-do-reino a gosto.\n")
    instrucoes_texto.insert(
        tk.END, "2. Em uma panela, aqueça o azeite e frite os bifes de peru até dourar dos dois lados.\n")
    instrucoes_texto.insert(
        tk.END, "3. Adicione o alho picado e refogue por mais alguns minutos.\n")
    instrucoes_texto.insert(
        tk.END, "4. Adicione o caldo de frango, o catchup, o vinagre, o açúcar, a mostarda e o orégano. Misture bem.\n")
    instrucoes_texto.insert(
        tk.END, "5. Deixe cozinhar em fogo baixo por cerca de 20 minutos, ou até que o molho esteja espesso e os bifes de peru estejam macios.\n")

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=20, height=2, bg="#ffff00")
    botao_favorito.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=20, height=2, bg="#1f77b4")
    botao_comentario.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(janela, text="Fechar", width=20,
                             height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.pack(side=tk.LEFT, padx=10, pady=10)

def janelaPicanha():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Receita")

    # Cria os rótulos
    titulo_receita = tk.Label(janela, text="Título da Receita")
    titulo_receita.pack()

    ingredientes = tk.Label(janela, text="Ingredientes:")
    ingredientes.pack()

    ingrediente_1 = tk.Label(janela, text="1kg de picanha")
    ingrediente_1.pack()

    ingrediente_2 = tk.Label(janela, text="Sal e pimenta-do-reino a gosto")
    ingrediente_2.pack()

    ingrediente_3 = tk.Label(janela, text="2 dentes de alho picados")
    ingrediente_3.pack()

    ingrediente_4 = tk.Label(janela, text="1 colher de chá de azeite")
    ingrediente_4.pack()

    instrucoes = tk.Label(janela, text="Instruções de Preparo:")
    instrucoes.pack()

    # Cria a área de texto para as instruções de preparo
    instrucoes_texto = tk.Text(janela)
    instrucoes_texto.pack()

    # Adiciona os dados da receita aos componentes
    titulo_receita["text"] = "Picanha Grelhada"

    instrucoes_texto.insert(
        tk.END, "1. Tempere a picanha com sal e pimenta-do-reino a gosto e o alho picado.\n")
    instrucoes_texto.insert(
        tk.END, "2. Em uma grelha ou frigideira quente, aqueça o azeite e grelhe a picanha dos dois lados até atingir o ponto desejado.\n")
    instrucoes_texto.insert(
        tk.END, "3. Sirva a picanha ainda quente, cortada em fatias finas.\n")
    titulo_receita["text"] = "Picanha Grelhada"

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=20, height=2, bg="#ffff00")
    botao_favorito.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=20, height=2, bg="#1f77b4")
    botao_comentario.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(janela, text="Fechar", width=20,
                             height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.pack(side=tk.LEFT, padx=10, pady=10)

def janelaCaril():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Receita")

    # Cria os rótulos
    titulo_receita = tk.Label(janela, text="Título da Receita")
    titulo_receita.pack()

    ingredientes = tk.Label(janela, text="Ingredientes:")
    ingredientes.pack()

    ingrediente_1 = tk.Label(janela, text="1kg de frango cortado em pedaços")
    ingrediente_1.pack()

    ingrediente_2 = tk.Label(janela, text="2 colheres de sopa de azeite")
    ingrediente_2.pack()

    ingrediente_3 = tk.Label(janela, text="1 cebola picada")
    ingrediente_3.pack()

    ingrediente_4 = tk.Label(janela, text="2 dentes de alho picados")
    ingrediente_4.pack()

    ingrediente_5 = tk.Label(janela, text="1 pimentão vermelho picado")
    ingrediente_5.pack()

    ingrediente_6 = tk.Label(janela, text="1 pimentão verde picado")
    ingrediente_6.pack()

    ingrediente_7 = tk.Label(janela, text="2 colheres de sopa de caril em pó")
    ingrediente_7.pack()

    ingrediente_8 = tk.Label(janela, text="1 xícara de caldo de frango")
    ingrediente_8.pack()

    ingrediente_9 = tk.Label(janela, text="1 xícara de leite de coco")
    ingrediente_9.pack()

    ingrediente_10 = tk.Label(janela, text="Sal e pimenta-do-reino a gosto")
    ingrediente_10.pack()

    instrucoes = tk.Label(janela, text="Instruções de Preparo:")
    instrucoes.pack()

    # Cria a área de texto para as instruções de preparo
    instrucoes_texto = tk.Text(janela)
    instrucoes_texto.pack()

    # Adiciona os dados da receita aos componentes
    titulo_receita["text"] = "Caril de Frango"

    instrucoes_texto.insert(
        tk.END, "1. Em uma panela, aqueça o azeite e refogue a cebola, o alho e os pimentões até ficarem macios.\n")
    instrucoes_texto.insert(
        tk.END, "2. Adicione o frango e refogue até dourar.\n")
    instrucoes_texto.insert(
        tk.END, "3. Adicione o caril em pó e misture bem. Adicione o caldo de frango, o leite de coco, o sal e a pimenta-do-reino.\n")
    instrucoes_texto.insert(
        tk.END, "4. Deixe cozinhar em fogo baixo por cerca de 20 minutos, ou até o frango ficar macio e o molho engrossar. Sirva quente.\n")

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=20, height=2, bg="#ffff00")
    botao_favorito.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=20, height=2, bg="#1f77b4")
    botao_comentario.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(janela, text="Fechar", width=20,
                             height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.pack(side=tk.LEFT, padx=10, pady=10)

def janelaFrango():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Receita")

    # Cria os rótulos
    titulo_receita = tk.Label(janela, text="Título da Receita")
    titulo_receita.pack()

    ingredientes = tk.Label(janela, text="Ingredientes:")
    ingredientes.pack()

    ingrediente_1 = tk.Label(janela, text="1 frango inteiro")
    ingrediente_1.pack()

    ingrediente_2 = tk.Label(janela, text="Sal e pimenta-do-reino a gosto")
    ingrediente_2.pack()

    ingrediente_3 = tk.Label(janela, text="2 dentes de alho picados")
    ingrediente_3.pack()

    ingrediente_4 = tk.Label(janela, text="1 limão espremido")
    ingrediente_4.pack()

    instrucoes = tk.Label(janela, text="Instruções de Preparo:")
    instrucoes.pack()

    # Cria a área de texto para as instruções de preparo
    instrucoes_texto = tk.Text(janela)
    instrucoes_texto.pack()

    # Adiciona os dados da receita aos componentes
    titulo_receita["text"] = "Frango Assado"

    instrucoes_texto.insert(
        tk.END, "1. Preaqueça o forno a 180°C.\n")
    instrucoes_texto.insert(
        tk.END, "2. Tempere o frango com o sal, a pimenta-do-reino, o alho e o limão espremido.\n")
    instrucoes_texto.insert(
        tk.END, "3. Coloca o frango em uma assadeira e leve ao forno por cerca de 1 hora e 30 minutos, ou até que o frango esteja assado e dourado.\n")
    instrucoes_texto.insert(
        tk.END, "4. Retire o frango do forno e deixe descansar por alguns minutos antes de servir. Corte em pedaços e sirva ainda quente.\n")

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=20, height=2, bg="#ffff00")
    botao_favorito.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=20, height=2, bg="#1f77b4")
    botao_comentario.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(janela, text="Fechar", width=20,
                             height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.pack(side=tk.LEFT, padx=10, pady=10)

def janelaEmpadaoCarne():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Receita")

    # Cria os rótulos
    titulo_receita = tk.Label(janela, text="Título da Receita")
    titulo_receita.pack()

    ingredientes = tk.Label(janela, text="Ingredientes:")
    ingredientes.pack()

    ingrediente_1 = tk.Label(janela, text="1 kg de carne moída")
    ingrediente_1.pack()

    ingrediente_2 = tk.Label(janela, text="1 cebola, picada")
    ingrediente_2.pack()

    ingrediente_3 = tk.Label(janela, text="1 pimentão verde picado")
    ingrediente_3.pack()

    ingrediente_4 = tk.Label(janela, text="2 dentes de alho picados")
    ingrediente_4.pack()

    ingrediente_5 = tk.Label(janela, text="1 xícara de caldo de carne")
    ingrediente_5.pack()

    ingrediente_6 = tk.Label(janela, text="1 xícara de molho de tomate")
    ingrediente_6.pack()

    ingrediente_7 = tk.Label(janela, text="Sal e pimenta a gosto")
    ingrediente_7.pack()

    ingrediente_8 = tk.Label(janela, text="1 pacote de massa para empadão")
    ingrediente_8.pack()

    instrucoes = tk.Label(janela, text="Instruções de Preparo:")
    instrucoes.pack()

    # Cria a área de texto para as instruções de preparo
    instrucoes_texto = tk.Text(janela)
    instrucoes_texto.pack()

    # Adiciona os dados da receita aos componentes
    titulo_receita["text"] = "Empadao de Carne"

    instrucoes_texto.insert(
        tk.END, "1. Em uma panela grande, frite a carne moída em fogo médio-alto até que esteja cozida. Escorra o excesso de gordura.\n")
    instrucoes_texto.insert(
        tk.END, "2. Adicione a cebola, pimentão e alho picado à panela. Refogue até que os vegetais estejam macios.\n")
    instrucoes_texto.insert(
        tk.END, "3. Adicione o caldo de carne, molho de tomate, e uma pitada de sal e pimenta. Cozinhe por 10 minutos.\n")
    instrucoes_texto.insert(
        tk.END, "4. Deixe ferver e deixe cozinhar por 10 minutos.\n")
    instrucoes_texto.insert(tk.END, "5. Pré-aqueça o forno a 190°C.\n")
    instrucoes_texto.insert(
        tk.END, "6. Abra a massa para empadão em uma espessura de 0,5 cm e corte círculos com a ajuda de um cortador ou uma tampa de panela grande.\n")
    instrucoes_texto.insert(
        tk.END, "7. Coloque uma colher de carne no centro de cada círculo de massa.\n")
    instrucoes_texto.insert(
        tk.END, "8. Dobre a massa ao meio, formando um meio-luar, pressione as bordas para fechar.\n")
    instrucoes_texto.insert(
        tk.END, "9. Disponha os empadões em uma assadeira e leve ao forno por cerca de 25-30 minutos, ou até que esteja dourado e crocante.\n")
    instrucoes_texto.insert(tk.END, "10. Sirva quente.\n")

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=20, height=2, bg="#ffff00")
    botao_favorito.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=20, height=2, bg="#1f77b4")
    botao_comentario.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(janela, text="Fechar", width=20,
                             height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.pack(side=tk.LEFT, padx=10, pady=10)

def janelaBacalhau():
    # Create the main window
    janela = tk.Tk()
    janela.title("Receita")

    # Create labels
    recipe_title = tk.Label(janela, text="Título da Receita")
    recipe_title.pack()

    ingredients = tk.Label(janela, text="Ingredientes:")
    ingredients.pack()

    ingredient_1 = tk.Label(
        janela, text="1 libra de bacalhau dessalgado, deixado de molho durante a noite e escorrido")
    ingredient_1.pack()

    ingredient_2 = tk.Label(
        janela, text="4 batatas, descascadas e cortadas em pedaços")
    ingredient_2.pack()

    ingredient_3 = tk.Label(janela, text="1 cebola picada")
    ingredient_3.pack()

    ingredient_4 = tk.Label(janela, text="2 dentes de alho picados")
    ingredient_4.pack()

    ingredient_5 = tk.Label(janela, text="1 xícara de leite")
    ingredient_5.pack()

    ingredient_6 = tk.Label(janela, text="1/2 xícara de creme de leite")
    ingredient_6.pack()

    ingredient_7 = tk.Label(janela, text="1/4 xícara de azeite")
    ingredient_7.pack()

    ingredient_8 = tk.Label(janela, text="Sal e pimenta a gosto")
    ingredient_8.pack()

    preparation_instructions = tk.Label(janela, text="Instruções de Preparo:")
    preparation_instructions.pack()

    # Create the text area for the preparation instructions
    instructions_text = tk.Text(janela)
    instructions_text.pack()

    # Add recipe data to the components
    recipe_title["text"] = "Bacalhau"

    instructions_text.insert(tk.END, "1. Em uma panela grande, cubra o bacalhau com água. Leve ao fogo alto e deixe ferver, em seguida, reduza o fogo e deixe cozinhar por 10-15 minutos, ou até que o bacalhau esteja macio. Escorra e desfie o bacalhau com um garfo.\n")
    instructions_text.insert(
        tk.END, "2. Em outra panela, cozinhe as batatas em água com sal até que estejam macias. Escorra e amasse as batatas.\n")
    instructions_text.insert(
        tk.END, "3. Em uma frigideira grande, refogue a cebola e alho no azeite até que estejam macios.\n")
    instructions_text.insert(
        tk.END, "4. Adicione o bacalhau desfiado, batatas amassadas, leite, creme de leite e um pitada de sal e pimenta. Cozinhe por alguns minutos, até que a mistura esteja quente.\n")
    instructions_text.insert(tk.END, "5. Pré-aqueça o forno a 180°C.\n")
    instructions_text.insert(
        tk.END, "6. Transfira a mistura de bacalhau para uma assadeira. Leve ao forno pré-aquecido por 20-25 minutos, ou até que esteja dourado e levemente bolhante.\n")
    instructions_text.insert(tk.END, "7. Sirva quente.\n")

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=20, height=2, bg="#ffff00")
    botao_favorito.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=20, height=2, bg="#1f77b4")
    botao_comentario.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(janela, text="Fechar", width=20,
                             height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.pack(side=tk.LEFT, padx=10, pady=10)

def janelaCamarao():
    # Create the main window
    janela = tk.Tk()
    janela.title("Receita")

    # Create labels
    recipe_title = tk.Label(janela, text="Título da Receita")
    recipe_title.pack()

    ingredients = tk.Label(janela, text="Ingredientes:")
    ingredients.pack()

    ingredient_1 = tk.Label(janela, text="1 kg de camarão limpo e sem casca")
    ingredient_1.pack()

    ingredient_2 = tk.Label(
        janela, text="3 colheres de sopa de azeite de oliva")
    ingredient_2.pack()

    ingredient_3 = tk.Label(janela, text="2 dentes de alho picados")
    ingredient_3.pack()

    ingredient_4 = tk.Label(janela, text="1/4 xícara de suco de limão")
    ingredient_4.pack()

    ingredient_5 = tk.Label(janela, text="1/4 xícara de vinho branco")
    ingredient_5.pack()

    ingredient_6 = tk.Label(
        janela, text="1/4 xícara de caldo de frango ou água")
    ingredient_6.pack()

    ingredient_7 = tk.Label(janela, text="1/4 xícara de coentro picado")
    ingredient_7.pack()

    ingredient_8 = tk.Label(janela, text="Sal e pimenta do reino a gosto")
    ingredient_8.pack()

    preparation_instructions = tk.Label(janela, text="Instruções de Preparo:")
    preparation_instructions.pack()

def janelaFeijoadaPeixe():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Receita")

    # Cria os rótulos
    titulo_receita = tk.Label(janela, text="Título da Receita")
    titulo_receita.pack()

    ingredientes = tk.Label(janela, text="Ingredientes:")
    ingredientes.pack()

    ingrediente_1 = tk.Label(janela, text="2 kg de peixe (corvina, pescada ou outro de sua preferência)")
    ingrediente_1.pack()

    ingrediente_2 = tk.Label(janela, text="2 kg de feijão preto")
    ingrediente_2.pack()

    ingrediente_3 = tk.Label(janela, text="3 cebolas grandes")
    ingrediente_3.pack()

    ingrediente_4 = tk.Label(janela, text="3 dentes de alho")
    ingrediente_4.pack()

    ingrediente_5 = tk.Label(janela, text="2 tabletes de caldo de camarão")
    ingrediente_5.pack()

    ingrediente_6 = tk.Label(janela, text="1/2 xícara de azeite")
    ingrediente_6.pack()

    ingrediente_7 = tk.Label(janela, text="1/2 xícara de óleo")
    ingrediente_7.pack()

    ingrediente_8 = tk.Label(janela, text="1 xícara de farinha de mandioca")
    ingrediente_8.pack()

    ingrediente_9 = tk.Label(janela, text="Sal e pimenta-do-reino a gosto")
    ingrediente_9.pack()

    instrucoes = tk.Label(janela, text="Instruções de Preparo:")
    instrucoes.pack()

    # Cria a área de texto para as instruções de preparo
    instrucoes_texto = tk.Text(janela)
    instrucoes_texto.pack()

    # Adiciona os dados da receita aos componentes
    titulo_receita["text"] = "Feijoada de Peixe"

    instrucoes_texto.insert(
        tk.END, "1. Lave bem o peixe e corte em pedaços.\n")
    instrucoes_texto.insert(
        tk.END, "2. Coloque o feijão de molho por pelo menos 12 horas.\n")
    instrucoes_texto.insert(
        tk.END, "3. Escorra o feijão e cozinhe-o em água fervente com cebola e alho até ficar macio.\n")
    instrucoes_texto.insert(
        tk.END, "4. Em uma panela, refogue a cebola e o alho com o azeite e o óleo.\n")
    instrucoes_texto.insert(
        tk.END, "5. Adicione o peixe, tempere com sal e pimenta-do-reino e refogue por cerca de 5 minutos.\n")
    instrucoes_texto.insert(
        tk.END, "6. Acrescente o caldo de camarão e a farinha de mandioca dissolvida em água.\n")
    instrucoes_texto.insert(
        tk.END, "7. Misture bem, cubra a panela e deixe cozinhando por cerca de 15 minutos.\n")
    instrucoes_texto.insert(
        tk.END, "8. Por último, adicione o feijão ao peixe e deixe ferver por mais 10 minutos.\n")
    instrucoes_texto.insert(
        tk.END, "9. Sirva a feijoada ainda quente e acompanhada de arroz branco.\n")
    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=20, height=2, bg="#ffff00")
    botao_favorito.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=20, height=2, bg="#1f77b4")
    botao_comentario.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(janela, text="Fechar", width=20,
                             height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.pack(side=tk.LEFT, padx=10, pady=10)

def janelaGaropa():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Receita")

    # Cria os rótulos
    titulo_receita = tk.Label(janela, text="Título da Receita")
    titulo_receita.pack()

    ingredientes = tk.Label(janela, text="Ingredientes:")
    ingredientes.pack()

    ingrediente_1 = tk.Label(janela, text="2 filés de peixe garopa")
    ingrediente_1.pack()

    ingrediente_2 = tk.Label(janela, text="1 cebola picada")
    ingrediente_2.pack()

    ingrediente_3 = tk.Label(janela, text="2 dentes de alho picados")
    ingrediente_3.pack()

    ingrediente_4 = tk.Label(janela, text="1/2 xícara de suco de limão")
    ingrediente_4.pack()

    ingrediente_5 = tk.Label(janela, text="Sal e pimenta-do-reino a gosto")
    ingrediente_5.pack()

    instrucoes = tk.Label(janela, text="Instruções de Preparo:")
    instrucoes.pack()

    # Cria a área de texto para as instruções de preparo
    instrucoes_texto = tk.Text(janela)
    instrucoes_texto.pack()

    # Adiciona os dados da receita aos componentes
    titulo_receita["text"] = "Peixe Garopa Assado"

    instrucoes_texto.insert(
        tk.END, "1. Tempere os filés de peixe com sal e pimenta-do-reino.\n")
    instrucoes_texto.insert(
        tk.END, "2. Coloque o peixe em um refratário com a cebola e o alho. Regue com o suco de limão.\n")
    instrucoes_texto.insert(
        tk.END, "3. Leve ao forno pré-aquecido a 200°C por aproximadamente 15 minutos, ou até que os filés estejam assados e dourados.\n")
    instrucoes_texto.insert(
        tk.END, "4. Retire do forno e sirva ainda quente.\n")
    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=20, height=2, bg="#ffff00")
    botao_favorito.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=20, height=2, bg="#1f77b4")
    botao_comentario.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(janela, text="Fechar", width=20,
                             height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.pack(side=tk.LEFT, padx=10, pady=10)

def janelaPolvo():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Receita")

    # Cria os rótulos
    titulo_receita = tk.Label(janela, text="Título da Receita")
    titulo_receita.pack()

    ingredientes = tk.Label(janela, text="Ingredientes:")
    ingredientes.pack()

    ingrediente_1 = tk.Label(janela, text="1 polvo médio")
    ingrediente_1.pack()

    ingrediente_2 = tk.Label(janela, text="3 dentes de alho")
    ingrediente_2.pack()

    ingrediente_3 = tk.Label(janela, text="2 colheres (sopa) de azeite")
    ingrediente_3.pack()

    ingrediente_4 = tk.Label(janela, text="Sal e pimenta-do-reino a gosto")
    ingrediente_4.pack()

    instrucoes = tk.Label(janela, text="Instruções de Preparo:")
    instrucoes.pack()

    # Cria a área de texto para as instruções de preparo
    instrucoes_texto = tk.Text(janela)
    instrucoes_texto.pack()

    # Adiciona os dados da receita aos componentes
    titulo_receita["text"] = "Polvo Assado"

    instrucoes_texto.insert(
        tk.END, "1. Lave e limpe bem o polvo.\n")
    instrucoes_texto.insert(
        tk.END, "2. Coloque o polvo em uma assadeira e tempere com o sal, a pimenta-do-reino, o alho e o azeite.\n")
    instrucoes_texto.insert(
        tk.END, "3. Leve ao forno preaquecido a 200°C por cerca de 40 minutos, virando o polvo ao meio do tempo.\n")
    instrucoes_texto.insert(
        tk.END, "4. Retire do forno e sirva quente.\n")
    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=20, height=2, bg="#ffff00")
    botao_favorito.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=20, height=2, bg="#1f77b4")
    botao_comentario.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(janela, text="Fechar", width=20,
                             height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.pack(side=tk.LEFT, padx=10, pady=10)

def janelaSalmao():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Receita")

    # Cria os rótulos
    titulo_receita = tk.Label(janela, text="Título da Receita")
    titulo_receita.pack()

    ingredientes = tk.Label(janela, text="Ingredientes:")
    ingredientes.pack()

    ingrediente_1 = tk.Label(janela, text="2 filés de salmão")
    ingrediente_1.pack()

    ingrediente_2 = tk.Label(janela, text="Sal e pimenta-do-reino a gosto")
    ingrediente_2.pack()

    ingrediente_3 = tk.Label(janela, text="2 colheres de sopa de azeite")
    ingrediente_3.pack()

    ingrediente_4 = tk.Label(janela, text="2 dentes de alho picados")
    ingrediente_4.pack()

    ingrediente_5 = tk.Label(janela, text="Limão espremido a gosto")
    ingrediente_5.pack()

    instrucoes = tk.Label(janela, text="Instruções de Preparo:")
    instrucoes.pack()

    # Cria a área de texto para as instruções de preparo
    instrucoes_texto = tk.Text(janela)
    instrucoes_texto.pack()

    # Adiciona os dados da receita aos componentes
    titulo_receita["text"] = "Salmão Assado"

    instrucoes_texto.insert(
        tk.END, "1. Pré-aqueça o forno a 200°C.\n")
    instrucoes_texto.insert(
        tk.END, "2. Tempere os filés de salmão com sal e pimenta-do-reino.\n")
    instrucoes_texto.insert(
        tk.END, "3. Em uma assadeira, coloque os filés de salmão e regue-os com azeite.\n")
    instrucoes_texto.insert(
        tk.END, "4. Adicione o alho e o limão e leve ao forno por cerca de 15 minutos.\n")
    instrucoes_texto.insert(
        tk.END, "5. Retire do forno e sirva quente com salada ou acompanhamentos de sua preferência.\n")
    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=20, height=2, bg="#ffff00")
    botao_favorito.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=20, height=2, bg="#1f77b4")
    botao_comentario.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(janela, text="Fechar", width=20,
                             height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.pack(side=tk.LEFT, padx=10, pady=10)

def janelaSbacalhau():
    
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Receita")

    # Cria os rótulos
    titulo_receita = tk.Label(janela, text="Título da Receita")
    titulo_receita.pack()

    ingredientes = tk.Label(janela, text="Ingredientes:")
    ingredientes.pack()

    ingrediente_1 = tk.Label(janela, text="300 g de bacalhau desfiado")
    ingrediente_1.pack()

    ingrediente_2 = tk.Label(janela, text="2 tomates maduros cortados em cubos")
    ingrediente_2.pack()

    ingrediente_3 = tk.Label(janela, text="2 cebolas roxas cortadas em rodelas")
    ingrediente_3.pack()

    ingrediente_4 = tk.Label(janela, text="1/2 xícara (chá) de azeite")
    ingrediente_4.pack()

    ingrediente_5 = tk.Label(janela, text="1/2 xícara (chá) de vinagre de vinho tinto")
    ingrediente_5.pack()

    ingrediente_6 = tk.Label(janela, text="1 colher (sopa) de alcaparras")
    ingrediente_6.pack()

    ingrediente_7 = tk.Label(janela, text="1 colher (sopa) de salsinha picada")
    ingrediente_7.pack()

    ingrediente_8 = tk.Label(janela, text="Sal a gosto")
    ingrediente_8.pack()

    instrucoes = tk.Label(janela, text="Instruções de Preparo:")
    instrucoes.pack()

    # Cria a área de texto para as instruções de preparo
    instrucoes_texto = tk.Text(janela)
    instrucoes_texto.pack()

    # Adiciona os dados da receita aos componentes
    titulo_receita["text"] = "Salada de Bacalhau"

    instrucoes_texto.insert(
        tk.END, "1. Em uma tigela, misture o bacalhau desfiado com os tomates, a cebola e o azeite.\n")
    instrucoes_texto.insert(
        tk.END, "2. Acrescente o vinagre, as alcaparras e a salsinha.\n")
    instrucoes_texto.insert(
        tk.END, "3. Tempere com sal a gosto e misture bem.\n")
    instrucoes_texto.insert(
        tk.END, "4. Leve à geladeira por pelo menos 2 horas antes de servir.\n")
    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=20, height=2, bg="#ffff00")
    botao_favorito.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=20, height=2, bg="#1f77b4")
    botao_comentario.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(janela, text="Fechar", width=20,
                             height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.pack(side=tk.LEFT, padx=10, pady=10)

def janelaSbolonhesa():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Receita")

    # Cria os rótulos
    titulo_receita = tk.Label(janela, text="Título da Receita")
    titulo_receita.pack()

    ingredientes = tk.Label(janela, text="Ingredientes:")
    ingredientes.pack()

    ingrediente_1 = tk.Label(janela, text="500g de macarrão tipo parafuso")
    ingrediente_1.pack()

    ingrediente_2 = tk.Label(janela, text="1/2 lata de molho de tomate")
    ingrediente_2.pack()

    ingrediente_3 = tk.Label(janela, text="1 lata de ervilhas")
    ingrediente_3.pack()

    ingrediente_4 = tk.Label(janela, text="1 cebola picada")
    ingrediente_4.pack()

    ingrediente_5 = tk.Label(janela, text="1/2 lata de milho")
    ingrediente_5.pack()

    ingrediente_6 = tk.Label(janela, text="1/2 lata de azeitona preta")
    ingrediente_6.pack()

    instrucoes = tk.Label(janela, text="Instruções de Preparo:")
    instrucoes.pack()

    # Cria a área de texto para as instruções de preparo
    instrucoes_texto = tk.Text(janela)
    instrucoes_texto.pack()

    # Adiciona os dados da receita aos componentes
    titulo_receita["text"] = "Salada de Bolonhesa"

    instrucoes_texto.insert(
        tk.END, "1. Cozinhe o macarrão em uma panela com água fervente até que fique al dente.\n")
    instrucoes_texto.insert(
        tk.END, "2. Enquanto o macarrão cozinha, prepare a salada. Em uma tigela, misture o molho de tomate, a cebola, as ervilhas, o milho e a azeitona.\n")
    instrucoes_texto.insert(
        tk.END, "3. Escorra o macarrão quando estiver pronto, e adicione na tigela com os outros ingredientes. Misture bem.\n")
    instrucoes_texto.insert(
        tk.END, "4. Sirva a salada ainda quente ou à temperatura ambiente.\n")
    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=20, height=2, bg="#ffff00")
    botao_favorito.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=20, height=2, bg="#1f77b4")
    botao_comentario.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(janela, text="Fechar", width=20,
                             height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.pack(side=tk.LEFT, padx=10, pady=10)

def janelaSbulgur():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Receita")

    # Cria os rótulos
    titulo_receita = tk.Label(janela, text="Título da Receita")
    titulo_receita.pack()

    ingredientes = tk.Label(janela, text="Ingredientes:")
    ingredientes.pack()

    ingrediente_1 = tk.Label(janela, text="1 xícara (chá) de bulgur")
    ingrediente_1.pack()

    ingrediente_2 = tk.Label(janela, text="1 e 1/2 xícara (chá) de água")
    ingrediente_2.pack()

    ingrediente_3 = tk.Label(janela, text="2 tomates em cubos")
    ingrediente_3.pack()

    ingrediente_4 = tk.Label(janela, text="1 cebola roxa cortada em cubinhos")
    ingrediente_4.pack()

    ingrediente_5 = tk.Label(janela, text="1/2 xícara (chá)de pepino em cubos")
    ingrediente_5.pack()

    ingrediente_6 = tk.Label(janela, text="1/4 xícara (chá) de azeite")
    ingrediente_6.pack()

    ingrediente_7 = tk.Label(janela, text="2 colheres (sopa) de suco de limão")
    ingrediente_7.pack()

    ingrediente_8 = tk.Label(janela, text="1 colher (sopa) de manjericão picado")
    ingrediente_8.pack()

    ingrediente_9 = tk.Label(janela, text="Sal e pimenta-do-reino a gosto")
    ingrediente_9.pack()


    instrucoes = tk.Label(janela, text="Instruções de Preparo:")
    instrucoes.pack()

    # Cria a área de texto para as instruções de preparo
    instrucoes_texto = tk.Text(janela)
    instrucoes_texto.pack()

    # Adiciona os dados da receita aos componentes
    titulo_receita["text"] = "Salada Bulgur"

    instrucoes_texto.insert(
        tk.END, "1. Em uma panela, coloque o bulgur com a água, tampe a panela e deixe por 15 minutos.\n")
    instrucoes_texto.insert(
        tk.END, "2. Em uma tigela, coloque o bulgur, os tomates, a cebola, o pepino, o azeite, o suco de limão, o manjericão, sal e pimenta-do-reino.\n")
    instrucoes_texto.insert(
        tk.END, "3. Misture bem e leve à geladeira por 1 hora. Sirva em seguida.\n")
    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=20, height=2, bg="#ffff00")
    botao_favorito.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=20, height=2, bg="#1f77b4")
    botao_comentario.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(janela, text="Fechar", width=20,
                             height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.pack(side=tk.LEFT, padx=10, pady=10)

def janelaSdelicias():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Receita")

    # Cria os rótulos
    titulo_receita = tk.Label(janela, text="Título da Receita")
    titulo_receita.pack()

    ingredientes = tk.Label(janela, text="Ingredientes:")
    ingredientes.pack()

    ingrediente_1 = tk.Label(janela, text="1 xícara de azeitonas verdes picadas")
    ingrediente_1.pack()

    ingrediente_2 = tk.Label(janela, text="1 xícara de milho verde")
    ingrediente_2.pack()

    ingrediente_3 = tk.Label(janela, text="2 cenouras raladas")
    ingrediente_3.pack()

    ingrediente_4 = tk.Label(janela, text="1/2 xícara de cebola em cubos")
    ingrediente_4.pack()

    ingrediente_5 = tk.Label(janela, text="1/2 xícara de azeite")
    ingrediente_5.pack()
 
    ingrediente_6 = tk.Label(janela, text="1/2 xícara de vinagre de maçã")
    ingrediente_6.pack()

    ingrediente_7 = tk.Label(janela, text="1/4 xícara de salsinha picada")
    ingrediente_7.pack()

    ingrediente_8 = tk.Label(janela, text="Sal e pimenta-do-reino a gosto")
    ingrediente_8.pack()

    instrucoes = tk.Label(janela, text="Instruções de Preparo:")
    instrucoes.pack()

    # Cria a área de texto para as instruções de preparo
    instrucoes_texto = tk.Text(janela)
    instrucoes_texto.pack()

    # Adiciona os dados da receita aos componentes
    titulo_receita["text"] = "Salada de Delícias"

    instrucoes_texto.insert(
        tk.END, "1. Em uma tigela grande, misture o milho, as azeitonas, a cenoura, a cebola e a salsinha.\n")
    instrucoes_texto.insert(
        tk.END, "2. Em uma tigela pequena, misture o azeite, o vinagre, o sal e a pimenta-do-reino.\n")
    instrucoes_texto.insert(
        tk.END, "3. Despeje a mistura de azeite sobre a salada e misture bem.\n")
    instrucoes_texto.insert(
        tk.END, "4. Sirva a salada ainda quente ou refrigerada.\n")
    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=20, height=2, bg="#ffff00")
    botao_favorito.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=20, height=2, bg="#1f77b4")
    botao_comentario.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(janela, text="Fechar", width=20,
                             height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.pack(side=tk.LEFT, padx=10, pady=10)

def janelaSfrango():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Receita")

    # Cria os rótulos
    titulo_receita = tk.Label(janela, text="Título da Receita")
    titulo_receita.pack()

    ingredientes = tk.Label(janela, text="Ingredientes:")
    ingredientes.pack()

    ingrediente_1 = tk.Label(janela, text="200g de frango cozido e desfiado")
    ingrediente_1.pack()

    ingrediente_2 = tk.Label(janela, text="1 pimentão verde cortado em cubos")
    ingrediente_2.pack()

    ingrediente_3 = tk.Label(janela, text="1 cebola roxa cortada em cubos")
    ingrediente_3.pack()

    ingrediente_4 = tk.Label(janela, text="100g de milho cozido")
    ingrediente_4.pack()

    ingrediente_5 = tk.Label(janela, text="100g de ervilha cozida")
    ingrediente_5.pack()

    ingrediente_6 = tk.Label(janela, text="1/2 xícara de azeite")
    ingrediente_6.pack()

    ingrediente_7 = tk.Label(janela, text="1/2 xícara de vinagre de maçã")
    ingrediente_7.pack()

    ingrediente_8 = tk.Label(janela, text="Sal e pimenta-do-reino a gosto")
    ingrediente_8.pack()

    instrucoes = tk.Label(janela, text="Instruções de Preparo:")
    instrucoes.pack()

    # Cria a área de texto para as instruções de preparo
    instrucoes_texto = tk.Text(janela)
    instrucoes_texto.pack()

    # Adiciona os dados da receita aos componentes
    titulo_receita["text"] = "Salada de Frango"

    instrucoes_texto.insert(
        tk.END, "1. Em uma tigela, misture o frango, o pimentão, a cebola, o milho e a ervilha.\n")
    instrucoes_texto.insert(
        tk.END, "2. Em outra tigela, misture o azeite, o vinagre, o sal e a pimenta-do-reino.\n")
    instrucoes_texto.insert(
        tk.END, "3. Junte o líquido à tigela com os ingredientes sólidos e misture bem.\n")
    instrucoes_texto.insert(
        tk.END, "4. Coloque a salada na geladeira por algumas horas antes de servir.\n")
    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=20, height=2, bg="#ffff00")
    botao_favorito.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=20, height=2, bg="#1f77b4")
    botao_comentario.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(janela, text="Fechar", width=20,
                             height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.pack(side=tk.LEFT, padx=10, pady=10)

def janelaSsalsichas():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Receita")

    # Cria os rótulos
    titulo_receita = tk.Label(janela, text="Título da Receita")
    titulo_receita.pack()

    ingredientes = tk.Label(janela, text="Ingredientes:")
    ingredientes.pack()

    ingrediente_1 = tk.Label(janela, text="1kg de salsichas cozidas")
    ingrediente_1.pack()

    ingrediente_2 = tk.Label(janela, text="1 xícara (chá) de azeitonas verdes")
    ingrediente_2.pack()

    ingrediente_3 = tk.Label(janela, text="1 maço de alface crespa")
    ingrediente_3.pack()

    ingrediente_4 = tk.Label(janela, text="1 cebola roxa")
    ingrediente_4.pack()

    ingrediente_5 = tk.Label(janela, text="2 tomates maduros")
    ingrediente_5.pack()

    ingrediente_6 = tk.Label(janela, text="1 xícara (chá) de azeite")
    ingrediente_6.pack()

    ingrediente_7 = tk.Label(janela, text="1/2 xícara (chá) de vinagre balsâmico")
    ingrediente_7.pack()

    ingrediente_8 = tk.Label(janela, text="2 colheres (sopa) de mostarda")
    ingrediente_8.pack()

    ingrediente_9 = tk.Label(janela, text="Sal e pimenta-do-reino a gosto")
    ingrediente_9.pack()

    instrucoes = tk.Label(janela, text="Instruções de Preparo:")
    instrucoes.pack()

    # Cria a área de texto para as instruções de preparo
    instrucoes_texto = tk.Text(janela)
    instrucoes_texto.pack()

    # Adiciona os dados da receita aos componentes
    titulo_receita["text"] = "Salada de Salsichas"

    instrucoes_texto.insert(
        tk.END, "1. Corte as salsichas cozidas em rodelas e coloque-as em uma tigela. \n")
    instrucoes_texto.insert(
        tk.END, "2. Corte a alface, a cebola e os tomates em pedaços pequenos e coloque-os na tigela com as salsichas. \n")
    instrucoes_texto.insert(
        tk.END, "3. Coloque as azeitonas verdes na tigela. \n")
    instrucoes_texto.insert(
        tk.END, "4. Em uma tigela separada, misture o azeite, o vinagre balsâmico, a mostarda, o sal e a pimenta-do-reino. \n")
    instrucoes_texto.insert(
        tk.END, "5. Despeje a mistura sobre a salada e misture bem. \n")
    instrucoes_texto.insert(
        tk.END, "6. Sirva a salada de salsichas ainda quente. \n")
    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=20, height=2, bg="#ffff00")
    botao_favorito.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=20, height=2, bg="#1f77b4")
    botao_comentario.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(janela, text="Fechar", width=20,
                             height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.pack(side=tk.LEFT, padx=10, pady=10)

def janelaCaneloneVegetariano():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Receita")

    # Cria os rótulos
    titulo_receita = tk.Label(janela, text="Título da Receita")
    titulo_receita.pack()

    ingredientes = tk.Label(janela, text="Ingredientes:")
    ingredientes.pack()

    ingrediente_1 = tk.Label(janela, text="1 pacote de canelone (sem ovos)")
    ingrediente_1.pack()

    ingrediente_2 = tk.Label(janela, text="1 colher de sopa de azeite")
    ingrediente_2.pack()

    ingrediente_3 = tk.Label(janela, text="1 cebola picada")
    ingrediente_3.pack()

    ingrediente_4 = tk.Label(janela, text="2 dentes de alho picados")
    ingrediente_4.pack()

    ingrediente_5 = tk.Label(janela, text="2 xícaras de molho de tomate")
    ingrediente_5.pack()

    ingrediente_6 = tk.Label(janela, text="2 xícaras de ricota")
    ingrediente_6.pack()

    ingrediente_7 = tk.Label(janela, text="2 xícaras de espinafre picado")
    ingrediente_7.pack()

    ingrediente_8 = tk.Label(janela, text="1/2 xícara de queijo parmesão ralado")
    ingrediente_8.pack()

    ingrediente_9 = tk.Label(janela, text="Sal e pimenta-do-reino a gosto")
    ingrediente_9.pack()

    instrucoes = tk.Label(janela, text="Instruções de Preparo:")
    instrucoes.pack()

    # Cria a área de texto para as instruções de preparo
    instrucoes_texto = tk.Text(janela)
    instrucoes_texto.pack()

    # Adiciona os dados da receita aos componentes
    titulo_receita["text"] = "Canelone Vegetariano"

    instrucoes_texto.insert(
        tk.END, "1. Em uma panela, aqueça o azeite e refogue a cebola e o alho.\n")
    instrucoes_texto.insert(
        tk.END, "2. Junte o molho de tomate e misture bem.\n")
    instrucoes_texto.insert(
        tk.END, "3. Em seguida, adicione a ricota, o espinafre e o queijo parmesão. Misture bem.\n")
    instrucoes_texto.insert(
        tk.END, "4. Tempere com sal e pimenta-do-reino a gosto.\n")
    instrucoes_texto.insert(
        tk.END, "5. Reserve.\n")
    instrucoes_texto.insert(
        tk.END, "6. Em uma assadeira, coloque uma camada de molho de tomate e, em seguida, coloque uma camada de canelone preenchido com a ricota.\n")
    instrucoes_texto.insert(
        tk.END, "7. Repita o processo até terminar todos os ingredientes.\n")
    instrucoes_texto.insert(
        tk.END, "8. Polvilhe o queijo parmesão ralado.\n")
    instrucoes_texto.insert(
        tk.END, "9. Leve ao forno preaquecido a 180°C por aproximadamente 25 minutos.\n")
    instrucoes_texto.insert(
        tk.END, "10. Sirva quente.\n")
    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=20, height=2, bg="#ffff00")
    botao_favorito.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=20, height=2, bg="#1f77b4")
    botao_comentario.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(janela, text="Fechar", width=20,
                             height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.pack(side=tk.LEFT, padx=10, pady=10)

def janelaCogumelos():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Receita")

    # Cria os rótulos
    titulo_receita = tk.Label(janela, text="Título da Receita")
    titulo_receita.pack()

    ingredientes = tk.Label(janela, text="Ingredientes:")
    ingredientes.pack()

    ingrediente_1 = tk.Label(janela, text="4 cogumelos portobello")
    ingrediente_1.pack()

    ingrediente_2 = tk.Label(janela, text="1 colher de sopa de azeite")
    ingrediente_2.pack()

    ingrediente_3 = tk.Label(janela, text="1/4 de xícara de cebola picada")
    ingrediente_3.pack()

    ingrediente_4 = tk.Label(janela, text="1 dente de alho picado")
    ingrediente_4.pack()

    ingrediente_5 = tk.Label(janela, text="1/2 xícara de abobrinha em cubos")
    ingrediente_5.pack()

    ingrediente_6 = tk.Label(janela, text="1/2 xícara de tomate em cubos")
    ingrediente_6.pack()

    ingrediente_7 = tk.Label(janela, text="1/4 xícara de queijo parmesão ralado")
    ingrediente_7.pack()

    ingrediente_8 = tk.Label(janela, text="1 colher de sopa de salsa picada")
    ingrediente_8.pack()

    ingrediente_9 = tk.Label(janela, text="Sal e pimenta a gosto")
    ingrediente_9.pack()

    instrucoes = tk.Label(janela, text="Instruções de Preparo:")
    instrucoes.pack()

    # Cria a área de texto para as instruções de preparo
    instrucoes_texto = tk.Text(janela)
    instrucoes_texto.pack()

    # Adiciona os dados da receita aos componentes
    titulo_receita["text"] = "Cogumelos Recheados Vegetarianos"

    instrucoes_texto.insert(
        tk.END, "1. Pré-aqueça o forno a 200 °C.\n")
    instrucoes_texto.insert(
        tk.END, "2. Limpe os cogumelos e retire os talos e as gílias.\n")
    instrucoes_texto.insert(
        tk.END, "3. Em uma frigideira, aqueça o azeite e refogue a cebola e o alho.\n")
    instrucoes_texto.insert(
        tk.END, "4. Acrescente a abobrinha, o tomate, o queijo parmesão e a salsa. Misture bem e deixe cozinhar por 5 minutos.\n")
    instrucoes_texto.insert(
        tk.END, "5. Tempere com sal e pimenta a gosto.\n")
    instrucoes_texto.insert(
        tk.END, "6. Recheie os cogumelos com a mistura de legumes.\n")
    instrucoes_texto.insert(
        tk.END, "7. Coloque os cogumelos em uma assadeira untada com azeite.\n")
    instrucoes_texto.insert(
        tk.END, "8. Asse por 15 minutos ou até que os cogumelos estejam macios e dourados.\n")
    instrucoes_texto.insert(
        tk.END, "9. Sirva os cogumelos recheados ainda quentes.\n")
    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=20, height=2, bg="#ffff00")
    botao_favorito.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=20, height=2, bg="#1f77b4")
    botao_comentario.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(janela, text="Fechar", width=20,
                             height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.pack(side=tk.LEFT, padx=10, pady=10)

def janelaCrepeVegetariano():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Receita")

    # Cria os rótulos
    titulo_receita = tk.Label(janela, text="Título da Receita")
    titulo_receita.pack()

    ingredientes = tk.Label(janela, text="Ingredientes:")
    ingredientes.pack()

    ingrediente_1 = tk.Label(janela, text="1 xícara de farinha de trigo")
    ingrediente_1.pack()

    ingrediente_2 = tk.Label(janela, text="1/2 xícara de leite")
    ingrediente_2.pack()

    ingrediente_3 = tk.Label(janela, text="2 ovos")
    ingrediente_3.pack()

    ingrediente_4 = tk.Label(janela, text="1 colher de sopa de óleo")
    ingrediente_4.pack()

    ingrediente_5 = tk.Label(janela, text="1/2 xícara de azeite")
    ingrediente_5.pack()
 
    ingrediente_6 = tk.Label(janela, text="1/2 xícara de milho verde")
    ingrediente_6.pack()

    ingrediente_7 = tk.Label(janela, text="2 cenouras raladas")
    ingrediente_7.pack()

    ingrediente_8 = tk.Label(janela, text="1/2 xícara de cebola em cubos")
    ingrediente_8.pack()

    ingrediente_9 = tk.Label(janela, text="1/4 xícara de salsinha picada")
    ingrediente_9.pack()

    ingrediente_10 = tk.Label(janela, text="Sal e pimenta-do-reino a gosto")
    ingrediente_10.pack()

    instrucoes = tk.Label(janela, text="Instruções de Preparo:")
    instrucoes.pack()

    # Cria a área de texto para as instruções de preparo
    instrucoes_texto = tk.Text(janela)
    instrucoes_texto.pack()

    # Adiciona os dados da receita aos componentes
    titulo_receita["text"] = "Crepe Vegetariano"

    instrucoes_texto.insert(
        tk.END, "1. Em uma tigela, misture a farinha, o leite, os ovos e o óleo. Misture bem até não haver grumos.\n")
    instrucoes_texto.insert(
        tk.END, "2. Despeje uma quantidade generosa de óleo em uma frigideira antiaderente e aqueça em fogo médio.\n")
    instrucoes_texto.insert(
        tk.END, "3. Despeje 1/4 xícara da massa na frigideira e espalhe-a para formar um círculo.\n")
    instrucoes_texto.insert(
        tk.END, "4. Cozinhe o crepe por cerca de 1 minuto, ou até que este fique dourado. Vire o crepe e cozinhe por mais 30 segundos.\n")
    instrucoes_texto.insert(
        tk.END, "5. Enquanto o crepe cozinha, misture o milho, as cenouras, a cebola, a salsinha e os temperos em uma tigela.\n")
    instrucoes_texto.insert(
        tk.END, "6. Quando o crepe estiver pronto, espalhe a mistura de vegetais por cima. Enrole o crepe e sirva.\n")
    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=20, height=2, bg="#ffff00")
    botao_favorito.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=20, height=2, bg="#1f77b4")
    botao_comentario.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(janela, text="Fechar", width=20,
                             height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.pack(side=tk.LEFT, padx=10, pady=10)

def janelaFolhadoVegetariano():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Receita")

    # Cria os rótulos
    titulo_receita = tk.Label(janela, text="Título da Receita")
    titulo_receita.pack()

    ingredientes = tk.Label(janela, text="Ingredientes:")
    ingredientes.pack()

    ingrediente_1 = tk.Label(janela, text="2 pacotes de massa folhada")
    ingrediente_1.pack()

    ingrediente_2 = tk.Label(janela, text="1 xícara de cebola em cubos")
    ingrediente_2.pack()

    ingrediente_3 = tk.Label(janela, text="1/2 xícara de azeite")
    ingrediente_3.pack()

    ingrediente_4 = tk.Label(janela, text="1/2 xícara de queijo parmesão ralado")
    ingrediente_4.pack()

    ingrediente_5 = tk.Label(janela, text="250mL de leite")
    ingrediente_5.pack()

    ingrediente_6 = tk.Label(janela, text="1 xícara de molho de tomate")
    ingrediente_6.pack()

    ingrediente_7 = tk.Label(janela, text="1 cenoura em cubos pequenos")
    ingrediente_7.pack()

    ingrediente_8 = tk.Label(janela, text="1/2 xícara de ervilhas")
    ingrediente_8.pack()

    ingrediente_9 = tk.Label(janela, text="1 colher de sopa de azeite extra-virgem")
    ingrediente_9.pack()

    ingrediente_10 = tk.Label(janela, text="Sal e pimenta-do-reino a gosto")
    ingrediente_10.pack()

    instrucoes = tk.Label(janela, text="Instruções de Preparo:")
    instrucoes.pack()

    # Cria a área de texto para as instruções de preparo
    instrucoes_texto = tk.Text(janela)
    instrucoes_texto.pack()

    # Adiciona os dados da receita aos componentes
    titulo_receita["text"] = "Folhado Vegetariano"

    instrucoes_texto.insert(
        tk.END, "1. Pré-aqueça o forno a 180°C.\n")
    instrucoes_texto.insert(
        tk.END, "2. Em uma panela, coloque o azeite e a cebola e deixe refogar por alguns minutos.\n")
    instrucoes_texto.insert(
        tk.END, "3. Acrescente o molho de tomate, a cenoura, as ervilhas, o sal e a pimenta-do-reino e deixe cozinhar por mais alguns minutos.\n")
    instrucoes_texto.insert(
        tk.END, "4. Despeje o leite na panela, misture e deixe cozinhar por mais alguns minutos.\n")
    instrucoes_texto.insert(
        tk.END, "5. Retire a panela do fogo e deixe esfriar.\n")
    instrucoes_texto.insert(
        tk.END, "6. Em uma assadeira, coloque uma das massas folhadas.\n")
    instrucoes_texto.insert(
        tk.END, "7. Espalhe a mistura de legumes sobre a massa folhada.\n")
    instrucoes_texto.insert(
        tk.END, "8. Cubra com a segunda massa folhada e pressione os bordos para fechar.\n")
    instrucoes_texto.insert(
        tk.END, "9. Pincele a superfície com o azeite extra-virgem e polvilhe o queijo parmesão.\n")
    instrucoes_texto.insert(
        tk.END, "10. Leve para assar em forno pré-aquecido por aproximadamente 25 minutos.\n")
    instrucoes_texto.insert(
        tk.END, "11. Retire do forno e sirva quente.\n")
    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=20, height=2, bg="#ffff00")
    botao_favorito.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=20, height=2, bg="#1f77b4")
    botao_comentario.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(janela, text="Fechar", width=20,
                             height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.pack(side=tk.LEFT, padx=10, pady=10)

def janelaMigasVegetariano():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Receita")

    # Cria os rótulos
    titulo_receita = tk.Label(janela, text="Título da Receita")
    titulo_receita.pack()

    ingredientes = tk.Label(janela, text="Ingredientes:")
    ingredientes.pack()

    ingrediente_1 = tk.Label(janela, text="2 colheres de sopa de azeite")
    ingrediente_1.pack()

    ingrediente_2 = tk.Label(janela, text="1 cebola grande em cubos")
    ingrediente_2.pack()

    ingrediente_3 = tk.Label(janela, text="2 dentes de alho picados")
    ingrediente_3.pack()

    ingrediente_4 = tk.Label(janela, text="3 tomates maduros picados")
    ingrediente_4.pack()

    ingrediente_5 = tk.Label(janela, text="1 pimentão vermelho em cubos")
    ingrediente_5.pack()

    ingrediente_6 = tk.Label(janela, text="1/2 xícara de azeitonas verdes")
    ingrediente_6.pack()

    ingrediente_7 = tk.Label(janela, text="1 xícara de pão em cubos")
    ingrediente_7.pack()

    ingrediente_8 = tk.Label(janela, text="Sal e pimenta-do-reino a gosto")
    ingrediente_8.pack()

    ingrediente_9 = tk.Label(janela, text="1/4 xícara de salsinha picada")
    ingrediente_9.pack()

    instrucoes = tk.Label(janela, text="Instruções de Preparo:")
    instrucoes.pack()

    # Cria a área de texto para as instruções de preparo
    instrucoes_texto = tk.Text(janela)
    instrucoes_texto.pack()

    # Adiciona os dados da receita aos componentes
    titulo_receita["text"] = "Migas Vegetarianas"

    instrucoes_texto.insert(
        tk.END, "1. Aqueça o azeite em uma panela grande.\n")
    instrucoes_texto.insert(
        tk.END, "2. Adicione a cebola, o alho, os tomates e o pimentão. Refogue por 5 minutos.\n")
    instrucoes_texto.insert(
        tk.END, "3. Adicione as azeitonas, o pão e tempere com sal e pimenta.\n")
    instrucoes_texto.insert(
        tk.END, "4. Refogue por mais 10 minutos, mexendo ocasionalmente.\n")
    instrucoes_texto.insert(
        tk.END, "5. Desligue o fogo e misture a salsinha.\n")
    instrucoes_texto.insert(
        tk.END, "6. Sirva quente.\n")
    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=20, height=2, bg="#ffff00")
    botao_favorito.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=20, height=2, bg="#1f77b4")
    botao_comentario.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(janela, text="Fechar", width=20,
                             height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.pack(side=tk.LEFT, padx=10, pady=10)

def janelaOvosVegetarianos():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Receita")

    # Cria os rótulos
    titulo_receita = tk.Label(janela, text="Título da Receita")
    titulo_receita.pack()

    ingredientes = tk.Label(janela, text="Ingredientes:")
    ingredientes.pack()

    ingrediente_1 = tk.Label(janela, text="4 ovos cozidos")
    ingrediente_1.pack()

    ingrediente_2 = tk.Label(janela, text="1/3 xícara de queijo ralado")
    ingrediente_2.pack()

    ingrediente_3 = tk.Label(janela, text="2 colheres de sopa de salsa")
    ingrediente_3.pack()

    ingrediente_4 = tk.Label(janela, text="1/4 xícara de cebola picada")
    ingrediente_4.pack()

    ingrediente_5 = tk.Label(janela, text="1/4 xícara de cenoura picada")
    ingrediente_5.pack()

    ingrediente_6 = tk.Label(janela, text="1/4 xícara de milho verde")
    ingrediente_6.pack()

    ingrediente_7 = tk.Label(janela, text="Sal e pimenta-do-reino a gosto")
    ingrediente_7.pack()

    instrucoes = tk.Label(janela, text="Instruções de Preparo:")
    instrucoes.pack()

    # Cria a área de texto para as instruções de preparo
    instrucoes_texto = tk.Text(janela)
    instrucoes_texto.pack()

    # Adiciona os dados da receita aos componentes
    titulo_receita["text"] = "Ovos Recheados Vegetarianos"

    instrucoes_texto.insert(
        tk.END, "1. Corte um dos lados dos ovos cozidos para abrir.\n")
    instrucoes_texto.insert(
        tk.END, "2. Retire a gema dos ovos e coloque em uma tigela.\n")
    instrucoes_texto.insert(
        tk.END, "3. Misture a gema dos ovos com o queijo, a salsa, a cebola, a cenoura e o milho.\n")
    instrucoes_texto.insert(
        tk.END, "4. Tempere com sal e pimenta-do-reino a gosto.\n")
    instrucoes_texto.insert(
        tk.END, "5. Recheie os ovos com a mistura anterior.\n")
    instrucoes_texto.insert(
        tk.END, "6. Sirva os ovos recheados ainda quentes.\n")
    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=20, height=2, bg="#ffff00")
    botao_favorito.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=20, height=2, bg="#1f77b4")
    botao_comentario.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(janela, text="Fechar", width=20,
                             height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.pack(side=tk.LEFT, padx=10, pady=10)

def janelaSopaCenoura():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Receita")

    # Cria os rótulos
    titulo_receita = tk.Label(janela, text="Título da Receita")
    titulo_receita.pack()

    ingredientes = tk.Label(janela, text="Ingredientes:")
    ingredientes.pack()

    ingrediente_1 = tk.Label(janela, text="2 cebolas picadas")
    ingrediente_1.pack()

    ingrediente_2 = tk.Label(janela, text="5 cenouras raladas")
    ingrediente_2.pack()

    ingrediente_3 = tk.Label(janela, text="1 litro de água")
    ingrediente_3.pack()

    ingrediente_4 = tk.Label(janela, text="1/2 xícara de azeite")
    ingrediente_4.pack()

    ingrediente_5 = tk.Label(janela, text="Sal e pimenta-do-reino a gosto")
    ingrediente_5.pack()

    instrucoes = tk.Label(janela, text="Instruções de Preparo:")
    instrucoes.pack()

    # Cria a área de texto para as instruções de preparo
    instrucoes_texto = tk.Text(janela)
    instrucoes_texto.pack()

    # Adiciona os dados da receita aos componentes
    titulo_receita["text"] = "Sopa de Cenoura"

    instrucoes_texto.insert(
        tk.END, "1. Em uma panela, aqueça o azeite e doure a cebola.\n")
    instrucoes_texto.insert(
        tk.END, "2. Adicione a cenoura e refogue por 5 minutos.\n")
    instrucoes_texto.insert(
        tk.END, "3. Adicione a água e deixe ferver por 10 minutos.\n")
    instrucoes_texto.insert(
        tk.END, "4. Tempere com sal e pimenta-do-reino a gosto.\n")
    instrucoes_texto.insert(
        tk.END, "5. Bata no liquidificador até obter uma consistência homogênea.\n")
    instrucoes_texto.insert(
        tk.END, "6. Sirva quente.\n")
    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=20, height=2, bg="#ffff00")
    botao_favorito.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=20, height=2, bg="#1f77b4")
    botao_comentario.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(janela, text="Fechar", width=20,
                             height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.pack(side=tk.LEFT, padx=10, pady=10)

def janelaSopaPedra():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Receita")

    # Cria os rótulos
    titulo_receita = tk.Label(janela, text="Título da Receita")
    titulo_receita.pack()

    ingredientes = tk.Label(janela, text="Ingredientes:")
    ingredientes.pack()

    ingrediente_1 = tk.Label(janela, text="2 litros de água")
    ingrediente_1.pack()

    ingrediente_2 = tk.Label(janela, text="2 cebolas médias cortadas em cubos")
    ingrediente_2.pack()

    ingrediente_3 = tk.Label(janela, text="2 tomates grandes picados")
    ingrediente_3.pack()

    ingrediente_4 = tk.Label(janela, text="2 colheres de sopa de azeite")
    ingrediente_4.pack()

    ingrediente_5 = tk.Label(janela, text="2 dentes de alho picados")
    ingrediente_5.pack()

    ingrediente_6 = tk.Label(janela, text="Sal e pimenta-do-reino a gosto")
    ingrediente_6.pack()

    ingrediente_7 = tk.Label(janela, text="1 pedra de sal")
    ingrediente_7.pack()

    instrucoes = tk.Label(janela, text="Instruções de Preparo:")
    instrucoes.pack()

    # Cria a área de texto para as instruções de preparo
    instrucoes_texto = tk.Text(janela)
    instrucoes_texto.pack()

    # Adiciona os dados da receita aos componentes
    titulo_receita["text"] = "Sopa Pedra"

    instrucoes_texto.insert(
        tk.END, "1. Em uma panela grande, aqueça o azeite em fogo médio.\n")
    instrucoes_texto.insert(
        tk.END, "2. Acrescente a cebola, o alho e o tomate. Refogue por cerca de 5 minutos.\n")
    instrucoes_texto.insert(
        tk.END, "3. Despeje a água e coloque a pedra de sal.\n")
    instrucoes_texto.insert(
        tk.END, "4. Deixe cozinhar por cerca de 15 minutos.\n")
    instrucoes_texto.insert(
        tk.END, "5. Tempere com sal e pimenta-do-reino a gosto.\n")
    instrucoes_texto.insert(
        tk.END, "6. Desligue o fogo e sirva.\n")
    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=20, height=2, bg="#ffff00")
    botao_favorito.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=20, height=2, bg="#1f77b4")
    botao_comentario.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(janela, text="Fechar", width=20,
                             height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.pack(side=tk.LEFT, padx=10, pady=10)

def janelaSopaConquilha():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Receita")

    # Cria os rótulos
    titulo_receita = tk.Label(janela, text="Título da Receita")
    titulo_receita.pack()

    ingredientes = tk.Label(janela, text="Ingredientes:")
    ingredientes.pack()

    ingrediente_1 = tk.Label(janela, text="1 litro de água")
    ingrediente_1.pack()

    ingrediente_2 = tk.Label(janela, text="1/2 xícara de cebola em cubos")
    ingrediente_2.pack()

    ingrediente_3 = tk.Label(janela, text="1/4 xícara de azeite")
    ingrediente_3.pack()

    ingrediente_4 = tk.Label(janela, text="1/2 xícara de arroz integral")
    ingrediente_4.pack()

    ingrediente_5 = tk.Label(janela, text="1 xícara de conquilhas")
    ingrediente_5.pack()

    ingrediente_6 = tk.Label(janela, text="1/2 xícara de tomate em cubos")
    ingrediente_6.pack()

    ingrediente_7 = tk.Label(janela, text="Sal e pimenta-do-reino a gosto")
    ingrediente_7.pack()

    instrucoes = tk.Label(janela, text="Instruções de Preparo:")
    instrucoes.pack()

    # Cria a área de texto para as instruções de preparo
    instrucoes_texto = tk.Text(janela)
    instrucoes_texto.pack()

    # Adiciona os dados da receita aos componentes
    titulo_receita["text"] = "Sopa de Conquilha"

    instrucoes_texto.insert(
        tk.END, "1. Em uma panela, aqueça o azeite e refogue a cebola. \n")
    instrucoes_texto.insert(
        tk.END, "2. Adicione o arroz e deixe por alguns minutos para refogar. \n")
    instrucoes_texto.insert(
        tk.END, "3. Adicione a água, o tomate e as conquilhas. \n")
    instrucoes_texto.insert(
        tk.END, "4. Tempere com sal e pimenta do reino a gosto. \n")
    instrucoes_texto.insert(
        tk.END, "5. Deixe a sopa cozinhar até que as conquilhas estejam prontas. \n")
    instrucoes_texto.insert(
        tk.END, "6. Sirva a sopa ainda quente. \n")
    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=20, height=2, bg="#ffff00")
    botao_favorito.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=20, height=2, bg="#1f77b4")
    botao_comentario.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(janela, text="Fechar", width=20,
                             height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.pack(side=tk.LEFT, padx=10, pady=10)

def janelaSopaPeixe():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Receita")

    # Cria os rótulos
    titulo_receita = tk.Label(janela, text="Título da Receita")
    titulo_receita.pack()

    ingredientes = tk.Label(janela, text="Ingredientes:")
    ingredientes.pack()

    ingrediente_1 = tk.Label(janela, text="1 cebola picada")
    ingrediente_1.pack()

    ingrediente_2 = tk.Label(janela, text="2 dentes de alho picados")
    ingrediente_2.pack()

    ingrediente_3 = tk.Label(janela, text="1/2 xícara de azeite")
    ingrediente_3.pack()

    ingrediente_4 = tk.Label(janela, text="2 tomates maduros cortados em cubos")
    ingrediente_4.pack()

    ingrediente_5 = tk.Label(janela, text="2 xícaras de água")
    ingrediente_5.pack()

    ingrediente_6 = tk.Label(janela, text="1/2 xícara de vinho branco")
    ingrediente_6.pack()

    ingrediente_7 = tk.Label(janela, text="1/2 colher de chá de pimenta-do-reino")
    ingrediente_7.pack()

    ingrediente_8 = tk.Label(janela, text="1/4 colher de chá de sal")
    ingrediente_8.pack()

    ingrediente_9 = tk.Label(janela, text="1/4 xícara de azeitonas pretas picadas")
    ingrediente_9.pack()

    ingrediente_10 = tk.Label(janela, text="400 g de filé de peixe")
    ingrediente_10.pack()

    ingrediente_11 = tk.Label(janela, text="1 xícara de salsinha picada")
    ingrediente_11.pack()

    instrucoes = tk.Label(janela, text="Instruções de Preparo:")
    instrucoes.pack()

    # Cria a área de texto para as instruções de preparo
    instrucoes_texto = tk.Text(janela)
    instrucoes_texto.pack()

    # Adiciona os dados da receita aos componentes
    titulo_receita["text"] = "Sopa de Peixe"

    instrucoes_texto.insert(tk.END, "1. Em uma panela, aqueça o azeite e refogue a cebola e o alho por 2 minutos.\n")
    instrucoes_texto.insert(tk.END, "2. Acrescente os tomates, a água, o vinho, a pimenta-do-reino, o sal e as azeitonas. Misture bem.\n")
    instrucoes_texto.insert(tk.END, "3. Deixe ferver por 10 minutos.\n")
    instrucoes_texto.insert(tk.END, "4. Adicione o peixe e deixe cozinhar por mais 5 minutos.\n")
    instrucoes_texto.insert(tk.END, "5. Desligue o fogo e adicione a salsinha.\n")
    instrucoes_texto.insert(tk.END, "6. Sirva a sopa quente.\n")
    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=20, height=2, bg="#ffff00")
    botao_favorito.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=20, height=2, bg="#1f77b4")
    botao_comentario.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(janela, text="Fechar", width=20,
                             height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.pack(side=tk.LEFT, padx=10, pady=10)

def janelaSopaJuliana():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Receita")

    # Cria os rótulos
    titulo_receita = tk.Label(janela, text="Título da Receita")
    titulo_receita.pack()

    ingredientes = tk.Label(janela, text="Ingredientes:")
    ingredientes.pack()

    ingrediente_1 = tk.Label(janela, text="2 xícaras de arroz arbóreo")
    ingrediente_1.pack()

    ingrediente_2 = tk.Label(janela, text="1 cebola média")
    ingrediente_2.pack()

    ingrediente_3 = tk.Label(janela, text="2 dentes de alho")
    ingrediente_3.pack()

    ingrediente_4 = tk.Label(janela, text="2 colheres de sopa de manteiga")
    ingrediente_4.pack()

    ingrediente_5 = tk.Label(janela, text="1 litro de água")
    ingrediente_5.pack()
 
    ingrediente_6 = tk.Label(janela, text="2 folhas de louro")
    ingrediente_6.pack()

    ingrediente_7 = tk.Label(janela, text="1 colher de sopa de colorau")
    ingrediente_7.pack()

    ingrediente_8 = tk.Label(janela, text="Sal a gosto")
    ingrediente_8.pack()

    instrucoes = tk.Label(janela, text="Instruções de Preparo:")
    instrucoes.pack()

    # Cria a área de texto para as instruções de preparo
    instrucoes_texto = tk.Text(janela)
    instrucoes_texto.pack()

    # Adiciona os dados da receita aos componentes
    titulo_receita["text"] = "Sopa Juliana"

    instrucoes_texto.insert(
        tk.END, "1. Pique a cebola e o alho e refogue com a manteiga em uma panela grande.\n")
    instrucoes_texto.insert(
        tk.END, "2. Acrescente o arroz e refogue por alguns minutos.\n")
    instrucoes_texto.insert(
        tk.END, "3. Coloque a água, o louro, o colorau e sal a gosto.\n")
    instrucoes_texto.insert(
        tk.END, "4. Deixe ferver por 15 minutos, mexendo sempre.\n")
    instrucoes_texto.insert(
        tk.END, "5. Desligue o fogo e sirva a sopa quente.\n")
    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=20, height=2, bg="#ffff00")
    botao_favorito.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=20, height=2, bg="#1f77b4")
    botao_comentario.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(janela, text="Fechar", width=20,
                             height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.pack(side=tk.LEFT, padx=10, pady=10)

def janelaSopaCaldoVerde():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Receita")

    # Cria os rótulos
    titulo_receita = tk.Label(janela, text="Título da Receita")
    titulo_receita.pack()

    ingredientes = tk.Label(janela, text="Ingredientes:")
    ingredientes.pack()

    ingrediente_1 = tk.Label(janela, text="1 cebola grande picada")
    ingrediente_1.pack()

    ingrediente_2 = tk.Label(janela, text="2 dentes de alho picados")
    ingrediente_2.pack()

    ingrediente_3 = tk.Label(janela, text="200g de batatas cortadas em cubos")
    ingrediente_3.pack()

    ingrediente_4 = tk.Label(janela, text="200g de couve portuguesa picada")
    ingrediente_4.pack()

    ingrediente_5 = tk.Label(janela, text="1 lata de caldo de legumes")
    ingrediente_5.pack()

    ingrediente_4 = tk.Label(janela, text="Azeite")
    ingrediente_4.pack()

    ingrediente_5 = tk.Label(janela, text="Sal e pimenta-do-reino a gosto")
    ingrediente_5.pack()

    instrucoes = tk.Label(janela, text="Instruções de Preparo:")
    instrucoes.pack()

    # Cria a área de texto para as instruções de preparo
    instrucoes_texto = tk.Text(janela)
    instrucoes_texto.pack()

    # Adiciona os dados da receita aos componentes
    titulo_receita["text"] = "Sopa Caldo Verde"

    instrucoes_texto.insert(
        tk.END, "1. Em uma panela, aqueça o azeite e refogue a cebola e o alho por 2 minutos.\n")
    instrucoes_texto.insert(
        tk.END, "2. Adicione as batatas e refogue por mais 5 minutos.\n")
    instrucoes_texto.insert(
        tk.END, "3. Junte o caldo de legumes e a couve e deixe ferver.\n")
    instrucoes_texto.insert(
        tk.END, "4. Abaixe o fogo e cozinhe por 15 minutos.\n")
    instrucoes_texto.insert(
        tk.END, "5. Tempere com sal e pimenta-do-reino a gosto.\n")
    instrucoes_texto.insert(
        tk.END, "6. Sirva a sopa quente.\n")
    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=20, height=2, bg="#ffff00")
    botao_favorito.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=20, height=2, bg="#1f77b4")
    botao_comentario.pack(side=tk.LEFT, padx=10, pady=10)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(janela, text="Fechar", width=20,
                             height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.pack(side=tk.LEFT, padx=10, pady=10)

# endregion

def janelaCriarReceita():
    global entry_title, entry_ingredients, entry_instructions, entry_photo, window
    # Create the main window
    janelaReceita = tk.Tk()
    janelaReceita.title("Criar Receita")

    x=600
    y=400

    # Get the screen width and height
    ws = janelaReceita.winfo_screenwidth() # width of the screen
    hs = janelaReceita.winfo_screenheight() # height of the screen

    #Centrar
    janelaReceita.geometry('%dx%d+%d+%d' % (x, y, (ws/2)-(x/2), (hs/2)-(y/2)))

    # Label e entry titulo
    lblTitulo=Label(janelaReceita, text="Título:")
    lblTitulo.place(x=10, y=10)

    entTitulo = Entry(janelaReceita, width=30)
    entTitulo.place(x=60, y=10)

    # Label e textarea ingredientes
    lblIngredientes=Label(janelaReceita, text="Ingredientes:")
    lblIngredientes.place(x=10, y=80)
    
    txtIngredientes = Text(janelaReceita, width=30, height=5)
    txtIngredientes.place(x=80, y=80)

    # Label e textarea instruções
    lblInstrucoes=Label(janelaReceita, text="Instruções:")
    lblInstrucoes.place(x=10, y=200)

    txtInstrucoes = Text(janelaReceita, width=30, height=5)
    txtInstrucoes.place(x=80, y=200)

    # Label e entry foto
    lblFoto=Label(janelaReceita, text="Foto:")
    lblFoto.place(x=10, y=300)

    imagem=StringVar()
    entFoto = Entry(janelaReceita, width=30,textvariable=imagem)
    entFoto.place(x=80, y=300)

    # Botão para Guardar a direita
    btnGuardar = Button(janelaReceita, text="Guardar", width=20,height=7, command=lambda:guardarFicheiro(entTitulo.get(), txtIngredientes.get("1.0",END), txtInstrucoes.get("1.0",END), entFoto.get()))
    btnGuardar.place(x=400, y=10)
    # Botão para adicionar foto

    
    btnFoto = Button(janelaReceita, text="Adicionar Foto", width=10, command=lambda:adicionarFoto(imagem))
    btnFoto.place(x=400, y=150)

    # Botão para Fechar a direita
    btnFechar = Button(janelaReceita, text="Fechar", width=10, command=janelaReceita.destroy)
    btnFechar.place(x=500, y=300)

def guardarFicheiro(entTitulo, txtIngredientes, txtInstrucoes, entFoto):
    # Get the values from the entry boxes
    

    fReceitas=open("./ficheiros/receitas.txt", "a",encoding="utf-8")
    fReceitas.write(entTitulo + ";" + txtIngredientes + ";" + txtInstrucoes + ";" + entFoto + "\n")
    fReceitas.close()
    window.destroy()

def adicionarFoto(imagem):
    #abrir um filelog para selecionar a foto
    file=filedialog.askopenfilename(initialdir = "./img/categorias",title = "Select file",filetypes = (("png files","*.png"),("gif files","*.gif"),("all files","*.*")))
    imagem.set(file)

    
