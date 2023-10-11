
import tkinter.ttk as TKK
from controller import *
def Cadastro(telapai):
    tela=TK.Toplevel(telapai)
    tela.geometry('800x450')
    tela.title('Petshop')

    Cadastro=TKK.Notebook(tela)
    Cadastro.option_add('*Font',"Arial 12")
    Cadastro.pack(expand=True,fill='both')

    #Criação das Telas
    cadastro_cliente=TK.Frame(Cadastro)
    cadastro_animal=TK.Frame(Cadastro)
    cadastro_servico=TK.Frame(Cadastro)

    def Enviar_Cadastro_Cliente(Tela,Nome:str,telefone:str,cpf:str,endereco:str):
        cadastrar_cliente(Nome,telefone,cpf,endereco)
        LimparFrame(Tela)
    # def Enviar_Cadastro_animal():
    #     cadastro_animal()

    def Enviar_Cadastro_Servico(Tela,nome,descricao,preco):
        cadastrar_servico(nome,descricao,preco)
        LimparFrame(Tela)


    #cadrasto Cliente
    label_cliente_nome=TK.Label(cadastro_cliente,text='Nome').grid(column=0,row=0)

    entry_cliente_nome=TK.Entry(cadastro_cliente)
    entry_cliente_nome.grid(column=1,row=0,pady=10)

    label_cliente_telefone=TK.Label(cadastro_cliente,text='Telefone').grid(column=0,row=1)

    entry_cliente_telefone=TK.Entry(cadastro_cliente)
    entry_cliente_telefone.grid(column=1,row=1,pady=10)

    label_cliente_cpf=TK.Label(cadastro_cliente,text='CPF').grid(column=0,row=2)

    entry_cliente_cpf=TK.Entry(cadastro_cliente)
    entry_cliente_cpf.grid(column=1,row=2,pady=10)

    label_cliente_endereco=TK.Label(cadastro_cliente,text='Endereço').grid(column=0,row=3)

    text_cliente_endereco=TK.Text(cadastro_cliente,width=20,height=2)
    text_cliente_endereco.grid(column=1,row=3,pady=10,columnspan=3)

    button_cliente_enviar=TK.Button(cadastro_cliente,text='Enviar',command=
                        lambda: Enviar_Cadastro_Cliente(cadastro_cliente,
                                                        entry_cliente_nome.get(),
                                                        entry_cliente_telefone.get(),
                                                        entry_cliente_cpf.get(),
                                                        text_cliente_endereco.get("1.0",'end-1c')
                                                        )).grid(column=0,columnspan=2,row=4,pady=10)

    #cadrasto Animal
    label_animal_nome=TK.Label(cadastro_animal,text='nome do animal',).grid(column=0,row=0)

    entry_animal_nome=TK.Entry(cadastro_animal)
    entry_animal_nome.grid(column=1,row=0)

    label_animal_raca=TK.Label(cadastro_animal,text='raça').grid(column=0,row=1)

    entry_animal_raca=TK.Entry(cadastro_animal)
    entry_animal_raca.grid(column=1,row=1)

    label_animal_dono_cpf=TK.Label(cadastro_animal,text='cpf do dono').grid(column=0,row=2)

    entry_animal_dono_cpf=TK.Entry(cadastro_animal)
    entry_animal_dono_cpf.grid(column=1,row=2)

    label_animal_raca=TK.Label(cadastro_animal,text='Tipo de animal').grid(column=0,row=3)

    tipo_animal=TK.StringVar()
    commobox_tipo_animal=TKK.Combobox(cadastro_animal,textvariable=tipo_animal)
    commobox_tipo_animal['value']= ['Gato','Cachorro','outros']
    commobox_tipo_animal.grid(column=1,row=3)

    button_animal_enviar=TK.Button(cadastro_animal,text='Enviar')
    button_animal_enviar.grid(column=0,columnspan=2,row=4)

    #Cadastro serviço

    label_servico_nome=TK.Label(cadastro_servico,text='nome do serviço').grid(column=0,row=0)

    entry_servico_nome=TK.Entry(cadastro_servico)
    entry_servico_nome.grid(column=1,row=0)

    label_servico_descricao=TK.Label(cadastro_servico,text='Descricao').grid(column=0,row=1)

    text_servico_descricao=TK.Text(cadastro_servico,width=20,height=5)
    text_servico_descricao.grid(column=1,row=1,pady=10)

    label_servico_preco=TK.Label(cadastro_servico,text='Preço do serviço').grid(column=0,row=2)

    entry_servico_preco=TK.Entry(cadastro_servico)
    entry_servico_preco.grid(column=1,row=2)

    button_servico_enviar=TK.Button(cadastro_servico,text='Enviar',command= 
                                    lambda:Enviar_Cadastro_Servico(cadastro_servico,
                                                                    entry_servico_nome.get(),
                                                                    text_servico_descricao.get("1.0",'end-1c'),
                                                                    entry_servico_preco.get()
                                                                    )).grid(column=0,columnspan=2,row=4)

    #link dos frames para os notebook
    Cadastro.add(cadastro_cliente,text='Cadastro Cliente')
    Cadastro.add(cadastro_animal,text='Cadastro Animal')
    Cadastro.add(cadastro_servico,text='Cadastro Serviços')

    tela.mainloop()