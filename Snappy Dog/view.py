from tkinter import *
from tkinter.ttk import *

from controller import *

tela=Tk()
tela.geometry('800x450')
tela.title('Petshop')

api=Notebook(tela)
api.pack(expand=True,fill='both')
api.option_add('*Font',"Arial 12")

Cadastro=Notebook(api)
Cadastro.pack(expand=True,fill='both')

consulta=Notebook(api)
consulta.pack(expand=True,fill='both')

api.add(Cadastro,text='Cadastro')
api.add(consulta,text='Consulta')


#Criação das Telas
cadastro_cliente=Frame(Cadastro)
cadastro_animal=Frame(Cadastro)
cadastro_servico=Frame(Cadastro)
#Funções para Cadastros
def Enviar_Cliente():
    #enviar as Informações ao controlador:
    cadastrar_cliente(entry_cliente_nome.get(),
                      entry_cliente_telefone.get(),
                      entry_cliente_endereco.get(),
                      entry_cliente_cpf.get())
    #apaga
    # entry_cliente_nome.delete(0, 'end')
    # entry_cliente_telefone.delete(0, 'end')
    # entry_cliente_endereco.delete(0, 'end')
    # entry_cliente_cpf.delete(0, 'end')

# def enviar_Animal():
#     Cadastrar_Animal(entry_animal_nome.get(),
#                      entry_animal_raca(),
#                      entry_animal_dono_cpf.get(),
#                      commobox_tipo_animal.get())
def Enviar_Servico():
    cadastrar_servico(entry_servico_nome.get(),
                      text_servico_descricao.get(1.0, "end-1c"),
                      entry_servico_preco.get())
    

#cadrasto Cliente
label_cliente_nome=Label(cadastro_cliente,text='nome')
label_cliente_nome.grid(column=0,row=0)

entry_cliente_nome=Entry(cadastro_cliente)
entry_cliente_nome.grid(column=1,row=0)

label_cliente_telefone=Label(cadastro_cliente,text='Telefone')
label_cliente_telefone.grid(column=0,row=1)

entry_cliente_telefone=Entry(cadastro_cliente)
entry_cliente_telefone.grid(column=1,row=1)

label_cliente_cpf=Label(cadastro_cliente,text='CPF')
label_cliente_cpf.grid(column=0,row=2)

entry_cliente_cpf=Entry(cadastro_cliente)
entry_cliente_cpf.grid(column=1,row=2)

label_cliente_endereco=Label(cadastro_cliente,text='Endereço')
label_cliente_endereco.grid(column=0,row=3)

entry_cliente_endereco=Entry(cadastro_cliente)
entry_cliente_endereco.grid(column=1,row=3)

button_cliente_enviar=Button(cadastro_cliente,text='Enviar',command= Enviar_Cliente())
button_cliente_enviar.grid(column=0,columnspan=2,row=4)

#cadrasto Animal
label_animal_nome=Label(cadastro_animal,text='nome do animal',)
label_animal_nome.grid(column=0,row=0)

entry_animal_nome=Entry(cadastro_animal)
entry_animal_nome.grid(column=1,row=0)

label_animal_raca=Label(cadastro_animal,text='raça')
label_animal_raca.grid(column=0,row=1)

entry_animal_raca=Entry(cadastro_animal)
entry_animal_raca.grid(column=1,row=1)

label_animal_dono_cpf=Label(cadastro_animal,text='cpf do dono')
label_animal_dono_cpf.grid(column=0,row=2)

entry_animal_dono_cpf=Entry(cadastro_animal)
entry_animal_dono_cpf.grid(column=1,row=2)

label_animal_raca=Label(cadastro_animal,text='Tipo de animal')
label_animal_raca.grid(column=0,row=3)

tipo_animal=StringVar()
commobox_tipo_animal=Combobox(cadastro_animal,textvariable=tipo_animal)
commobox_tipo_animal['value']= ['Gato','Cachorro','outros']
commobox_tipo_animal.grid(column=1,row=3)

button_animal_enviar=Button(cadastro_animal,text='Enviar')
button_animal_enviar.grid(column=0,columnspan=2,row=4)

#Cadastro serviço

label_servico_nome=Label(cadastro_servico,text='nome do serviço')
label_servico_nome.grid(column=0,row=0)

entry_servico_nome=Entry(cadastro_servico)
entry_servico_nome.grid(column=1,row=0)

label_servico_descricao=Label(cadastro_servico,text='Descricao')
label_servico_descricao.grid(column=0,row=1)

text_servico_descricao=Text(cadastro_servico,width=20,height=5)
text_servico_descricao.grid(column=1,row=1,pady=10)

label_servico_preco=Label(cadastro_servico,text='Preço do serviço')
label_servico_preco.grid(column=0,row=2)

entry_servico_preco=Entry(cadastro_servico)
entry_servico_preco.grid(column=1,row=2)

button_servico_enviar=Button(cadastro_servico,text='Enviar',command=Enviar_Servico())
button_animal_enviar.grid(column=0,columnspan=2,row=4)
button_servico_enviar.grid(column=0,columnspan=2,row=4)

#link dos frames para os notebook
Cadastro.add(cadastro_cliente,text='Cadastro Cliente')
Cadastro.add(cadastro_animal,text='Cadastro Animal')
Cadastro.add(cadastro_servico,text='Cadastro Serviços')

tela.mainloop()