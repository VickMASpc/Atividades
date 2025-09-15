class aluno:
    nome = ""
    nota = 0

    def mostrarSituacao(self):
        if self.nota >= 5:
            print(self.nome, "foi aprovado")
        else:
            print(self.nome, "foi reprovado")


a1 = aluno()
a1.nome = "Diego"
a1.nota = 3
a1.mostrarSituacao()

a2 = aluno()
a2.nome = "Johnny"
a2.nota = 9
a2.mostrarSituacao()

a3 = aluno()
a3.nome = "Beatrix"
a3.nota = 6
a3.mostrarSituacao()

a4 = aluno()
a4.nome = "Caleb"
a4.nota = 10
a4.mostrarSituacao()

a5 = aluno()
a5.nome = "Nicolas"
a5.nota = 1
a5.mostrarSituacao()

a6 = aluno()
a6.nome = "Austin"
a6.nota = 8
a6.mostrarSituacao()

a7 = aluno()
a7.nome = "Elizabeth"
a7.nota = 7
a7.mostrarSituacao()
