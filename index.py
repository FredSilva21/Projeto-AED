from tkinter import *
from tkinter import messagebox


window = Tk()
window.title("ToDo Eat")
window.iconbitmap("./assets/icone.ico")
window.configure(bg="white")


screenWidth = window.winfo_screenwidth()
screenHeigth = window.winfo_screenheight()


# region Janela Login e Criar Conta
def janelaCriarConta():
    # Janela Inicial

    # Obter resolução do portátil
    screenWidth = window.winfo_screenwidth()
    screenHeigth = window.winfo_screenheight()

    # Resolução da Aplicação
    appWidth = 550
    appHeigth = 300

    # Centrar
    x = (screenWidth/2)-(appWidth/2)
    y = (screenHeigth/2)-(appHeigth/2)

    window.geometry(f'{appWidth}x{appHeigth}+{int(x)}+{int(y)}')

    # INSERE A LABEL E ENTRY DO UTILIZADOR
    lblUtilizador.place(x=60, y=20)
    entUtilizador.place(x=280, y=24)

    # INSERE A LABEL E EMAIL DO UTILIZADOR
    lblEmail.place(x=60, y=50)
    entEmail.place(x=280, y=54)

    # INSERE LABEL E PALAVRA PASSE DO UTILIZADOR
    lblPass.place(x=50, y=80)
    entPass.place(x=280, y=84)

    # INSERE CONFIRMAÇÃO PALAVRA PASSE DO UTILIZADOR
    lblCpass.place(x=50, y=110)
    entCpass.place(x=280, y=114)

    # INSERE BOTÕES CRIAR E ENTRAR CONTA
    btnCriarConta.place(x=120, y=200)
    btnConvidUtil.place(x=240, y=200)
    btnVoltar.place(x=360, y=200)

    # Interfaces não utilizadas na janela
    ctnImg.place_forget()
    lblBemVindo.place_forget()
    btnCriar.place_forget()
    btnEntrar.place_forget()
    btnConvid.place_forget()


def janelaLogin():
    # Janela Inicial

    # Obter resolução do portátil
    screenWidth = window.winfo_screenwidth()
    screenHeigth = window.winfo_screenheight()

    # Resolução da Aplicação
    appWidth = 550
    appHeigth = 300

    # Centrar
    x = (screenWidth/2)-(appWidth/2)
    y = (screenHeigth/2)-(appHeigth/2)

    window.geometry(f'{appWidth}x{appHeigth}+{int(x)}+{int(y)}')

    # INSERE A LABEL E ENTRY DO UTILIZADOR
    lblUtilizador.place(x=60, y=20)
    entUtilizador.place(x=280, y=24)

    # INSERE LABEL E PALAVRA PASSE DO UTILIZADOR
    lblPass.place(x=50, y=80)
    entPass.place(x=280, y=84)

    # INSERE BOTÕES CRIAR E ENTRAR CONTA
    btnEntrarApp.place(x=120, y=200)
    btnCriar.place(x=240, y=200)
    btnVoltar.place(x=360, y=200)

    # Interfaces não utilizadas na janela
    ctnImg.place_forget()
    lblBemVindo.place_forget()
    btnCriarConta.place_forget()
    btnConvid.place_forget()
    lblEmail.place_forget()
    entEmail.place_forget()
    lblCpass.place_forget()
    entCpass.place_forget()
    btnEntrar.place_forget()

# endregion

# region Window Inicial
def janelaInicial():
    # Janela Inicial
    
    # Obter resolução do portátil
    screenWidth = window.winfo_screenwidth()
    screenHeigth = window.winfo_screenheight()
    
    
    # Resolução da Aplicação
    appWidth =600
    appHeigth = 400

    # Centrar
    x = (screenWidth/2)-(appWidth/2)
    y = (screenHeigth/2)-(appHeigth/2)

    window.geometry(f'{appWidth}x{appHeigth}+{int(x)}+{int(y)}')
    

    window.configure(bg="white",menu="")
    print(x)
    print(y)
    # Insere Imagem com Icone
    ctnImg.place(x=185, y=50)

    # Insere Texto
    lblBemVindo.place(x=230, y=230)

    # Insere os botões
    btnCriar.place(x=130, y=280)
    btnEntrar.place(x=250, y=280)
    btnConvid.place(x=370, y=280)

    # Remove a interface da janela criar conta e login
    lblUtilizador.place_forget()
    entUtilizador.place_forget()
    lblEmail.place_forget()
    entEmail.place_forget()
    lblPass.place_forget()
    entPass.place_forget()
    lblCpass.place_forget()
    entCpass.place_forget()
    btnCriarConta.place_forget()
    btnConvidUtil.place_forget()
    btnVoltar.place_forget()

    #Remove a interface da janela app
    lblMenuPrincipal.place_forget()
    btnEntrarApp.place_forget()
    btnEntradas.place_forget()
    btnSopas.place_forget()
    btnCarnes.place_forget()
    btnPeixes.place_forget()
    btnSaladas.place_forget()
    btnVegeta.place_forget()
# endregion

# region Janela App


def janelaApp():
    # Resolução da Aplicação
    appWidth = screenWidth
    appHeigth = screenHeigth

    window.geometry("%dx%d" % (appWidth, appHeigth))
    window.state("zoomed")
    topBar = Menu(window)
    window.configure(bg="white", menu=topBar)
    window.resizable(False,False)
    print(appWidth)
    print(appHeigth)

    utilizadoresMenu = Menu(topBar)
    utilizadoresMenu.add_command(label="Utilizador")
    topBar.add_cascade(label="Minha Conta", menu=utilizadoresMenu)

    ordenarMenu = Menu(topBar)
    ordenarMenu.add_command(label="Mais Popular")
    ordenarMenu.add_command(label="Mais Comentada")
    topBar.add_cascade(label="Ordenar", menu=ordenarMenu)

    favoritosMenu = Menu(topBar)
    favoritosMenu.add_command(label="Favoritos")
    topBar.add_cascade(label="Favoritos", menu=favoritosMenu)

    sairMenu = Menu(topBar)
    sairMenu.add_command(label="Sair", command=terminarSessao)

    criarReceita=Menu(topBar)
    criarReceita.add_cascade(label="Criar Receita")
    topBar.add_cascade(label="Criar Receita",menu=criarReceita)

    topBar.add_cascade(label="Sair", menu=sairMenu)

    lblMenuPrincipal.place(x=appWidth/2, y=80, anchor=CENTER)

    

    btnEntradas.place(x=100, y=180)
    btnSopas.place(x=600, y=180)
    btnCarnes.place(x=1100, y=180)
    btnPeixes.place(x=100, y=500)
    btnSaladas.place(x=600, y=500)
    btnVegeta.place(x=1100, y=500)

    # Remove a interface da janela window e criar conta
    ctnImg.place_forget()
    lblBemVindo.place_forget()
    btnCriar.place_forget()
    btnEntrar.place_forget()
    btnConvid.place_forget()
    lblUtilizador.place_forget()
    entUtilizador.place_forget()
    lblPass.place_forget()
    entPass.place_forget()
    btnEntrarApp.place_forget()
    btnCriar.place_forget()
    btnVoltar.place_forget()
    
    #Remove a interface das janelas das Entradas
    btnVoltarApp.place_forget()
    btnPao.place_forget()
    btnPizza.place_forget()
    btnQuiche.place_forget()
    btnSupremo.place_forget()
    
    #Remove a interface da janela das Carnes
    btnFrancesinha.place_forget()
    btnPicanha.place_forget()
    btnBifesPeru.place_forget()
    btnFrango.place_forget()

    #Remove a interface da janela dos peixes
    btnbacalhau.place_forget()
    btnCamarao.place_forget()
    btnFeijoada.place_forget()
    btnPolvo.place_forget()

    #Remove a interface da janela das Saladas
    btnSbacalhau.place_forget()
    btnSbolonhesa.place_forget()
    btnSbulgur.place_forget()
    btnSdelicias.place_forget()

# endregion

# region Janela App Convidado


def janelaAppConvidado():
    # Resolução da Aplicação
    appWidth = screenWidth
    appHeigth = screenHeigth

    window.geometry("%dx%d" % (appWidth, appHeigth))
    window.state("zoomed")
    window.configure(bg="grey")

    # Interface não utilizada
    ctnImg.place_forget()
    lblBemVindo.place_forget()
    btnCriar.place_forget()
    btnEntrar.place_forget()
    btnConvid.place_forget()
    lblUtilizador.place_forget()
    entUtilizador.place_forget()
    lblPass.place_forget()
    entPass.place_forget()
    btnEntrarApp.place_forget()
    btnCriar.place_forget()
    btnVoltar.place_forget()
# endregion

# region Janela Entradas
def janelaEntradas():
    # Resolução da Aplicação
    appWidth = screenWidth
    appHeigth = screenHeigth

    window.geometry("%dx%d" % (appWidth, appHeigth))
    window.state("zoomed")
    topBar = Menu(window)
    window.configure(bg="white", menu=topBar)

    utilizadoresMenu = Menu(topBar)
    utilizadoresMenu.add_command(label="Utilizador")
    topBar.add_cascade(label="Minha Conta", menu=utilizadoresMenu)

    ordenarMenu = Menu(topBar)
    ordenarMenu.add_command(label="Mais Popular")
    ordenarMenu.add_command(label="Mais Comentada")
    topBar.add_cascade(label="Ordenar", menu=ordenarMenu)

    favoritosMenu = Menu(topBar)
    favoritosMenu.add_command(label="Favoritos")
    topBar.add_cascade(label="Favoritos", menu=favoritosMenu)

    sairMenu = Menu(topBar)
    sairMenu.add_command(label="Sair", command=terminarSessao)

    topBar.add_cascade(label="Sair", menu=sairMenu)

    lblMenuPrincipal.place(x=appWidth/2, y=80, anchor=CENTER)

    btnVoltarApp.place(x=80,y=70)

    btnPao.place(x=300, y=180)
    btnPizza.place(x=900, y=180)
    btnQuiche.place(x=300, y=500)
    btnSupremo.place(x=900, y=500)

    # Interface não utilizada
    ctnImg.place_forget()
    lblBemVindo.place_forget()
    btnCriar.place_forget()
    btnEntrar.place_forget()
    btnConvid.place_forget()
    lblUtilizador.place_forget()
    entUtilizador.place_forget()
    lblPass.place_forget()
    entPass.place_forget()
    btnEntrarApp.place_forget()
    btnCriar.place_forget()
    btnVoltar.place_forget()
    btnEntradas.place_forget()
    btnSopas.place_forget()
    btnCarnes.place_forget()
    btnPeixes.place_forget()
    btnSaladas.place_forget()
    btnVegeta.place_forget()
#endregion

# region Janela Carnes
def janelaCarnes():
    # Resolução da Aplicação
    appWidth = screenWidth
    appHeigth = screenHeigth

    window.geometry("%dx%d" % (appWidth, appHeigth))
    window.state("zoomed")
    topBar = Menu(window)
    window.configure(bg="white", menu=topBar)

    utilizadoresMenu = Menu(topBar)
    utilizadoresMenu.add_command(label="Utilizador")
    topBar.add_cascade(label="Minha Conta", menu=utilizadoresMenu)

    ordenarMenu = Menu(topBar)
    ordenarMenu.add_command(label="Mais Popular")
    ordenarMenu.add_command(label="Mais Comentada")
    topBar.add_cascade(label="Ordenar", menu=ordenarMenu)

    favoritosMenu = Menu(topBar)
    favoritosMenu.add_command(label="Favoritos")
    topBar.add_cascade(label="Favoritos", menu=favoritosMenu)

    sairMenu = Menu(topBar)
    sairMenu.add_command(label="Sair", command=terminarSessao)

    topBar.add_cascade(label="Sair", menu=sairMenu)

    lblMenuPrincipal.place(x=appWidth/2, y=80, anchor=CENTER)

    btnVoltarApp.place(x=80,y=70)

    btnFrancesinha.place(x=300, y=180)
    btnPicanha.place(x=900, y=180)
    btnBifesPeru.place(x=300, y=500)
    btnFrango.place(x=900, y=500)

    # Interface não utilizada
    ctnImg.place_forget()
    lblBemVindo.place_forget()
    btnCriar.place_forget()
    btnEntrar.place_forget()
    btnConvid.place_forget()
    lblUtilizador.place_forget()
    entUtilizador.place_forget()
    lblPass.place_forget()
    entPass.place_forget()
    btnEntrarApp.place_forget()
    btnCriar.place_forget()
    btnVoltar.place_forget()
    btnEntradas.place_forget()
    btnSopas.place_forget()
    btnCarnes.place_forget()
    btnPeixes.place_forget()
    btnSaladas.place_forget()
    btnVegeta.place_forget()
