import tkinter as TK
from tkinter import messagebox
from model import *

def validar_cpf(cpf):
    Etapa1_validacao=False
    Etapa2_validacao=False

    lista_cpf=[]
    for x in cpf:
        lista_cpf.append(x)

    nums_validação1=[]
    for y in range(0,9):
        nums_validação1.append(int(lista_cpf[y]))

    validante1=int(lista_cpf[-2])

    soma1=0
    for Ncpf,multi in zip(nums_validação1,range(10,1,-1)):
        soma1+=(Ncpf*multi)

    validacao1=(soma1*10)%11
    if validacao1== 10:
        validacao1=0
    if validacao1==validante1:
        Etapa1_validacao=True

    validante2=int(lista_cpf[-1])
    nums_validação2=nums_validação1
    nums_validação2.append(validante1)


    soma2=0
    for Ncpf,multi in zip(nums_validação2,range(11,1,-1)):
        soma2+=(Ncpf*multi)

    validacao2=(soma2*10)%11
    if validacao2== 10:
        validacao2=0

    if validacao2==validante2:
        Etapa2_validacao=True 

    if Etapa1_validacao and Etapa2_validacao:
        return(True)
    else:
        return(False)
    

def cadastrar_cliente(entrada_Nome:str,entrada_Telefone:str,entrada_Cpf:str,entrada_Endereco:str,tree):
    entrada_Nome=entrada_Nome.capitalize()
    if len(entrada_Nome)<=0:
        messagebox.showerror('Erro de Entrada','Nome Invalido')
        return False
    elif entrada_Telefone == '' or len(entrada_Telefone)>11 or len(entrada_Telefone)<11:
        messagebox.showerror('Erro de Entrada','Telefone Invalido')
        return False
    elif entrada_Cpf == '' or len(entrada_Cpf)>11 or len(entrada_Cpf)<11 or not(validar_cpf(entrada_Cpf)):
        messagebox.showerror('Erro de Entrada','CPF Invalido')
        return False
    else:
        messagebox.showinfo('Concluido','Cadastro Concluido')
        Cliente=clientes.create(nome=entrada_Nome,telefone=entrada_Telefone,cpf=entrada_Cpf,endereco=entrada_Endereco)
        Atualizar_tree_cliente(tree,select_cliente())
        return True
    

   



def cadastrar_servico(Entrada_Nome,Entrada_Descricao,Entrada_Preco):
    servico=servicos.create(nome=Entrada_Nome,descricao=Entrada_Descricao,preco=Entrada_Preco)

def Cadastrar_Animal(Entrada_Nome,Entrada_Especie,Entrada_Raca,Entrada_Porte,Entrada_cpf_dono):
    if len(Entrada_Nome)<=0:
         messagebox.showerror('Erro de Entrada','Nome Invalido')
         return False
    elif len(Entrada_Especie)<=0:
         messagebox.showerror('Erro de Entrada','Especie Invalida')
    elif len(Entrada_Raca)<=0:
        messagebox.showerror('Erro de Entrada','Raça Invalida')
    elif len(Entrada_Porte)<=0:
        messagebox.showerror('Erro de Entrada','Porte Invalido')
    Animal=animais.create()

def LimparFrame(telapai):
    for widget in telapai.winfo_children():
        if isinstance(widget,TK.Entry):
            widget.delete(0, "end")
        if isinstance(widget,TK.Text):
            widget.delete(1.0, "end")

def select_cliente():
    tuplas=clientes.select()
    return tuplas
def select_animal():
    tuplas=animais.select()
    return tuplas



def filtrar_cliente(pesquisa,tipo):

    match tipo:
        case 'nome':
            pesquisa=pesquisa.capitalize()
            query=clientes.select().where(clientes.nome==pesquisa)
        case 'cpf':
            query=clientes.select().where(clientes.cpf==pesquisa)
        case 'telefone':
            query=clientes.select().where(clientes.telefone==pesquisa)
    return query
    

def Atualizar_tree_cliente(treeview,origem:list):
    treeview.delete(*treeview.get_children())
    for tupla in origem:
        treeview.insert('', TK.END, values=[str(tupla),
                                            str(tupla.nome),
                                            str(f'({tupla.telefone[0:2]}) {tupla.telefone[2:]}'),
                                            str(f'{tupla.cpf[0:3]}.{tupla.cpf[3:6]}.{tupla.cpf[6:9]}-{tupla.cpf[9:11]}'),
                                            str(tupla.endereco)])
def Atualizar_tree_animal(treeview,origem:list):
    treeview.delete(*treeview.get_children())
    for tupla in origem:
        treeview.insert('', TK.END, values=[str(tupla),
                                            str(tupla.nome),
                                            str(tupla.especie),
                                            str(tupla.raca),
                                            str(tupla.porte),
                                            str(tupla.dono)])

def Apagar_Instancia(ID:int,classe:str,tree):
    match classe:
        case 'Cliente':
            clientes.delete_by_id(ID)
            Atualizar_tree_cliente(tree,select_cliente())
        case 'Animal':
            animais.delete_by_id(ID)
            Atualizar_tree_animal(tree,select_animal())


    




    

