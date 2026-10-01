from typing import Literal

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field, field_validator
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_URL = "sqlite:///./banco.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


class ProdutoBanco(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    codigo = Column(String, unique=True, nullable=False)
    preco = Column(Float, nullable=False)


app = FastAPI(
    title="SmartCheckout API",
    description="API de validação e gerenciamento de produtos do SmartCheckout",
    version="1.4.0"
)


app.mount(
    "/interface",
    StaticFiles(directory="frontend", html=True),
    name="interface"
)


def validar_gtin(codigo: str) -> bool:
    codigo = codigo.strip()

    if not codigo.isdigit():
        return False

    tamanho = len(codigo)

    if tamanho not in (8, 12, 13, 14):
        return False

    digitos = [int(digito) for digito in codigo]

    digito_verificador = digitos[-1]
    digitos_base = digitos[:-1]

    soma = 0
    multiplicador = 3

    for digito in reversed(digitos_base):
        soma += digito * multiplicador

        if multiplicador == 3:
            multiplicador = 1
        else:
            multiplicador = 3

    calculado = (10 - (soma % 10)) % 10

    return calculado == digito_verificador


def classificar_leitura(leitura: str) -> str:
    leitura = leitura.strip()

    if not leitura:
        return "invalida"

    if not leitura.isdigit():
        return "nao_gtin"

    if not validar_gtin(leitura):
        return "gtin_invalido"

    return "gtin"


def buscar_produto(codigo: str):
    db = SessionLocal()

    try:
        produto = (
            db.query(ProdutoBanco)
            .filter(ProdutoBanco.codigo == codigo)
            .first()
        )

        return produto

    finally:
        db.close()


def produto_para_resposta(produto):
    if not produto:
        return None

    return {
        "id": produto.id,
        "nome": produto.nome,
        "codigo": produto.codigo,
        "preco": produto.preco
    }


def decidir_leitura(leitura: str, tipo: str):
    if tipo == "qrcode":
        return {
            "resultado": "ignorar",
            "codigo": "qrcode_bloqueado",
            "mensagem": "Leitura de QR Code bloqueada.",
            "produto": None
        }

    if tipo == "desconhecido":
        return {
            "resultado": "ignorar",
            "codigo": "tipo_leitura_desconhecido",
            "mensagem": "Não foi possível identificar o tipo da leitura.",
            "produto": None
        }

    if tipo != "codigo_barras":
        return {
            "resultado": "ignorar",
            "codigo": "tipo_leitura_invalido",
            "mensagem": "Tipo de leitura não reconhecido.",
            "produto": None
        }

    classificacao = classificar_leitura(leitura)

    if classificacao == "invalida":
        return {
            "resultado": "ignorar",
            "codigo": "leitura_vazia",
            "mensagem": "A leitura está vazia.",
            "produto": None
        }

    if classificacao == "nao_gtin":
        return {
            "resultado": "ignorar",
            "codigo": "nao_gtin",
            "mensagem": "A leitura não corresponde a um GTIN.",
            "produto": None
        }

    if classificacao == "gtin_invalido":
        return {
            "resultado": "ignorar",
            "codigo": "gtin_invalido",
            "mensagem": "O código numérico não possui um GTIN válido.",
            "produto": None
        }

    produto = buscar_produto(leitura)

    if not produto:
        return {
            "resultado": "nao_cadastrado",
            "codigo": "produto_nao_cadastrado",
            "mensagem": "Produto não cadastrado.",
            "produto": None
        }

    return {
        "resultado": "permitir",
        "codigo": "produto_cadastrado",
        "mensagem": "Produto cadastrado e leitura permitida.",
        "produto": produto_para_resposta(produto)
    }


class Produto(BaseModel):
    id: int = Field(gt=0)
    nome: str
    codigo: str
    preco: float = Field(ge=0)

    @field_validator("nome")
    @classmethod
    def validar_nome(cls, valor: str) -> str:
        valor = valor.strip()

        if not valor:
            raise ValueError(
                "O nome do produto não pode ficar vazio."
            )

        return valor

    @field_validator("codigo")
    @classmethod
    def validar_codigo(cls, valor: str) -> str:
        valor = valor.strip()

        if not validar_gtin(valor):
            raise ValueError(
                "O código deve ser um GTIN válido de 8, 12, 13 ou 14 "
                "dígitos, com dígito verificador correto."
            )

        return valor


class LeituraSmartCheckout(BaseModel):
    leitura: str
    tipo: Literal["codigo_barras", "qrcode", "desconhecido"]

    @field_validator("leitura")
    @classmethod
    def validar_leitura(cls, valor: str) -> str:
        valor = valor.strip()

        if not valor:
            raise ValueError(
                "A leitura não pode ficar vazia."
            )

        return valor


Base.metadata.create_all(bind=engine)


@app.get("/")
def inicio():
    return {
        "mensagem": "SmartCheckout API funcionando!"
    }


@app.post("/smartcheckout/ler")
def smartcheckout_ler(dados: LeituraSmartCheckout):
    leitura = dados.leitura.strip()

    return decidir_leitura(
        leitura,
        dados.tipo
    )


@app.get("/produtos")
def listar_produtos():

    db = SessionLocal()

    try:
        produtos = db.query(ProdutoBanco).all()

        resultado = []

        for produto in produtos:
            resultado.append({
                "id": produto.id,
                "nome": produto.nome,
                "codigo": produto.codigo,
                "preco": produto.preco
            })

        return resultado

    finally:
        db.close()


@app.get("/produtos/{produto_id}")
def buscar_produto_por_id(produto_id: int):

    db = SessionLocal()

    try:
        produto = (
            db.query(ProdutoBanco)
            .filter(ProdutoBanco.id == produto_id)
            .first()
        )

        if not produto:
            raise HTTPException(
                status_code=404,
                detail=f"Produto com ID {produto_id} não encontrado."
            )

        return {
            "id": produto.id,
            "nome": produto.nome,
            "codigo": produto.codigo,
            "preco": produto.preco
        }

    finally:
        db.close()


@app.post("/produtos")
def cadastrar_produto(produto: Produto):

    db = SessionLocal()

    try:
        produto_existente = (
            db.query(ProdutoBanco)
            .filter(ProdutoBanco.id == produto.id)
            .first()
        )

        if produto_existente:
            raise HTTPException(
                status_code=409,
                detail=f"O ID {produto.id} já está cadastrado."
            )

        produto_existente = (
            db.query(ProdutoBanco)
            .filter(ProdutoBanco.codigo == produto.codigo)
            .first()
        )

        if produto_existente:
            raise HTTPException(
                status_code=409,
                detail=f"O código {produto.codigo} já está cadastrado."
            )

        novo_produto = ProdutoBanco(
            id=produto.id,
            nome=produto.nome,
            codigo=produto.codigo,
            preco=produto.preco
        )

        db.add(novo_produto)
        db.commit()
        db.refresh(novo_produto)

        return {
            "id": novo_produto.id,
            "nome": novo_produto.nome,
            "codigo": novo_produto.codigo,
            "preco": novo_produto.preco
        }

    finally:
        db.close()


@app.put("/produtos/{produto_id}")
def atualizar_produto(
    produto_id: int,
    produto_atualizado: Produto
):

    if produto_atualizado.id != produto_id:
        raise HTTPException(
            status_code=400,
            detail=(
                "O ID da URL deve ser igual ao ID "
                "do produto enviado."
            )
        )

    db = SessionLocal()

    try:
        produto_existente = (
            db.query(ProdutoBanco)
            .filter(ProdutoBanco.id == produto_id)
            .first()
        )

        if not produto_existente:
            raise HTTPException(
                status_code=404,
                detail=(
                    f"Produto com ID {produto_id} "
                    "não encontrado."
                )
            )

        outro_produto = (
            db.query(ProdutoBanco)
            .filter(
                ProdutoBanco.codigo == produto_atualizado.codigo,
                ProdutoBanco.id != produto_id
            )
            .first()
        )

        if outro_produto:
            raise HTTPException(
                status_code=409,
                detail=(
                    f"O código {produto_atualizado.codigo} "
                    "já está cadastrado."
                )
            )

        produto_existente.nome = produto_atualizado.nome
        produto_existente.codigo = produto_atualizado.codigo
        produto_existente.preco = produto_atualizado.preco

        db.commit()
        db.refresh(produto_existente)

        return {
            "id": produto_existente.id,
            "nome": produto_existente.nome,
            "codigo": produto_existente.codigo,
            "preco": produto_existente.preco
        }

    finally:
        db.close()


@app.delete("/produtos/{produto_id}")
def excluir_produto(produto_id: int):

    db = SessionLocal()

    try:
        produto_existente = (
            db.query(ProdutoBanco)
            .filter(ProdutoBanco.id == produto_id)
            .first()
        )

        if not produto_existente:
            raise HTTPException(
                status_code=404,
                detail=(
                    f"Produto com ID {produto_id} "
                    "não encontrado."
                )
            )

        db.delete(produto_existente)
        db.commit()

        return {
            "mensagem": "Produto excluído com sucesso!"
        }

    finally:
        db.close()