#endregion

# region Janela Sopas
def janelaSopas():
    # Resolução da Aplicação
    appWidth = screenWidth
    appHeigth = screenHeigth

    window.geometry("%dx%d" % (appWidth, appHeigth))
    window.state("zoomed")
    topBar = Menu(window)
    window.configure(bg="white", menu=topBar)

    utilizadoresMenu = Menu(topBar)
    utilizadoresMenu.add_command(label="Utilizador")
    topBar.add_cascade(label="Minha Conta", menu=utilizadoresMenu)

    ordenarMenu = Menu(topBar)
    ordenarMenu.add_command(label="Mais Popular")
    ordenarMenu.add_command(label="Mais Comentada")
    topBar.add_cascade(label="Ordenar", menu=ordenarMenu)

    favoritosMenu = Menu(topBar)
    favoritosMenu.add_command(label="Favoritos")
    topBar.add_cascade(label="Favoritos", menu=favoritosMenu)

    sairMenu = Menu(topBar)
    sairMenu.add_command(label="Sair", command=terminarSessao)

    topBar.add_cascade(label="Sair", menu=sairMenu)

    lblMenuPrincipal.place(x=appWidth/2, y=80, anchor=CENTER)

    btnVoltarApp.place(x=80,y=70)

    btnFrancesinha.place(x=300, y=180)
    btnPicanha.place(x=900, y=180)
    btnBifesPeru.place(x=300, y=500)
    btnFrango.place(x=900, y=500)

    # Interface não utilizada
    ctnImg.place_forget()
    lblBemVindo.place_forget()
    btnCriar.place_forget()
    btnEntrar.place_forget()
    btnConvid.place_forget()
    lblUtilizador.place_forget()
    entUtilizador.place_forget()
    lblPass.place_forget()
    entPass.place_forget()
    btnEntrarApp.place_forget()
    btnCriar.place_forget()
    btnVoltar.place_forget()
    btnEntradas.place_forget()
    btnSopas.place_forget()
    btnCarnes.place_forget()
    btnPeixes.place_forget()
    btnSaladas.place_forget()
    btnVegeta.place_forget()
#endregion

# region Janela Peixes
def janelaPeixes():
    # Resolução da Aplicação
    appWidth = screenWidth
    appHeigth = screenHeigth

    window.geometry("%dx%d" % (appWidth, appHeigth))
    window.state("zoomed")
    topBar = Menu(window)
    window.configure(bg="white", menu=topBar)

    utilizadoresMenu = Menu(topBar)
    utilizadoresMenu.add_command(label="Utilizador")
    topBar.add_cascade(label="Minha Conta", menu=utilizadoresMenu)

    ordenarMenu = Menu(topBar)
    ordenarMenu.add_command(label="Mais Popular")
    ordenarMenu.add_command(label="Mais Comentada")
    topBar.add_cascade(label="Ordenar", menu=ordenarMenu)

    favoritosMenu = Menu(topBar)
    favoritosMenu.add_command(label="Favoritos")
    topBar.add_cascade(label="Favoritos", menu=favoritosMenu)

    sairMenu = Menu(topBar)
    sairMenu.add_command(label="Sair", command=terminarSessao)

    topBar.add_cascade(label="Sair", menu=sairMenu)

    lblMenuPrincipal.place(x=appWidth/2, y=80, anchor=CENTER)

    btnVoltarApp.place(x=80,y=70)

    btnbacalhau.place(x=300, y=180)
    btnCamarao.place(x=900, y=180)
    btnFeijoada.place(x=300, y=500)
    btnPolvo.place(x=900, y=500)

    # Interface não utilizada
    ctnImg.place_forget()
    lblBemVindo.place_forget()
    btnCriar.place_forget()
    btnEntrar.place_forget()
    btnConvid.place_forget()
    lblUtilizador.place_forget()
    entUtilizador.place_forget()
    lblPass.place_forget()
    entPass.place_forget()
    btnEntrarApp.place_forget()
    btnCriar.place_forget()
    btnVoltar.place_forget()
    btnEntradas.place_forget()
    btnSopas.place_forget()
    btnCarnes.place_forget()
    btnPeixes.place_forget()
    btnSaladas.place_forget()
    btnVegeta.place_forget()
