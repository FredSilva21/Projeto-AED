from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk



window = Tk()
window.title("ToDo Eat")
window.iconbitmap("./assets/icone.ico")
window.configure(bg="white")
originalWindow=window


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
    btnEntrar.place(x=360, y=200)
    

    # Interfaces não utilizadas na janela
    ctnImg.place_forget()
    lblBemVindo.place_forget()
    btnCriar.place_forget()
    btnConvid.place_forget()
    btnEntrarApp.place_forget()


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

    #Remove a interface da janela utilizador
    lblMinhaConta.place_forget()
    ctnFotoPerfil.place_forget()
    btnGuardarAlteracoes.place_forget()
    btnEscolherFoto.place_forget()   
    lblNomeUtilizador.place_forget() 

    #Interface janela convidado
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

    #Remove a interface da janela das Vegetarianas
    btnCanelone.place_forget()
    btnCogumelos.place_forget()
    btnFolhadinhos.place_forget()
    btnOvos.place_forget()

    #Remove a interface da janela das Sopas
    btnSopaCenoura.place_forget()
    btnSopaPedra.place_forget()
    btnSopaConquilha.place_forget()
    btnSopaPeixe.place_forget()

    #Remove a interface da janela utilizador
    lblMinhaConta.place_forget()
    ctnFotoPerfil.place_forget()
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
    
    print(appWidth)
    print(appHeigth)

    utilizadoresMenu = Menu(topBar)
    utilizadoresMenu.add_command(label="Utilizador",command=janelaConta)
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

    #Remove a interface da janela das Vegetarianas
    btnCanelone.place_forget()
    btnCogumelos.place_forget()
    btnFolhadinhos.place_forget()
    btnOvos.place_forget()

    #Remove a interface da janela das Sopas
    btnSopaCenoura.place_forget()
    btnSopaPedra.place_forget()
    btnSopaConquilha.place_forget()
    btnSopaPeixe.place_forget()

    #Remove a interface da janela utilizador
    lblMinhaConta.place_forget()
    ctnFotoPerfil.place_forget()
    btnVoltarPaginaInicial.place_forget()
    btnGuardarAlteracoes.place_forget()
    lblNomeUtilizador.place_forget()
    btnEscolherFoto.place_forget()


# endregion

# region Janela Admin

