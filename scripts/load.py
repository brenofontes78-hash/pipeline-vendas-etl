import logging
from sqlalchemy import create_engine, URL


def load_data(dados):

    try:
        logging.info("Iniciando carregamento no PostgreSQL")

        url = URL.create(
            drivername="postgresql+psycopg2",
            username="usuario",
            password="suasenha",
            host="localhost",
            port=5432,
            database="seubanco"
        )

        engine = create_engine(url)

        dados.to_sql(
            "vendas",
            engine,
            if_exists="replace",
            index=False
        )

        logging.info(
            f"Carregamento concluído. Linhas inseridas: {len(dados)}"
        )


    except Exception as e:
        logging.error(f"Erro no carregamento: {e}")
        raise