#endregion

# region Janela Saladas
def janelaSaladas():
    # Resolução da Aplicação
    appWidth = screenWidth
    appHeigth = screenHeigth

    window.geometry("%dx%d" % (appWidth, appHeigth))
    window.state("zoomed")
    topBar = Menu(window)
    window.configure(bg="white", menu=topBar)

    utilizadoresMenu = Menu(topBar)
    utilizadoresMenu.add_command(label="Utilizador")
    topBar.add_cascade(label="Minha Conta", menu=utilizadoresMenu)

    ordenarMenu = Menu(topBar)
    ordenarMenu.add_command(label="Mais Popular")
    ordenarMenu.add_command(label="Mais Comentada")
    topBar.add_cascade(label="Ordenar", menu=ordenarMenu)

    favoritosMenu = Menu(topBar)
    favoritosMenu.add_command(label="Favoritos")
    topBar.add_cascade(label="Favoritos", menu=favoritosMenu)

    sairMenu = Menu(topBar)
    sairMenu.add_command(label="Sair", command=terminarSessao)

    topBar.add_cascade(label="Sair", menu=sairMenu)

    lblMenuPrincipal.place(x=appWidth/2, y=80, anchor=CENTER)

    btnVoltarApp.place(x=80,y=70)

    btnSbacalhau.place(x=300, y=180)
    btnSbolonhesa.place(x=900, y=180)
    btnSbulgur.place(x=300, y=500)
    btnSdelicias.place(x=900, y=500)

    # Interface não utilizada
    ctnImg.place_forget()
    lblBemVindo.place_forget()
    btnCriar.place_forget()
    btnEntrar.place_forget()
    btnConvid.place_forget()
    lblUtilizador.place_forget()
    entUtilizador.place_forget()
    lblPass.place_forget()
    entPass.place_forget()
    btnEntrarApp.place_forget()
    btnCriar.place_forget()
    btnVoltar.place_forget()
    btnEntradas.place_forget()
    btnSopas.place_forget()
    btnCarnes.place_forget()
    btnPeixes.place_forget()
    btnSaladas.place_forget()
    btnVegeta.place_forget()
#endregion

# region Janela Vegetariana
def janelaVegeta():
    # Resolução da Aplicação
    appWidth = screenWidth
    appHeigth = screenHeigth

    window.geometry("%dx%d" % (appWidth, appHeigth))
    window.state("zoomed")
    topBar = Menu(window)
    window.configure(bg="white", menu=topBar)

    utilizadoresMenu = Menu(topBar)
    utilizadoresMenu.add_command(label="Utilizador")
    topBar.add_cascade(label="Minha Conta", menu=utilizadoresMenu)

    ordenarMenu = Menu(topBar)
    ordenarMenu.add_command(label="Mais Popular")
    ordenarMenu.add_command(label="Mais Comentada")
    topBar.add_cascade(label="Ordenar", menu=ordenarMenu)

    favoritosMenu = Menu(topBar)
    favoritosMenu.add_command(label="Favoritos")
    topBar.add_cascade(label="Favoritos", menu=favoritosMenu)

    sairMenu = Menu(topBar)
    sairMenu.add_command(label="Sair", command=terminarSessao)

    topBar.add_cascade(label="Sair", menu=sairMenu)

    lblMenuPrincipal.place(x=appWidth/2, y=80, anchor=CENTER)

    btnVoltarApp.place(x=80,y=70)

    btnFrancesinha.place(x=300, y=180)
    btnPicanha.place(x=900, y=180)
    btnBifesPeru.place(x=300, y=500)
    btnFrango.place(x=900, y=500)

    # Interface não utilizada
    ctnImg.place_forget()
    lblBemVindo.place_forget()
    btnCriar.place_forget()
    btnEntrar.place_forget()
    btnConvid.place_forget()
    lblUtilizador.place_forget()
    entUtilizador.place_forget()
    lblPass.place_forget()
    entPass.place_forget()
    btnEntrarApp.place_forget()
    btnCriar.place_forget()
    btnVoltar.place_forget()
    btnEntradas.place_forget()
    btnSopas.place_forget()
    btnCarnes.place_forget()
    btnPeixes.place_forget()
    btnSaladas.place_forget()
    btnVegeta.place_forget()
