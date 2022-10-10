from models.node import Node
from models.conjuntonodes import ConjuntoNodes

from typing import Tuple, Optional

POSSIVEIS: Tuple = ('1', '2', '3', '4', '5', '6', '7', '8', 'x')


def gera_nodes() -> ConjuntoNodes:
    """Gera todos os nodes possiveis existentes"""
    def recursiva(conjunto: ConjuntoNodes, config: str, pos: int):
        q = config.count('0')
        if q == 0:
            # caso base da recusao
            conjunto.push(Node(configuracao=config))
            return

        else:
            for i, e in enumerate(config):
                if e == '0':
                    try:
                        recursiva(
                            conjunto=conjunto,
                            config=config[:i] + POSSIVEIS[pos] + config[i+1:],
                            pos=pos + 1
                        )
                    except IndexError:
                        print(f'{config=}, {pos=}, {i=}, {e=}')
                        raise Exception()

    c = ConjuntoNodes()
    recursiva(c, "000000000", 0)
    return c


def tarefa1():
    # criando os nodes
    nodes: ConjuntoNodes = gera_nodes()

    # contando as arestas
    quantidade_arestas = 0
    for nd in nodes:
        nd.gera_vizinhos()
        quantidade_arestas += len(nd.vizinhos)

    # arestas = #vizinhos / 2. Pois estão sendo contadas duas vezes cada aresta
    quantidade_arestas //= 2

    print(f"Nodes: {nodes.size}, Arestas: {quantidade_arestas}")


def breadth_first_search(nodes_nao_visitados: ConjuntoNodes,
                         nodes_visitados: ConjuntoNodes,
                         node_inicial: Optional[Node] = None
                         ) -> ConjuntoNodes:
    """Executa o algoritmo de BFS nos nós do grafo a partir de um nó especifico

    A função modifica os dois ConjuntosNodes fornecidos, adicionando ou removendo nodes.

    Retorna também o último nível do BFS, que representa quais nodes estão mais distantes do node_inicial.

    Args:
        nodes_nao_visitados (ConjuntoNodes): Um conjunto os nodes a serem pesquisados. node_inicial deve estar contido
            neste conjunto
        nodes_visitados (ConjuntoNodes): O conjunto de nodes já visitados (que serão desconsiderados). Será modificado
            com a execução dessa função.
        node_inicial (Node): Node de onde iniciar o BFS. Caso seja None, será utilizado um qualquer do grafo

    Returns:
        (ConjuntoNode): Conjunto contendo os nodes do último nível verificado
    """
    prox_nivel = ConjuntoNodes()
    fila: ConjuntoNodes = ConjuntoNodes()
    i_nivel = 0

    # adiciona o no inicial na fila
    if node_inicial is not None:
        nodes_nao_visitados.remove(node_inicial)              # remove dos possiveis
        prox_nivel.push(node_inicial)                         # adiciona para ser verificado
    else:
        node_first = nodes_nao_visitados.popfirst()           # pega um node qualquer dos possiveis
        prox_nivel.push(node_first)                           # adiciona para ser verificado

    while prox_nivel:
        # novo nivel
        print(f"{i_nivel=}")
        fila = prox_nivel.clone()
        prox_nivel.clear()
        i_nivel += 1

        # fazendo todos os do nivel atual e preenchendo o proximo nivel
        for node in fila:       # type: Node
            for v in node.vizinhos:
                if v not in nodes_visitados:
                    prox_nivel.push(v)

            nodes_visitados.push(node)
            if node in nodes_nao_visitados:
                nodes_nao_visitados.remove(node)

    # quando acabou prox_nivel, a fila ainda não foi reiniciada. Entao o ultimo nivel esta na fila
    return fila


def tarefa2():
    # gera os nodes
    g: ConjuntoNodes = gera_nodes()
    for nod in g:
        nod.gera_vizinhos()
    print(f"Total de nodes no grafo: {g.size}")

    nodes_verificados: ConjuntoNodes = ConjuntoNodes()     # conjunto vazio
    nodes_nao_visitados: ConjuntoNodes = g.clone()         # conjunto completo
    q_conexos = 0

    while nodes_verificados.size != g.size:
        q_conexos += 1
        breadth_first_search(
            nodes_nao_visitados=nodes_nao_visitados,
            nodes_visitados=nodes_verificados,
            node_inicial=None
        )

    print(f"Total de conexos: {q_conexos}")
    return


if __name__ == "__main__":
    tarefa2()
