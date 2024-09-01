class Nodo:
    def __init__(self, sigla, nome_estado):
        self.sigla = sigla
        self.nome_estado = nome_estado
        self.proximo = None

class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho

    def funcao_hash(self, sigla):
        if sigla == "DF":
            return 7
        else:
            return (ord(sigla[0]) + ord(sigla[1])) % self.tamanho

    def inserir(self, sigla, nome_estado):
        indice = self.funcao_hash(sigla)
        novo_nodo = Nodo(sigla, nome_estado)
        novo_nodo.proximo = self.tabela[indice]
        self.tabela[indice] = novo_nodo

    def imprimir(self):
        for i in range(self.tamanho):
            print(f"Posição {i}: ", end="")
            nodo_atual = self.tabela[i]
            while nodo_atual:
                print(nodo_atual.sigla, end=" ")
                nodo_atual = nodo_atual.proximo
            print()

# Criar a tabela hash
tabela_hash = TabelaHash(10)

# Imprimir a tabela hash vazia
print("Tabela Hash vazia:")
tabela_hash.imprimir()

# Inserir os 26 estados e o Distrito Federal
estados = [
    ("AC", "Acre"),("AL", "Alagoas"),("AP", "Amapá"),("AM", "Amazonas"),
    ("BA", "Bahia"), ("CE", "Ceará"), ("DF", "Distrito Federal"), ("ES", "Espírito Santo"),
    ("GO", "Goiás"), ("MA", "Maranhão"), ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"),
    ("MG", "Minas Gerais"), ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"),
    ("PE", "Pernambuco"), ("PI", "Piauí"), ("RJ", "Rio de Janeiro"), ("RN", "Rio Grande do Norte"),
    ("RS", "Rio Grande do Sul"), ("RO", "Rondônia"), ("RR", "Roraima"), ("SC", "Santa Catarina"),
    ("SP", "São Paulo"), ("SE", "Sergipe"), ("TO", "Tocantins")
]

for sigla, nome_estado in estados:
    tabela_hash.inserir(sigla, nome_estado)

# Imprimindo a tabela hash após inserir os estados
print("\nTabela Hash após inserir os estados:")
tabela_hash.imprimir()

# Inseririndo o estado fictício
nome_completo = "Andrei Barbosa" #Meu nome é Andrei Morais Barbosa, porem encurtei para ficar AB.
sigla_ficticia = nome_completo[0] + nome_completo.split()[-1][0]
tabela_hash.inserir(sigla_ficticia, nome_completo)

# Imprimindo a tabela hash após inserir o estado fictício
print("\nTabela Hash após inserir o estado fictício:")
tabela_hash.imprimir()
