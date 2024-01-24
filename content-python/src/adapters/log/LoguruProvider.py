from loguru import logger
import sys
from src.domain.ports.logprovider import LogProviderInterface

class LogProvider(LogProviderInterface):
    
    def __init__(self) -> None:        
        log_format = '<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>';
        logger.add(sys.stderr, level="TRACE")
        logger.add("logs/sample.log", serialize=True, level=20, format=log_format)
        self.debug = logger.debug
        self.info =  logger.info
        self.critical = logger.critical

    def debug(log: str):
        pass
    
    def info(log: str):
        pass
    
    def critical(log: str):
        pass