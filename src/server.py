# run > uvicorn nome-do-arquivo:app --realod
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.infra.sqlAlchemy.config.database import get_db, criar_db
from src.schemas import schemas
from src.infra.sqlAlchemy.repositorios.produto import RepositorioProduto


criar_db()
app = FastAPI()


@app.get("/produtos")
def listar_produtos():
    return {'Mensagem': 'Lisatagem de produtos'}


@app.post('/produto')
def criar_produto(produto: schemas.Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)

    return produto_criado