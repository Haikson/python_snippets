import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s",
    handlers=[
        logging.FileHandler(os.path.join(os.path.dirname(os.path.abspath('__file__')), 'logging_example.log')),
        logging.StreamHandler()
    ])
    
logger = logging.getLogger()

logger.info("Logging configured")
