'''
A empresa que você trabalha resolveu conceder um aumento salarial a todos funcionários,
de acordo com a tabela abaixo:

Salário	Percentual de Reajuste
0 - 600.00
600.01 - 900.00
900.01 - 1500.00
1500.01 - 2000.00
Acima de 2000.00

17%
13%
12%
10%
5%

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de
reajuste ganho e o índice reajustado, em percentual.

A entrada contém apenas um valor de ponto flutuante, que pode ser maior ou igual a zero,
com duas casas decimais, conforme exemplos abaixo.
'''

#ATENÇÃO: cuidado com os espaços usando f-string, o teste cobra isso tambem

#ATENÇÃO² : Usar a variavel 'percentual_' porque ele não aceita o print( com a porcentagem fixa)
# ex: print('Ajuste de 12%') ele pede o -> print(f'Ajuste de  {percentual} %')

salario = int(input()) 

if salario <=600:
    percentual = 0.17
    reajuste = salario * percentual
    novo_salario = salario + reajuste
    percentual_ = 17
  
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')                                                                                 
    print(f'Em percentual: {percentual_} %')

elif salario >600 and salario <=900:
    percentual = 0.13
    reajuste = salario * percentual
    novo_salario = salario + reajuste
    percentual_ = 13
    
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')                                                                                 
    print(f'Em percentual: {percentual_} %')

elif salario > 900 and salario <=1500:
    percentual = 0.12
    reajuste = salario * percentual
    novo_salario = salario + reajuste
    percentual_ = 12
    
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')                                                                                 
    print(f'Em percentual: {percentual_} %')
    
elif salario >1500 and salario <=2000:
    percentual = 0.10
    reajuste = salario * percentual
    novo_salario = salario + reajuste
    percentual_ = 10
    
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')                                                                                 
    print(f'Em percentual: {percentual_} %')
    
else:
    percentual = 0.05
    reajuste = salario * percentual
    novo_salario = salario + reajuste
    percentual_ = 5
    
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')                                                                                 
    print(f'Em percentual: {percentual_} %')
