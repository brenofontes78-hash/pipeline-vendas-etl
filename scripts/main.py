import logging

from extract import extract_data
from transform import transform_data
from load import load_data


logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():

    try:

        df = extract_data()

        df = transform_data(df)

        load_data(df)

        logging.info("Pipeline executada com sucesso")


    except Exception as e:

        logging.error(f"Pipeline interrompida: {e}")


if __name__ == "__main__":
    main()