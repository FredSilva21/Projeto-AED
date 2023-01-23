from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkVideoPlayer import TkinterVideo 
from tkinter import filedialog
from PIL import ImageTk, Image
import os

#region JANELAS RECEITAS
def janelaPao(cat,entUtilizador):
   #CREATE A WINDOW
    janela = tk.Tk()
    w = 800
    h = 700
    ws = janela.winfo_screenwidth()
    hs = janela.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janela.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #SET THE TITLE OF THE WINDOW
    janela.title("Pão Recheado")
    
    #dont let the window resize
    janela.resizable(0,0)
    titulo_receita = "Pão Recheado"
    #ADD A TEXT BOX TO THE WINDOW
    text_box_ingredientes = tk.Text(janela, width=50, height=12)
    text_box_ingredientes.place(x=190, y=50)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_ingredientes.insert(tk.END,titulo_receita + "\n\nIngredientes:\n\n1 pão de forma\n1/2 xícara de queijo ralado\n1/2 xícara de presunto fatiado")
    text_box_ingredientes.tag_configure("center", justify='center')
    text_box_ingredientes.tag_add("center", 1.0, "end")
    text_box_ingredientes.config(state=DISABLED)


    #ADD A TEXT BOX TO THE WINDOW
    text_box_intruçoes = tk.Text(janela, width=50, height=20)
    text_box_intruçoes.place(x=190, y=220)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_intruçoes.insert(tk.END, "Instruções:\n\n1. Pré-aqueça o forno a 180°C.\n2. Corte o pão de forma ao meio, formando dois discos.\n3. Coloque o presunto e o queijo na parte inferior do pão.\n4. Coloque a parte superior do pão e pressione as bordas para fechá-lo.\n5. Coloque o pão numa assadeira untada com azeite.\n6. Leve ao forno por cerca de 15 minutos.\n7. Sirva quente.")
    text_box_intruçoes.tag_configure("center", justify='center')
    text_box_intruçoes.tag_add("center", 1.0, "end")
    text_box_intruçoes.config(state=DISABLED)

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=17, height=2, bg="#ffff00", command=lambda:marcarFavorito(cat,titulo_receita,entUtilizador))
    botao_favorito.place(x=190, y=550)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=17, height=2, bg="#1f77b4", command=lambda:comentar(titulo_receita,entUtilizador))
    botao_comentario.place(x=330,y=550)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(
        janela, text="Fechar", width=17, height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.place(x=470, y=550)

def janelaQuiche(cat,entUtilizador):
   #CREATE A WINDOW
    janela = tk.Tk()
    w = 800
    h = 700
    ws = janela.winfo_screenwidth()
    hs = janela.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janela.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #SET THE TITLE OF THE WINDOW
    janela.title("Quiche")

    #dont let the window resize
    janela.resizable(0,0)
    titulo_receita = "Quiche"
    #ADD A TEXT BOX TO THE WINDOW
    text_box_ingredientes = tk.Text(janela, width=50, height=12)
    text_box_ingredientes.place(x=190, y=50)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_ingredientes.insert(tk.END,titulo_receita + "\n\nIngredientes:\n\n2 xícaras de farinha\n1/2 xícara de manteiga\n1/4 xícara de água fria\n1/4 de colher de sal\n3 ovos\n3/4 xícara de leite\n1/2 xícara de creme de leite\n2 xícaras de queijo cheddar ralado\n1/4 de xícara de cebola picada\n1/4 de xícara de bacon cozido e picado")
    text_box_ingredientes.tag_configure("center", justify='center')
    text_box_ingredientes.tag_add("center", 1.0, "end")
    text_box_ingredientes.config(state=DISABLED)

    #ADD A TEXT BOX TO THE WINDOW
    text_box_intruçoes = tk.Text(janela, width=50, height=20)
    text_box_intruçoes.place(x=190, y=220)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_intruçoes.insert(tk.END, "Instruções:\n\n1. Pré-aqueça o forno a 375 graus\n2. Misture a farinha, sal e manteiga\n3. Adicione água fria até que a mistura fique homogênea\n4. Abra a massa e coloque-a em um pirex de 9 polegadas\n5. Aqueça o bacon e a cebola por 3 minutos\n6. Misture o ovo, o leite, o creme de leite, o queijo, o bacon e a cebola\n7. Despeje a mistura no pirex\n8. Asse por 40 minutos ou até que esteja dourado")
    text_box_intruçoes.tag_configure("center", justify='center')
    text_box_intruçoes.tag_add("center", 1.0, "end")
    text_box_intruçoes.config(state=DISABLED)

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=17, height=2, bg="#ffff00", command=lambda:marcarFavorito(cat,titulo_receita,entUtilizador))
    botao_favorito.place(x=190, y=550)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=17, height=2, bg="#1f77b4", command=lambda:comentar(titulo_receita,entUtilizador))
    botao_comentario.place(x=330,y=550)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(
        janela, text="Fechar", width=17, height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.place(x=470, y=550)
    
def janelaPizza(cat,entUtilizador):
   #CREATE A WINDOW
    janela = tk.Tk()
    w = 800
    h = 700
    ws = janela.winfo_screenwidth()
    hs = janela.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janela.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #SET THE TITLE OF THE WINDOW
    janela.title("Mini Pizzas")

    #dont let the window resize
    janela.resizable(0,0)
    titulo_receita = "Mini Pizzas"
    #ADD A TEXT BOX TO THE WINDOW
    text_box_ingredientes = tk.Text(janela, width=50, height=12)
    text_box_ingredientes.place(x=190, y=50)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_ingredientes.insert(tk.END,titulo_receita + "\n\nIngredientes:\n\n1/2 xícara de leite morno\n1/2 xícara de água morna\n2 colheres de sopa de açúcar\n2 colheres de sopa de óleo\n1 colher de chá de sal\n3 xícaras de farinha de trigo\n1 colher de sopa de fermento em pó\n1/2 xícara de molho de tomate\n1/2 xícara de queijo ralado\n1/4 xícara de cebola picada\n1/4 xícara de azeitonas verdes picadas")
    text_box_ingredientes.tag_configure("center", justify='center')
    text_box_ingredientes.tag_add("center", 1.0, "end")
    text_box_ingredientes.config(state=DISABLED)

    #ADD A TEXT BOX TO THE WINDOW
    text_box_intruçoes = tk.Text(janela, width=50, height=20)
    text_box_intruçoes.place(x=190, y=220)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_intruçoes.insert(tk.END, "Instruções:\n\n1. Pré-aqueça o forno a 350 graus\n2. Misture o leite, a água, o açúcar, o óleo e o sal\n3. Adicione a farinha e o fermento e misture\n4. Abra a massa e corte em discos\n5. Coloque os discos em assadeiras de 12 polegadas\n6. Cubra com molho, queijo, cebola e azeitonas\n7. Asse por 20 minutos ou até que esteja levemente dourado")
    text_box_intruçoes.tag_configure("center", justify='center')
    text_box_intruçoes.tag_add("center", 1.0, "end")
    text_box_intruçoes.config(state=DISABLED)

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=17, height=2, bg="#ffff00", command=lambda:marcarFavorito(cat,titulo_receita,entUtilizador))
    botao_favorito.place(x=190, y=550)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=17, height=2, bg="#1f77b4", command=lambda:comentar(titulo_receita,entUtilizador))
    botao_comentario.place(x=330,y=550)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(
        janela, text="Fechar", width=17, height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.place(x=470, y=550)

def janelaSupremo(cat,entUtilizador):
   #CREATE A WINDOW
    janela = tk.Tk()
    w = 800
    h = 700
    ws = janela.winfo_screenwidth()
    hs = janela.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janela.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #SET THE TITLE OF THE WINDOW
    janela.title("Suprême de Camembert")

    #dont let the window resize
    janela.resizable(0,0)
    titulo_receita = "Suprême de Camembert"
    #ADD A TEXT BOX TO THE WINDOW
    text_box_ingredientes = tk.Text(janela, width=50, height=12)
    text_box_ingredientes.place(x=190, y=50)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_ingredientes.insert(tk.END,titulo_receita + "\n\nIngredientes:\n\n1 embalagem de massa folhada\n2 ovos\n2 colheres de sopa de creme de leite\n200 gramas de camembert\n2 colheres de sopa de manteiga\n1/2 xícara de leite\n1/2 xícara de cebola picada\n1/2 xícara de bacon picado")
    text_box_ingredientes.tag_configure("center", justify='center')
    text_box_ingredientes.tag_add("center", 1.0, "end")
    text_box_ingredientes.config(state=DISABLED)

    #ADD A TEXT BOX TO THE WINDOW
    text_box_intruçoes = tk.Text(janela, width=50, height=20)
    text_box_intruçoes.place(x=190, y=220)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_intruçoes.insert(tk.END, "Instruções:\n\n1. Pré-aqueça o forno a 375 graus\n2. Desembrulhe a massa folhada e coloque-a em uma assadeira\n3. Cubra com o camembert e as cebolas\n4. Misture os ovos, o leite, o creme de leite e o bacon\n5. Despeje sobre o camembert\n6. Coloque os pedaços de manteiga por cima\n7. Asse por 30 minutos ou até que esteja dourado")
    text_box_intruçoes.tag_configure("center", justify='center')
    text_box_intruçoes.tag_add("center", 1.0, "end")
    text_box_intruçoes.config(state=DISABLED)

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=17, height=2, bg="#ffff00", command=lambda:marcarFavorito(cat,titulo_receita,entUtilizador))
    botao_favorito.place(x=190, y=550)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=17, height=2, bg="#1f77b4", command=lambda:comentar(titulo_receita,entUtilizador))
    botao_comentario.place(x=330,y=550)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(
        janela, text="Fechar", width=17, height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.place(x=470, y=550)

def janelaRissois(cat,entUtilizador):
    #CREATE A WINDOW
    janela = tk.Tk()
    w = 800
    h = 700
    ws = janela.winfo_screenwidth()
    hs = janela.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janela.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #SET THE TITLE OF THE WINDOW
    janela.title("Rissois")

    #dont let the window resize
    janela.resizable(0,0)
    titulo_receita = "Rissois"
    #ADD A TEXT BOX TO THE WINDOW
    text_box_ingredientes = tk.Text(janela, width=50, height=12)
    text_box_ingredientes.place(x=190, y=50)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_ingredientes.insert(tk.END,titulo_receita + "\n\nIngredientes:\n\n250 g de massa de pastelaria\n250 g de carne de frango\n1 cebola\n1 dente de alho\n1 colher (sopa) de azeite\nSal e pimenta a gosto\n1 colher (chá) de mostarda\n1/2 limão\n1 colher (sopa) de salsa picada\n1/2 colher (sopa) de vinho branco\n100 g de presunto\n100 g de queijo ralado\nÓleo para fritar")
    text_box_ingredientes.tag_configure("center", justify='center')
    text_box_ingredientes.tag_add("center", 1.0, "end")
    text_box_ingredientes.config(state=DISABLED)

    #ADD A TEXT BOX TO THE WINDOW
    text_box_intruçoes = tk.Text(janela, width=50, height=20)
    text_box_intruçoes.place(x=190, y=220)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_intruçoes.insert(tk.END, "Instruções:\n\n1. Desfie o frango e tempere-o com sal, pimenta, mostarda, limão, salsa e vinho branco.\n2. Corte o presunto em cubinhos e adicione-os à mistura.\n3. Corte a cebola e o alho em pedaços pequenos e refogue-os no azeite.\n4. Junte o frango desfiado à cebola e alho e deixe cozinhar por alguns minutos.\n5. Aqueça o óleo para fritar.\n6. Corte a massa de pastelaria em discos.\n7. Coloque os discos de massa num tabuleiro e coloque um pouco de recheio no centro de cada disco.\n8. Cubra com outro disco de massa e aperte bem as bordas com um garfo para fechar.\n9. Frite os rissois em óleo quente até que fiquem dourados.\n10. Escorra em papel absorvente e sirva com o queijo ralado.")
    text_box_intruçoes.tag_configure("center", justify='center')
    text_box_intruçoes.tag_add("center", 1.0, "end")
    text_box_intruçoes.config(state=DISABLED)

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=17, height=2, bg="#ffff00", command=lambda:marcarFavorito(cat,titulo_receita,entUtilizador))
    botao_favorito.place(x=190, y=550)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=17, height=2, bg="#1f77b4", command=lambda:comentar(titulo_receita,entUtilizador))
    botao_comentario.place(x=330,y=550)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(
        janela, text="Fechar", width=17, height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.place(x=470, y=550)

def janelaTapas(cat,entUtilizador):
   #CREATE A WINDOW
    janela = tk.Tk()
    w = 800
    h = 700
    ws = janela.winfo_screenwidth()
    hs = janela.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janela.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #SET THE TITLE OF THE WINDOW
    janela.title("Tapas")

    #dont let the window resize
    janela.resizable(0,0)
    titulo_receita = "Tapas"
    #ADD A TEXT BOX TO THE WINDOW
    text_box_ingredientes = tk.Text(janela, width=50, height=12)
    text_box_ingredientes.place(x=190, y=50)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_ingredientes.insert(tk.END,titulo_receita + "\n\nIngredientes:\n\n1/2 xícara de azeite de oliva\n1/4 de xícara de limão\n1 cebola picada\n2 dentes de alho picados\n1/4 de xícara de pimentão vermelho picado\n2 tomates maduros picados\n1 colher de chá de orégano\n1/4 de colher de chá de alho em pó\n1/4 de colher de chá de sal\n1/8 de colher de chá de pimenta preta")
    text_box_ingredientes.tag_configure("center", justify='center')
    text_box_ingredientes.tag_add("center", 1.0, "end")
    text_box_ingredientes.config(state=DISABLED)

    #ADD A TEXT BOX TO THE WINDOW
    text_box_intruçoes = tk.Text(janela, width=50, height=20)
    text_box_intruçoes.place(x=190, y=220)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_intruçoes.insert(tk.END, "Instruções:\n\n1. Aqueça o azeite em uma panela média\n2. Adicione a cebola, alho e pimentão e cozinhe por 5 minutos\n3. Adicione os tomates, orégano, alho em pó, sal e pimenta e cozinhe por mais 3 minutos\n4. Retire do fogo e adicione o suco de limão\n5. Despeje em tigelinhas individuais\n6. Sirva quente ou à temperatura ambiente")
    text_box_intruçoes.tag_configure("center", justify='center')
    text_box_intruçoes.tag_add("center", 1.0, "end")
    text_box_intruçoes.config(state=DISABLED)

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=17, height=2, bg="#ffff00", command=lambda:marcarFavorito(cat,titulo_receita,entUtilizador))
    botao_favorito.place(x=190, y=550)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=17, height=2, bg="#1f77b4", command=lambda:comentar(titulo_receita,entUtilizador))
    botao_comentario.place(x=330,y=550)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(
        janela, text="Fechar", width=17, height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.place(x=470, y=550)

def janelaFrancesinha(cat,entUtilizador):
    #CREATE A WINDOW
    janela = tk.Tk()
    w = 800
    h = 700
    ws = janela.winfo_screenwidth()
    hs = janela.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janela.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #SET THE TITLE OF THE WINDOW
    janela.title("Francesinha")

    #dont let the window resize
    janela.resizable(0,0)
    titulo_receita = "Francesinha"
    #ADD A TEXT BOX TO THE WINDOW
    text_box_ingredientes = tk.Text(janela, width=50, height=12)
    text_box_ingredientes.place(x=190, y=50)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_ingredientes.insert(tk.END,titulo_receita + "\n\nIngredientes:\n\n1/2 xícara de manteiga\n2 colheres de sopa de farinha\n2 xícaras de leite\n1/2 colher de chá de sal\n1/4 colher de chá de noz-moscada\n2 xícaras de carne moída\n1 xícara de queijo cheddar ralado\n1/4 xícara de cebola picada\n1/4 xícara de tomate picado\n1/4 xícara de presunto picado\n1/4 xícara de azeitona picada")
    text_box_ingredientes.tag_configure("center", justify='center')
    text_box_ingredientes.tag_add("center", 1.0, "end")
    text_box_ingredientes.config(state=DISABLED)

    #ADD A TEXT BOX TO THE WINDOW
    text_box_intruçoes = tk.Text(janela, width=50, height=20)
    text_box_intruçoes.place(x=190, y=220)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_intruçoes.insert(tk.END, "Instruções:\n\n1. Pré-aqueça o forno a 375 graus\n2. Derreta a manteiga em uma panela\n3. Adicione a farinha e mexa por 2 minutos\n4. Adicione o leite e mexa até engrossar\n5. Tempere com sal e noz-moscada\n6. Em uma tigela, misture a carne, o queijo, a cebola, o tomate, o presunto e a azeitona\n7. Coloque a mistura em um pirex de 9 polegadas\n8. Cubra com a mistura de manteiga\n9. Asse por 40 minutos ou até que esteja dourado")
    text_box_intruçoes.tag_configure("center", justify='center')
    text_box_intruçoes.tag_add("center", 1.0, "end")
    text_box_intruçoes.config(state=DISABLED)

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=17, height=2, bg="#ffff00", command=lambda:marcarFavorito(cat,titulo_receita,entUtilizador))
    botao_favorito.place(x=190, y=550)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=17, height=2, bg="#1f77b4", command=lambda:comentar(titulo_receita,entUtilizador))
    botao_comentario.place(x=330,y=550)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(
        janela, text="Fechar", width=17, height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.place(x=470, y=550)

def janelaBifesPeru(cat,entUtilizador):
   #CREATE A WINDOW
    janela = tk.Tk()
    w = 800
    h = 700
    ws = janela.winfo_screenwidth()
    hs = janela.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janela.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #SET THE TITLE OF THE WINDOW
    janela.title("Bife de Peru")

    #dont let the window resize
    janela.resizable(0,0)
    titulo_receita = "Bife de Peru"
    #ADD A TEXT BOX TO THE WINDOW
    text_box_ingredientes = tk.Text(janela, width=50, height=12)
    text_box_ingredientes.place(x=190, y=50)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_ingredientes.insert(tk.END,titulo_receita + "\n\nIngredientes:\n\n2 bifes de peru\n1/4 xícara de vinagre de maçã\n1 colher de sopa de azeite\n1 colher de sopa de mel\n1 colher de chá de mostarda\n1/2 colher de chá de sal\n1/4 colher de chá de pimenta\n1/4 xícara de cebola finamente picada\n1 dente de alho picado")
    text_box_ingredientes.tag_configure("center", justify='center')
    text_box_ingredientes.tag_add("center", 1.0, "end")
    text_box_ingredientes.config(state=DISABLED)

    #ADD A TEXT BOX TO THE WINDOW
    text_box_intruçoes = tk.Text(janela, width=50, height=20)
    text_box_intruçoes.place(x=190, y=220)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_intruçoes.insert(tk.END, "Instruções:\n\n1. Coloque os bifes de peru em uma tigela\n2. Misture o vinagre de maçã, o azeite, o mel, a mostarda, o sal e a pimenta\n3. Coloque a mistura sobre os bifes\n4. Adicione a cebola e o alho a mistura\n5. Deixe marinar por 20 minutos\n6. Pré-aqueça uma frigideira em fogo médio-alto\n7. Coloque os bifes na frigideira e deixe-os dourar dos dois lados\n8. Cozinhe os bifes por 10 minutos ou até que estejam cozidos")
    text_box_intruçoes.tag_configure("center", justify='center')
    text_box_intruçoes.tag_add("center", 1.0, "end")
    text_box_intruçoes.config(state=DISABLED)

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=17, height=2, bg="#ffff00", command=lambda:marcarFavorito(cat,titulo_receita,entUtilizador))
    botao_favorito.place(x=190, y=550)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=17, height=2, bg="#1f77b4", command=lambda:comentar(titulo_receita,entUtilizador))
    botao_comentario.place(x=330,y=550)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(
        janela, text="Fechar", width=17, height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.place(x=470, y=550)

def janelaPicanha(cat,entUtilizador):
   #CREATE A WINDOW
    janela = tk.Tk()
    w = 800
    h = 700
    ws = janela.winfo_screenwidth()
    hs = janela.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janela.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #SET THE TITLE OF THE WINDOW
    janela.title("Picanha")

    #dont let the window resize
    janela.resizable(0,0)
    titulo_receita = "Picanha"
    #ADD A TEXT BOX TO THE WINDOW
    text_box_ingredientes = tk.Text(janela, width=50, height=12)
    text_box_ingredientes.place(x=190, y=50)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_ingredientes.insert(tk.END,titulo_receita + "\n\nIngredientes:\n\n1 picanha\nSal grosso\nAzeite\nAlho\nPimenta-do-reino\nLimão")
    text_box_ingredientes.tag_configure("center", justify='center')
    text_box_ingredientes.tag_add("center", 1.0, "end")
    text_box_ingredientes.config(state=DISABLED)

    #ADD A TEXT BOX TO THE WINDOW
    text_box_intruçoes = tk.Text(janela, width=50, height=20)
    text_box_intruçoes.place(x=190, y=220)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_intruçoes.insert(tk.END, "Instruções:\n\n1. Lave a picanha com água e seque-a bem\n2. Coloque a picanha em uma assadeira e tempere com sal grosso, alho, pimenta-do-reino, azeite e limão\n3. Leve a assadeira ao forno pré-aquecido a 220ºC\n4. Deixe assar por aproximadamente 45 minutos ou até que o líquido se evapore\n5. Sirva a carne ainda quente")
    text_box_intruçoes.tag_configure("center", justify='center')
    text_box_intruçoes.tag_add("center", 1.0, "end")
    text_box_intruçoes.config(state=DISABLED)

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=17, height=2, bg="#ffff00", command=lambda:marcarFavorito(cat,titulo_receita,entUtilizador))
    botao_favorito.place(x=190, y=550)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=17, height=2, bg="#1f77b4", command=lambda:comentar(titulo_receita,entUtilizador))
    botao_comentario.place(x=330,y=550)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(
        janela, text="Fechar", width=17, height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.place(x=470, y=550)

def janelaCaril(cat,entUtilizador):
   #CREATE A WINDOW
    janela = tk.Tk()
    w = 800
    h = 700
    ws = janela.winfo_screenwidth()
    hs = janela.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janela.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #SET THE TITLE OF THE WINDOW
    janela.title("Frango Caril")

    #dont let the window resize
    janela.resizable(0,0)
    titulo_receita = "Frango Caril"
    #ADD A TEXT BOX TO THE WINDOW
    text_box_ingredientes = tk.Text(janela, width=50, height=12)
    text_box_ingredientes.place(x=190, y=50)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_ingredientes.insert(tk.END,titulo_receita + "\n\nIngredientes:\n\n4 filés de frango\n1/4 xícara de azeite\n1 cebola picada\n2 dentes de alho picados\n1 xícara de tomate pelado\n2 xícaras de caldo de galinha\n1/2 xícara de leite de coco\n1 colher de chá de caril em pó\n1 colher de chá de gengibre em pó\n1 colher de chá de cominhos em pó\n1/2 colher de chá de pimenta caiena\n1/4 xícara de salsinha picada")
    text_box_ingredientes.tag_configure("center", justify='center')
    text_box_ingredientes.tag_add("center", 1.0, "end")
    text_box_ingredientes.config(state=DISABLED)

    #ADD A TEXT BOX TO THE WINDOW
    text_box_intruçoes = tk.Text(janela, width=50, height=20)
    text_box_intruçoes.place(x=190, y=220)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_intruçoes.insert(tk.END, "Instruções:\n\n1. Aqueça o azeite em uma panela grande\n2. Junte a cebola e o alho e refogue por 3 minutos\n3. Adicione o tomate, o caldo de galinha, o leite de coco, o caril, o gengibre, os cominhos e a pimenta caiena\n4. Misture bem e deixe ferver por 5 minutos\n5. Adicione o frango e cozinhe por 15 minutos ou até que o frango esteja cozido\n6. Sirva em seguida com salsinha picada")
    text_box_intruçoes.tag_configure("center", justify='center')
    text_box_intruçoes.tag_add("center", 1.0, "end")
    text_box_intruçoes.config(state=DISABLED)

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=17, height=2, bg="#ffff00", command=lambda:marcarFavorito(cat,titulo_receita,entUtilizador))
    botao_favorito.place(x=190, y=550)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=17, height=2, bg="#1f77b4", command=lambda:comentar(titulo_receita,entUtilizador))
    botao_comentario.place(x=330,y=550)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(
        janela, text="Fechar", width=17, height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.place(x=470, y=550)

def janelaFrango(cat,entUtilizador):
   #CRIAR UMA JANELA
    janela = tk.Tk()
    w = 800
    h = 700
    ws = janela.winfo_screenwidth()
    hs = janela.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janela.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #DEFINIR O TÍTULO DA JANELA
    janela.title("Frango")

    #não permitir que a janela seja redimensionada
    janela.resizable(0,0)
    titulo_receita = "Frango"
    #ADICIONAR UMA CAIXA DE TEXTO À JANELA
    text_box_ingredientes = tk.Text(janela, width=50, height=12)
    text_box_ingredientes.place(x=190, y=50)
    #ADICIONAR TEXTO À CAIXA DE TEXTO CENTRALIZADO
    text_box_ingredientes.insert(tk.END,titulo_receita + "\n\nIngredientes:\n\n1 xícara de farinha\n1/2 xícara de manteiga\n3/4 xícara de água fria\n1/2 colher de sal\n2 ovos\n1/2 xícara de leite\n1/2 xícara de creme de leite\n2 xícaras de queijo cheddar ralado\n1/2 xícara de cebola picada\n1/2 xícara de bacon cozido e picado")
    text_box_ingredientes.tag_configure("center", justify='center')
    text_box_ingredientes.tag_add("center", 1.0, "end")
    text_box_ingredientes.config(state=DISABLED)

    #ADICIONAR UMA CAIXA DE TEXTO À JANELA
    text_box_intruçoes = tk.Text(janela, width=50, height=20)
    text_box_intruçoes.place(x=190, y=220)
    #ADICIONAR TEXTO À CAIXA DE TEXTO CENTRALIZADO
    text_box_intruçoes.insert(tk.END, "Instruções:\n\n1. Pré-aqueça o forno a 375 graus\n2. Misture a farinha, sal e manteiga\n3. Adicione água fria até que a mistura fique homogênea\n4. Abra a massa e coloque-a em um pirex de 9 polegadas\n5. Aqueça o bacon e a cebola por 3 minutos\n6. Misture o ovo, o leite, o creme de leite, o queijo, o bacon e a cebola\n7. Despeje a mistura no pirex\n8. Asse por 40 minutos ou até que esteja dourado")
    text_box_intruçoes.tag_configure("center", justify='center')
    text_box_intruçoes.tag_add("center", 1.0, "end")
    text_box_intruçoes.config(state=DISABLED)

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=17, height=2, bg="#ffff00", command=lambda:marcarFavorito(cat,titulo_receita,entUtilizador))
    botao_favorito.place(x=190, y=550)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=17, height=2, bg="#1f77b4", command=lambda:comentar(titulo_receita,entUtilizador))
    botao_comentario.place(x=330,y=550)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(
        janela, text="Fechar", width=17, height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.place(x=470, y=550)

def janelaEmpadaoCarne(cat,entUtilizador):
   #CREATE A WINDOW
    janela = tk.Tk()
    w = 800
    h = 700
    ws = janela.winfo_screenwidth()
    hs = janela.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janela.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #SET THE TITLE OF THE WINDOW
    janela.title("Empadão de Carne")

    #dont let the window resize
    janela.resizable(0,0)
    titulo_receita = "Empadão de Carne"
    #ADD A TEXT BOX TO THE WINDOW
    text_box_ingredientes = tk.Text(janela, width=50, height=12)
    text_box_ingredientes.place(x=190, y=50)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_ingredientes.insert(tk.END,titulo_receita + "\n\nIngredientes:\n\n1/2 kg de carne moída\n1 cebola média picada\n1 xícara de molho de tomate\n1 colher (sopa) de cheiro verde\n1 colher (café) de orégano\n1 colher (sopa) de azeite\nsal a gosto\n2 xícaras de farinha de trigo\n1/2 xícara de óleo\n1/2 xícara de leite\n1 ovo")
    text_box_ingredientes.tag_configure("center", justify='center')
    text_box_ingredientes.tag_add("center", 1.0, "end")
    text_box_ingredientes.config(state=DISABLED)

    #ADD A TEXT BOX TO THE WINDOW
    text_box_intruçoes = tk.Text(janela, width=50, height=20)
    text_box_intruçoes.place(x=190, y=220)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_intruçoes.insert(tk.END, "Instruções:\n\n1. Em uma panela, refogue a cebola e a carne moída\n2. Adicione o molho de tomate, o cheiro verde, o orégano, o azeite e o sal.\n3. Misture bem e deixe cozinhar por 5 minutos.\n4. Em uma tigela, misture a farinha com o óleo, o leite e o ovo.\n5. Misture bem até obter uma massa homogênea.\n6. Abra a massa em um refratário e coloque a carne refogada por cima.\n7. Cubra com a massa restante.\n8. Asse em forno pré-aquecido a 180°C por aproximadamente 40 minutos.")
    text_box_intruçoes.tag_configure("center", justify='center')
    text_box_intruçoes.tag_add("center", 1.0, "end")
    text_box_intruçoes.config(state=DISABLED)

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=17, height=2, bg="#ffff00", command=lambda:marcarFavorito(cat,titulo_receita,entUtilizador))
    botao_favorito.place(x=190, y=550)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=17, height=2, bg="#1f77b4", command=lambda:comentar(titulo_receita,entUtilizador))
    botao_comentario.place(x=330,y=550)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(
        janela, text="Fechar", width=17, height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.place(x=470, y=550)

def janelaBacalhau(cat,entUtilizador):
   #CREATE A WINDOW
    janela = tk.Tk()
    w = 800
    h = 700
    ws = janela.winfo_screenwidth()
    hs = janela.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janela.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #SET THE TITLE OF THE WINDOW
    janela.title("Bacalhau")

    #dont let the window resize
    janela.resizable(0,0)
    titulo_receita = "Bacalhau"
    #ADD A TEXT BOX TO THE WINDOW
    text_box_ingredientes = tk.Text(janela, width=50, height=12)
    text_box_ingredientes.place(x=190, y=50)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_ingredientes.insert(tk.END,titulo_receita + "\n\nIngredientes:\n\n1 kg de bacalhau limpo\n2 colheres de sopa de azeite\n1 colher de sopa de alho picado\n2 tomates maduros picados\n2 cebolas grandes picadas\n1/2 xícara de azeitona verde\n1/2 xícara de azeitona preta\n1/2 xícara de salsinha picada\n1 copo de vinho branco\n1/2 xícara de passas\nSal e pimenta a gosto")
    text_box_ingredientes.tag_configure("center", justify='center')
    text_box_ingredientes.tag_add("center", 1.0, "end")
    text_box_ingredientes.config(state=DISABLED)

    #ADD A TEXT BOX TO THE WINDOW
    text_box_intruçoes = tk.Text(janela, width=50, height=20)
    text_box_intruçoes.place(x=190, y=220)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_intruçoes.insert(tk.END, "Instruções:\n\n1. Coloque o bacalhau em uma assadeira\n2. Regue com o azeite, sal, pimenta e o alho picado\n3. Adicione as cebolas, o tomate, as azeitonas, a salsinha e as passas\n4. Regue com o vinho\n5. Leve ao forno pré-aquecido por 40 minutos ou até o bacalhau ficar dourado")
    text_box_intruçoes.tag_configure("center", justify='center')
    text_box_intruçoes.tag_add("center", 1.0, "end")
    text_box_intruçoes.config(state=DISABLED)

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=17, height=2, bg="#ffff00", command=lambda:marcarFavorito(cat,titulo_receita,entUtilizador))
    botao_favorito.place(x=190, y=550)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=17, height=2, bg="#1f77b4", command=lambda:comentar(titulo_receita,entUtilizador))
    botao_comentario.place(x=330,y=550)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(
        janela, text="Fechar", width=17, height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.place(x=470, y=550)

def janelaCamarao(cat,entUtilizador):
   #CREATE A WINDOW
    janela = tk.Tk()
    w = 800
    h = 700
    ws = janela.winfo_screenwidth()
    hs = janela.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janela.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #SET THE TITLE OF THE WINDOW
    janela.title("Camarão")

    #dont let the window resize
    janela.resizable(0,0)
    titulo_receita = "Camarão"
    #ADD A TEXT BOX TO THE WINDOW
    text_box_ingredientes = tk.Text(janela, width=50, height=12)
    text_box_ingredientes.place(x=190, y=50)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_ingredientes.insert(tk.END,titulo_receita + "\n\nIngredientes:\n\n500 g de camarão\n2 dentes de alho\n1 cebola grande\n2 colheres de sopa de azeite\n1 colher de sopa de manteiga\n1 colher de sopa de molho de tomate\n1/2 colher de chá de pimenta caiena\n1/2 colher de chá de pimenta-do-reino\n1/2 colher de chá de sal\n1/2 limão (sumo)")
    text_box_ingredientes.tag_configure("center", justify='center')
    text_box_ingredientes.tag_add("center", 1.0, "end")
    text_box_ingredientes.config(state=DISABLED)

    #ADD A TEXT BOX TO THE WINDOW
    text_box_intruçoes = tk.Text(janela, width=50, height=20)
    text_box_intruçoes.place(x=190, y=220)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_intruçoes.insert(tk.END, "Instruções:\n\n1. Lave os camarões e coloque-os em uma tigela.\n2. Em uma tigela separada, misture o alho, a cebola, o azeite, a manteiga, o molho de tomate, a pimenta caiena, a pimenta-do-reino e o sal.\n3. Despeje a mistura de temperos sobre os camarões e misture bem.\n4. Deixe os camarões marinando por 15 minutos.\n5. Em uma frigideira grande, aqueça um pouco de azeite.\n6. Adicione os camarões e cozinhe por cerca de 5 minutos.\n7. Regue com o suco de limão e sirva.")
    text_box_intruçoes.tag_configure("center", justify='center')
    text_box_intruçoes.tag_add("center", 1.0, "end")
    text_box_intruçoes.config(state=DISABLED)

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=17, height=2, bg="#ffff00", command=lambda:marcarFavorito(cat,titulo_receita,entUtilizador))
    botao_favorito.place(x=190, y=550)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=17, height=2, bg="#1f77b4", command=lambda:comentar(titulo_receita,entUtilizador))
    botao_comentario.place(x=330,y=550)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(
        janela, text="Fechar", width=17, height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.place(x=470, y=550)

def janelaFeijoadaPeixe(cat,entUtilizador):
   #CREATE A WINDOW
    janela = tk.Tk()
    w = 800
    h = 700
    ws = janela.winfo_screenwidth()
    hs = janela.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janela.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #SET THE TITLE OF THE WINDOW
    janela.title("Feijoada de Peixe")

    #dont let the window resize
    janela.resizable(0,0)
    titulo_receita = "Feijoada de Peixe"
    #ADD A TEXT BOX TO THE WINDOW
    text_box_ingredientes = tk.Text(janela, width=50, height=12)
    text_box_ingredientes.place(x=190, y=50)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_ingredientes.insert(tk.END,titulo_receita + "\n\nIngredientes:\n\n2 xícaras de arroz\n3 xícaras de água\n1 cebola média picada\n1 dente de alho picado\n1/2 xícara de azeite de oliva\n1 lata de tomate pelado\n1/2 xícara de azeitonas pretas\n1/2 xícara de azeitonas verdes\n1 xícara de feijão preto cozido\n1/2 xícara de ervilhas congeladas\n1 colher de sopa de colorau\n1 lata de sardinhas em lata\n1/2 xícara de camarão cozido")
    text_box_ingredientes.tag_configure("center", justify='center')
    text_box_ingredientes.tag_add("center", 1.0, "end")
    text_box_ingredientes.config(state=DISABLED)

    #ADD A TEXT BOX TO THE WINDOW
    text_box_intruçoes = tk.Text(janela, width=50, height=20)
    text_box_intruçoes.place(x=190, y=220)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_intruçoes.insert(tk.END, "Instruções:\n\n1. Coloque o arroz em uma panela e adicione água e sal\n2. Ferva por 15 minutos ou até o arroz estar cozido\n3. Escorra o arroz e reserve\n4. Aqueça o azeite em uma panela grande\n5. Adicione a cebola e o alho e cozinhe até que a cebola esteja murcha\n6. Adicione o tomate pelado, as azeitonas, o feijão, as ervilhas, o colorau, as sardinhas e o camarão\n7. Misture bem e deixe ferver por 10 minutos\n8. Adicione o arroz à panela e misture bem\n9. Deixe ferver por 10 minutos e sirva")
    text_box_intruçoes.tag_configure("center", justify='center')
    text_box_intruçoes.tag_add("center", 1.0, "end")
    text_box_intruçoes.config(state=DISABLED)

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=17, height=2, bg="#ffff00", command=lambda:marcarFavorito(cat,titulo_receita,entUtilizador))
    botao_favorito.place(x=190, y=550)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=17, height=2, bg="#1f77b4", command=lambda:comentar(titulo_receita,entUtilizador))
    botao_comentario.place(x=330,y=550)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(
        janela, text="Fechar", width=17, height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.place(x=470, y=550)

def janelaGaropa(cat,entUtilizador):
   #CREATE A WINDOW
    janela = tk.Tk()
    w = 800
    h = 700
    ws = janela.winfo_screenwidth()
    hs = janela.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janela.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #SET THE TITLE OF THE WINDOW
    janela.title("Garopa")

    #dont let the window resize
    janela.resizable(0,0)
    titulo_receita = "Garopa"
    #ADD A TEXT BOX TO THE WINDOW
    text_box_ingredientes = tk.Text(janela, width=50, height=12)
    text_box_ingredientes.place(x=190, y=50)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_ingredientes.insert(tk.END,titulo_receita + "\n\nIngredientes:\n\n1/2 xícara de açúcar mascavo\n1/2 xícara de açúcar\n1/2 xícara de óleo de canola\n2 ovos\n1/2 xícara de leite\n1/2 xícara de suco de laranja\n2 xícaras de farinha de trigo\n1 colher de chá de canela em pó\n1 colher de chá de fermento em pó\n1/2 colher de chá de sal")
    text_box_ingredientes.tag_configure("center", justify='center')
    text_box_ingredientes.tag_add("center", 1.0, "end")
    text_box_ingredientes.config(state=DISABLED)

    #ADD A TEXT BOX TO THE WINDOW
    text_box_intruçoes = tk.Text(janela, width=50, height=20)
    text_box_intruçoes.place(x=190, y=220)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_intruçoes.insert(tk.END, "Instruções:\n\n1. Pré-aqueça o forno a 375 graus\n2. Misture o açúcar mascavo, o açúcar, o óleo, o ovo e o leite\n3. Misture o suco de laranja, a farinha, a canela, o fermento e o sal\n4. Misture os dois misturas até obter uma massa homogênea\n5. Despeje a massa em uma forma untada\n6. Asse por 35 a 40 minutos ou até que esteja dourado")
    text_box_intruçoes.tag_configure("center", justify='center')
    text_box_intruçoes.tag_add("center", 1.0, "end")
    text_box_intruçoes.config(state=DISABLED)

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=17, height=2, bg="#ffff00", command=lambda:marcarFavorito(cat,titulo_receita,entUtilizador))
    botao_favorito.place(x=190, y=550)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=17, height=2, bg="#1f77b4", command=lambda:comentar(titulo_receita,entUtilizador))
    botao_comentario.place(x=330,y=550)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(
        janela, text="Fechar", width=17, height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.place(x=470, y=550)

def janelaPolvo(cat,entUtilizador):
   #CREATE A WINDOW
    janela = tk.Tk()
    w = 800
    h = 700
    ws = janela.winfo_screenwidth()
    hs = janela.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janela.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #SET THE TITLE OF THE WINDOW
    janela.title("Polvo")

    #dont let the window resize
    janela.resizable(0,0)
    titulo_receita = "Polvo"
    #ADD A TEXT BOX TO THE WINDOW
    text_box_ingredientes = tk.Text(janela, width=50, height=12)
    text_box_ingredientes.place(x=190, y=50)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_ingredientes.insert(tk.END,titulo_receita + "\n\nIngredientes:\n\n1 Polvo\n1 Limão\n1 Cebola\n2 Dentes de alho\n1 Xícara de azeite de oliva\n1 Colher de sopa de vinho branco\n2 Colheres de sopa de salsa picada\n1 Colher de sopa de coentro picado\n1 Pitada de pimenta do reino\nSal a gosto")
    text_box_ingredientes.tag_configure("center", justify='center')
    text_box_ingredientes.tag_add("center", 1.0, "end")
    text_box_ingredientes.config(state=DISABLED)

    #ADD A TEXT BOX TO THE WINDOW
    text_box_intruçoes = tk.Text(janela, width=50, height=20)
    text_box_intruçoes.place(x=190, y=220)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_intruçoes.insert(tk.END, "Instruções:\n\n1. Coloque o polvo em uma panela com água e sal\n2. Cozinhe por 25 minutos\n3. Retire o polvo da água e deixe esfriar\n4. Corte a cebola em pedaços pequenos\n5. Coloque o azeite em uma panela e adicione a cebola, o alho e o polvo\n6. Refogue por cerca de 5 minutos\n7. Junte o vinho branco, a salsa, o coentro, o limão, a pimenta do reino e sal a gosto\n8. Deixe cozinhar por mais 20 minutos")
    text_box_intruçoes.tag_configure("center", justify='center')
    text_box_intruçoes.tag_add("center", 1.0, "end")
    text_box_intruçoes.config(state=DISABLED)

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=17, height=2, bg="#ffff00", command=lambda:marcarFavorito(cat,titulo_receita,entUtilizador))
    botao_favorito.place(x=190, y=550)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=17, height=2, bg="#1f77b4", command=lambda:comentar(titulo_receita,entUtilizador))
    botao_comentario.place(x=330,y=550)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(
        janela, text="Fechar", width=17, height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.place(x=470, y=550)

def janelaSalmao(cat,entUtilizador):
   #CREATE A WINDOW
    janela = tk.Tk()
    w = 800
    h = 700
    ws = janela.winfo_screenwidth()
    hs = janela.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janela.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #SET THE TITLE OF THE WINDOW
    janela.title("Salmão")

    #dont let the window resize
    janela.resizable(0,0)
    titulo_receita = "Salmão"
    #ADD A TEXT BOX TO THE WINDOW
    text_box_ingredientes = tk.Text(janela, width=50, height=12)
    text_box_ingredientes.place(x=190, y=50)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_ingredientes.insert(tk.END,titulo_receita + "\n\nIngredientes:\n\n2 filés de salmão\n2 colheres de sopa de manteiga\n1/4 de xícara de suco de limão\n1 colher de sopa de alho picado\n1/4 de colher de chá de sal\n1/4 de colher de chá de pimenta\n1/4 de xícara de salsa fresca picada")
    text_box_ingredientes.tag_configure("center", justify='center')
    text_box_ingredientes.tag_add("center", 1.0, "end")
    text_box_ingredientes.config(state=DISABLED)

    #ADD A TEXT BOX TO THE WINDOW
    text_box_intruçoes = tk.Text(janela, width=50, height=20)
    text_box_intruçoes.place(x=190, y=220)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_intruçoes.insert(tk.END, "Instruções:\n\n1. Pré-aqueça o forno a 375 graus\n2. Coloque os filés de salmão em um prato para assar\n3. Derreta a manteiga em uma panela pequena\n4. Adicione o suco de limão, o alho, o sal e a pimenta\n5. Despeje a mistura de manteiga sobre o salmão\n6. Polvilhe a salsa fresca desidratada sobre o salmão\n7. Asse por 15 a 20 minutos ou até que o peixe esteja dourado e cozido")
    text_box_intruçoes.tag_configure("center", justify='center')
    text_box_intruçoes.tag_add("center", 1.0, "end")
    text_box_intruçoes.config(state=DISABLED)

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=17, height=2, bg="#ffff00", command=lambda:marcarFavorito(cat,titulo_receita,entUtilizador))
    botao_favorito.place(x=190, y=550)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=17, height=2, bg="#1f77b4", command=lambda:comentar(titulo_receita,entUtilizador))
    botao_comentario.place(x=330,y=550)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(
        janela, text="Fechar", width=17, height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.place(x=470, y=550)

def janelaSbacalhau(cat,entUtilizador):
   #CREATE A WINDOW
    janela = tk.Tk()
    w = 800
    h = 700
    ws = janela.winfo_screenwidth()
    hs = janela.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janela.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #SET THE TITLE OF THE WINDOW
    janela.title("Salada de Bacalhau")

    #dont let the window resize
    janela.resizable(0,0)
    titulo_receita = "Salada de Bacalhau"
    #ADD A TEXT BOX TO THE WINDOW
    text_box_ingredientes = tk.Text(janela, width=50, height=12)
    text_box_ingredientes.place(x=190, y=50)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_ingredientes.insert(tk.END,titulo_receita + "\n\nIngredientes:\n\n1/2 quilo de bacalhau desfiado\n2 ovos cozidos\n2 tomates maduros\n1/2 pimentão verde\n1/2 pimentão vermelho\n1 cebola roxa média\n50 ml de azeite\nSuco de 1/2 limão\n1/2 maço de salsinha")
    text_box_ingredientes.tag_configure("center", justify='center')
    text_box_ingredientes.tag_add("center", 1.0, "end")
    text_box_ingredientes.config(state=DISABLED)

    #ADD A TEXT BOX TO THE WINDOW
    text_box_intruçoes = tk.Text(janela, width=50, height=20)
    text_box_intruçoes.place(x=190, y=220)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_intruçoes.insert(tk.END, "Instruções:\n\n1. Cozinhe o bacalhau em água até que esteja macio\n2. Desfie o bacalhau\n3. Pique os tomates, pimentões e cebola\n4. Corte os ovos cozidos em quartos\n5. Misture todos os ingredientes em uma tigela\n6. Tempere com azeite, suco de limão e sal\n7. Sirva a salada com salsinha picada")
    text_box_intruçoes.tag_configure("center", justify='center')
    text_box_intruçoes.tag_add("center", 1.0, "end")
    text_box_intruçoes.config(state=DISABLED)

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=17, height=2, bg="#ffff00", command=lambda:marcarFavorito(cat,titulo_receita,entUtilizador))
    botao_favorito.place(x=190, y=550)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=17, height=2, bg="#1f77b4", command=lambda:comentar(titulo_receita,entUtilizador))
    botao_comentario.place(x=330,y=550)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(
        janela, text="Fechar", width=17, height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.place(x=470, y=550)

def janelaSbolonhesa(cat,entUtilizador):
   #CREATE A WINDOW
    janela = tk.Tk()
    w = 800
    h = 700
    ws = janela.winfo_screenwidth()
    hs = janela.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janela.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #SET THE TITLE OF THE WINDOW
    janela.title("Salada de Bolonhesa")

    #dont let the window resize
    janela.resizable(0,0)
    titulo_receita = "Salada de Bolonhesa"
    #ADD A TEXT BOX TO THE WINDOW
    text_box_ingredientes = tk.Text(janela, width=50, height=12)
    text_box_ingredientes.place(x=190, y=50)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_ingredientes.insert(tk.END,titulo_receita + "\n\nIngredientes:\n\n2 xícaras de macarrão\n1/4 xícara de azeite\n1/4 xícara de água\n1/4 de colher de sal\n1/2 xícara de molho de tomate\n1/2 xícara de queijo parmesão ralado\n1/4 de xícara de cebola picada\n1/4 de xícara de alho picado\n1/2 xícara de ervilhas congeladas\n1/4 de xícara de bacon cozido e picado")
    text_box_ingredientes.tag_configure("center", justify='center')
    text_box_ingredientes.tag_add("center", 1.0, "end")
    text_box_ingredientes.config(state=DISABLED)

    #ADD A TEXT BOX TO THE WINDOW
    text_box_intruçoes = tk.Text(janela, width=50, height=20)
    text_box_intruçoes.place(x=190, y=220)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_intruçoes.insert(tk.END, "Instruções:\n\n1. Cozinhe o macarrão de acordo com as instruções do pacote\n2. Enquanto isso, aqueça o azeite em uma panela\n3. Adicione o alho e a cebola e cozinhe até que estejam macios\n4. Adicione o molho de tomate, a água e o sal\n5. Deixe ferver por 5-10 minutos\n6. Despeje o molho em uma tigela e misture o macarrão, o queijo, as ervilhas e o bacon\n7. Sirva quente")
    text_box_intruçoes.tag_configure("center", justify='center')
    text_box_intruçoes.tag_add("center", 1.0, "end")
    text_box_intruçoes.config(state=DISABLED)

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=17, height=2, bg="#ffff00", command=lambda:marcarFavorito(cat,titulo_receita,entUtilizador))
    botao_favorito.place(x=190, y=550)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=17, height=2, bg="#1f77b4", command=lambda:comentar(titulo_receita,entUtilizador))
    botao_comentario.place(x=330,y=550)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(
        janela, text="Fechar", width=17, height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.place(x=470, y=550)

def janelaSbulgur(cat,entUtilizador):
   #CREATE A WINDOW
    janela = tk.Tk()
    w = 800
    h = 700
    ws = janela.winfo_screenwidth()
    hs = janela.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janela.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #SET THE TITLE OF THE WINDOW
    janela.title("Salada de Bulgur")

    #dont let the window resize
    janela.resizable(0,0)
    titulo_receita = "Salada de Bulgur"
    #ADD A TEXT BOX TO THE WINDOW
    text_box_ingredientes = tk.Text(janela, width=50, height=12)
    text_box_ingredientes.place(x=190, y=50)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_ingredientes.insert(tk.END,titulo_receita + "\n\nIngredientes:\n\n1 xícara de bulgur\n1 xícara de água\n1/4 xícara de azeite de oliva\n1/4 xícara de suco de limão\n2 tomates maduros, sem sementes, picados\n1/4 xícara de cebola picada\n1/4 xícara de hortelã fresca\n1/4 xícara de passas\n1 colher de chá de sal")
    text_box_ingredientes.tag_configure("center", justify='center')
    text_box_ingredientes.tag_add("center", 1.0, "end")
    text_box_ingredientes.config(state=DISABLED)

    #ADD A TEXT BOX TO THE WINDOW
    text_box_intruçoes = tk.Text(janela, width=50, height=10)
    text_box_intruçoes.place(x=190, y=220)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_intruçoes.insert(tk.END, "Instruções:\n\n1. Coloque o bulgur em uma tigela\n2. Aqueça a água em uma panela e despeje sobre o bulgur\n3. Deixe o bulgur de molho por 15 minutos\n4. Escorra o excesso de água\n5. Misture o azeite, suco de limão, tomate, cebola, hortelã e passas com o bulgur\n6. Tempere com sal a gosto\n7. Sirva")
    text_box_intruçoes.tag_configure("center", justify='center')
    text_box_intruçoes.tag_add("center", 1.0, "end")
    text_box_intruçoes.config(state=DISABLED)

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=17, height=2, bg="#ffff00", command=lambda:marcarFavorito(cat,titulo_receita,entUtilizador))
    botao_favorito.place(x=190, y=550)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=17, height=2, bg="#1f77b4", command=lambda:comentar(titulo_receita,entUtilizador))
    botao_comentario.place(x=330,y=550)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(
        janela, text="Fechar", width=17, height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.place(x=470, y=550)

def janelaSdelicias(cat,entUtilizador):
   #CREATE A WINDOW
    janela = tk.Tk()
    w = 800
    h = 700
    ws = janela.winfo_screenwidth()
    hs = janela.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janela.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #SET THE TITLE OF THE WINDOW
    janela.title("Salada de Delícias do Mar")

    #dont let the window resize
    janela.resizable(0,0)
    titulo_receita = "Salada de Delícias do Mar"
    #ADD A TEXT BOX TO THE WINDOW
    text_box_ingredientes = tk.Text(janela, width=50, height=12)
    text_box_ingredientes.place(x=190, y=50)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_ingredientes.insert(tk.END,titulo_receita + "\n\nIngredientes:\n\n1 xícara de camarão cozido\n1 xícara de salmão cozido\n1 xícara de atum em lata\n1 xícara de azeitona verde picada\n1/2 xícara de milho\n2 colheres de sopa de cebola picada\n2 colheres de sopa de azeite\n1/4 xícara de limão\nSal e pimenta a gosto")
    text_box_ingredientes.tag_configure("center", justify='center')
    text_box_ingredientes.tag_add("center", 1.0, "end")
    text_box_ingredientes.config(state=DISABLED)

    #ADD A TEXT BOX TO THE WINDOW
    text_box_intruçoes = tk.Text(janela, width=50, height=20)
    text_box_intruçoes.place(x=190, y=220)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_intruçoes.insert(tk.END, "Instruções:\n\n1. Coloque todos os ingredientes em uma tigela grande\n2. Misture bem\n3. Adicione o azeite e o limão e misture novamente\n4. Tempere com sal e pimenta a gosto\n5. Deixe descansar na geladeira por 2-3 horas antes de servir")
    text_box_intruçoes.tag_configure("center", justify='center')
    text_box_intruçoes.tag_add("center", 1.0, "end")
    text_box_intruçoes.config(state=DISABLED)

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=17, height=2, bg="#ffff00", command=lambda:marcarFavorito(cat,titulo_receita,entUtilizador))
    botao_favorito.place(x=190, y=550)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=17, height=2, bg="#1f77b4", command=lambda:comentar(titulo_receita,entUtilizador))
    botao_comentario.place(x=330,y=550)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(
        janela, text="Fechar", width=17, height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.place(x=470, y=550)

def janelaSfrango(cat,entUtilizador):
   #CREATE A WINDOW
    janela = tk.Tk()
    w = 800
    h = 700
    ws = janela.winfo_screenwidth()
    hs = janela.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janela.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #SET THE TITLE OF THE WINDOW
    janela.title("Salada de Frango")

    #dont let the window resize
    janela.resizable(0,0)
    titulo_receita = "Salada de Frango"
    #ADD A TEXT BOX TO THE WINDOW
    text_box_ingredientes = tk.Text(janela, width=50, height=12)
    text_box_ingredientes.place(x=190, y=50)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_ingredientes.insert(tk.END,titulo_receita + "\n\nIngredientes:\n\n3 xícaras de frango cozido e desfiado\n1 xícara de maçã verde picada\n1/2 xícara de castanha de caju\n1/2 xícara de passas\n1/2 xícara de abacaxi picado\n1/2 xícara de iogurte natural\n1 colher de chá de sal\n1/4 colher de chá de pimenta-do-reino")
    text_box_ingredientes.tag_configure("center", justify='center')
    text_box_ingredientes.tag_add("center", 1.0, "end")
    text_box_ingredientes.config(state=DISABLED)

    #ADD A TEXT BOX TO THE WINDOW
    text_box_intruçoes = tk.Text(janela, width=50, height=20)
    text_box_intruçoes.place(x=190, y=220)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_intruçoes.insert(tk.END, "Instruções:\n\n1. Em uma tigela grande, misture o frango, a maçã, a castanha de caju, as passas e o abacaxi\n2. Em outra tigela pequena, misture o iogurte, o sal e a pimenta.\n3. Coloque a mistura de iogurte sobre o frango e misture até que todos os ingredientes fiquem bem misturados.\n4. Sirva a salada de frango fria.")
    text_box_intruçoes.tag_configure("center", justify='center')
    text_box_intruçoes.tag_add("center", 1.0, "end")
    text_box_intruçoes.config(state=DISABLED)

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=17, height=2, bg="#ffff00", command=lambda:marcarFavorito(cat,titulo_receita,entUtilizador))
    botao_favorito.place(x=190, y=550)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=17, height=2, bg="#1f77b4", command=lambda:comentar(titulo_receita,entUtilizador))
    botao_comentario.place(x=330,y=550)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(
        janela, text="Fechar", width=17, height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.place(x=470, y=550)

def janelaSsalsichas(cat,entUtilizador):
   #CREATE A WINDOW
    janela = tk.Tk()
    w = 800
    h = 700
    ws = janela.winfo_screenwidth()
    hs = janela.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janela.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #SET THE TITLE OF THE WINDOW
    janela.title("Salada de Salsichas")

    #dont let the window resize
    janela.resizable(0,0)
    titulo_receita = "Salada de Salsichas"
    #ADD A TEXT BOX TO THE WINDOW
    text_box_ingredientes = tk.Text(janela, width=50, height=8)
    text_box_ingredientes.place(x=190, y=50)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_ingredientes.insert(tk.END,titulo_receita + "\n\nIngredientes:\n\n6 salsichas tipo frankfurt\n1/2 xícara de maionese\n1/3 xícara de mostarda\n1/2 xícara de azeite de oliva\n1/4 xícara de vinagre de vinho branco\n2 colheres de sopa de alcaparras\n1/2 xícara de cebola roxa picada\n1/4 xícara de picles picados")
    text_box_ingredientes.tag_configure("center", justify='center')
    text_box_ingredientes.tag_add("center", 1.0, "end")
    text_box_ingredientes.config(state=DISABLED)

    #ADD A TEXT BOX TO THE WINDOW
    text_box_intruçoes = tk.Text(janela, width=50, height=12)
    text_box_intruçoes.place(x=190, y=220)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_intruçoes.insert(tk.END, "Instruções:\n\n1. Cozinhe as salsichas em água fervente por 10 minutos\n2. Escorra a água e deixe esfriar\n3. Corte as salsichas em pedaços de 2 polegadas\n4. Misture a maionese, a mostarda, o azeite, o vinagre, as alcaparras, a cebola e os picles em uma tigela\n5. Adicione as salsichas na tigela e misture bem\n6. Leve a tigela à geladeira por pelo menos 1 hora")
    text_box_intruçoes.tag_configure("center", justify='center')
    text_box_intruçoes.tag_add("center", 1.0, "end")
    text_box_intruçoes.config(state=DISABLED)

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=17, height=2, bg="#ffff00", command=lambda:marcarFavorito(cat,titulo_receita,entUtilizador))
    botao_favorito.place(x=190, y=550)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=17, height=2, bg="#1f77b4", command=lambda:comentar(titulo_receita,entUtilizador))
    botao_comentario.place(x=330,y=550)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(
        janela, text="Fechar", width=17, height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.place(x=470, y=550)

def janelaCaneloneVegetariano(cat,entUtilizador):
   #CREATE A WINDOW
    janela = tk.Tk()
    w = 800
    h = 700
    ws = janela.winfo_screenwidth()
    hs = janela.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janela.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #SET THE TITLE OF THE WINDOW
    janela.title("Canelone Vegetariano")

    #dont let the window resize
    janela.resizable(0,0)
    titulo_receita = "Canelone Vegetariano"
    #ADD A TEXT BOX TO THE WINDOW
    text_box_ingredientes = tk.Text(janela, width=50, height=12)
    text_box_ingredientes.place(x=190, y=50)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_ingredientes.insert(tk.END,titulo_receita + "\n\nIngredientes:\n\n2 xícaras de ricota\n2 xícaras de espinafre picado\n1/2 xícara de queijo parmesão ralado\n1/4 xícara de cebola picada\n2 colheres de sopa de azeite\n1/2 colher de chá de sal\n1/4 colher de chá de pimenta\n1/4 xícara de nozes picadas\n1/4 xícara de salsa picada\n400 g de massa de canelone\n1 xícara de molho de tomate")
    text_box_ingredientes.tag_configure("center", justify='center')
    text_box_ingredientes.tag_add("center", 1.0, "end")
    text_box_ingredientes.config(state=DISABLED)

    #ADD A TEXT BOX TO THE WINDOW
    text_box_intruçoes = tk.Text(janela, width=50, height=20)
    text_box_intruçoes.place(x=190, y=220)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_intruçoes.insert(tk.END, "Instruções:\n\n1. Pré-aqueça o forno a 375 graus\n2. Misture a ricota, o espinafre, o queijo parmesão, a cebola, o azeite, o sal e a pimenta\n3. Misture as nozes e a salsa\n4. Encha os canelones com a mistura\n5. Coloque os canelones em um pirex e despeje o molho de tomate\n6. Cubra com papel alumínio e leve ao forno por 25 minutos\n7. Retire o papel alumínio e asse por mais 10 minutos")
    text_box_intruçoes.tag_configure("center", justify='center')
    text_box_intruçoes.tag_add("center", 1.0, "end")
    text_box_intruçoes.config(state=DISABLED)

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=17, height=2, bg="#ffff00", command=lambda:marcarFavorito(cat,titulo_receita,entUtilizador))
    botao_favorito.place(x=190, y=550)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=17, height=2, bg="#1f77b4", command=lambda:comentar(titulo_receita,entUtilizador))
    botao_comentario.place(x=330,y=550)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(
        janela, text="Fechar", width=17, height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.place(x=470, y=550)

def janelaCogumelos(cat,entUtilizador):
   #CREATE A WINDOW
    janela = tk.Tk()
    w = 800
    h = 700
    ws = janela.winfo_screenwidth()
    hs = janela.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janela.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #SET THE TITLE OF THE WINDOW
    janela.title("Cogumelos")

    #dont let the window resize
    janela.resizable(0,0)
    titulo_receita = "Cogumelos"
    #ADD A TEXT BOX TO THE WINDOW
    text_box_ingredientes = tk.Text(janela, width=50, height=12)
    text_box_ingredientes.place(x=190, y=50)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_ingredientes.insert(tk.END,titulo_receita + "\n\nIngredientes:\n\n2 xícaras de cogumelos picados\n3 colheres de sopa de azeite\n2 dentes de alho picados\n1/4 de xícara de cebola picada\n1/4 de xícara de salsinha picada\n1 colher de sopa de vinho branco\nSal e pimenta a gosto")
    text_box_ingredientes.tag_configure("center", justify='center')
    text_box_ingredientes.tag_add("center", 1.0, "end")
    text_box_ingredientes.config(state=DISABLED)

    #ADD A TEXT BOX TO THE WINDOW
    text_box_intruçoes = tk.Text(janela, width=50, height=20)
    text_box_intruçoes.place(x=190, y=220)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_intruçoes.insert(tk.END, "Instruções:\n\n1. Aqueça o azeite em uma panela média\n2. Adicione o alho, a cebola e os cogumelos\n3. Cozinhe em fogo médio-alto por 5 minutos\n4. Acrescente a salsinha e o vinho branco\n5. Tempere com sal e pimenta a gosto\n6. Cozinhe por mais 5 minutos ou até que os cogumelos estejam macios\n7. Sirva quente")
    text_box_intruçoes.tag_configure("center", justify='center')
    text_box_intruçoes.tag_add("center", 1.0, "end")
    text_box_intruçoes.config(state=DISABLED)

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=17, height=2, bg="#ffff00", command=lambda:marcarFavorito(cat,titulo_receita,entUtilizador))
    botao_favorito.place(x=190, y=550)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=17, height=2, bg="#1f77b4", command=lambda:comentar(titulo_receita,entUtilizador))
    botao_comentario.place(x=330,y=550)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(
        janela, text="Fechar", width=17, height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.place(x=470, y=550)

def janelaCrepeVegetariano(cat,entUtilizador):
   #CREATE A WINDOW
    janela = tk.Tk()
    w = 800
    h = 700
    ws = janela.winfo_screenwidth()
    hs = janela.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janela.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #SET THE TITLE OF THE WINDOW
    janela.title("Crepes Vegetarianos")

    #dont let the window resize
    janela.resizable(0,0)
    titulo_receita = "Crepes Vegetarianos"
    #ADD A TEXT BOX TO THE WINDOW
    text_box_ingredientes = tk.Text(janela, width=50, height=12)
    text_box_ingredientes.place(x=190, y=50)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_ingredientes.insert(tk.END,titulo_receita + "\n\nIngredientes:\n\n1 xícara de farinha\n2 ovos\n1 xícara de leite\n1/4 de colher de sal\n2 colheres de sopa de óleo\n1/2 xícara de cebola picada\n1/4 xícara de cogumelos picados\n1/4 xícara de azeitona\n1/4 xícara de pimentão vermelho picado\n1/2 colher de chá de alho em pó\n1/4 colher de chá de pimenta do reino")
    text_box_ingredientes.tag_configure("center", justify='center')
    text_box_ingredientes.tag_add("center", 1.0, "end")
    text_box_ingredientes.config(state=DISABLED)

    #ADD A TEXT BOX TO THE WINDOW
    text_box_intruçoes = tk.Text(janela, width=50, height=20)
    text_box_intruçoes.place(x=190, y=220)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_intruçoes.insert(tk.END, "Instruções:\n\n1. Misture a farinha, o sal e os ovos.\n2. Adicione o leite e mexa bem.\n3. Aqueça o óleo em uma frigideira.\n4. Adicione a cebola, os cogumelos, a azeitona, o pimentão, o alho e a pimenta e refogue por 5 minutos.\n5. Despeje a mistura de crepe na frigideira e cozinhe por 1 minuto.\n6. Vire a crepe e cozinhe por mais 1 minuto.\n7. Repita o processo até acabar toda a massa.")
    text_box_intruçoes.tag_configure("center", justify='center')
    text_box_intruçoes.tag_add("center", 1.0, "end")
    text_box_intruçoes.config(state=DISABLED)

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=17, height=2, bg="#ffff00", command=lambda:marcarFavorito(cat,titulo_receita,entUtilizador))
    botao_favorito.place(x=190, y=550)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=17, height=2, bg="#1f77b4", command=lambda:comentar(titulo_receita,entUtilizador))
    botao_comentario.place(x=330,y=550)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(
        janela, text="Fechar", width=17, height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.place(x=470, y=550)

def janelaFolhadoVegetariano(cat,entUtilizador):
    #CREATE A WINDOW
    janela = tk.Tk()
    w = 800
    h = 700
    ws = janela.winfo_screenwidth()
    hs = janela.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janela.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #SET THE TITLE OF THE WINDOW
    janela.title("Folhado Vegetariano")

    #dont let the window resize
    janela.resizable(0,0)
    titulo_receita = "Folhado Vegetariano"
    #ADD A TEXT BOX TO THE WINDOW
    text_box_ingredientes = tk.Text(janela, width=50, height=12)
    text_box_ingredientes.place(x=190, y=50)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_ingredientes.insert(tk.END,titulo_receita + "\n\nIngredientes:\n\n1 embalagem de massa folhada\n1 cebola grande picada\n2 dentes de alho picados\n1 colher de sopa de azeite\n1/2 xícara de cogumelos fatiados\n1/2 xícara de ervilha\n1/4 xícara de espinafre picado\n1/2 xícara de queijo ralado\n1/2 xícara de creme de leite\n1 ovo\nSal e pimenta a gosto")
    text_box_ingredientes.tag_configure("center", justify='center')
    text_box_ingredientes.tag_add("center", 1.0, "end")
    text_box_ingredientes.config(state=DISABLED)

    #ADD A TEXT BOX TO THE WINDOW
    text_box_intruçoes = tk.Text(janela, width=50, height=20)
    text_box_intruçoes.place(x=190, y=220)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_intruçoes.insert(tk.END, "Instruções:\n\n1. Pré-aqueça o forno a 350 graus\n2. Em uma panela grande, doure a cebola e o alho no azeite\n3. Adicione os cogumelos, as ervilhas, o espinafre e refogue por 5 minutos\n4. Misture o queijo, o creme de leite e o ovo\n5. Tempere com sal e pimenta a gosto\n6. Abra a massa folhada e coloque-a em uma assadeira de tamanho médio\n7. Despeje a mistura de legumes e cubra com a massa folhada\n8. Asse por 40 minutos ou até que esteja dourado")
    text_box_intruçoes.tag_configure("center", justify='center')
    text_box_intruçoes.tag_add("center", 1.0, "end")
    text_box_intruçoes.config(state=DISABLED)

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=17, height=2, bg="#ffff00", command=lambda:marcarFavorito(cat,titulo_receita,entUtilizador))
    botao_favorito.place(x=190, y=550)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=17, height=2, bg="#1f77b4", command=lambda:comentar(titulo_receita,entUtilizador))
    botao_comentario.place(x=330,y=550)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(
        janela, text="Fechar", width=17, height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.place(x=470, y=550)

def janelaMigasVegetariano(cat,entUtilizador):
   #CREATE A WINDOW
    janela = tk.Tk()
    w = 800
    h = 700
    ws = janela.winfo_screenwidth()
    hs = janela.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janela.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #SET THE TITLE OF THE WINDOW
    janela.title("Migas Vegetariano")

    #dont let the window resize
    janela.resizable(0,0)
    titulo_receita = "Migas Vegetariano"
    #ADD A TEXT BOX TO THE WINDOW
    text_box_ingredientes = tk.Text(janela, width=50, height=12)
    text_box_ingredientes.place(x=190, y=50)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_ingredientes.insert(tk.END,titulo_receita + "\n\nIngredientes:\n\n6 ovos\n1 colher (sopa) de azeite\n2 dentes de alho picados\n2 pimentões vermelhos picados\n3 tomates maduros picados\n1/2 xícara de pão ralado\n1/4 xícara de salsinha picada\n1/4 xícara de cebolinha verde picada\nSal e pimenta-do-reino a gosto")
    text_box_ingredientes.tag_configure("center", justify='center')
    text_box_ingredientes.tag_add("center", 1.0, "end")
    text_box_ingredientes.config(state=DISABLED)

    #ADD A TEXT BOX TO THE WINDOW
    text_box_intruçoes = tk.Text(janela, width=50, height=20)
    text_box_intruçoes.place(x=190, y=220)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_intruçoes.insert(tk.END, "Instruções:\n\n1. Bata os ovos em uma tigela\n2. Aqueça o azeite em uma panela\n3. Refogue os alhos e os pimentões\n4. Adicione os tomates e deixe refogar por mais alguns minutos\n5. Adicione os ovos batidos, misture bem\n6. Junte o pão ralado, a salsinha e a cebolinha\n7. Tempere com sal e pimenta-do-reino\n8. Deixe cozinhar até que os ovos estejam no ponto desejado")
    text_box_intruçoes.tag_configure("center", justify='center')
    text_box_intruçoes.tag_add("center", 1.0, "end")
    text_box_intruçoes.config(state=DISABLED)

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=17, height=2, bg="#ffff00", command=lambda:marcarFavorito(cat,titulo_receita,entUtilizador))
    botao_favorito.place(x=190, y=550)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=17, height=2, bg="#1f77b4", command=lambda:comentar(titulo_receita,entUtilizador))
    botao_comentario.place(x=330,y=550)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(
        janela, text="Fechar", width=17, height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.place(x=470, y=550)

def janelaOvosVegetarianos(cat,entUtilizador):
   #CREATE A WINDOW
    janela = tk.Tk()
    w = 800
    h = 700
    ws = janela.winfo_screenwidth()
    hs = janela.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janela.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #SET THE TITLE OF THE WINDOW
    janela.title("Ovos Vegetarianos")

    #dont let the window resize
    janela.resizable(0,0)
    titulo_receita = "Ovos Vegetarianos"
    #ADD A TEXT BOX TO THE WINDOW
    text_box_ingredientes = tk.Text(janela, width=50, height=12)
    text_box_ingredientes.place(x=190, y=50)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_ingredientes.insert(tk.END,titulo_receita + "\n\nIngredientes:\n\n1/4 xícara de azeite de oliva\n1/2 cebola picada\n1/2 xícara de pimentão vermelho picado\n1/2 xícara de pimentão amarelo picado\n1/4 xícara de tomate picado\n2 dentes de alho picados\n3 ovos\n3 colheres de sopa de queijo ralado\nSal e pimenta a gosto")
    text_box_ingredientes.tag_configure("center", justify='center')
    text_box_ingredientes.tag_add("center", 1.0, "end")
    text_box_ingredientes.config(state=DISABLED)

    #ADD A TEXT BOX TO THE WINDOW
    text_box_intruçoes = tk.Text(janela, width=50, height=20)
    text_box_intruçoes.place(x=190, y=220)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_intruçoes.insert(tk.END, "Instruções:\n\n1. Aqueça o azeite em uma panela média\n2. Adicione a cebola, o pimentão, o tomate e o alho\n3. Cozinhe até que a cebola esteja macia\n4. Assim que a cebola estiver macia, adicione os ovos e mexa até que eles estejam quase cozidos\n5. Polvilhe o queijo por cima dos ovos\n6. Tempere com sal e pimenta a gosto\n7. Tampe a panela e cozinhe por mais alguns minutos ou até o ovo estar completamente cozido")
    text_box_intruçoes.tag_configure("center", justify='center')
    text_box_intruçoes.tag_add("center", 1.0, "end")
    text_box_intruçoes.config(state=DISABLED)

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=17, height=2, bg="#ffff00", command=lambda:marcarFavorito(cat,titulo_receita,entUtilizador))
    botao_favorito.place(x=190, y=550)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=17, height=2, bg="#1f77b4", command=lambda:comentar(titulo_receita,entUtilizador))
    botao_comentario.place(x=330,y=550)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(
        janela, text="Fechar", width=17, height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.place(x=470, y=550)

def janelaSopaCenoura(cat,entUtilizador):
   #CREATE A WINDOW
    janela = tk.Tk()
    w = 800
    h = 700
    ws = janela.winfo_screenwidth()
    hs = janela.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janela.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #SET THE TITLE OF THE WINDOW
    janela.title("Sopa de Cenoura")

    #dont let the window resize
    janela.resizable(0,0)
    titulo_receita = "Sopa de Cenoura"
    #ADD A TEXT BOX TO THE WINDOW
    text_box_ingredientes = tk.Text(janela, width=50, height=12)
    text_box_ingredientes.place(x=190, y=50)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_ingredientes.insert(tk.END,titulo_receita + "\n\nIngredientes:\n\n1 kg de cenouras\n1 cebola média\n3 dentes de alho\n1 litro de água\n2 colheres de sopa de azeite\nSal e pimenta a gosto\n2 folhas de louro")
    text_box_ingredientes.tag_configure("center", justify='center')
    text_box_ingredientes.tag_add("center", 1.0, "end")
    text_box_ingredientes.config(state=DISABLED)

    #ADD A TEXT BOX TO THE WINDOW
    text_box_intruçoes = tk.Text(janela, width=50, height=20)
    text_box_intruçoes.place(x=190, y=220)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_intruçoes.insert(tk.END, "Instruções:\n\n1. Lave, descasque e corte as cenouras em pedaços pequenos\n2. Em uma panela, coloque as cenouras, a cebola, o alho, a água, as folhas de louro, sal e pimenta a gosto e deixe cozinhar por 30 minutos\n3. Desligue o fogo e bata no liquidificador\n4. Volte a panela ao fogo, acrescente o azeite e deixe ferver por mais 10 minutos\n5. Sirva a sopa acompanhada de pão ou torradas")
    text_box_intruçoes.tag_configure("center", justify='center')
    text_box_intruçoes.tag_add("center", 1.0, "end")
    text_box_intruçoes.config(state=DISABLED)

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=17, height=2, bg="#ffff00", command=lambda:marcarFavorito(cat,titulo_receita,entUtilizador))
    botao_favorito.place(x=190, y=550)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=17, height=2, bg="#1f77b4", command=lambda:comentar(titulo_receita,entUtilizador))
    botao_comentario.place(x=330,y=550)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(
        janela, text="Fechar", width=17, height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.place(x=470, y=550)

def janelaSopaPedra(cat,entUtilizador):
   #CREATE A WINDOW
    janela = tk.Tk()
    w = 800
    h = 700
    ws = janela.winfo_screenwidth()
    hs = janela.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janela.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #SET THE TITLE OF THE WINDOW
    janela.title("Sopa Pedra")

    #dont let the window resize
    janela.resizable(0,0)
    titulo_receita = "Sopa Pedra"
    #ADD A TEXT BOX TO THE WINDOW
    text_box_ingredientes = tk.Text(janela, width=50, height=12)
    text_box_ingredientes.place(x=190, y=50)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_ingredientes.insert(tk.END,titulo_receita + "\n\nIngredientes:\n\n2 colheres de sopa de óleo\n1/2 cebola picada\n1 dente de alho picado\n2 xícaras de caldo de frango\n3 colheres de sopa de manteiga\n3 colheres de sopa de farinha\n1 xícara de leite\n2 xícaras de repolho picado\n1 xícara de cenoura picada\n1/2 xícara de salsinha picada\n1/2 xícara de salsa picada")
    text_box_ingredientes.tag_configure("center", justify='center')
    text_box_ingredientes.tag_add("center", 1.0, "end")
    text_box_ingredientes.config(state=DISABLED)

    #ADD A TEXT BOX TO THE WINDOW
    text_box_intruçoes = tk.Text(janela, width=50, height=20)
    text_box_intruçoes.place(x=190, y=220)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_intruçoes.insert(tk.END, "Instruções:\n\n1. Aqueça o óleo em uma panela grande\n2. Refogue a cebola e o alho até que fiquem macios\n3. Adicione o caldo de frango, a manteiga, a farinha, o leite, o repolho, a cenoura, a salsinha e a salsa\n4. Cozinhe em fogo médio por 20 minutos ou até que o repolho esteja macio\n5. Sirva a sopa em tigelas e polvilhe com salsinha para decorar")
    text_box_intruçoes.tag_configure("center", justify='center')
    text_box_intruçoes.tag_add("center", 1.0, "end")
    text_box_intruçoes.config(state=DISABLED)

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=17, height=2, bg="#ffff00", command=lambda:marcarFavorito(cat,titulo_receita,entUtilizador))
    botao_favorito.place(x=190, y=550)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=17, height=2, bg="#1f77b4", command=lambda:comentar(titulo_receita,entUtilizador))
    botao_comentario.place(x=330,y=550)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(
        janela, text="Fechar", width=17, height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.place(x=470, y=550)
    

def janelaSopaConquilha(cat,entUtilizador):
   #CRIAR UMA JANELA
    janela = tk.Tk()
    w = 800
    h = 700
    ws = janela.winfo_screenwidth()
    hs = janela.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janela.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #DEFINIR O TÍTULO DA JANELA
    janela.title("Sopa de Conchilha")

    #não permitir que a janela seja redimensionada
    janela.resizable(0,0)
    titulo_receita = "Sopa de Conchilha"
    #ADICIONAR UMA CAIXA DE TEXTO À JANELA
    text_box_ingredientes = tk.Text(janela, width=50, height=12)
    text_box_ingredientes.place(x=190, y=50)
    #ADICIONAR TEXTO À CAIXA DE TEXTO CENTRALIZADO
    text_box_ingredientes.insert(tk.END,titulo_receita + "\n\nIngredientes:\n\n2 xícaras de conchilha seca\n3 xícaras de água\n1/4 de xícara de azeite de oliva\n1/4 de xícara de cebola picada\n1/4 de xícara de alho picado\n1/4 de xícara de tomate picado\n1/4 de xícara de pimentão verde picado\n1/4 de xícara de pimentão vermelho picado\n1/4 de xícara de azeitona verde picada\n1/2 colher de chá de sal\n1/4 colher de chá de pimenta-do-reino\n1/4 de xícara de queijo parmesão ralado")
    text_box_ingredientes.tag_configure("center", justify='center')
    text_box_ingredientes.tag_add("center", 1.0, "end")
    text_box_ingredientes.config(state=DISABLED)

    #ADICIONAR UMA CAIXA DE TEXTO À JANELA
    text_box_intruçoes = tk.Text(janela, width=50, height=20)
    text_box_intruçoes.place(x=190, y=220)
    #ADICIONAR TEXTO À CAIXA DE TEXTO CENTRALIZADO
    text_box_intruçoes.insert(tk.END, "Instruções:\n\n1. Deixe as conchilhas de molho na água por 30 minutos\n2. Aqueça o azeite em uma panela grande em fogo médio\n3. Adicione a cebola, o alho, o tomate, o pimentão, a azeitona e o sal\n4. Cozinhe por 5 minutos ou até que a cebola esteja macia\n5. Adicione as conchilhas e a água\n6. Cozinhe por 20 minutos ou até que as conchilhas estejam macias\n7. Tempere com pimenta-do-reino\n8. Despeje a sopa em tigelas individuais e polvilhe com queijo parmesão")
    text_box_intruçoes.tag_configure("center", justify='center')
    text_box_intruçoes.tag_add("center", 1.0, "end")
    text_box_intruçoes.config(state=DISABLED)

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=17, height=2, bg="#ffff00", command=lambda:marcarFavorito(cat,titulo_receita,entUtilizador))
    botao_favorito.place(x=190, y=550)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=17, height=2, bg="#1f77b4", command=lambda:comentar(titulo_receita,entUtilizador))
    botao_comentario.place(x=330,y=550)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(
        janela, text="Fechar", width=17, height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.place(x=470, y=550)

def janelaSopaPeixe(cat,entUtilizador):
   #CREATE A WINDOW
    janela = tk.Tk()
    w = 800
    h = 700
    ws = janela.winfo_screenwidth()
    hs = janela.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janela.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #SET THE TITLE OF THE WINDOW
    janela.title("Sopa de Peixe")

    #dont let the window resize
    janela.resizable(0,0)
    titulo_receita = "Sopa de Peixe"
    #ADD A TEXT BOX TO THE WINDOW
    text_box_ingredientes = tk.Text(janela, width=50, height=12)
    text_box_ingredientes.place(x=190, y=50)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_ingredientes.insert(tk.END,titulo_receita + "\n\nIngredientes:\n\n1 cebola média picada\n1 dente de alho picado\n2 colheres de sopa de azeite\n2 colheres de sopa de manteiga\n2 xícaras de água\n1 xícara de vinho branco\n1/2 xícara de leite\n1 cubo de caldo de peixe\n2 colheres de sopa de suco de limão\n1/2 colher de chá de sal\n1/4 colher de chá de pimenta\n1 1/2 xícaras de peixe cozido e desfiado\n1 xícara de cogumelos fatiados\n1 xícara de pimentão picado\n1/2 xícara de azeitonas verdes fatiadas")
    text_box_ingredientes.tag_configure("center", justify='center')
    text_box_ingredientes.tag_add("center", 1.0, "end")
    text_box_ingredientes.config(state=DISABLED)

    #ADD A TEXT BOX TO THE WINDOW
    text_box_intruçoes = tk.Text(janela, width=50, height=20)
    text_box_intruçoes.place(x=190, y=220)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_intruçoes.insert(tk.END, "Instruções:\n\n1. Aqueça o azeite e a manteiga em uma panela\n2. Adicione a cebola e o alho e refogue por 5 minutos\n3. Adicione a água, o vinho, o leite, o caldo de peixe, o suco de limão, o sal e a pimenta\n4. Deixe ferver por 10 minutos\n5. Adicione o peixe, os cogumelos, o pimentão e as azeitonas\n6. Cozinhe por mais 10 minutos\n7. Sirva quente")
    text_box_intruçoes.tag_configure("center", justify='center')
    text_box_intruçoes.tag_add("center", 1.0, "end")
    text_box_intruçoes.config(state=DISABLED)

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=17, height=2, bg="#ffff00", command=lambda:marcarFavorito(cat,titulo_receita,entUtilizador))
    botao_favorito.place(x=190, y=550)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=17, height=2, bg="#1f77b4", command=lambda:comentar(titulo_receita,entUtilizador))
    botao_comentario.place(x=330,y=550)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(
        janela, text="Fechar", width=17, height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.place(x=470, y=550)

def janelaSopaJuliana(cat,entUtilizador):
   #CREATE A WINDOW
    janela = tk.Tk()
    w = 800
    h = 700
    ws = janela.winfo_screenwidth()
    hs = janela.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janela.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #SET THE TITLE OF THE WINDOW
    janela.title("Sopa Juliana")

    #dont let the window resize
    janela.resizable(0,0)
    titulo_receita = "Sopa Juliana"
    #ADD A TEXT BOX TO THE WINDOW
    text_box_ingredientes = tk.Text(janela, width=50, height=12)
    text_box_ingredientes.place(x=190, y=50)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_ingredientes.insert(tk.END,titulo_receita + "\n\nIngredientes:\n\n1/4 xícara de manteiga\n1/4 xícara de farinha\n3 xícaras de caldo de galinha\n2 xícaras de água\n1/2 xícara de cebola picada\n2 dentes de alho picados\n1/2 xícara de arroz\n1/2 xícara de cenoura ralada\n1/2 xícara de brócolis\n2 ovos cozidos picados\n1/4 xícara de salsa picada\n1/4 xícara de creme de leite\n1/4 xícara de queijo parmesão\nSal e pimenta a gosto")
    text_box_ingredientes.tag_configure("center", justify='center')
    text_box_ingredientes.tag_add("center", 1.0, "end")
    text_box_ingredientes.config(state=DISABLED)

    #ADD A TEXT BOX TO THE WINDOW
    text_box_intruçoes = tk.Text(janela, width=50, height=20)
    text_box_intruçoes.place(x=190, y=220)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_intruçoes.insert(tk.END, "Instruções:\n\n1. Aqueça a manteiga e misture a farinha\n2. Acrescente o caldo de galinha e a água, mexendo por 1 minuto\n3. Adicione a cebola, alho, arroz, cenoura, brócolis, ovos e salsa\n4. Cozinhe por 15 minutos ou até que o arroz esteja cozido\n5. Acrescente o creme de leite e o queijo parmesão\n6. Tempere com sal e pimenta a gosto\n7. Sirva quente ou frio")
    text_box_intruçoes.tag_configure("center", justify='center')
    text_box_intruçoes.tag_add("center", 1.0, "end")
    text_box_intruçoes.config(state=DISABLED)

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=17, height=2, bg="#ffff00", command=lambda:marcarFavorito(cat,titulo_receita,entUtilizador))
    botao_favorito.place(x=190, y=550)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=17, height=2, bg="#1f77b4", command=lambda:comentar(titulo_receita,entUtilizador))
    botao_comentario.place(x=330,y=550)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(
        janela, text="Fechar", width=17, height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.place(x=470, y=550)

def janelaSopaCaldoVerde(cat,entUtilizador):
    #CREATE A WINDOW
    janela = tk.Tk()
    w = 800
    h = 700
    ws = janela.winfo_screenwidth()
    hs = janela.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    janela.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #SET THE TITLE OF THE WINDOW
    janela.title("Sopa de Caldo Verde")

    #dont let the window resize
    janela.resizable(0,0)
    titulo_receita = "Sopa de Caldo Verde"
    #ADD A TEXT BOX TO THE WINDOW
    text_box_ingredientes = tk.Text(janela, width=50, height=12)
    text_box_ingredientes.place(x=190, y=50)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_ingredientes.insert(tk.END,titulo_receita + "\n\nIngredientes:\n\n1/4 xícara de azeite\n2 dentes de alho picados\n1 cebola média picada\n2 litros de caldo de legumes\n3 batatas médias cozidas e cortadas em cubos\n1/2 xícara de couve-flor congelada\n1/2 xícara de brócolis congelado\n2 xícaras de repolho roxo cortado em tiras finas\n1/4 xícara de salsinha picada\n1/4 xícara de cebolinha picada\nSal e pimenta a gosto")
    text_box_ingredientes.tag_configure("center", justify='center')
    text_box_ingredientes.tag_add("center", 1.0, "end")
    text_box_ingredientes.config(state=DISABLED)

    #ADD A TEXT BOX TO THE WINDOW
    text_box_intruçoes = tk.Text(janela, width=50, height=20)
    text_box_intruçoes.place(x=190, y=220)
    #ADD TEXT TO THE TEXT BOX CENTRALIZED
    text_box_intruçoes.insert(tk.END, "Instruções:\n\n1. Aqueça o azeite em uma panela grande em fogo médio\n2. Adicione o alho e a cebola e frite por 5 minutos\n3. Adicione o caldo de legumes, as batatas e os legumes congelados\n4. Deixe ferver por 10 minutos\n5. Adicione o repolho roxo e cozinhe por mais 5 minutos\n6. Desligue o fogo e misture a salsinha e a cebolinha\n7. Tempere com sal e pimenta a gosto\n8. Sirva quente")
    text_box_intruçoes.tag_configure("center", justify='center')
    text_box_intruçoes.tag_add("center", 1.0, "end")
    text_box_intruçoes.config(state=DISABLED)

    # Cria o botão para marcar a receita como favorita
    botao_favorito = tk.Button(
        janela, text="Marcar como Favorita", width=17, height=2, bg="#ffff00", command=lambda:marcarFavorito(cat,titulo_receita,entUtilizador))
    botao_favorito.place(x=190, y=550)

    # Cria o botão para adicionar um comentário
    botao_comentario = tk.Button(
        janela, text="Adicionar Comentário", width=17, height=2, bg="#1f77b4", command=lambda:comentar(titulo_receita,entUtilizador))
    botao_comentario.place(x=330,y=550)

    # Cria o botão para fechar a janela
    botao_fechar = tk.Button(
        janela, text="Fechar", width=17, height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.place(x=470, y=550)

# endregion

def guardarFicheiro(entTitulo, txtIngredientes, txtInstrucoes, entFoto,janelaReceita):
    # Get the values from the entry boxes
    

    fReceitas=open("./ficheiros/receitas.txt", "a",encoding="utf-8")

    #Le todas as linhas do texto ingredientes
    txtIngredientes = txtIngredientes.get("1.0", "end-1c")
    txtInstrucoes = txtInstrucoes.get("1.0", "end-1c")


    fReceitas.write(entTitulo + ";" + txtIngredientes + ";" + txtInstrucoes + ";" + entFoto + "\n")
    fReceitas.close()
    messagebox.showinfo("Sucesso", "Receita criada com sucesso!")
    janelaReceita.destroy()

def adicionarFoto(img):
    #abrir um filelog para selecionar a foto
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("png files","*.png"),("jpeg files",".jpg"),("all files","*.*")))
    img.set(filename)

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
    entTitulo.place(x=80, y=10)

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

    img=StringVar()
    entFoto = Entry(janelaReceita, width=30,textvariable=img)
    entFoto.place(x=80, y=300)

    # Botão para Guardar a direita
    btnGuardar = Button(janelaReceita, text="Guardar", width=20,height=7, command=lambda:guardarFicheiro(entTitulo.get(), txtIngredientes, txtInstrucoes, entFoto.get(),janelaReceita))
    btnGuardar.place(x=400, y=10)
    # Botão para adicionar foto

    
    btnFoto = Button(janelaReceita, text="Adicionar Foto", width=20,height=7, command=lambda:adicionarFoto(img))
    btnFoto.place(x=400, y=130)

    # Botão para Fechar a direita
    btnFechar = Button(janelaReceita, text="Fechar", width=20, height=7, command=janelaReceita.destroy)
    btnFechar.place(x=400, y=250)


