class Nodo:
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None

class TabelaHash:
    def __init__(self):
        self.tabela = [None] * 10

    def funcao_hash(self, sigla):
        if sigla == 'DF':
            return 7
        else:
            char1_ascii = ord(sigla[0])
            char2_ascii = ord(sigla[1])
            return (char1_ascii + char2_ascii) % 10

    def inserir(self, sigla, nomeEstado):
        posicao = self.funcao_hash(sigla)
        novo_nodo = Nodo(sigla, nomeEstado)
        if self.tabela[posicao] is None:
            self.tabela[posicao] = novo_nodo
        else:
            novo_nodo.proximo = self.tabela[posicao]
            self.tabela[posicao] = novo_nodo

    def imprimir(self):
        for i in range(10):
            print(f"Posição {i}: ", end="")
            nodo = self.tabela[i]
            while nodo is not None:
                print(f"{nodo.sigla} -> ", end="")
                nodo = nodo.proximo
            print("None")

# Criação da tabela hash
tabela_hash = TabelaHash()

# Inserção dos 27 estados e Distrito Federal
estados = [
    ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'),
    ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
    ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')
]

for sigla, nome in estados:
    tabela_hash.inserir(sigla, nome)

# Inserção de um estado fictício
tabela_hash.inserir('BK', 'Bruno Kostiuk')

# Impressão da tabela hash
tabela_hash.imprimir()