#endregion

# region Criar Conta


def guardarConta(resultado):
    fBaseDados = open("./ficheiros/basedados.txt", "a", encoding="utf-8")
    fBaseDados.write(resultado)
    fBaseDados.close()
    janelaLogin()


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

        if nome == campos[0]:
            messagebox.showerror(
                "Erro", "Já existe uma conta com esses dados, por favor efetue login.")

        # SE A PALAVRA-PASSE FOR CONFIRMADA CORRETAMENTE CRIA A CONTA
        else:
            if passe == cpasse:
                guardarConta(resultado)
            else:
                messagebox.showerror(
                    "Erro", "As duas passwords não coincidem.")


def criarConta():
    nome = entUtilizador.get()
    email = entEmail.get()
    passe = entPass.get()
    cpasse = entCpass.get()

    resultado = "\n" + nome + ";" + email + ";" + passe + ";" + "user"

    verificarConta(nome, email, passe, cpasse, resultado)

# endregion

# region Login


def login():
    nome = entUtilizador.get()
    passe = entPass.get()

    # ABRE O FICHEIRO basedados.txt E PARA LEITURA
    fBaseDados = open("ficheiros/basedados.txt", "r", encoding="utf-8")
    linhas = fBaseDados.readlines()
    campos = []

    for lin in linhas:
        campos = lin.split(";")

    # CASO OS CAMPOS "UTILIZADOR" OU "PALAVRA-PASSE" ESTEJAM VAZIOS, RETORNA UM ERRO
    if nome == "" or passe == "":
        messagebox.showerror(
            "Erro", "Por favor forneça os seus dados de acesso.")

    # CASO OS DADOS DE ACESSO ESTEJAM CORRETOS, EFETUA LOGIN
    if nome != "" and passe != "":
        if campos[0] == nome and campos[2] == passe and campos[3] == "admin":
            messagebox.showinfo("Bem vindo ADMINISTRADOR",
                                f"Olá {nome}! Está autenticado como ADMIN")
            janelaApp()
            return campos[0]

        elif campos[0] == nome and campos[2] == passe and campos[3] == "user":
            messagebox.showinfo(
                "Bem vindo", f"Olá {nome}, o seu login foi efetuado com sucesso!")
            janelaApp()
            return campos[0]

        # SE OS DADOS ESTIVEREM ERRADOS, RETORNA UM ERRO
        else:
            messagebox.showerror("Tentativa de Login sem sucesso",
                                 "Utilizador ou palavra-passe incorreta. Por favor tente novamente ou crie conta.")
            entPass.delete(0, "end")
# endregion

def criar_janela_receita():
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
  instrucoes_texto.insert(END, "2. Em uma tigela, misture o açúcar, a farinha de trigo, o cacau em pó e o fermento.\n")
  instrucoes_texto.insert(END, "3. Adicione os ovos, o óleo e o leite e misture até formar uma massa homogênea.\n")
  # etc.


# region Convidado


def convidado():
    fBaseDados = open("./ficheiros/basedados.txt", "r", encoding="utf-8")
    linha = fBaseDados.readline()
    campos = linha.split(";")

    if campos[0] == "conv":
        messagebox.showinfo(
            "Bem vindo", f"Olá {campos[0]}, o seu login foi efetuado com sucesso!")
        janelaApp()


# endregion

# region Terminar Sessão
def terminarSessao():
    messagebox.showinfo("Sessão terminada", "Sessão terminada,volte sempre!")
    janelaInicial()