#region Comentarios
#função para comentar
def comentar(titulo_receita,entUtilizador):
    # Create the main window
    window = tk.Tk()
    window.title("Comentar")

    x=500
    y=300

    # Get the screen width and height
    ws = window.winfo_screenwidth() # width of the screen
    hs = window.winfo_screenheight() # height of the screen

    #Centrar
    window.geometry('%dx%d+%d+%d' % (x, y, (ws/2)-(x/2), (hs/2)-(y/2)))

    # Label e entry comentario
    lblComentario=Label(window, text="Comentário:")
    lblComentario.place(x=10, y=10)

    #Textarea para o comentario
    entry_comentario = Text(window, width=40, height=5)
    entry_comentario.place(x=80, y=10)

    # Botão para Guardar a direita
    btnGuardar = Button(window, text="Guardar", width=20,height=5, command=lambda:guardarComentario(entry_comentario.get("1.0", "end-1c"), titulo_receita,entUtilizador))
    btnGuardar.place(x=10, y=150)

    #Botão para ver comentarios
    btnVerComentarios = Button(window, text="Ver Comentários", width=20,height=5, command=lambda:janelaVerComentarios(titulo_receita))
    btnVerComentarios.place(x=170, y=150)
    # Botão para Fechar a direita
    btnFechar = Button(window, text="Fechar", width=20, height=5 , command=window.destroy)
    btnFechar.place(x=330, y=150)

