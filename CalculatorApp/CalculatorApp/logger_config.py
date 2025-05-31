import logging

def setup_logger():
    logger = logging.getLogger("CalculatorLogger")
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler("operation_history.txt")
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    file_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(file_handler)

    return logger
