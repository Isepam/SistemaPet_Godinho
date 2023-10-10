import tkinter as TK
from tkinter import messagebox
from model import *
def cadastrar_cliente(entrada_Nome,entrada_Telefone,entrada_Cpf,entrada_Endereco):
    if entrada_Nome == '':
        messagebox.showinfo('Erro de Entrada','Nome Invalido')
        return False
    elif entrada_Telefone == '' or len(entrada_Telefone)>11 or len(entrada_Telefone)<11:
        messagebox.showinfo('Erro de Entrada','Telefone Invalido')
        return False
    elif entrada_Cpf == '' or len(entrada_Cpf)>11 or len(entrada_Cpf)<11:
        messagebox.showinfo('Erro de Entrada','CPF Invalido')
        return False
        

    # Cliente=clientes.create(nome=entrada_Nome,telefone=entrada_Telefone,cpf=entrada_Cpf,endereco=entrada_Endereco)



def cadastrar_servico(Entrada_Nome,Entrada_Descricao,Entrada_Preco):
    servico=servicos.create(nome=Entrada_Nome,descricao=Entrada_Descricao,preco=Entrada_Preco)

def Cadastrar_Animal(Entrada_Nome,Entrada_Especie,Entrada_Raca,Entrada_Porte,Entrada_cpf_dono):
     
     Animal=animais.create()

def LimparFrame(telapai):
    for widget in telapai.winfo_children():
        if isinstance(widget,TK.Entry):
            widget.delete(0, "end")
        if isinstance(widget,TK.Text):
            widget.delete(1.0, "end")

def validar_cpf(cpf):
    # cpf='18239440789'
    lista_cpf=[]
    for x in cpf:
        lista_cpf.append(x)

    lista_cpf_cru=[]
    for y in range(0,9):
        lista_cpf_cru.append(int(lista_cpf[y]))

    validante1=lista_cpf[-2]
    validante2=lista_cpf[-1]

    soma1=0
    for Ncpf,multi in zip(lista_cpf_cru,range(10,1,-1)):
        print(Ncpf,multi)
        soma1+=(Ncpf*multi)

    validacao1=(soma1*10)%11
    if validacao1== 10:
        validacao1=0
    if validante1==validante1:
        print()

    




    

