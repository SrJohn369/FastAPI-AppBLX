from pydantic import BaseModel
from typing import Optional, List


class Usuario(BaseModel):
    id: Optional[str] = None
    nome: str
    telefone: str


class Produto(BaseModel):
    nome: str 
    id: Optional[str] = None
    detalhes: str
    preco: float
    disponivel: bool = False

    class config:
        orm_mode = True


class Pedido(BaseModel):
    id: Optional[str] = None
    quantiddade: int
    entrega: bool = False
    endereco: str
    observacoes: Optional[str] = 'Sem observações'