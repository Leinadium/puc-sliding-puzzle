from .node import Node
from collections import OrderedDict

from typing import Iterator


class ConjuntoNodes:
    def __init__(self):
        self._d: OrderedDict[str, Node] = OrderedDict()

    def clear(self):
        """Remove todos os nós do conjunto"""
        self._d.clear()

    def push(self, n: Node):
        """Insere um node no conjunto"""
        self._d[n.configuracao] = n

    def popfirst(self) -> Node:
        """Remove e retorna um node do conjunto, na ordem FIFO

        Returns:
            (Node) O node do conjunto na ordem FIFO

        Raises:
            (KeyError) Se não houver nenhum nó no conjunto
        """
        return self._d.popitem(last=False)[1]

    def remove(self, n: Node):
        """Remove o node especificado do conjunto

        Args:
            n (Node): Um node contido no conjunto

        Raises:
            (KeyError) Se o node não está contido no conjunto
        """
        del self._d[n.configuracao]

    def __bool__(self) -> bool:
        """Retorna se o conjunto possui algum node"""
        return bool(self._d)

    def __contains__(self, item: Node) -> bool:
        """Retorna se o conjunto contem aquele node"""
        return item.configuracao in self._d

    def __iter__(self) -> Iterator[Node]:
        for _k, v in self._d.items():
            yield v

    def clone(self) -> "ConjuntoNodes":
        """Retorna uma copia do conjunto"""
        new_conjunto = ConjuntoNodes()
        new_conjunto._d = self._d.copy()
        return new_conjunto

    @property
    def size(self) -> int:
        """Retorna o tamanho do conjunto"""
        return len(self._d)

    def __repr__(self):
        return f'<ConjuntoNodes size={self.size}>'
