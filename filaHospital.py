class Nodo:
    def __init__(self, cor, numero):
        self.cor = cor
        self.numero = numero
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.head = None
        self.numero_verde = 201
        self.numero_amarelo = 1

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
            while atual.proximo is not None and atual.cor == "A":
                atual = atual.proximo
            if atual.cor == "V":
                nodo.proximo = atual
                self.head = nodo
            else:
                nodo.proximo = atual.proximo
                atual.proximo = nodo

    def inserir(self):
        cor = input("Digite a cor do cartão (A ou V): ")
        if cor.upper() == "V":
            numero = self.numero_verde
            self.numero_verde += 1
        elif cor.upper() == "A":
            numero = self.numero_amarelo
            self.numero_amarelo += 1
        else:
            print("Cor inválida. Por favor, digite A ou V.")
            print("\n \n")
            return
        nodo = Nodo(cor, numero)
        if self.head is None:
            self.head = nodo
        elif cor.upper() == "V":
            self.inserirSemPrioridade(nodo)
        elif cor.upper() == "A":
            self.inserirComPrioridade(nodo)

    def imprimirListaEspera(self):
        atual = self.head
        output = "Lista ->"
        while atual is not None:
            output += f" [{atual.cor}, {atual.numero}]"
            atual = atual.proximo
        print(output)

    def atenderPaciente(self):
        if self.head is None:
            print("Não há pacientes na fila.")
        else:
            paciente = self.head
            self.head = paciente.proximo
            print(f"Paciente {paciente.cor} - Número: {paciente.numero} chamado para atendimento.")

    def menu(self):
        while True:
            print("************  MENU  ******************")
            print("*  [1]  Adicionar paciente à fila    *")
            print("*  [2]  Mostrar pacientes na fila    *")
            print("*  [3]  Chamar paciente              *")
            print("*  [4]  Sair                         *")
            print("**************************************")
            print("\n")
            opcao = input("Digite a opção desejada:")
            if opcao == "1":
                self.inserir()
            elif opcao == "2":
                self.imprimirListaEspera()
            elif opcao == "3":
                self.atenderPaciente()
            elif opcao == "4":
                break
            else:
                print("Opção inválida. Digite uma opção válida. [1] [2] [3] [4]")

lista = ListaEncadeada()
lista.menu()