#função para guardar comentario
def guardarComentario(comentario, titulo_receita,entUtilizador):
    if entUtilizador == "":
        messagebox.showerror("Erro", "Tem de estar logado para comentar!")
        return
    
    # Get the values from the entry boxes
    fComentarios=open("./ficheiros/comentarios.txt", "a",encoding="utf-8")
    fComentarios.write(titulo_receita + ";" + entUtilizador + ";" + comentario + "\n")
    fComentarios.close()
    messagebox.showinfo("Comentário", "Obrigado pelo seu comentário!")
    window.destroy()

#função para ver comentarios
def janelaVerComentarios(titulo_receita):
    
    # Create the main window
    window = tk.Tk()
    window.title("Ver Receita")

    x=600
    y=400

    # Get the screen width and height
    ws = window.winfo_screenwidth() # width of the screen
    hs = window.winfo_screenheight() # height of the screen

    #Centrar
    window.geometry('%dx%d+%d+%d' % (x, y, (ws/2)-(x/2), (hs/2)-(y/2)))

    #Listbox com width e height da janela
    listbox = Listbox(window, width=90, height=20)
    listbox.place(x=10, y=10)

    #Botão para fechar
    btnFechar = Button(window, text="Fechar", width=15, command=window.destroy)
    btnFechar.place(x=10, y=350)
    inserirListbox(listbox,titulo_receita)

