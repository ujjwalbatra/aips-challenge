import logging

from data_reader import LocalTextFileReader

if __name__ == "__main__":
    logger = logging.getLogger()

    try:
        data_reader = LocalTextFileReader()
        data_frame = data_reader.get_content()
        print(data_frame)
    except Exception as e:
        logger.error(e, exc_info=True)
