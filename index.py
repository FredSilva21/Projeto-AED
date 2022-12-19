from tkinter import *
from tkinter import messagebox



window = Tk()
window.title("ToDo Eat")
window.iconbitmap("./assets/icone.ico")
window.configure(bg="white")


screenWidth = window.winfo_screenwidth()
screenHeigth = window.winfo_screenheight()


#region Janela Login e Criar Conta
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

    #INSERE A LABEL E EMAIL DO UTILIZADOR
    lblEmail.place(x=60,y=50)
    entEmail.place(x=280,y=54)

    #INSERE LABEL E PALAVRA PASSE DO UTILIZADOR
    lblPass.place(x=50,y=80)
    entPass.place(x=280,y=84)
    
    #INSERE CONFIRMAÇÃO PALAVRA PASSE DO UTILIZADOR
    lblCpass.place(x=50,y=110)
    entCpass.place(x=280,y=114)

    #INSERE BOTÕES CRIAR E ENTRAR CONTA
    btnCriarConta.place(x=120,y=200)
    btnConvidUtil.place(x=240,y=200)
    btnVoltar.place(x=360,y=200)
    
    #Interfaces não utilizadas na janela
    ctnImg.place_forget()
    lblBemVindo.place_forget()
    btnCriar.place_forget()
    btnEntrar.place_forget()
    btnConvid.place_forget()
    topBar.place_forget()

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

    #INSERE LABEL E PALAVRA PASSE DO UTILIZADOR
    lblPass.place(x=50,y=80)
    entPass.place(x=280,y=84)
    
    #INSERE BOTÕES CRIAR E ENTRAR CONTA
    btnEntrarApp.place(x=120,y=200)
    btnCriar.place(x=240,y=200)
    btnVoltar.place(x=360,y=200)
    
    #Interfaces não utilizadas na janela
    ctnImg.place_forget()
    lblBemVindo.place_forget()
    btnCriarConta.place_forget()
    btnConvid.place_forget()
    lblEmail.place_forget()
    entEmail.place_forget()
    lblCpass.place_forget()
    entCpass.place_forget()
    btnEntrar.place_forget()
    topBar.place_forget()
# endregion

#region Window Inicial
def janelaInicial():
    # Janela Inicial

    # Obter resolução do portátil
    screenWidth = window.winfo_screenwidth()
    screenHeigth = window.winfo_screenheight()
    
    # Resolução da Aplicação
    appWidth = 600
    appHeigth = 400

    # Centrar
    x = (screenWidth/2)-(appWidth/2)
    y = (screenHeigth/2)-(appHeigth/2)

    window.geometry(f'{appWidth}x{appHeigth}+{int(x)}+{int(y)}')
    #Insere Imagem com Icone   
    ctnImg.place(x=185, y=50)
    
    #Insere Texto
    lblBemVindo.place(x=230, y=230)
    
    #Insere os botões
    btnCriar.place(x=130, y=280)
    btnEntrar.place(x=250, y=280)
    btnConvid.place(x=370, y=280)
    
    # Remove a interface não utilizada
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
    btnEntrarApp.place_forget()
    topBar.place_forget()
    destaquesBar.place_forget()
#endregion

#region Janela App
def janelaApp():
    # Resolução da Aplicação
    appWidth = screenWidth
    appHeigth = screenHeigth

    window.geometry("%dx%d" % (appWidth, appHeigth))
    window.state("zoomed")
    window.configure(bg="white")
    topBar.place(x=0,y=0)
    destaquesBar.place(x=0,y=100)
    
    btnInicio.place(x=340,y=25)
    btnCategorias.place(x=500,y=25)
    btnVideos.place(x=730,y=25)
    btnReceita.place(x=900,y=25)
    btnSair.place(x=1210,y=25)

    lblDestaques.place(x=10,y=10)
    btnPaoRecheado.place(x=100,y=80)
    btnSupremoCamem.place(x=460,y=80)
    btnPeruNatal.place(x=820,y=80)
    btnBifesPeru.place(x=1180,y=80)

    lblPaoRecheado.place(x=170,y=290)
    lblSupremoCamem.place(x=490,y=290)

    lblPeruNatal.place(x=900,y=290)
    lblBifesPeru.place(x=1250,y=290)

    #Interface não utilizada
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

#endregion

#region Janela App Convidado
def janelaAppConvidado():
    # Resolução da Aplicação
    appWidth = screenWidth
    appHeigth = screenHeigth

    window.geometry("%dx%d" % (appWidth, appHeigth))
    window.state("zoomed")
    window.configure(bg="grey")
    topBar.place(x=0,y=0)
    
    
    btnInicio.place(x=340,y=25)
    btnCategorias.place(x=500,y=25)
    btnVideos.place(x=730,y=25)
    btnReceita.place(x=900,y=25)


    #Interface não utilizada
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
#endregion

#region Criar Conta
def guardarConta(resultado):
    fBaseDados=open("./ficheiros/basedados.txt","a",encoding="utf-8")
    fBaseDados.write(resultado)
    fBaseDados.close()
    janelaLogin()

def verificarConta(nome,email,passe,cpasse,resultado):
    fBaseDados=open("./ficheiros/basedados.txt","r",encoding="utf-8")
    campos=[]
    if nome == "" or email == "" or passe== "" or cpasse == "":
        messagebox.showerror("Erro","Por favor forneça todos os dados corretamente.")

    if nome != "" and  passe != "":
        
        linhas=fBaseDados.readlines()
        for lin in linhas:
            campos=lin.split(";")
        
        if nome == campos[0]:
            messagebox.showerror("Erro","Já existe uma conta com esses dados, por favor efetue login.")

        #SE A PALAVRA-PASSE FOR CONFIRMADA CORRETAMENTE CRIA A CONTA  
        else:
            if passe == cpasse:
                guardarConta(resultado)
            else:
                messagebox.showerror("Erro","As duas passwords não coincidem.")

def criarConta():
    nome=entUtilizador.get()
    email=entEmail.get()
    passe=entPass.get()
    cpasse=entCpass.get()

    resultado="\n" + nome + ";" + email + ";" + passe + ";" + "user" 

    verificarConta(nome,email,passe,cpasse,resultado)

#endregion  
   
#region Login
def login():
    nome=entUtilizador.get()
    passe=entPass.get()

    #ABRE O FICHEIRO basedados.txt E PARA LEITURA
    fBaseDados = open("ficheiros/basedados.txt","r",encoding="utf-8")
    linhas = fBaseDados.readlines()
    campos=[]

    for lin in linhas:
        campos=lin.split(";")

    #CASO OS CAMPOS "UTILIZADOR" OU "PALAVRA-PASSE" ESTEJAM VAZIOS, RETORNA UM ERRO
    if nome == "" or  passe== "":
        messagebox.showerror("Erro","Por favor forneça os seus dados de acesso.")
    
    #CASO OS DADOS DE ACESSO ESTEJAM CORRETOS, EFETUA LOGIN
    if nome != "" and passe!= "":
        if campos[0]==nome and campos[2]==passe and campos[3]=="admin":
           messagebox.showinfo("Bem vindo ADMINISTRADOR",f"Olá {nome}! Está autenticado como ADMIN")
           janelaApp()
           return campos[0]
           

        elif campos[0]==nome and campos[2]==passe and campos[3]=="user":
            messagebox.showinfo("Bem vindo",f"Olá {nome}, o seu login foi efetuado com sucesso!")
            janelaApp()
            return campos[0]
            
        
        #SE OS DADOS ESTIVEREM ERRADOS, RETORNA UM ERRO
        else:
            messagebox.showerror("Tentativa de Login sem sucesso","Utilizador ou palavra-passe incorreta. Por favor tente novamente ou crie conta.")
            entPass.delete(0,"end") 
#endregion

#region Convidado
def convidado():
    fBaseDados=open("./ficheiros/basedados.txt","r",encoding="utf-8")
    linha=fBaseDados.readline()
    campos=linha.split(";")

    if campos[0]=="conv":
        messagebox.showinfo("Bem vindo",f"Olá {campos[0]}, o seu login foi efetuado com sucesso!")
        janelaApp()
        


#endregion

#region Terminar sessão
def terminarSessao():
    messagebox.showinfo("Sessão Terminada","Sessão Terminada! Volte sempre! :)")
    janelaInicial()
#endregion
#region Interface Window

# Canvas para imagem
ctnImg = Canvas(window, width=200, height=150,bd=-2, relief="sunken", bg="white")

# Imagem Icone
imgIcone = PhotoImage(file=".//img//icone.png")
ctnImg.create_image(100, 78, image=imgIcone)

# Label Bem Vindo
lblBemVindo = Label(window, text="Bem Vindo :)", fg="black",relief="raised", font=("Playfair",20), bd=-2, bg="white")

# Botão Criar Conta
btnCriar = Button(window, text="Criar Conta", fg="white",bg="#62C370", width=10, height=1,command=janelaCriarConta)

# Botão Entrar Conta
btnEntrar = Button(window, text="Entrar", fg="black",bg="#99DDC8", width=10, height=1, command=janelaLogin)

# Botão Entrar como Convidado
btnConvid = Button(window, text="Convidado", fg="black",bg="#CBDFBD", width=10, height=1,command=convidado)

