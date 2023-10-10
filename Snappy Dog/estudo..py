cpf='18239440789'
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


