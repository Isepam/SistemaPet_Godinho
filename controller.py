import tkinter as TK
from tkinter import messagebox
from model import *
def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

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
    
def validar_cliente(entrada_Nome:str,entrada_Telefone:str,entrada_Cpf:str):
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
            return True

def cadastrar_cliente(entrada_Nome:str,entrada_Telefone:str,entrada_Cpf:str,entrada_Endereco:str):
    entrada_Nome=entrada_Nome.capitalize()
    if validar_cliente(entrada_Nome,entrada_Telefone,entrada_Cpf):
        messagebox.showinfo('Concluido','Cadastro Concluido')
        Cliente=clientes.create(nome=entrada_Nome,telefone=entrada_Telefone,cpf=entrada_Cpf,endereco=entrada_Endereco)
        return True
    else:
        return False
    
def Atualizar_cliente(entrada_Nome:str,entrada_Telefone:str,entrada_Cpf:str,entrada_Endereco:str,id):
    if validar_cliente(entrada_Nome,entrada_Telefone,entrada_Cpf):
        cliente=clientes.get_by_id(id)
        entrada_Nome=entrada_Nome.capitalize()
        cliente.nome=entrada_Nome
        cliente.telefone=entrada_Telefone
        cliente.cpf=entrada_Cpf
        cliente.endereco=entrada_Endereco
        cliente.save()
        messagebox.showinfo('Concluido','Atulização Concluida')
        return True
    else:
        return False
    
        
    
def validar_servico(Entrada_Nome:str,Entrada_Preco:str,Entrada_Descricao:str,isupdate=False):
    nomeServico=servicos.get_or_none(servicos.nome==Entrada_Nome)
    if len(Entrada_Nome)<=0:
        messagebox.showerror()
        return False
    elif nomeServico!=None and isupdate==False:
        messagebox.showerror("Erro de Entrada",'Nome de Servico já existente')
        return False
    elif not(is_float(Entrada_Preco)):
        messagebox.showerror("Erro de Entrada",'Preço deve ser Numerico')
        return False
    elif float(Entrada_Preco)<=0.0:
        messagebox.showerror("Erro de Entrada",'Preço Invalido')
        return False
    elif len(Entrada_Descricao)<=0:
        messagebox.showerror("Erro de Entrada",'Descrição invalida')
    else:
        return True
   



def cadastrar_servico(Entrada_Nome:str,Entrada_Preco:str,Entrada_Descricao:str):
    Entrada_Nome=Entrada_Nome.capitalize()
    if validar_servico(Entrada_Nome,Entrada_Preco,Entrada_Descricao):
        servico=servicos.create(nome=Entrada_Nome,descricao=Entrada_Descricao,preco=Entrada_Preco)
        return True
    else:
        False
def atualizar_servico(Entrada_Nome:str,Entrada_Preco:str,Entrada_Descricao:str,id):
    Entrada_Nome=Entrada_Nome.capitalize()
    if validar_servico(Entrada_Nome,Entrada_Preco,Entrada_Descricao,isupdate=True):
        servico=servicos.get_by_id(id)
        servico.nome=Entrada_Nome
        servico.preco=Entrada_Preco
        servico.descricao=Entrada_Descricao
        servico.save()
        return True
    else:
        return False

def validar_Animal(Entrada_Nome:str,Entrada_Especie:str,Entrada_Raca:str,Entrada_Porte:str,Entrada_dono:str):
    Entrada_Nome=Entrada_Nome.capitalize()
    Entrada_Especie=Entrada_Especie.capitalize()
    Entrada_Raca=Entrada_Raca.capitalize()

    if len(Entrada_dono)<=2:
        messagebox.showerror('Erro de Entrada','Dono Invalido')
        return False        
    elif len(Entrada_Nome)<=0:
        messagebox.showerror('Erro de Entrada','Nome Invalido')
        return False
    elif len(Entrada_Especie)<=0:
        messagebox.showerror('Erro de Entrada','Especie Invalida')
        return False
    elif len(Entrada_Raca)<=0:
        messagebox.showerror('Erro de Entrada','Raça Invalida')
        return False
    elif len(Entrada_Porte)<=0:
        messagebox.showerror('Erro de Entrada','Porte Invalido')
        return False
    else:
        return True
    