# endregion

# region Interface Window


# Canvas para imagem
ctnImg = Canvas(window, width=200, height=150,
                bd=-2, relief="sunken", bg="white")

# Imagem Icone
imgIcone = PhotoImage(file=".//img//icone.png")
ctnImg.create_image(100, 78, image=imgIcone)

# Label Bem Vindo
lblBemVindo = Label(window, text="Bem Vindo :)", fg="black",
                    relief="raised", font=("Playfair", 20), bd=-2, bg="white")

# Botão Criar Conta
btnCriar = Button(window, text="Criar Conta", fg="white",
                  bg="#62C370", width=10, height=1, command=janelaCriarConta)

# Botão Entrar Conta
btnEntrar = Button(window, text="Entrar", fg="black",
                   bg="#99DDC8", width=10, height=1, command=janelaLogin)

# Botão Entrar como Convidado
btnConvid = Button(window, text="Convidado", fg="black",
                   bg="#CBDFBD", width=10, height=1, command=convidado)

# endregion

# region Interface Criar Conta e Login
# Label Utilizador
lblUtilizador = Label(window, text="       Nome de Utilizador:",
                      fg="black", relief="raised", font="Playfair", bd=-2, bg="white")

# Entry Utilizador
entUtilizador = Entry(window, fg="black", width=25)

# Label Utilizador
lblEmail = Label(window, text="\t            Email:", fg="black",
                 relief="raised", font="Playfair", bd=-2, bg="white")

# Entry Utilizador
entEmail = Entry(window, fg="black", width=25)

# Label Utilizador
lblPass = Label(window, text="\tPalavra-Passe:", fg="black",
                relief="raised", font="Playfair", bd=-2, bg="white")

# Entry Utilizador
entPass = Entry(window, fg="black", width=25, show="*")

# Label Utilizador
lblCpass = Label(window, text="Confirmar Palavra-Passe:", fg="black",
                 relief="raised", font="Playfair", bd=-2, bg="white")

# Entry Utilizador
entCpass = Entry(window, fg="black", width=25, show="*")

# Botão Criar Conta do Utilizador
btnCriarConta = Button(window, text="Criar Conta", fg="white",
                       bg="#62C370", width=10, height=1, command=criarConta)
btnConvidUtil = Button(window, text="Convidado", fg="black",
                       bg="#CBDFBD", width=10, height=1, command=convidado)
btnVoltar = Button(window, text="Voltar", fg="black",
                   bg="#767B91", width=10, height=1, command=janelaInicial)
btnEntrarApp = Button(window, text="Entrar", fg="black",
                      bg="#99DDC8", width=10, height=1, command=login)

# endregion

# region Interface Janela App

# Label Menu Principal
lblMenuPrincipal = Label(window, text="MENU PRINCIPAL", fg="black",
                         bg="white", font=("Playfair Bold", 20), width=30, height=1)

#Botão Voltar
btnVoltarApp=Button(window, text="Voltar", fg="black",
                   bg="#767B91", width=15, height=3, command=janelaApp)

# Barra Menu Utilizador

#Imagens Categorias
imgCarnes=PhotoImage(file="./img/categorias/catCarnes.png")
imgEntradas=PhotoImage(file="./img/categorias/catEntradas.png")
imgSopas=PhotoImage(file="./img/categorias/catSopas.png")
imgPeixes=PhotoImage(file="./img/categorias/catPeixes.png")
imgSaladas=PhotoImage(file="./img/categorias/catSaladas.png")
imgVegeta=PhotoImage(file="./img/categorias/catVegeta.png")

# Imagens Entradas
imgPao = PhotoImage(file="./img/entradas/paorecheado.png")
imgSupremo = PhotoImage(file="./img/entradas/supremodecamembert.png")
imgPizza = PhotoImage(file="./img/entradas/pizzadenatal.png")
imgQuiche=PhotoImage(file="./img/entradas/quichequeijo.png")
imgRissois=PhotoImage(file="./img/entradas/rissois.png")
imgTapas=PhotoImage(file="./img/entradas/tapas.png")