#endregion

#region Interface Criar Conta e Login
#Label Utilizador
lblUtilizador = Label(window, text="       Nome de Utilizador:", fg="black",relief="raised", font="Playfair", bd=-2, bg="white")

#Entry Utilizador
entUtilizador = Entry(window, fg="black", width=25)

#Label Utilizador
lblEmail = Label(window, text="\t            Email:", fg="black",relief="raised", font="Playfair", bd=-2, bg="white")

#Entry Utilizador
entEmail = Entry(window, fg="black", width=25)

#Label Utilizador
lblPass = Label(window, text="\tPalavra-Passe:", fg="black",relief="raised", font="Playfair", bd=-2, bg="white")

#Entry Utilizador
entPass = Entry(window, fg="black", width=25,show="*")

#Label Utilizador
lblCpass = Label(window, text="Confirmar Palavra-Passe:", fg="black",relief="raised", font="Playfair", bd=-2, bg="white")

#Entry Utilizador
entCpass = Entry(window, fg="black", width=25,show="*")

# Botão Criar Conta do Utilizador
btnCriarConta = Button(window, text="Criar Conta", fg="white",bg="#62C370", width=10, height=1,command=criarConta)
btnConvidUtil=Button(window, text="Convidado", fg="black",bg="#CBDFBD", width=10, height=1,command=convidado)
btnVoltar=Button(window, text="Voltar", fg="black",bg="#767B91", width=10, height=1,command=janelaInicial)
btnEntrarApp=Button(window, text="Entrar", fg="black",bg="#99DDC8", width=10, height=1, command=login)

#endregion

#region Interface Janela App
topBar=PanedWindow(window,width=screenWidth,height=90,bd= -1,bg="#00FFFF")

#Menu Top Bar

#Botão Voltar ao inicio da app
btnInicio=Button(topBar,text="Início",fg="black",relief="raised", font=("Playfair",20), bd=-2, bg="#00FFFF",command=janelaApp)

#Categorias
btnCategorias=Button(topBar,text="Categorias",fg="black",relief="raised", font=("Playfair",20), bd=-2, bg="#00FFFF")

#Videos
btnVideos=Button(topBar,text="Videos",fg="black",relief="raised", font=("Playfair",20), bd=-2, bg="#00FFFF")

#Faça a sua receita
btnReceita=Button(topBar,text="Faça a sua receita",fg="black",relief="raised", font=("Playfair",20), bd=-2, bg="#00FFFF")

#Sair
btnSair=Button(topBar,text="Sair",fg="black",relief="raised", font=("Playfair",20), bd=-2, bg="#00FFFF",command=terminarSessao)

#Menu Destaques

#Barra de destaques 
destaquesBar=PanedWindow(window,width=screenWidth,height=350,bd= -1,bg="grey")

#Label destaques
lblDestaques=Label(destaquesBar, text="Destaques:", fg="black",relief="raised", font=("Playfair",20), bd=-2, bg="grey")

#Imagens Entradas
imgPaoRecheado=PhotoImage(file="./img/entradas/paorecheado.png")
imgSupremoCamem=PhotoImage(file="./img/entradas/supremodecamembert.png")

#Imagens Carnes
imgPeruNatal=PhotoImage(file="./img/carnes/perunatal.png")
imgBifesPeru=PhotoImage(file="./img/carnes/bifesperu.png")

#Botões Entradas
btnPaoRecheado=Button(destaquesBar,width=300,height=200,bd=-2, image=imgPaoRecheado,bg="grey")
btnSupremoCamem=Button(destaquesBar,width=300,height=200,bd=-2, image=imgSupremoCamem,bg="grey")

#Botoões Carnes
btnPeruNatal=Button(destaquesBar,width=300,height=200,bd=-2, image=imgPeruNatal,bg="grey")
btnBifesPeru=Button(destaquesBar,width=300,height=200,bd=-2, image=imgBifesPeru,bg="grey")

#Labels de Entradas
lblPaoRecheado=Label(destaquesBar, text="Pão Recheado", fg="black",relief="raised", font=("Playfair",16), bd=-2, bg="grey")
lblSupremoCamem=Label(destaquesBar, text="Supremo de Camembert", fg="black",relief="raised", font=("Playfair",16), bd=-2, bg="grey")

#Labels de Carnes
lblPeruNatal=Label(destaquesBar, text="Perú de Natal", fg="black",relief="raised", font=("Playfair",16), bd=-2, bg="grey")
lblBifesPeru=Label(destaquesBar, text="Bifes de Perú", fg="black",relief="raised", font=("Playfair",16), bd=-2, bg="grey")

#endregion

janelaInicial()

window.mainloop()
