import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class Produto(Prototype):
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} - R${self.preco}"

produto1 = Produto("Caneta", 5.0)
produto2 = produto1.clone()
produto2.nome = "Lápis"

print(produto1) 
print(produto2) 
