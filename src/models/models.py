from pydantic import BaseModel
from typing import Optional, List


class Usuario(BaseModel):
    id: Optional[str] = None
    nome: str
    telefone: str
    minhas_vendas: List[Pedido]
    meus_produtos: List[Produto]
    meus_pedidos: List[Pedido]


class Produto(BaseModel):
    nome: str 
    usuario: Usuario
    id: Optional[str] = None
    detalhes: str
    preco: float
    disponivel: bool = False


class Pedido(BaseModel):
    id: Optional[str] = None
    usuario: Usuario
    produto: Produto
    quantiddade: int
    entrega: bool = False
    endereco: str
    observacoes: Optional[str] = 'Sem observações'