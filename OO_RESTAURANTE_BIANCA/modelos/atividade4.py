#questão 1

class livro:
    livros=[]
    def __init__(self,titulo,autor,ano_publicacao):
        self.titulo=titulo
        self.autor=autor
        self.ano_publicacao=ano_publicacao
        self.disponivel=True
        #questão 3
        self.emprestar=False
        livro.livros.append(self)

#questao 2
    def __str__(self):
       # return self.nome
        return f'{self.titulo}|{self.autor}|{self.ano_publicacao}|{self.disponivel} | {self.emprestar}'
    
    @classmethod
    def listar_livros(cls):
        print(f'Título | Autor | Ano de publicação | Status | Diponível para emprestar')
        for livro in cls.livros:
            print(f'{livro.titulo.ljust(20)}|{livro.autor.ljust(20)}| {str(livro.ano_publicacao).ljust(20)} | {livro.disponivel} | {livro.emprestar}')

#questão 2   
livro1=livro('Homem aranha','Tom','2021')
livro2=livro('Os sete maridos de evelyn hugo','Jenny','2019')

livro.listar_livros()