# Imagens Carnes
imgFrancesinha=PhotoImage(file="./img/carnes/francesinha.png")
imgBifesPeru = PhotoImage(file="./img/carnes/bifesperu.png")
imgPicanha=PhotoImage(file="./img/carnes/picanha.png")
imgCaril=PhotoImage(file="./img/carnes/caril.png")
imgFrango=PhotoImage(file="./img/carnes/frango.png")
imgEmpadao=PhotoImage(file="./img/carnes/empadao.png")

#Imagens Peixes
imgBacalhau=PhotoImage(file="./img/peixes/bacalhau.png")
imgCamarao=PhotoImage(file="./img/peixes/camarao.png")
imgFeijoada=PhotoImage(file="./img/peixes/feijoada.png")
imgGaroupa=PhotoImage(file="./img/peixes/garoupa.png")
imgPolvo=PhotoImage(file="./img/peixes/polvo.png")
imgSalmao=PhotoImage(file="./img/peixes/salmao.png")

#Botões Saladas
imgSbacalhau=PhotoImage(file="./img/saladas/saladaBacalhau.png")
imgSbolonhesa=PhotoImage(file="./img/saladas/saladaBolonhesa.png")
imgSbulgur=PhotoImage(file="./img/saladas/saladaBulgur.png")
imgSdelicias=PhotoImage(file="./img/saladas/saladaDelicias.png")
imgSfrango=PhotoImage(file="./img/saladas/saladaFrango.png")
imgSsalsichas=PhotoImage(file="./img/saladas/saladaSalsicha.png")



# Botões com as categorias
btnEntradas = Button(window, width=350, height=250, image=imgEntradas,command=janelaEntradas)
btnSopas = Button(window, width=350, height=250, image=imgSopas,command=janelaSopas)
btnCarnes = Button(window, width=350, height=250, image=imgCarnes,command=janelaCarnes)
btnPeixes = Button(window, width=350, height=250, image=imgPeixes,command=janelaPeixes)
btnSaladas = Button(window, width=350, height=250, image=imgSaladas,command=janelaSaladas)
btnVegeta = Button(window, width=350, height=250, image=imgVegeta,command=janelaVegeta)

#Botões Entradas
btnPao = Button(window, width=350, height=250, image=imgPao)
btnPizza = Button(window, width=350, height=250, image=imgPizza)
btnQuiche = Button(window, width=350, height=250, image=imgQuiche)
btnSupremo = Button(window, width=350, height=250, image=imgSupremo)
btnRissois = Button(window, width=350, height=250, image=imgRissois)
btnTapas = Button(window, width=350, height=250, image=imgTapas)

#Botões Carnes
btnFrancesinha = Button(window, width=350, height=250, image=imgFrancesinha)
btnBifesPeru = Button(window, width=350, height=250, image=imgBifesPeru)
btnPicanha = Button(window, width=350, height=250, image=imgPicanha)
btnCaril = Button(window, width=350, height=250, image=imgCaril)
btnFrango = Button(window, width=350, height=250, image=imgFrango)
btnEmpadao = Button(window, width=350, height=250, image=imgEmpadao)

#Botões Peixes
btnbacalhau = Button(window, width=350, height=250, image=imgBacalhau)
btnCamarao = Button(window, width=350, height=250, image=imgCamarao)
btnFeijoada = Button(window, width=350, height=250, image=imgFeijoada)
btnGaroupa = Button(window, width=350, height=250, image=imgGaroupa)
btnPolvo = Button(window, width=350, height=250, image=imgPolvo)
btnSalmao = Button(window, width=350, height=250, image=imgSalmao)

#Botões Saladas
btnSbacalhau=Button(window, width=350, height=250, image=imgSbacalhau)
btnSbolonhesa=Button(window, width=350, height=250, image=imgSbolonhesa)
btnSbulgur=Button(window, width=350, height=250, image=imgSbulgur)
btnSdelicias=Button(window, width=350, height=250, image=imgSdelicias)
btnSfrango=Button(window, width=350, height=250, image=imgSfrango)
btnSsalsichas=Button(window, width=350, height=250, image=imgSsalsichas)
# endregion


janelaInicial()

window.mainloop()
