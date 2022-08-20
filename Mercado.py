from pydoc import describe
from tkinter import *


def Lista(root, lst):

    vezes = len(lst) / 2
    largura = 420
    altura = 10
    count = 1
    i = 1
    new = 4
    e = []

    while i <= int(vezes):
        e.append(Label(root, text="", width=20, fg='black', font=('Arial', 18, 'bold'),
                       borderwidth=2,
                       relief="ridge", anchor="w", justify=LEFT))
        e[i-1].place(x=largura, y=altura, width=275, height=35)
        e[i-1]["text"] = str(count) + "  " + lst[(i*2) - 2] + \
            " " + " R$ " + lst[(i*2) - 1]
        largura += 275
        if i == new:
            altura += 35
            largura = 420

        i += 1
        count += 1
    return e


def AdicionaLista(root, lst):
    vezes = len(lst) / 2
    largura = 420
    altura = 10
    count = 1
    i = 1
    new = 4
    e = []

    while i <= int(vezes):
        e.append(Label(root, text="", width=20, fg='black', font=('Arial', 18, 'bold'),
                       borderwidth=2,
                       relief="ridge", anchor="w", justify=LEFT))
        e[i-1].place(x=largura, y=altura, width=275, height=35)
        e[i-1]["text"] = str(count) + "  " + lst[(i*2) - 2] + \
            " " + " R$ " + lst[(i*2) - 1]
        largura += 275
        if i == new:
            altura += 35
            largura = 420

        i += 1
        count += 1
    return e


def Criaarquivo(lista):
    arquivo = open("lista.txt", "w", encoding="utf-8")

    for c in range(0, len(lista)):
        arquivo.write(lista[c])
        if c < len(lista) - 1:
            arquivo.write("\n")
    arquivo.close()


def CriaLista(janela, e2):
    def Adiciona():
        produto1 = produto.get()
        preco1 = preco.get()
        lista.append(produto1)
        lista.append(str(preco1))

        produto.delete("0", "end")
        preco.delete("0", "end")

    def Finalizar(adiciona, produto, preco, finalizar):

        adiciona.place_forget()
        produto.place_forget()
        preco.place_forget()
        finalizar.place_forget()
        global e2
        e2 = Lista(janela, lista)

    if (e2 == None):
        None
    else:
        count = 0

        while count < len(e2):
            a = e2[count]
            a.destroy()
            count += 1

    lista = []
    produto = Entry(janela, font="12")
    produto.place(x=10, y=190, width=200, height=30)
    preco = Entry(janela, font="12")
    preco.place(x=10, y=230, width=200, height=30)

    adiciona = Button(janela, text="Adicionar", font="12", command=lambda: [
                      Adiciona(), Criaarquivo(lista)], background="#fff")
    adiciona.place(x=10, y=270, width=200, height=30)
    finalizar = Button(janela, text="Finalizar", font="12", command=lambda: [
                       Finalizar(adiciona, produto, preco, finalizar)], background="#fff")
    finalizar.place(x=210, y=270, width=200, height=30)


def AumentaLista(janela, e2):
    def Adiciona():
        produto1 = produto.get()
        preco1 = preco.get()
        lista.append(produto1)
        lista.append(str(preco1))
        produto.delete("0", "end")
        preco.delete("0", "end")

    def Finalizar(adiciona, produto, preco, finalizar):

        adiciona.place_forget()
        produto.place_forget()
        preco.place_forget()
        finalizar.place_forget()
        global e2
        e2 = Lista(janela, lista)

    arquivo = open("lista.txt", "r", encoding="utf-8")
    lista = arquivo.read().split("\n")

    count = 0

    while count < len(e2):
        a = e2[count]
        a.destroy()
        count += 1

    produto = Entry(janela, font="12")
    produto.place(x=10, y=360, width=200, height=30)
    preco = Entry(janela, font="12")
    preco.place(x=10, y=400, width=200, height=30)
    adiciona = Button(janela, text="Adicionar", font="12", command=lambda: [
                      Adiciona(), Criaarquivo(lista)], background="#fff")
    adiciona.place(x=10, y=440, width=200, height=30)
    finalizar = Button(janela, text="Finalizar", font="12", command=lambda: [
                       Finalizar(adiciona, produto, preco, finalizar)], background="#fff")
    finalizar.place(x=210, y=440, width=200, height=30)


def MudaLista(janela, e2):
    def Mudar():
        mudar = posicao.get()
        produto1 = produto.get()
        preco1 = preco.get()
        if produto1 == "":
            None
        else:
            lista[(2 * int(mudar)) - 2] = produto1
            a = e2[int(mudar) - 1]
            a["text"] = mudar + "  " + \
                lista[(int(mudar)*2) - 2] + " " + \
                " R$ " + lista[(int(mudar)*2) - 1]
        if preco1 == "":
            None
        else:
            lista[(2 * int(mudar)) - 1] = preco1
            a = e2[int(mudar) - 1]
            a["text"] = mudar + "  " + \
                lista[(int(mudar)*2) - 2] + " " + \
                " R$ " + lista[(int(mudar)*2) - 1]
        produto.delete("0", "end")
        preco.delete("0", "end")
        posicao.delete("0", "end")

    def Finalizar(posicao, mudar, produto, preco, finalizar):
        posicao.place_forget()
        mudar.place_forget()
        produto.place_forget()
        preco.place_forget()
        finalizar.place_forget()
        global e2
        e2 = Lista(janela, lista)

    arquivo = open("lista.txt", "r", encoding="utf-8")
    lista = arquivo.read().split("\n")

    posicao = Entry(janela, font="12")
    posicao.place(x=10, y=530, width=50, height=30)
    produto = Entry(janela, font="12")
    produto.place(x=70, y=530, width=200, height=30)
    preco = Entry(janela, font="12")
    preco.place(x=70, y=570, width=200, height=30)
    mudar = Button(janela, text="Adicionar", font="12", command=lambda: [
                   Mudar(), Criaarquivo(lista)], background="#fff")
    mudar.place(x=10, y=610, width=200, height=30)
    finalizar = Button(janela, text="Finalizar", font="12", command=lambda: [
                       Finalizar(posicao, mudar, produto, preco, finalizar)], background="#fff")
    finalizar.place(x=210, y=610, width=200, height=30)