def Cadastrar_Animal(Entrada_Nome:str,Entrada_Especie:str,Entrada_Raca:str,Entrada_Porte:str,Entrada_dono:str):
    Entrada_Nome=Entrada_Nome.capitalize()
    Entrada_Especie=Entrada_Especie.capitalize()
    Entrada_Raca=Entrada_Raca.capitalize()
    

    if validar_Animal(Entrada_Nome,Entrada_Especie,Entrada_Raca,Entrada_Porte,Entrada_dono):
        Entrada_dono=Entrada_dono.split()[0]
        Dono=clientes.get_by_id(Entrada_dono)
        Animal=animais.create(nome=Entrada_Nome,especie=Entrada_Especie,raca=Entrada_Raca,porte=Entrada_Porte,dono=Dono)
        
        return True
    else:
        return False
    
def Atualizar_Animal(Entrada_Nome:str,Entrada_Especie:str,Entrada_Raca:str,Entrada_Porte:str,Entrada_dono:str,id):
    Entrada_Nome=Entrada_Nome.capitalize()
    Entrada_Especie=Entrada_Especie.capitalize()
    Entrada_Raca=Entrada_Raca.capitalize()

    
    if validar_Animal(Entrada_Nome,Entrada_Especie,Entrada_Raca,Entrada_Porte,Entrada_dono):
        Entrada_dono=Entrada_dono.split()[0]
        Dono=clientes.get_by_id(Entrada_dono)
        
        Animal=animais.get_by_id(id)

        Animal.nome=Entrada_Nome
        Animal.raca=Entrada_Raca
        Animal.especie=Entrada_Especie
        Animal.porte=Entrada_Porte
        Animal.dono=Dono
        Animal.save()
        return True
    else:
        return False

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
def select_servico():
    tuplas=servicos.select()
    return tuplas


def filtrar_cliente(pesquisa,tipo='ID'):

    match tipo:
        case 'ID':
            query=clientes.get_by_id(pesquisa)
        case 'nome':
            pesquisa=pesquisa.capitalize()
            query=clientes.select().where(clientes.nome==pesquisa)
        case 'cpf':
            query=clientes.select().where(clientes.cpf==pesquisa)
        case 'telefone':
            query=clientes.select().where(clientes.telefone==pesquisa)
    return query
def filtrar_animal(pesquisa,tipo='ID'):
    
    match tipo:
        case 'ID':
            query=animais.get_by_id(pesquisa)
        case 'ID do dono':
            pesquisa=pesquisa.capitalize()
            dono=clientes.get_by_id(pesquisa)
            query=dono.Pets
        case 'nome':
            pesquisa=pesquisa.capitalize()
            query=animais.select().where(animais.nome==pesquisa)
        case 'Especie':
            query=animais.select().where(animais.especie==pesquisa)
        case 'Raça':
            query=animais.select().where(animais.raca==pesquisa)
    return query

def filtrar_servico(pesquisa,tipo='ID'):
    
    match tipo:
        case 'ID':
            query=servicos.get_by_id(pesquisa)
        case 'Nome':
            query=servicos.select().where(servicos.nome==pesquisa)
        case 'Preço':
            float(pesquisa)
            query=servicos.select().where(servicos.preco==pesquisa)
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
                                            f'{tupla.dono} {tupla.dono.nome}'])
        
def Atualizar_tree_servico(treeview,origem:list):
    treeview.delete(*treeview.get_children())
    for tupla in origem:
        treeview.insert('', TK.END, values=[str(tupla),
                                            str(tupla.nome),
                                            str(tupla.preco),
                                            str(tupla.descricao)])

def Apagar_Instancia(ID:int,classe:str):
    match classe:
        case 'Cliente':
            clientes.delete_by_id(ID)
        case 'Animal':
            animais.delete_by_id(ID)
        case 'Servico':
            servicos.delete_by_id(ID)
            


    




    

