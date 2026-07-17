import pandas as pd
import logging


def extract_data():

    try:
        logging.info("Iniciando extração dos dados")

        df = pd.read_csv(
    "data/raw/vendas.csv",
    encoding="latin1"
)
        logging.info(f"Extração concluída. Linhas carregadas: {len(df)}")
        
        return df


    except FileNotFoundError:
        logging.error("Arquivo CSV não encontrado")
        raise


    except pd.errors.EmptyDataError:
        logging.error("Arquivo CSV está vazio")
        raise


    except Exception as e:
        logging.error(f"Erro na extração: {e}")
        raise
    