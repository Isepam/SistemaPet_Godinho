import tkinter as TK
import tkinter.ttk as TKK
from model import *
def cadastrar_cliente(entrada_Nome,entrada_Telefone,entrada_Cpf,entrada_Endereco):
    """if Nome == '':
        return 0
    elif telefone == '' or len(telefone)!= 9 :
        return 0
    elif cpf == '' or len(cpf)!=11:
        return 0
    else:
        Cliente=Cliente.create(Nome,telefone,cpf,endereco)
        return 1"""
    

    Cliente=clientes.create(nome=entrada_Nome,telefone=entrada_Telefone,cpf=entrada_Cpf,endereco=entrada_Endereco)



def cadastrar_servico(Entrada_Nome,Entrada_Descricao,Entrada_Preco):
    servico=servicos.create(nome=Entrada_Nome,descricao=Entrada_Descricao,preco=Entrada_Preco)

def Cadastrar_Animal(Entrada_Nome,Entrada_Especie,Entrada_Raca,Entrada_Porte,Entrada_cpf_dono):
     
     Animal=animais.create()





    

