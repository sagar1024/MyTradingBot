import logging

def get_logger():
    logger = logging.getLogger("MyTradingBot")
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        fh = logging.FileHandler("logs/bot.log")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    return logger
