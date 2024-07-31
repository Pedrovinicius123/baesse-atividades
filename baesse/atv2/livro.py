# Criando a Classe

class Livro:
    def __init__(self, ptitulo, pautor, ppaginas):
        self.titulo = ptitulo
        self.autor = pautor
        self.paginas = ppaginas

    def informacoes(self):
        print(f"O livro {self.titulo} do(a) autor(a) {self.autor} tem {self.paginas} paginas.")

# Instanciando as classes

livro1 = Livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 323)
livro2 = Livro("A Culpa é das Estrelas", "John Grenn", 313)
livro3 = Livro("Petrus Logus: Guardião do tempo", "Augusto Cury", 296)

# Mostrando as informações

livro1.informacoes()
livro2.informacoes()
livro3.informacoes()
