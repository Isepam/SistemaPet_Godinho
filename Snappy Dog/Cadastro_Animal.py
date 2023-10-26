import tkinter as TK
import tkinter.ttk as TKK
from controller import select_cliente


def Desenhar_cadastro_animal(telapai):
    def Tratamento_lista_dono():
        tuplas=select_cliente()
        Lista=[]
        for x in tuplas:
            Lista.append(str(x)+' '+str(x.nome))
        return Lista
     

    cadastro_animal=TK.Toplevel(telapai)
    cadastro_animal.geometry("400x250")

    label_animal_nome=TK.Label(cadastro_animal,text='nome do animal',).grid(column=0,row=0)

    entry_animal_nome=TK.Entry(cadastro_animal)
    entry_animal_nome.grid(column=1,row=0)

    label_animal_especie=TK.Label(cadastro_animal,text='Tipo de animal').grid(column=0,row=1)

    especie_animal=TK.StringVar()
    commobox_especie_animal=TKK.Combobox(cadastro_animal,textvariable=especie_animal)
    commobox_especie_animal['value']= ['Gato','Cachorro','outros']
    commobox_especie_animal.grid(column=1,row=1)

    label_animal_raca=TK.Label(cadastro_animal,text='raça').grid(column=0,row=2)

    entry_animal_raca=TK.Entry(cadastro_animal)
    entry_animal_raca.grid(column=1,row=2)

    label_animal_porte_cpf=TK.Label(cadastro_animal,text='Porte').grid(column=0,row=3)
    Porte_animal=TK.StringVar()
    commobox_porte_animal=TKK.Combobox(cadastro_animal,textvariable=Porte_animal)
    commobox_porte_animal['value']=['Grande','Médio','Pequeno']
    commobox_porte_animal.grid(column=1,row=3)

    label_animal_dono_cpf=TK.Label(cadastro_animal,text='Dono').grid(column=0,row=4)
    Clientes_animal=TK.StringVar()
    commobox_dono_animal=TKK.Combobox(cadastro_animal,textvariable=Clientes_animal)
    commobox_dono_animal['value']=Tratamento_lista_dono()
    commobox_dono_animal.grid(column=1,row=4)

    

    

    button_animal_enviar=TK.Button(cadastro_animal,text='Enviar')
    button_animal_enviar.grid(column=0,columnspan=2,row=5)