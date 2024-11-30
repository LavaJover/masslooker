import logging


def setup_logger(logfile: str = 'logs/app.log') -> logging.Logger:
    logger = logging.getLogger("myLogger")
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(logfile)
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger


if __name__ == '__main__':
    log = setup_logger()

    log.info("Hello")