def janelaAppAdmin():
    # Resolução da Aplicação
    appWidth = screenWidth
    appHeigth = screenHeigth

    window.geometry("%dx%d" % (appWidth, appHeigth))
    window.state("zoomed")
    topBarAdmin = Menu(window)
    window.configure(bg="white", menu=topBarAdmin)
    window.title("ToDo Eat (Administrador)")
    print(appWidth)
    print(appHeigth)

    adminMenu = Menu(topBarAdmin)
    adminMenu.add_command(label="Utilizador")
    topBarAdmin.add_cascade(label="Minha Conta", menu=adminMenu)

    gerirCategoriasMenu = Menu(topBarAdmin)
    topBarAdmin.add_cascade(label="Gerir Categorias", menu=gerirCategoriasMenu)
    gerirCategoriasMenu.add_command(label="Gerir Categorias", command=escolha_categorias)

    gerirUtilizadoresMenu = Menu(topBarAdmin)
    gerirUtilizadoresMenu.add_command(label="Adicionar Utilizador")
    gerirUtilizadoresMenu.add_command(label="Remover Utilizador")
    topBarAdmin.add_cascade(label="Gerir Utilizadores", menu=gerirUtilizadoresMenu)

    ordenarMenu = Menu(topBarAdmin)
    ordenarMenu.add_command(label="Mais Popular")
    ordenarMenu.add_command(label="Mais Comentada")
    topBarAdmin.add_cascade(label="Ordenar", menu=ordenarMenu)

    favoritosMenu = Menu(topBarAdmin)
    favoritosMenu.add_command(label="Favoritos")
    topBarAdmin.add_cascade(label="Favoritos", menu=favoritosMenu)

    sairMenu = Menu(topBarAdmin)
    sairMenu.add_command(label="Sair", command=terminarSessao)

    criarReceita=Menu(topBarAdmin)
    criarReceita.add_cascade(label="Criar Receita")
    topBarAdmin.add_cascade(label="Criar Receita",menu=criarReceita)

    topBarAdmin.add_cascade(label="Sair", menu=sairMenu)

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
    topBar = Menu(window)
    window.configure(bg="white", menu=topBar)
    window.title("ToDo Eat (Convidado)")
    
    print(appWidth)
    print(appHeigth)

    utilizadoresMenu = Menu(topBar)
    utilizadoresMenu.add_command(label="Utilizador",command=mensageConv)
    topBar.add_cascade(label="Minha Conta", menu=utilizadoresMenu)

    ordenarMenu = Menu(topBar)
    ordenarMenu.add_command(label="Mais Popular",command=mensageConv)
    ordenarMenu.add_command(label="Mais Comentada",command=mensageConv)
    topBar.add_cascade(label="Ordenar", menu=ordenarMenu)

    favoritosMenu = Menu(topBar)
    favoritosMenu.add_command(label="Favoritos",command=mensageConv)
    topBar.add_cascade(label="Favoritos", menu=favoritosMenu)

    sairMenu = Menu(topBar)
    sairMenu.add_command(label="Sair", command=terminarSessao)

    criarReceita=Menu(topBar)
    criarReceita.add_cascade(label="Criar Receita",command=mensageConv)
    topBar.add_cascade(label="Criar Receita",menu=criarReceita)

    topBar.add_cascade(label="Sair", menu=sairMenu)

    lblMenuPrincipal.place(x=appWidth/2, y=80, anchor=CENTER)


    #Restringe algumas categorias
    btnCarnes.configure(command=mensageConv)
    btnSopas.configure(command=mensageConv)
    btnPeixes.configure(command=mensageConv)
    btnVegeta.configure(command=mensageConv)
    btnSaladas.configure(command=mensageConv)

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

    #Remove a interface da janela das Vegetarianas
    btnCanelone.place_forget()
    btnCogumelos.place_forget()
    btnFolhadinhos.place_forget()
    btnOvos.place_forget()

    #Remove a interface da janela das Sopas
    btnSopaCenoura.place_forget()
    btnSopaPedra.place_forget()
    btnSopaConquilha.place_forget()
    btnSopaPeixe.place_forget()
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

    btnSopaCenoura.place(x=300, y=180)
    btnSopaPedra.place(x=900, y=180)
    btnSopaConquilha.place(x=300, y=500)
    btnSopaPeixe.place(x=900, y=500)

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

    btnCanelone.place(x=300, y=180)
    btnCogumelos.place(x=900, y=180)
    btnFolhadinhos.place(x=300, y=500)
    btnOvos.place(x=900, y=500)

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

# region janela receitas

def janelaPao():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Receita")
    
    # Resolução da Janela
    appWidth = 1000
    appHeigth = 800

    # Centrar
    x = (screenWidth/2)-(appWidth/2)
    y = (screenHeigth/2)-(appHeigth/2)

    janela.geometry(f'{appWidth}x{appHeigth}+{int(x)}+{int(y)}')

    # Cria os rótulos
    titulo_receita = tk.Label(janela, text="Título da Receita")
    titulo_receita.pack()

    ingredientes = tk.Label(janela, text="Ingredientes:")
    ingredientes.pack()

    ingrediente_1 = tk.Label(janela, text="2 xícaras de farinha de trigo")
    ingrediente_1.pack()

    ingrediente_2 = tk.Label(janela, text="1 xícara de água morna")
    ingrediente_2.pack()

    ingrediente_3 = tk.Label(janela, text="200g de queijo ralado")
    ingrediente_3.pack()

    ingrediente_4 = tk.Label(janela, text="200g de chouriço fatiado")
    ingrediente_4.pack()

    # etc.

    instrucoes = tk.Label(janela, text="Instruções de Preparo:")
    instrucoes.pack()

    # Cria a área de texto para as instruções de preparo
    instrucoes_texto = tk.Text(janela)
    instrucoes_texto.pack()

    # Adiciona os dados da receita aos componentes
    titulo_receita["text"] = "Pão Recheado com Queijo e Chouriço"
    imgPao
    instrucoes_texto.insert(
        tk.END, "1. Em uma tigela, misture a farinha de trigo e o sal. Adicione a água morna e misture até formar uma massa homogênea.\n")
    instrucoes_texto.insert(
        tk.END, "2. Abra a massa em uma superfície lisa e espalhe o queijo ralado e o chouriço fatiado no centro da massa. Feche a massa sobre o recheio e forme um rolo.\n")
    instrucoes_texto.insert(
        tk.END, "3. Coloque o rolo em uma assadeira e leve ao forno pré-aquecido a 180°C por cerca de 30 minutos, ou até dourar. Sirva quente.\n")
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
    botao_fechar = tk.Button(
        janela, text="Fechar", width=20, height=2, bg="#ff0000", command=janela.destroy)
    botao_fechar.pack(side=tk.LEFT, padx=10, pady=10)


def janelaQuiche():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Receita")

    # Cria os rótulos
    titulo_receita = tk.Label(janela, text="Título da Receita")
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
# endregion

# region Janela Utilizador


def janelaConta():
    # Resolução da Aplicação
    appWidth = screenWidth
    appHeigth = screenHeigth

    window.geometry("%dx%d" % (appWidth, appHeigth))
    window.state("zoomed")
    topBar = Menu(window)
    window.configure(bg="white", menu=topBar)
    
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

    lblMinhaConta.place(x=appWidth/2, y=80, anchor=CENTER)

    lblNomeUtilizador.place(x=appWidth/4, y=150)

    ctnFotoPerfil.place(x=50,y=100)
    btnEscolherFoto.place(x=50,y=360)
    btnGuardarAlteracoes.place(x=50, y=420)
    btnVoltarPaginaInicial.place(x=1200, y=60)

    #Remove interface janela App
    btnEntradas.place_forget()
    btnSopas.place_forget()
    btnCarnes.place_forget()
    btnPeixes.place_forget()
    btnSaladas.place_forget()
    btnVegeta.place_forget()
    lblMenuPrincipal.place_forget()

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

    #Remove a interface da janela das Vegetarianas
    btnCanelone.place_forget()
    btnCogumelos.place_forget()
    btnFolhadinhos.place_forget()
    btnOvos.place_forget()

# endregion

#region Janela escolher Categorias
def escolha_categorias():

    #CRIAÇÃO DE UMA NOVA JANELA
    JanEscolha = Toplevel(window)
    JanEscolha.title("Escolha de Categorias")

    #DIMENSIONAR E CENTRAR A JANELA
    w = 450
    h = 230
    ws = JanEscolha.winfo_screenwidth()
    hs = JanEscolha.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    JanEscolha.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #TÍTULO DA PÁGINA
    lblEscolha = Label(JanEscolha, text="Escolha as Categorias que deseja:",font=("Calibri 11 bold"),width=40,height=1)
    lblEscolha.place(x=225,y=25,anchor=CENTER)

    #CRIAÇÃO DOS CHECK BUTTONS
    chkEntradas = Checkbutton(JanEscolha, text="Entradas", variable = chkEnt)
    chkSopas = Checkbutton(JanEscolha, text="Sopas", variable = chkSop)
    chkCarnes = Checkbutton(JanEscolha, text="Carnes", variable = chkCarn)
    chkPeixes = Checkbutton(JanEscolha, text="Peixes", variable = chkPeix)
    chkSaladas = Checkbutton(JanEscolha, text="Saladas", variable = chkSalad)
    chkVegeta = Checkbutton(JanEscolha, text="Vegetarianas", variable = chkVeget)

    #POSICIONAMENTO DOS CHECK BUTTONS
    chkEntradas.place(x=90, y=50)
    chkSopas.place(x=90,y=70)
    chkCarnes.place(x=90,y=90)
    chkPeixes.place(x=250,y=50)
    chkSaladas.place(x=250,y=70)
    chkVegeta.place(x=250,y=90)

    #BOTÃO DE CONFIRMAR A ESCOLHA 
    btn_confirmar=Button(JanEscolha,text="Confirmar",bg="green",font = ("Calibri 12 bold"),fg="white",width=10,height=1,command=janelaAppAdmin)
    btn_confirmar.place(x=225,y=190,anchor=CENTER)

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
        
    campos1=campos[3].split("\n")

   

    # CASO OS CAMPOS "UTILIZADOR" OU "PALAVRA-PASSE" ESTEJAM VAZIOS, RETORNA UM ERRO
    if nome == "" or passe == "":
        messagebox.showerror(
            "Erro", "Por favor forneça os seus dados de acesso.")
    
    
    # CASO OS DADOS DE ACESSO ESTEJAM CORRETOS, EFETUA LOGIN
    if nome != "" and passe != "":
        if campos[0] == nome and campos[2] == passe and campos1[0] == "admin":
            messagebox.showinfo("Bem vindo ADMINISTRADOR",
                                f"Olá {nome}! Está autenticado como ADMIN")
            entUtilizador.delete(0,"end")
            entPass.delete(0,"end")
            janelaAppAdmin()
            return campos[0]

        elif campos[0] == nome and campos[2] == passe and campos[3] == "user":
            messagebox.showinfo(
                "Bem vindo", f"Olá {nome}, o seu login foi efetuado com sucesso!")
            entUtilizador.delete(0,"end")
            entPass.delete(0,"end")
            janelaApp()
            return campos[0]

        # SE OS DADOS ESTIVEREM ERRADOS, RETORNA UM ERRO
        else:
            messagebox.showerror("Tentativa de Login sem sucesso",
                                 "Utilizador ou palavra-passe incorreta. Por favor tente novamente ou crie conta.")
            entPass.delete(0, "end")
# endregion

#region GESTÃO DE CATEGORIAS

#CRIAÇÃO DOS CHECK BUTTONS COMO VARIÁVEIS
chkEnt = IntVar()    #Entradas
chkEnt.set(1)
chkSop = IntVar()    #Sopas
chkSop.set(1)
chkCarn = IntVar()    #Carnes
chkCarn.set(1)
chkPeix = IntVar()    #Peixes
chkPeix.set(1)
chkSalad = IntVar() #Saladas
chkSalad.set(1)   
chkVeget = IntVar()  #Vegetarianas
chkVeget.set(1) 
#endregion


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
  instrucoes_texto.insert(
    END, "2. Em uma tigela, misture o açúcar, a farinha de trigo, o cacau em pó e o fermento.\n")
  instrucoes_texto.insert(
    END, "3. Adicione os ovos, o óleo e o leite e misture até formar uma massa homogênea.\n")
  # etc.





# region Convidado


def convidado():
    fBaseDados = open("./ficheiros/basedados.txt", "r", encoding="utf-8")
    linha = fBaseDados.readline()
    campos = linha.split(";")

    if campos[0] == "conv":
        messagebox.showinfo(
            "Bem vindo", f"Olá {campos[0]}, o seu login foi efetuado com sucesso!")
        janelaAppConvidado()

def mensageConv():
    messagebox.showinfo("Sem Acesso!","Convidados não tem acesso a esta parte da aplicação,por favor crie uma conta!")   
# endregion

# region Terminar Sessão

def terminarSessao():
    messagebox.showinfo("Sessão terminada", "Sessão terminada,volte sempre!")
    janelaInicial()
# endregion

# region Minha Conta

def escolherFoto():
    global image1
    image1 = filedialog.askopenfilename(initialdir="/", title="Select file",
                                        filetypes=(("png files", "*.png"), ("all files", "*.*")))

    image1 = PhotoImage(file = image1)
    ctnImg.itemconfig(image_id, image=image1)

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

btnJanelaLogin=Button(window, text="Entrar", fg="black",
                      bg="#99DDC8", width=10, height=1, command=janelaLogin)

# endregion

# region Interface Janela App

# Label Menu Principal
lblMenuPrincipal = Label(window, text="MENU PRINCIPAL", fg="black",
                         bg="white", font=("Playfair Bold", 20), width=30, height=1)

#Botão Voltar
btnVoltarApp=Button(window, text="Voltar", fg="black",
                   bg="#767B91", width=15, height=3, command=janelaApp)

# Barra Menu Utilizador

#region Imagens para os botões
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

#Imagens Saladas
imgSbacalhau=PhotoImage(file="./img/saladas/saladaBacalhau.png")
imgSbolonhesa=PhotoImage(file="./img/saladas/saladaBolonhesa.png")
imgSbulgur=PhotoImage(file="./img/saladas/saladaBulgur.png")
imgSdelicias=PhotoImage(file="./img/saladas/saladaDelicias.png")
imgSfrango=PhotoImage(file="./img/saladas/saladaFrango.png")
imgSsalsichas=PhotoImage(file="./img/saladas/saladaSalsicha.png")

#Imagens Vegetarianas
imgCanelone=PhotoImage(file="./img/vegetarianas/canelone.png")
imgCogumelos=PhotoImage(file="./img/vegetarianas/cogumelos.png")
imgCrepe=PhotoImage(file="./img/vegetarianas/crepe.png")
imgFolhadinhos=PhotoImage(file="./img/vegetarianas/folhadinhos.png")
imgMigas=PhotoImage(file="./img/vegetarianas/migas.png")
imgOvos=PhotoImage(file="./img/vegetarianas/ovos.png")


#Imagens Sopas
imgSopaCenoura=PhotoImage(file="./img/sopas/sopaCenoura.png")
imgSopaConquilha=PhotoImage(file="./img/sopas/sopaConquilha.png")
imgSopaPedra=PhotoImage(file="./img/sopas/sopaPedra.png")
imgSopaJuliana=PhotoImage(file="./img/sopas/sopaJuliana.png")
imgSopaPeixe=PhotoImage(file="./img/sopas/sopaPeixe.png")
imgCaldoVerde=PhotoImage(file="./img/sopas/CaldoVerde.png")
#endregion

#region Botões
# Botões com as categorias
btnEntradas = Button(window, width=350, height=250, image=imgEntradas,command=janelaEntradas)
btnSopas = Button(window, width=350, height=250, image=imgSopas,command=janelaSopas)
btnCarnes = Button(window, width=350, height=250, image=imgCarnes,command=janelaCarnes)
btnPeixes = Button(window, width=350, height=250, image=imgPeixes,command=janelaPeixes)
btnSaladas = Button(window, width=350, height=250, image=imgSaladas,command=janelaSaladas)
btnVegeta = Button(window, width=350, height=250, image=imgVegeta,command=janelaVegeta)

#Botões Entradas
btnPao = Button(window, width=350, height=250, image=imgPao,command=janelaPao)
btnPizza = Button(window, width=350, height=250, image=imgPizza,command=janelaPizza)
btnQuiche = Button(window, width=350, height=250, image=imgQuiche,command=janelaQuiche)
btnSupremo = Button(window, width=350, height=250, image=imgSupremo,command=janelaSupremo)
btnRissois = Button(window, width=350, height=250, image=imgRissois,command=janelaRissois)
btnTapas = Button(window, width=350, height=250, image=imgTapas,command=janelaTapas)

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

#Botões Vegetarianas
btnCanelone=Button(window, width=350, height=250, image=imgCanelone)
btnCogumelos=Button(window, width=350, height=250, image=imgCogumelos)
btnCrepe=Button(window, width=350, height=250, image=imgCrepe)
btnFolhadinhos=Button(window, width=350, height=250, image=imgFolhadinhos)
btnMigas=Button(window, width=350, height=250, image=imgFolhadinhos)
btnOvos=Button(window, width=350, height=250, image=imgOvos)

#Botões Sopas
btnSopaCenoura=Button(window, width=350, height=250, image=imgSopaCenoura)
btnSopaPedra=Button(window, width=350, height=250, image=imgSopaPedra)
btnSopaConquilha=Button(window, width=350, height=250, image=imgSopaConquilha)
btnSopaPeixe=Button(window, width=350, height=250, image=imgSopaPeixe)
btnSopaJuliana=Button(window, width=350, height=250, image=imgSopaJuliana)
btnCaldoVerde=Button(window, width=350, height=250, image=imgCaldoVerde)
#endregion
# endregion

#region Interface Conta Utilizador
lblMinhaConta=Label(window, text="MINHA CONTA", fg="black",
                         bg="white", font=("Playfair Bold", 20), width=30, height=1)

lblNomeUtilizador=Label(window, text="Nome de utilizador:", fg="black",
                            bg="white", font=("Playfair Bold", 15), width=30, height=1)

# Canvas para imagem
ctnFotoPerfil = Canvas(window, width=250, height=250,
                bd=0, relief="sunken", bg="white")

image1 = PhotoImage(file="img//fotoperfil.png")
image_id = ctnFotoPerfil.create_image(0, 0, anchor=NW, image=image1)

# Botão para escolher imagem
btnEscolherFoto = Button(window, text="Escolher foto", fg="black",
                            bg="white", font=("Playfair Bold", 15), width=22, height=1, command=escolherFoto)

# Botão para guardar alterações
btnGuardarAlteracoes = Button(window, text="Guardar alterações", fg="black",
                            bg="white", font=("Playfair Bold", 15), width=22, height=1)

btnVoltarPaginaInicial=Button(window, text="Voltar", fg="black",
                            bg="white", font=("Playfair Bold", 15), width=20, height=1, command=janelaApp)

lblFavoritos=Label(window, text="FAVORITOS", fg="black",
                            bg="white", font=("Playfair Bold", 20), width=30, height=1)

#endregion
janelaInicial()

window.mainloop()
