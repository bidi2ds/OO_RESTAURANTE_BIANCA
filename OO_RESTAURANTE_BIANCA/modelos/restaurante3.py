#criando uma classe usando decoreitor @proprety

class Restaurante:
    restaurantes=[]
    def __init__(self,nome,categoria):
        self.nome=nome.title()
        self.categoria=categoria.upper()
        self._ativo=False
        Restaurante.restaurantes.append(self)

    def __str__(self):
       # return self.nome
        return f'{self.nome}|{self.categoria}|{self.ativo}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'Nome do Restaurante | Categoria | Status')
        for restaurante in cls.restaurantes:
            print(f'{restaurante.nome.ljust(20)}|{restaurante.categoria.ljust(20)}|{restaurante.ativo}')

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    def alternar_status(self):
        self._ativo=not self._ativo

restaurante_praca=Restaurante('Praça','Gourmet')
restaurante_pizza=Restaurante('Pizza Express','Italiana')

restaurante_praca.alternar_status()




restaurante_praca=Restaurante('Praça','Gourmet')
restaurante_pizza=Restaurante('Baeti','mexicana')
# restaurante_praca.nome='Bistro'
# restaurante_praca.categoria='Italiana'

# restaurante_pizza=Restaurante()

# restaurantes=[restaurante_praca,restaurante_pizza]

#print(restaurante_praca.ativo)

# print(dir(restaurante_praca))
# print('')
# print(vars(restaurante_praca))
Restaurante.listar_restaurantes()