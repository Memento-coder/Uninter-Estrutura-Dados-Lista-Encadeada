class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.head = None
        self.contadorV = 0
        self.contadorA = 200

    def inserirSemPrioridade(self, nodo):
        if self.head is None:
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = nodo

    def inserirComPrioridade(self, nodo):
        if self.head is None:
            self.head = nodo
        else:
            atual = self.head
            anterior = None

            while atual is not None and atual.cor == "A":
                anterior = atual
                atual = atual.proximo

            if anterior is None:
                nodo.proximo = self.head
                self.head = nodo
            else:
                anterior.proximo = nodo
                nodo.proximo = atual

    def inserir(self):
        cor = input("Digite A ou V: ").upper()

        if cor != "A" and cor != "V":
            print("Entrada inválida")
            return

        if cor == "V":
            self.contadorV += 1
            numero = self.contadorV
        else:
            self.contadorA += 1
            numero = self.contadorA

        novo = Nodo(numero, cor)

        if self.head is None:
            self.head = novo
        else:
            if cor == "V":
                self.inserirSemPrioridade(novo)
            else:
                self.inserirComPrioridade(novo)

    def imprimirListaEspera(self):
        atual = self.head

        while atual is not None:
            print(f"{atual.cor}{atual.numero}", end=" -> ")
            atual = atual.proximo
        print("None")

    def atenderPaciente(self):
        if self.head is None:
            print("Fila vazia")
        else:
            print(f"Atendendo {self.head.cor}{self.head.numero}")
            self.head = self.head.proximo


def menu():
    lista = ListaEncadeada()

    while True:
        print("\n1 - Inserir")
        print("2 - Mostrar")
        print("3 - Atender")
        print("4 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            lista.inserir()
        elif opcao == "2":
            lista.imprimirListaEspera()
        elif opcao == "3":
            lista.atenderPaciente()
        elif opcao == "4":
            break
        else:
            print("Opção inválida")


menu()