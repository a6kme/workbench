from pathlib import Path

from loguru import logger


def get_logger(log_dir: Path):
    logger.add(f"{log_dir}/api.log", backtrace=True, diagnose=True, serialize=True)
    return logger
