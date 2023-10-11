cpf='18239440789'
lista_cpf=[]
for x in cpf:
    lista_cpf.append(x)

nums_validação1=[]
for y in range(0,9):
    nums_validação1.append(int(lista_cpf[y]))

validante1=int(lista_cpf[-2])

soma1=0
for Ncpf,multi in zip(nums_validação1,range(10,1,-1)):
    print(Ncpf,multi)
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
    print(Ncpf,multi)
    soma2+=(Ncpf*multi)

validacao2=(soma2*10)%11
if validacao2== 10:
    validacao2=0

if validacao2==validante2:
     Etapa2_validacao=True 
if Etapa1_validacao and Etapa2_validacao:
    print('é verdade')