#Função para inserir na listbox
def inserirListbox(listbox,titulo_receita):

    fReceitas=open("./ficheiros/comentarios.txt", "r",encoding="utf-8")
    linhas=fReceitas.readlines()
    #Procurar comentarios com o titulo da receita
    for linha in linhas:
        campos=linha.split(";")
        if titulo_receita == campos[0]:
            print(campos[1] + " : " + campos[2])
            #Adicionar a listbox
            listbox.insert(END, campos[1] + " : " + campos[2])
    fReceitas.close()

#endregion

#region Gostos

def marcarFavorito(cat,titulo_receita, entUtilizador):
    
    if entUtilizador == "":
        messagebox.showerror("Erro", "Tem de estar logado para marcar como favorito")
    
    fGostos = open("ficheiros\\gostos.txt", "a",encoding="utf-8")
    fGostos.write(cat + ";" + titulo_receita + ";" + entUtilizador + "\n")
    fGostos.close()

    fGostos = open("ficheiros\\gostos.txt", "r")
    linhas = fGostos.readlines()
    fGostos.close()

    num=0

    #Contar linhas com o mesmo titulo
    for lin in linhas:
        campos=lin.split(";")
        
        if titulo_receita != campos[1]:
            pass
            
        num=linhas.count(lin)
            

    messagebox.showinfo("Gostos", "Obrigado pelo gosto,esta receita já conta com " + str(num) + " gostos")

