# Trabalho de Estrutura de Dados

Este repositório contém os exercícios desenvolvidos para a disciplina de Estrutura de Dados/Programação III. Cada exercício explora diferentes conceitos fundamentais de estrutura de dados, implementados em Python.

## Estrutura do Repositório

- `filaHospital.py`: Implementa uma Lista Encadeada Simples para gerenciar a fila de atendimento de um hospital, priorizando os casos mais urgentes de acordo com a cor e numeração dos cartões dos pacientes.

## Exercícios

### Exercício 1: Fila de Atendimento Hospitalar

**Descrição:** Um sistema de triagem hospitalar foi criado para priorizar o atendimento de pacientes com base em uma avaliação prévia. Pacientes recebem um cartão numerado de cor verde (V) ou amarelo (A), representando menor ou maior urgência, respectivamente.

**Implementação:**
- Lista Encadeada Simples onde cada nodo representa um cartão numerado (cor, número).
- Função `inserirSemPrioridade(nodo)`: Insere um novo nodo no final da lista.
- Função `inserirComPrioridade(nodo)`: Insere um novo nodo na lista, após todos os nodos com cor “A”.
- Função `inserir()`: Solicita a cor do cartão ao usuário e insere o paciente na lista com base na cor.
- Função `imprimirListaEspera()`: Imprime todos os cartões e números na lista de espera.
- Função `atenderPaciente()`: Remove e chama o primeiro paciente da fila.
- Menu interativo para adicionar pacientes à fila, mostrar pacientes na fila, chamar pacientes ou encerrar o programa.

**Como Executar:**
1. Clone o repositório: `git clone https://github.com/seu-usuario/Trabalho-De-Estrutura-de-Dados.git`
2. Navegue até o diretório: `cd Trabalho-De-Estrutura-de-Dados`
3. Execute o script: `python filaHospital.py`

### Exercício 2

*Ainda não implementado.*

## Tecnologias Utilizadas

- Python

## Autor

- **Andrei Morais Barbosa** - RU: 4529136

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.
