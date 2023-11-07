from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from  datetime import date
from controller import select_servico,select_animal,cadastrar_historico,Atualizar_tree_historico,select_historico,atualizar_historico
def desenhar_cadastro_historico(telapai,tree,update=False,historico=object):

    def Enviar_Cadastro_Historico(animal,servico,data):
                if update:
                        if atualizar_historico(animal,servico,data,historico):
                                cadastro_historico.destroy()
                                Atualizar_tree_historico(tree,select_historico())
                else:
                        if cadastrar_historico(animal,servico,data):
                                cadastro_historico.destroy()
                                Atualizar_tree_historico(tree,select_historico())
    def lista_historico_animal():
        tuplas=select_animal()
        Lista=[]
        for x in tuplas:
            Lista.append(str(x)+' '+str(x.nome))
        return Lista
    def lista_historico_servico():
        tuplas=select_servico()
        Lista=[]
        for x in tuplas:
            Lista.append(str(x)+' '+str(x.nome))
        return Lista    
    cadastro_historico = Toplevel(telapai)
    cadastro_historico.geometry("400x250")

    label_historico_data=Label(cadastro_historico,text="Data:").grid(row=0,column=0,pady=10,padx=10)
    Dt_entry=DateEntry(cadastro_historico)
    Dt_entry.grid(row=0,column=1,padx=10)
    
    label_historico_animal=Label(cadastro_historico,text="Animal:").grid(row=1,column=0,padx=10,pady=10)

    commbobox_historico_animal=ttk.Combobox(cadastro_historico,state='readonly')
    commbobox_historico_animal['value']=lista_historico_animal()
    commbobox_historico_animal.grid(row=1,column=1,padx=10)

    label_historico_servico=Label(cadastro_historico,text="Servico Prestado").grid(row=2,column=0,padx=10,pady=10)
    commbobox_historico_servico=ttk.Combobox(cadastro_historico,state='readonly')
    commbobox_historico_servico['value']=lista_historico_servico()
    commbobox_historico_servico.grid(row=2,column=1,padx=10)

    button_historico_enviar=Button(cadastro_historico,text='Enviar',command= 
                                    lambda:Enviar_Cadastro_Historico(
                                                                    commbobox_historico_animal.get(),
                                                                    commbobox_historico_servico.get(),
                                                                    Dt_entry.get_date()
                                                                    )).grid(row=3,column=0,columnspan=2)
    if update:
        lista_data=(historico.data).split('-')
        for x in range(len(lista_data)):
              lista_data[x]=int(lista_data[x])
        data=date(lista_data[0],lista_data[1],lista_data[2])
        Dt_entry.set_date(data)

    cadastro_historico.mainloop()

