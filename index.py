from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk
from tkVideoPlayer import TkinterVideo 


from users import *
from receitas import *
from admin import *
from receitas import *


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
    criarReceita.add_cascade(label="Criar Receita",command=janelaCriarReceita)
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
    
    adminMenu = Menu(topBarAdmin)
    adminMenu.add_command(label="Utilizador")
    topBarAdmin.add_cascade(label="Minha Conta", menu=adminMenu)

    gerirCategoriasMenu = Menu(topBarAdmin)
    topBarAdmin.add_cascade(label="Gerir Categorias", menu=gerirCategoriasMenu)
    gerirCategoriasMenu.add_command(label="Adicionar Categoria", command=lambda:janelaAddCategoria(window,categorias))
    gerirCategoriasMenu.add_command(label="Remover Categoria", command=lambda:janelaRemCategoria(window,categorias))

    gerirUtilizadoresMenu = Menu(topBarAdmin)
    gerirUtilizadoresMenu.add_command(label="Adicionar Utilizador",command=lambda:janelaAddUtilizador(window))
    gerirUtilizadoresMenu.add_command(label="Remover Utilizador",command=lambda:janelaRemUtilizador(window))
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
                   bg="#CBDFBD", width=10, height=1, command=lambda:convidado(janelaAppConvidado))

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
                       bg="#62C370", width=10, height=1, command=lambda:criarConta(entUtilizador.get(),entEmail.get(),entPass.get(),entCpass.get(),janelaLogin))
btnConvidUtil = Button(window, text="Convidado", fg="black",
                       bg="#CBDFBD", width=10, height=1, command=lambda:convidado(janelaAppConvidado))
btnVoltar = Button(window, text="Voltar", fg="black",
                   bg="#767B91", width=10, height=1, command=janelaInicial)
btnEntrarApp = Button(window, text="Entrar", fg="black",
                      bg="#99DDC8", width=10, height=1, command=lambda:login(entUtilizador.get(),entPass.get(),janelaAppAdmin,janelaApp))

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

categorias=[["Entradas","./img/categorias/catEntradas.png"],["Sopas","./img/categorias/catSopas.png"],["Carnes","./img/categorias/catCarnes.png"],["Peixes","./img/categorias/catPeixes.png"],["Saladas","./img/categorias/catSaladas.png"],["Vegetarianas","./img/categorias/catVegeta.png"]]


#region Imagens para os botões
#Imagens Categorias

imgEntradas=PhotoImage(file=categorias[0][1])
imgSopas=PhotoImage(file=categorias[1][1])
imgCarnes=PhotoImage(file=categorias[2][1])
imgPeixes=PhotoImage(file=categorias[3][1])
imgSaladas=PhotoImage(file=categorias[4][1])
imgVegeta=PhotoImage(file=categorias[5][1])

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
btnFrancesinha = Button(window, width=350, height=250, image=imgFrancesinha,command=janelaFrancesinha)
btnBifesPeru = Button(window, width=350, height=250, image=imgBifesPeru,command=janelaBifesPeru)
btnPicanha = Button(window, width=350, height=250, image=imgPicanha,command=janelaPicanha)
btnCaril = Button(window, width=350, height=250, image=imgCaril,command=janelaCaril)
btnFrango = Button(window, width=350, height=250, image=imgFrango,command=janelaFrango)
btnEmpadao = Button(window, width=350, height=250, image=imgEmpadao,command=janelaEmpadaoCarne)

#Botões Peixes
btnbacalhau = Button(window, width=350, height=250, image=imgBacalhau,command=janelaBacalhau)
btnCamarao = Button(window, width=350, height=250, image=imgCamarao,command=janelaCamarao)
btnFeijoada = Button(window, width=350, height=250, image=imgFeijoada,command=janelaFeijoadaPeixe)
btnGaroupa = Button(window, width=350, height=250, image=imgGaroupa,command=janelaGaropa)
btnPolvo = Button(window, width=350, height=250, image=imgPolvo,command=janelaPolvo)
btnSalmao = Button(window, width=350, height=250, image=imgSalmao,command=janelaSalmao)

#Botões Saladas
btnSbacalhau=Button(window, width=350, height=250, image=imgSbacalhau,command=janelaSbacalhau)
btnSbolonhesa=Button(window, width=350, height=250, image=imgSbolonhesa,command=janelaSbolonhesa)
btnSbulgur=Button(window, width=350, height=250, image=imgSbulgur,command=janelaSbulgur)
btnSdelicias=Button(window, width=350, height=250, image=imgSdelicias,command=janelaSdelicias)
btnSfrango=Button(window, width=350, height=250, image=imgSfrango,command=janelaSfrango)
btnSsalsichas=Button(window, width=350, height=250, image=imgSsalsichas,command=janelaSsalsichas)

#Botões Vegetarianas
btnCanelone=Button(window, width=350, height=250, image=imgCanelone,command=janelaCaneloneVegetariano)
btnCogumelos=Button(window, width=350, height=250, image=imgCogumelos,command=janelaCogumelos)
btnCrepe=Button(window, width=350, height=250, image=imgCrepe,command=janelaCrepeVegetariano)
btnFolhadinhos=Button(window, width=350, height=250, image=imgFolhadinhos,command=janelaFolhadoVegetariano)
btnMigas=Button(window, width=350, height=250, image=imgMigas,command=janelaMigasVegetariano)
btnOvos=Button(window, width=350, height=250, image=imgOvos,command=janelaOvosVegetarianos)

#Botões Sopas
btnSopaCenoura=Button(window, width=350, height=250, image=imgSopaCenoura,command=janelaSopaCenoura)
btnSopaPedra=Button(window, width=350, height=250, image=imgSopaPedra,command=janelaSopaPedra)
btnSopaConquilha=Button(window, width=350, height=250, image=imgSopaConquilha,command=janelaSopaConquilha)
btnSopaPeixe=Button(window, width=350, height=250, image=imgSopaPeixe,command=janelaSopaPeixe)
btnSopaJuliana=Button(window, width=350, height=250, image=imgSopaJuliana,command=janelaSopaJuliana)
btnCaldoVerde=Button(window, width=350, height=250, image=imgCaldoVerde,command=janelaSopaCaldoVerde)
#endregion
#endregion

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
