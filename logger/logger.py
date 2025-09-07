import logging
from logging.handlers import RotatingFileHandler
import os

# name is name of process; log_file is the name of the log file
def setup_logger(name, log_file, level=logging.INFO, max_bytes=1_000_000, backup_count=3, to_console=True):
    """
    Creates a logger with rotating file handler and optional console output.

    Parameters:
        name (str): Logical name of the logger (e.g., 'etl_process')
        log_file (str): Path to the log file
        level (int): Logging level (e.g., logging.INFO)
        max_bytes (int): Max size in bytes before rotation
        backup_count (int): Number of backup files to keep
        to_console (bool): Whether to also log to console
    Returns:
        logging.Logger: Configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    if to_console:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    logger.propagate = False

    return logger