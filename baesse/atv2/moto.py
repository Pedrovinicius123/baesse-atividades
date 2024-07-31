# Criando a classe

class Moto:
    def __init__(self, pmarca, pmodelo, pcilindradas):
        self.marca = pmarca
        self.modelo = pmodelo
        self.cilindradas = pcilindradas

    def dados(self):
        print(f"A moto {self.modelo} possui {self.cilindradas} cilindradas.")
    
# Instanciando a classe

moto1 = Moto("Honda", "Honda CB 500F", 500)
moto2 = Moto("Yamaha", "Yamaha YZF-R6", 600)

# Mostrando a mensagem de cada modelo

moto1.dados()
moto2.dados()
