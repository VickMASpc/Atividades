class animais:
    nomeCientífico = ""
    nomeComum = ""

    def latir(self):
        print("Au")

    def miar(self):
        print("Miau")

    def piar(self):
        print("Piu")

    def relinchar(self):
        print("Neigh")

    def arrulhar(self):
        print("Coo")


a1 = animais()
a1.nomeCientífico = "Canis lupus familiaris"
a1.nomeComum = "Cachorro"

a2 = animais()
a2.nomeCientífico = "Felis catus"
a2.nomeComum = "Gato"

a3 = animais()
a3.nomeCientífico = "Cyanocitta cristata"
a3.nomeComum = "Gaio-azul"

a4 = animais()
a4.nomeCientífico = "Equus caballus"
a4.nomeComum = "Cavalo"

a5 = animais()
a5.nomeCientífico = "Columbidae"
a5.nomeComum = "Pombo"

print("Nome científico:", a1.nomeCientífico)
print("Nome comum:", a1.nomeComum)
a1.latir()
print("")
print("Nome científico:", a2.nomeCientífico)
print("Nome comum:", a2.nomeComum)
a2.miar()
print("")
print("Nome científico:", a3.nomeCientífico)
print("Nome comum:", a3.nomeComum)
a3.piar()
print("")
print("Nome científico:", a4.nomeCientífico)
print("Nome comum:", a4.nomeComum)
a4.relinchar()
print("")
print("Nome científico:", a5.nomeCientífico)
print("Nome comum:", a5.nomeComum)
a5.arrulhar()
