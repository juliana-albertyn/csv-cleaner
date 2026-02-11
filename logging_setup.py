"""
Module: logging_setup
Purpose: Provide a consistent logging setup for all Fynbyte modules.

This module configures a simple, readable logging format suitable for
development and production use. Other modules can import `get_logger`
to obtain a preconfigured logger.
"""
__author__ = "Juliana Albertyn"
__email__ = "julie_albertyn@yahoo.com"
__status__ = "development"  # or testing or production
__date__    = "19 December 2025"

import logging
from logging import Logger

def setup_logging(level: int = logging.INFO) -> None:
    """
    Configure the root logger with a standard format.
    Logs will be written to the console.
    """
    logging.basicConfig(
        level=level,
        format=f"%(asctime)s [%(levelname)s] %(name)s (v{'0.0.0.1'}): %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )


def get_logger(name: str) -> Logger:
    """
    Return a logger with the given name.

    Args:
    name (str) : The name of the logger, usually __name__.

    Returns:
    logging.Logger: A configured logger instance.
    """
    return logging.getLogger(name)