#endregion

#region Ordernar
#Funçao para ordenar as categorias por gostos
def ordenarCategoriasGostos(catEntradas,catSopas,catCarnes,catPeixes,catSaladas,catVegeta):
    fGostos = open("ficheiros\\gostos.txt", "r")
    linhas = fGostos.readlines()
    

    ordenar=[]    
   
    #Contar linhas com a mesma categoria
    for lin in linhas:
        ordenar.append([])
        for i in range(len(linhas)):    
            campos=lin.split(";")
            if campos[0] == ~catEntradas:
                countEntradas=countEntradas+1
                ordenar.append(catEntradas, countEntradas)
            elif campos[0] == catSopas:
                countSopas=countSopas+1
                ordenar.append(catSopas, countSopas)
            elif campos[0] == catCarnes:
                countCarnes=countCarnes+1
                ordenar.append(catCarnes, countCarnes)
            elif campos[0] == catPeixes:
                countPeixes=countPeixes+1
                ordenar.append(catPeixes, countPeixes)
            elif campos[0] == catSaladas:
                countSaladas=countSaladas+1
                ordenar.append(catSaladas, countSaladas)
            elif campos[0] == catVegeta:
                countVegeta=countVegeta+1
                ordenar.append(catVegeta, countVegeta)

    fGostos.close()
    #Ordenar por ordem decrescente de gostos

    ordenar.sort(reverse=True)




        





    
            


#endregion