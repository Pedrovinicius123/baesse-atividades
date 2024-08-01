# Criando a classe de número
class Numero:
    def __init__(self, pnum):
        self.num = pnum

    def sucessor(self):
        """
        O sucessor do número
        """
        valor = self.num + 1
        print(f"O sucessor de {self.num} é {valor}.\n")

    #Criando as classes antecessor, dobro, triplo e metade
    def antecessor(self):
        """
        O antecessor do número
        """

        valor = self.num - 1
        print(f"O antecessor de {self.num} é {valor}.\n")

    def dobro(self):
        """
        O dobro do número
        """

        valor = self.num*2
        print(f"O dobro de {self.num} é {valor}.\n")

    def triplo(self):
        """
        O triplo do número
        """

        valor = self.num*3
        print(f"O triplo de {self.num} é {valor}\n")

    def metade(self):
        """
        A metade de um número; note que se ele
        for ímpar, o resultado sairá em decimal
        """

        valor = self.num/2
        print(f"A metade de {self.num} é {int(valor)}\n")

# Número 2
dois = Numero(2)

# Número 8
oito = Numero(8)

# Sucessores
dois.sucessor()
oito.sucessor()

# Antecessores
dois.antecessor()
oito.antecessor()

# Dobro
dois.dobro()
oito.dobro()

# Triplo
dois.triplo()
oito.triplo()

# Metade
dois.metade()
oito.metade()
