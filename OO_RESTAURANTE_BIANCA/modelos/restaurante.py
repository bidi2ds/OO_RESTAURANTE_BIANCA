class Restaurante:
    nome=''
    #questão 4
    categoria=''
    ativo=False

restaurante_praca=Restaurante()
#questão 5
restaurante_praca.nome='baeti'
#questão 1
restaurante_praca.categoria='Italiana'

restaurante_pasta=Restaurante()
#questão 6
restaurante_pasta.nome='Pasta Place'
restaurante_pasta.categoria='Fast Food'

restaurantes=[restaurante_praca,restaurante_pasta]

#print(restaurante_praca.ativo)

print(dir(restaurante_praca))
print('')
#questão 9
print(vars(restaurante_praca))
#questão 2
print(restaurante_praca.nome)

#questão 3
if (restaurante_praca.ativo):
        print('Restaurante praça ativo ')
else:
        print('Restaurante praça inativo')

#questão 7
if(restaurante_pasta.categoria):
       print('A categoria é fast food')
else:
       print('A categoria não é fast food')       

#questão 8
if (restaurante_pasta.ativo):
        print('Restaurante pasta inativo')
else:
        print('Restaurante pasta ativo')