from dataclasses import dataclass
from typing import List, Optional, Dict, Tuple


class Node:
    """Representa uma possível configuração no jogo"""

    _nodes_dict: Dict[str, "Node"] = {}

    def __init__(self, configuracao: str, vizinhos: Optional[List["Node"]] = None):
        self.configuracao: str = configuracao
        self.vizinhos: List[Node] = vizinhos if vizinhos is not None else list()
        self.visitado: bool = False

        # guarda no hash de nodes
        self._nodes_dict[configuracao] = self

    @classmethod
    def from_conf(cls, conf: str) -> "Node":
        """Retorna o Node a partir de uma configuração

        Raises:
            (KeyError) caso a configuração não tenha sido já gerada
        """
        return cls._nodes_dict[conf]

    @classmethod
    def is_created(cls):
        """Retorna se o grafo já foi gerado"""
        return bool(cls._nodes_dict)

    @staticmethod
    def _troca_posicoes(conf: str, pos1: int, pos2: int) -> str:
        """Recebe uma configuração e duas posicoes, e retorna a configuração com as duas posicoes trocadas

        Returns:
            (str) A nova configuração em string, com as duas posições trocadas
        """
        i1, i2 = min(pos1, pos2), max(pos1, pos2)
        v1, v2 = conf[i1], conf[i2]
        return conf[:i1] + v2 + conf[i1 + 1: i2] + v1 + conf[i2 + 1:]

    def _gera_configuracoes(self, tuplas: List[Tuple[int, int]]) -> List["Node"]:
        """Retorna configurações a partir de tuplas de posições a serem trocadas

        Args:
            tuplas (list(tuple(int, int))): Uma lista de tuplas que contem duas posições para serem trocadas

        Returns:
            (list): Uma lista com os nós gerados a partir das trocas
        """
        return [
            self.from_conf(
                self._troca_posicoes(
                    conf=self.configuracao, pos1=p1, pos2=p2
                )
            ) for p1, p2 in tuplas
        ]

    def gera_vizinhos(self):
        """Gera os vizinhos do nó"""
        pos_x = self.configuracao.index('x')
        trocas: List[Tuple[int, int]] = []
        if pos_x == 0:
            trocas = [(0, 1), (0, 3)]
        elif pos_x == 1:
            trocas = [(1, 0), (1, 2), (1, 4)]
        elif pos_x == 2:
            trocas = [(2, 1), (2, 5)]
        elif pos_x == 3:
            trocas = [(3, 0), (3, 4), (3, 6)]
        elif pos_x == 4:
            trocas = [(4, 1), (4, 3), (4, 5), (4, 7)]
        elif pos_x == 5:
            trocas = [(5, 2), (5, 4), (5, 8)]
        elif pos_x == 6:
            trocas = [(6, 3), (6, 7)]
        elif pos_x == 7:
            trocas = [(7, 4), (7, 6), (7, 8)]
        elif pos_x == 8:
            trocas = [(8, 5), (8, 7)]

        self.vizinhos = self._gera_configuracoes(trocas)

    def __repr__(self):
        return f'<Node "{self.configuracao}">'

    def representacao_3x3(self) -> str:
        """Retorna o Node em uma matriz 3x3

        Imprime o Node em uma matriz 3x3,
        em que coluna da matriz é separada por '\t',
        e cada linha é separada por '\n'

        Returns:
            (str): a representação do Node
        """
        return (
            f'{self.configuracao[0]}\t{self.configuracao[1]}\t{self.configuracao[2]}\n'
            f'{self.configuracao[3]}\t{self.configuracao[4]}\t{self.configuracao[5]}\n'
            f'{self.configuracao[6]}\t{self.configuracao[7]}\t{self.configuracao[8]}'
        )
