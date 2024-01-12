# Aqui no repositorio estamos sempre lidando com modelos 
# Schema é usado apenas para Request e Response
from sqlalchemy.orm import Session
from src.schemas.schemas import Produto as ProdutoSchema
from src.infra.sqlAlchemy.models.models import Produto


class RepositorioProduto():
    def __init__(self, db: Session):
        self.db = db

    # convertendo um schema num modelo
    def criar(self, produto: ProdutoSchema):
        db_produto = Produto(
            nome=produto.nome,
            detalhes=produto.detalhes,
            preco=produto.preco,
            disponivel=produto.disponivel
        )

        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)

        return db_produto

    def listar(self):
        produto = self.db.query(Produto).all()
        
        return produto

    def obter(self):
        pass

    def remover(self):
        pass