def Deleta(janela, e2):
    deletando = []
    i = 0
    j = 0

    def Teste(posicao, i, j):

        delete = posicao.get()
        print(int(delete))
        lista.pop(int(delete) * 2 - 1)
        lista.pop(int(delete) * 2 - 2)

        count = 0

        while count < len(e2):
            a = e2[count]
            a.destroy()
            count += 1
            Lista(janela, lista)

        print(lista)
        posicao.delete("0", "end")

    def Finalizar(posicao, deletar, finalizar):
        posicao.place_forget()
        deletar.place_forget()
        finalizar.place_forget()
        Criaarquivo(lista)
        global e2
        e2 = Lista(janela, lista)

    arquivo = open("lista.txt", "r", encoding="utf-8")
    lista = arquivo.read().split("\n")

    print(lista)

    posicao = Entry(janela, font="12")
    posicao.place(x=10, y=700, width=50, height=30)
    deletar = Button(janela, text="Deletar", font="12", command=lambda: [
                     Teste(posicao, i, j)], background="#fff")
    deletar.place(x=10, y=740, width=200, height=30)
    finalizar = Button(janela, text="Finalizar", font="12", command=lambda: [
                       Finalizar(posicao, deletar, finalizar)], background="#fff")
    finalizar.place(x=210, y=740, width=200, height=30)


def Carrinho(item, quantidade):
    item2 = item.get()
    quantidade2 = quantidade.get()
    comprarr = open("Comprar.txt", "a", encoding="utf-8")
    comprarr.write(item2)
    comprarr.write("\n")
    comprarr.write(quantidade2)
    comprarr.write("\n")
    item.delete("0", "end")
    Quantidade.delete("0", "end")


def Comprar(janela):
    arquivo2 = open("lista.txt", "r", encoding="utf-8")
    lista = arquivo2.read().split("\n")

    arquivo = open("Comprar.txt", "r", encoding="utf-8")
    ctxt = arquivo.read().split("\n")
    ctxt.pop()

    print(lista)

    vezes = len(ctxt) / 2
    i = 1
    Soma = 0
    while i <= vezes:
        Soma = Soma + \
            float(lista[(int(ctxt[(i*2) - 2]) * 2) - 1]) * int(ctxt[(i*2) - 1])
        i += 1

    comprando["text"] = "Total: R$ " + str(Soma)

    arquivo = open("Comprar.txt", "w", encoding="utf-8")
    arquivo.close()


arquivo = open("lista.txt", "a", encoding="utf-8")
arquivo.write("\na22")
arquivo.close()
arquivo = open("lista.txt", "r", encoding="utf-8")
lista = arquivo.read().split("\n")
arquivo.close()


janela = Tk()
janela.title('Your Market')
janela.state('zoomed')
janela.iconbitmap('Your_Market.ico')
img = PhotoImage(file="Your_Market.png")
label_imagem = Label(janela, image=img).place(x=10, y=0)

e2 = None

if lista[1] == "a22":
    e2 = None
else:
    lista.pop()
    Criaarquivo(lista)
    e2 = Lista(janela, lista)

Cria = Button(janela, text="Criar Lista", font="12", command=lambda: [
              CriaLista(janela, e2)], background="#fff")
Cria.place(x=10, y=150, width=300, height=30)

Aumenta = Button(janela, text="Adicionar mais produtos a lista", font="12",
                 command=lambda: [AumentaLista(janela, e2)], background="#fff")
Aumenta.place(x=10, y=320, width=300, height=30)

Muda = Button(janela, text="Mudar os produtos da lista", font="12",
              command=lambda: [MudaLista(janela, e2)], background="#fff")
Muda.place(x=10, y=490, width=300, height=30)

Delete = Button(janela, text="Deletar produto da lista", font="12",
                command=lambda: [Deleta(janela, e2)], background="#fff")
Delete.place(x=10, y=660, width=300, height=30)


item = Entry(janela, font="12")
item.place(x=500, y=550, width=50, height=30)
Quantidade = Entry(janela, font="12")
Quantidade.place(x=560, y=550, width=100, height=30)

Compra = Button(janela, text="Adicionar ao Carrinho", font="12",
                command=lambda: [Carrinho(item, Quantidade)], background="#fff")
Compra.place(x=500, y=590, width=200, height=30)

Soma = Button(janela, text="Finalizar Compra", font="12",
              command=lambda: [Comprar(janela)], background="#fff")
Soma.place(x=700, y=590, width=200, height=30)

comprando = Label(janela, text="", font="12")
comprando.place(x=620, y=550, width=200, height=30)


janela.mainloop()
