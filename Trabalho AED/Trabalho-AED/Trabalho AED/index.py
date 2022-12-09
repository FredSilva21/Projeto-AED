from tkinter import *
from tkinter import messagebox




window = Tk()
window.title("ToDo Eat")
window.iconbitmap("./assets/icone.ico")
window.configure(bg="white")
window.resizable(0,0)




#region Janela Login e Criar Conta
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

# endregion


# region Window Inicial
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



def criarConta():
    fBaseDados=open("./ficheiros/basedados.txt","a",encoding="utf-8")
    nome=entUtilizador.get()
    email=entEmail.get()
    passe=entPass.get()

    resultado=nome + ";" + email + ";" + passe + "\n"

    """
    if contaExiste()==False:
        fBaseDados.write(resultado)
        fBaseDados.close()
    else:
        messagebox.ERROR("A conta já existe,tente novamente!")
    """

#region Interface Window

# Canvas para imagem
ctnImg = Canvas(window, width=200, height=150,bd=-2, relief="sunken", bg="white")

# Imagem Icone
imgIcone = PhotoImage(file=".//img//icone.png")
ctnImg.create_image(100, 78, image=imgIcone)

# Label Bem Vindo
lblBemVindo = Label(window, text="Bem Vindo :)", fg="black",relief="raised", font="Playfair", bd=-2, bg="white")

# Botão Criar Conta
btnCriar = Button(window, text="Criar Conta", fg="white",bg="#62C370", width=10, height=1)

# Botão Entrar Conta
btnEntrar = Button(window, text="Entrar", fg="black",bg="#99DDC8", width=10, height=1, command=janelaLogin)

# Botão Entrar como Convidado
btnConvid = Button(window, text="Convidado", fg="black",bg="#CBDFBD", width=10, height=1)

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
entPass = Entry(window, fg="black", width=25)

#Label Utilizador
lblCpass = Label(window, text="Confirmar Palavra-Passe:", fg="black",relief="raised", font="Playfair", bd=-2, bg="white")

#Entry Utilizador
entCpass = Entry(window, fg="black", width=25)

# Botão Criar Conta do Utilizador
btnCriarConta = Button(window, text="Criar Conta", fg="white",bg="#62C370", width=10, height=1,command=criarConta)
btnConvidUtil=Button(window, text="Convidado", fg="black",bg="#CBDFBD", width=10, height=1)
btnVoltar=Button(window, text="Voltar", fg="black",bg="#767B91", width=10, height=1,command=janelaInicial)


#endregion



janelaInicial()

window.mainloop()
