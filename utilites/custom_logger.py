import logging
import os

class LoggingGenerator:
    
    def log_gen():
        log_file = os.path.join(os.path.dirname(__file__), '..', 'Logs', 'automation.log')
        logging.basicConfig(filename= log_file , format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger