import logging

if __name__ == "__main__":
    logger = logging.getLogger()

    try:
        print("test")
    except Exception as e:
        logger.error(e, exc_info=True)