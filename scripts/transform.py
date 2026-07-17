import pandas as pd
import logging


def transform_data(dados):

    try:
        logging.info("Iniciando transformação dos dados")

        linhas_iniciais = len(dados)

        
        dados['preco_unitario'] = pd.to_numeric(
            dados['preco_unitario'],
            errors='coerce'
        )

       
        dados['data'] = pd.to_datetime(
            dados['data'],
            errors='coerce'
        )

        dados = dados
        dados = dados.dropna()

        linhas_finais = len(dados)

        logging.info(
            f"Transformação concluída. "
            f"Linhas iniciais: {linhas_iniciais} | "
            f"Linhas finais: {linhas_finais}"
        )

        return dados


    except KeyError as e:
        logging.error(f"Coluna não encontrada: {e}")
        raise


    except Exception as e:
        logging.error(f"Erro na transformação: {e}")
        raise