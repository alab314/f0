import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fast_zero.app import app
from fast_zero.models import Base


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def session():
    ## cria um mecanismo de banco de dados SQLite em memória usando SQLAlchemy
    engine = create_engine('sqlite:///:memory')
    ## cria uma fábrica de sessões para criar sessões de banco de dados para nossos testes
    Session = sessionmaker(bind=engine)
    ## cria todas as tabelas no banco de dados de teste antes de cada teste que usa a fixture
    Base.metadata.create_all(engine)
    ## fornece uma instância de Session que será injetada em cada teste que solicita a fixture session
    yield Session()
    ## após cada teste que usa a fixture session, todas as tabelas do banco de dados de teste são eliminadas
    Base.metadata.drop_all(engine)
