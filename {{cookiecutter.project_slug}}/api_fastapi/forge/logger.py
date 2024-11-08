from pathlib import Path

from loguru import Logger, logger


def get_logger(log_dir: Path) -> Logger:
    logger.add(f"{log_dir}/api.log", backtrace=True, diagnose=True, serialize=True)
    return logger
