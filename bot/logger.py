# import logging

# def get_logger():
#     logger = logging.getLogger("MyTradingBot")
#     logger.setLevel(logging.INFO)
#     if not logger.handlers:
#         fh = logging.FileHandler("logs/bot.log")
#         formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
#         fh.setFormatter(formatter)
#         logger.addHandler(fh)
#     return logger

import os
import logging

def get_logger():
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger("MyTradingBot")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        fh = logging.FileHandler(os.path.join(log_dir, "bot.log"))
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger
