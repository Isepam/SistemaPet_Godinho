from peewee import *

banco_petShop=SqliteDatabase('Petshop.db')

class Bmodel(Model):
    class Meta:
        database=banco_petShop
class clientes(Bmodel):
    nome=CharField()
    telefone=CharField(max_length=11)
    cpf=CharField(max_length=11)
    endereco=CharField()
class animais(Bmodel):
    nome=CharField()
    especie=CharField()
    raca=CharField()
    porte=CharField()
    dono=ForeignKeyField(clientes,backref='Pets')
class servicos(Bmodel):
    nome=CharField()
    descricao=CharField()
    preco=CharField()
class principal(Bmodel):
    animal=ForeignKeyField(animais,backref='historico')
    data=DateField()
    servico_prestado=ForeignKeyField(servicos,backref='prestados')


banco_petShop.create_tables([principal,servicos,animais,clientes])


