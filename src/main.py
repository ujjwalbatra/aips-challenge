import logging
from datetime import datetime

from data_reader import LocalTextFileReader
from output_generator import OutputGenerator

if __name__ == "__main__":
    logger = logging.getLogger()

    try:
        data_reader = LocalTextFileReader()
        data_frame = data_reader.get_content()
        result = 'test'

        if len(result) > 0:
            OutputGenerator(result, f'output/report:{datetime.now()}.txt').write_output()
    except Exception as e:
        logger.error(e, exc_info=True)
